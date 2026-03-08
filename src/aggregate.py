"""
aggregate.py
Fetches all data sources and writes combined output to docs/data.json.
Run by GitHub Actions twice daily; also runnable locally.

Usage:
    python src/aggregate.py
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

from fetch_gauges import fetch_gauges
from fetch_reservoirs import fetch_reservoirs


def run():
    print("=== Colorado River Basin — Data Aggregator ===")
    print(f"Fetching at {datetime.now(timezone.utc).isoformat()}\n")

    # Fetch all sources
    gauges = fetch_gauges()
    reservoirs = fetch_reservoirs()

    # Assemble output
    output = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "basin": "Colorado River Basin",
        "sources": {
            "gauges": "USGS Water Services API — waterservices.usgs.gov",
            "reservoirs": "USGS Water Services API — waterservices.usgs.gov",
        },
        "gauges": gauges,
        "reservoirs": reservoirs,
    }

    # Write to docs/data.json (served by GitHub Pages)
    out_path = Path(__file__).parent.parent / "docs" / "data.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2))
    print(f"\n✓ Wrote {out_path}")
    print(f"  Gauges:    {len(gauges)} sites")
    print(f"  Reservoirs:{len(reservoirs)} sites")

    return output


if __name__ == "__main__":
    run()
