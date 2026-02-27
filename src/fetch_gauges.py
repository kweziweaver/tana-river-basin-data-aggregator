"""
fetch_gauges.py
Pulls real-time stream gauge data (discharge + gage height) from the
USGS Water Services API for key Colorado River Basin monitoring sites.

No API key required. Free public data.
Docs: https://waterservices.usgs.gov/
"""

import requests
from datetime import datetime, timezone

# Key Colorado River Basin USGS gauge sites
# Ordered upstream → downstream
GAUGE_SITES = [
    {"id": "09070500",  "name": "Colorado River near Dotsero, CO",           "state": "CO"},
    {"id": "09095500",  "name": "Colorado River near Cameo, CO",              "state": "CO"},
    {"id": "09163500",  "name": "Colorado River nr CO-UT state line",         "state": "CO"},
    {"id": "09180000",  "name": "Colorado River near Moab, UT",               "state": "UT"},
    {"id": "09315000",  "name": "Colorado River at Hite Crossing, UT",        "state": "UT"},
    {"id": "09380000",  "name": "Colorado River at Lees Ferry, AZ",           "state": "AZ"},
    {"id": "09402500",  "name": "Colorado River near Grand Canyon, AZ",       "state": "AZ"},
    {"id": "09421500",  "name": "Colorado River below Hoover Dam, AZ-NV",     "state": "NV"},
    # Major tributaries
    {"id": "09306500",  "name": "White River near Watson, UT",                "state": "UT"},
    {"id": "09328500",  "name": "San Rafael River near Green River, UT",      "state": "UT"},
    {"id": "09430500",  "name": "Gila River near Clifton, AZ",                "state": "AZ"},
]

PARAM_CODES = "00060,00065"  # Discharge (cfs), Gage height (ft)
BASE_URL = "https://waterservices.usgs.gov/nwis/iv/"


def fetch_gauges() -> list[dict]:
    """Fetch latest gauge readings for all monitored sites."""
    site_ids = ",".join(s["id"] for s in GAUGE_SITES)
    params = {
        "format": "json",
        "sites": site_ids,
        "parameterCd": PARAM_CODES,
        "siteStatus": "active",
    }
    resp = requests.get(BASE_URL, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    # Build lookup from site id → metadata
    site_meta = {s["id"]: s for s in GAUGE_SITES}

    # Parse time series
    results = {}
    for ts in data["value"]["timeSeries"]:
        site_code = ts["sourceInfo"]["siteCode"][0]["value"]
        param_name = ts["variable"]["variableName"]
        param_code = ts["variable"]["variableCode"][0]["value"]
        unit = ts["variable"]["unit"]["unitCode"]
        values = ts["values"][0]["value"]
        latest = values[-1] if values else {}

        if site_code not in results:
            meta = site_meta.get(site_code, {})
            results[site_code] = {
                "site_id": site_code,
                "name": meta.get("name", ts["sourceInfo"]["siteName"]),
                "state": meta.get("state", ""),
                "latitude": ts["sourceInfo"]["geoLocation"]["geogLocation"]["latitude"],
                "longitude": ts["sourceInfo"]["geoLocation"]["geogLocation"]["longitude"],
                "parameters": {},
            }

        if latest.get("value") and latest["value"] != "-999999":
            results[site_code]["parameters"][param_code] = {
                "name": param_name,
                "value": float(latest["value"]),
                "unit": unit,
                "datetime": latest.get("dateTime"),
            }

    gauges = list(results.values())
    print(f"[gauges] fetched {len(gauges)} sites")
    return gauges


if __name__ == "__main__":
    import json
    gauges = fetch_gauges()
    print(json.dumps(gauges, indent=2))
