# How It Works — Tana River Basin Watershed Data Aggregator

---

## The short version

It's deliberately lightweight — no custom infrastructure to maintain.

Data is aggregated, written to a static JSON file, and GitHub Pages serves the dashboard. No complex backend or database. Just public data points forming a commons.

---

## Data sources

Currently, the system uses a comprehensive mock data generator (`generate_tana_data.py`) that simulates the holistic health of the Tana River Basin ecosystem:

### 1. River Flow & Levels
Water levels at key stations like the Garissa Bridge, including discharge rates and flood thresholds.

### 2. Vegetation Health
Vegetation Condition Index (VCI) across key counties (Garissa, Tana River, Kitui) to track drought and ecological health.

### 3. Headwater Health
Forest cover percentages, streamflow trends, and deforestation alerts in the upper basin (Nyeri/Nyandarua).

### 4. Biodiversity
Tracking movements of key species like Elephants (Route 13) and the endangered Hirola Antelope.

### 5. Economic Value Flows
Metrics on livestock offtake and the status of solar-powered cold-chain infrastructure.

### 6. Governance
Tracking the status of Community Forest Associations (CFAs) and allocations of climate and conservation grants.

### 7. Warm Data (Traditional Ecological Knowledge)
Insights from indigenous oracles and local communities regarding weather anomalies, seasonal expectations, and holistic basin health.

---

## Architecture

```
Data Generation Script (generate_tana_data.py)
    → generate mock data across 7 dimensions
    → write docs/data.json
GitHub Pages
    → serve index.html + data.json as static site
```

No server. No database. The entire pipeline runs via a Python script in `/src`. Legacy scripts for fetching raw gauge and reservoir data are preserved in the repository for future adaptation.

---

## Why static?

Sampling data periodically is appropriate for a watershed health overview — the kind of data that informs coordination decisions, not real-time operations. This approach keeps maintenance low and transparency high.
