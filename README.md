# Tana River Basin — Watershed Data Aggregator

A live data aggregator for the Tana River Basin, contextualizing bioregional infrastructure for Kenya.

---

## What It Does

Pulls data streams representing the health and status of the Tana River Basin and serves a live dashboard. Currently running a mock data generator (`generate_tana_data.py`) to simulate these streams while live data connectors are developed.

| Data Layer | Source / Description | Update Frequency |
|---|---|---|
| River Flow & Levels | Simulated gauges (e.g., Garissa Bridge) | Mocked |
| Vegetation Health | VCI (Vegetation Condition Index) for counties | Mocked |
| Headwater Health | Forest cover & streamflow trends | Mocked |
| Biodiversity | Elephant & Hirola antelope migration | Mocked |
| Economic Value | Livestock offtake and cold-chain status | Mocked |
| Governance | CFA and CCRI grants progress | Mocked |
| Warm Data (TEK) | Somali Indigenous Oracles (Council of Elders) | Mocked |

A process runs and writes the data to `docs/data.json`, and GitHub Pages serves the live dashboard.

---

## Data Sources (Planned & Adapted)

### River Gauges & Reservoirs
Scripts to fetch live gauges (`fetch_gauges.py`) and reservoirs (`fetch_reservoirs.py`) are retained from a previous architecture and can be adapted to pull from the Water Resources Authority (WRA) or public satellite data once APIs are accessible.

---

## Project Structure

```
watershed-data-collection/
├── src/
│   ├── generate_tana_data.py  # Mock data generator for Tana Basin
│   ├── fetch_gauges.py        # Stream gauge fetcher (to be adapted)
│   ├── fetch_reservoirs.py    # Reservoir elevation fetcher (to be adapted)
│   └── aggregate.py           # Legacy aggregator script
├── docs/
│   ├── index.html             # Live dashboard (GitHub Pages)
│   └── data.json              # Latest aggregated data snapshot
├── .github/
│   └── workflows/
│       └── update-data.yml    # Data refresh workflow via GitHub Actions
└── requirements.txt
```

---

## Running Locally

```bash
pip install -r requirements.txt
python src/generate_tana_data.py
# Writes fresh data to docs/data.json
# Open docs/index.html in a browser
```

---

## Relation to Bioregional Infrastructure

This tool is a unit of the knowledge commons. Every fetch enriches a shared, verifiable, queryable dataset for the Tana River Basin. The JSON output is structured to be:

- Machine-readable (for AI agents like the Energy Trust Engine)
- Human-readable (for the dashboard)
- Composable (for future aggregation into basin-wide indicators)

This is the data layer that a Bioregional Financing Facility would need to track outcomes: river levels, watershed health, and social-ecological indicators.
