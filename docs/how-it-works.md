# How It Works — Colorado River Basin Watershed Data Aggregator

**Built by Techne Institute / RegenHub, LCA · Boulder, Colorado**

---

## The short version

It's deliberately lightweight — no custom infrastructure to maintain.

A GitHub Actions cron runs twice daily, calls three public APIs, writes fresh data to a static JSON file, and GitHub Pages serves the dashboard. No backend, no database, no real-time stream. Just public data, refreshed twice a day, in the commons.

---

## Data sources

### USGS Water Services API
Free, no authentication required. Updates every 15 minutes at the source.

Stream gauges monitored along the Colorado River mainstem:

| Site | Location | Data |
|---|---|---|
| 09070500 | Colorado R. near Dotsero, CO | Discharge (cfs) |
| 09095500 | Colorado R. near Cameo, CO | Discharge |
| 09163500 | Colorado R. near CO-UT state line | Discharge |
| 09380000 | Colorado R. at Lees Ferry, AZ | Discharge + gage height |
| 09402500 | Colorado R. near Grand Canyon, AZ | Discharge + gage height |
| 09379900 | Glen Canyon Dam (Lake Powell) | Reservoir elevation (ft) |
| 09421500 | Colorado R. below Hoover Dam, AZ-NV | Gage height |

### NRCS SNOTEL — AWDB REST API
Free, no authentication required. Updates daily at the source.

Pulls Snow Water Equivalent (SWE) and precipitation from ~100+ active stations across HUC basins 14 (Upper Colorado) and 15 (Lower Colorado) — covering headwaters in Colorado, Utah, Wyoming, and New Mexico.

### Bureau of Reclamation (via USGS)
Lake Powell and Lake Mead reservoir elevation data accessed via USGS gauge sites co-located with the dams.

---

## Architecture

```
GitHub Actions (twice daily)
    → fetch USGS gauges
    → fetch USGS reservoir levels
    → fetch NRCS SNOTEL snowpack
    → write docs/data.json
GitHub Pages
    → serve index.html + data.json as static site
```

No server. No database. No API keys required. The entire pipeline is ~300 lines of Python in four scripts, visible in `/src`.

---

## Why static?

The USGS and SNOTEL APIs update every 15 minutes to daily. Sampling them twice a day is appropriate for a watershed health overview — the kind of data that informs coordination decisions, not real-time operations.

For higher-resolution monitoring, the same public APIs are there. This is the open floor, not the ceiling.

---

## Open data, open infrastructure

All data sources are public domain. The aggregator code is open source. The dashboard is publicly accessible at no cost.

This is what bioregional public goods look like — built on public data, maintained in the commons, available to anyone coordinating the health of the Colorado River.

**Live dashboard:** https://nou-techne.github.io/watershed-data-collection/  
**Source:** https://github.com/nou-techne/watershed-data-collection  
**Built for:** [owockibot.xyz](https://owockibot.xyz) Bounty #237
