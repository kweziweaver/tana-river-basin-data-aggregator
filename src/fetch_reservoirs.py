"""
fetch_reservoirs.py
Pulls reservoir water surface elevation data from USGS for
Lake Powell (Glen Canyon Dam) and Lake Mead (Hoover Dam).

Uses USGS parameter code 00062 (lake/reservoir water surface elevation).
No API key required.
"""

import requests

# USGS reservoir sites in the Colorado River Basin
# Note: Lake Mead elevation is maintained by BOR, not USGS real-time.
# Future enhancement: integrate BOR RISE API for Lake Mead.
RESERVOIR_SITES = [
    {
        "id": "09379900",
        "name": "Lake Powell (Glen Canyon Dam)",
        "full_pool_ft": 3700.0,
        "dead_pool_ft": 3370.0,
        "notes": "Full pool 3700 ft; dead pool 3370 ft (generators go offline)"
    },
]

BASE_URL = "https://waterservices.usgs.gov/nwis/iv/"
ELEV_PARAM = "62614"  # Lake/reservoir water surface elevation, ft above NGVD29


def fetch_reservoirs() -> list[dict]:
    """Fetch latest reservoir elevation readings."""
    site_ids = ",".join(s["id"] for s in RESERVOIR_SITES)
    params = {
        "format": "json",
        "sites": site_ids,
        "parameterCd": ELEV_PARAM,
    }
    resp = requests.get(BASE_URL, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    site_meta = {s["id"]: s for s in RESERVOIR_SITES}
    results = []

    for ts in data["value"]["timeSeries"]:
        site_code = ts["sourceInfo"]["siteCode"][0]["value"]
        values = ts["values"][0]["value"]
        latest = values[-1] if values else {}
        meta = site_meta.get(site_code, {})

        if not latest.get("value") or latest["value"] == "-999999":
            continue

        elevation_ft = float(latest["value"])
        full_pool = meta.get("full_pool_ft", 0)
        dead_pool = meta.get("dead_pool_ft", 0)

        # Compute fill percentage between dead pool and full pool
        if full_pool > dead_pool:
            fill_pct = max(0, min(100, (elevation_ft - dead_pool) / (full_pool - dead_pool) * 100))
        else:
            fill_pct = None

        results.append({
            "site_id": site_code,
            "name": meta.get("name", ts["sourceInfo"]["siteName"]),
            "elevation_ft": elevation_ft,
            "full_pool_ft": full_pool,
            "dead_pool_ft": dead_pool,
            "fill_pct": round(fill_pct, 1) if fill_pct is not None else None,
            "latitude": ts["sourceInfo"]["geoLocation"]["geogLocation"]["latitude"],
            "longitude": ts["sourceInfo"]["geoLocation"]["geogLocation"]["longitude"],
            "datetime": latest.get("dateTime"),
            "notes": meta.get("notes", ""),
        })

    print(f"[reservoirs] fetched {len(results)} sites")
    return results


if __name__ == "__main__":
    import json
    reservoirs = fetch_reservoirs()
    print(json.dumps(reservoirs, indent=2))
