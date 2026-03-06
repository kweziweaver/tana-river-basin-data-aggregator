import json
import random
from datetime import datetime, timedelta, timezone

def generate_mock_data():
    now = datetime.now(timezone.utc)
    data = {
        "fetched_at": now.isoformat(),
        "river_flow": [],
        "vegetation_health": [],
        "headwater_health": {},
        "biodiversity": [],
        "economic_value": {},
        "governance": {},
        "warm_data": {}
    }

    # 1. River Flow & Levels: Water levels at the Garissa Bridge
    # Coordinates for Garissa Bridge: -0.4532, 39.6461
    data["river_flow"].append({
        "station_name": "Garissa Bridge (WRA)",
        "latitude": -0.4532,
        "longitude": 39.6461,
        "water_level_m": round(random.uniform(2.5, 4.8), 2),  # meters
        "flood_threshold_m": 4.5,
        "discharge_m3s": round(random.uniform(150, 450), 1), # cubic meters per second
        "status": "Normal" if random.random() > 0.1 else "Alert",
        "updated_at": (now - timedelta(hours=random.randint(0, 11))).isoformat()
    })

    # 2. Vegetation Health: Vegetation Condition Index (VCI)
    # Different counties in the basin: Garissa, Tana River, Kitui
    counties = [
        {"name": "Garissa County", "lat": -0.45, "lon": 39.65},
        {"name": "Tana River County", "lat": -1.5, "lon": 40.0},
        {"name": "Kitui County", "lat": -1.36, "lon": 38.01}
    ]
    for c in counties:
        vci = round(random.uniform(20, 60), 1) # 0-100 scale
        status = "Severe Drought" if vci < 35 else "Moderate Drought" if vci < 50 else "Normal"
        data["vegetation_health"].append({
            "county": c["name"],
            "latitude": c["lat"],
            "longitude": c["lon"],
            "vci_score": vci,
            "status": status,
            "updated_at": (now - timedelta(days=random.randint(0, 2))).isoformat()
        })

    # 3. Headwater Health: Forest cover & streamflow in Nyeri/Nyandarua
    data["headwater_health"] = {
        "region": "Upper Basin (Nyeri/Nyandarua)",
        "latitude": -0.41,
        "longitude": 36.95,
        "forest_cover_pct": round(random.uniform(15.0, 25.0), 1),
        "streamflow_trend": random.choice(["Stable", "Declining", "Improving"]),
        "deforestation_alerts": random.randint(0, 5),
        "updated_at": (now - timedelta(days=random.randint(1, 5))).isoformat()
    }

    # 4. Biodiversity & Migration: Elephant Route 13 and Hirola
    data["biodiversity"] = [
        {
            "species": "Elephant (Route 13)",
            "tracked_individuals": random.randint(12, 30),
            "location_cluster": {
                "latitude": round(random.uniform(-1.0, -0.5), 4),
                "longitude": round(random.uniform(39.0, 39.8), 4)
            },
            "movement_status": random.choice(["Migrating South", "Foraging", "Stationary"]),
            "updated_at": (now - timedelta(hours=random.randint(1, 10))).isoformat()
        },
        {
            "species": "Hirola Antelope",
            "tracked_individuals": random.randint(40, 80),
            "location_cluster": {
                "latitude": round(random.uniform(-1.5, -1.2), 4),
                "longitude": round(random.uniform(40.0, 40.5), 4)
            },
            "movement_status": "Grazing (Protected Area)",
            "updated_at": (now - timedelta(days=random.randint(0, 2))).isoformat()
        }
    ]

    # 5. Economic Value Flows: Livestock & Cold-chain
    data["economic_value"] = {
        "livestock_offtake_daily": random.randint(500, 1200),
        "average_price_kes": random.randint(30000, 45000),
        "cold_chain_nodes_active": random.randint(8, 15),
        "solar_uptime_pct": round(random.uniform(92.0, 99.9), 1),
        "updated_at": now.isoformat()
    }

    # 6. Governance Progress: CCRI & CFA
    data["governance"] = {
        "ccri_grants_allocated_kes": random.randint(5000000, 20000000),
        "cfa_restructuring_status": random.choice(["In Progress", "Phase 1 Complete", "Planning"]),
        "active_community_forest_associations": random.randint(10, 25),
        "updated_at": (now - timedelta(days=random.randint(5, 20))).isoformat()
    }

    # 7. Warm Data (TEK): Somali Indigenous Oracles
    data["warm_data"] = {
        "source": "Somali Indigenous Oracles (Council of Elders)",
        "seasonal_forecast": random.choice([
            "Delayed short rains expected; conserve dry-season grazing areas.",
            "Favorable rains indicated by local flora indicators; prepare for planting.",
            "High likelihood of flash floods in lower basin; move livestock to higher ground."
        ]),
        "community_sentiment": random.choice(["Cautiously Optimistic", "Concerned (Drought)", "Preparing Action"]),
        "updated_at": (now - timedelta(days=random.randint(10, 30))).isoformat()
    }

    return data

if __name__ == "__main__":
    import os
    
    # Ensure docs directory exists
    docs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs")
    os.makedirs(docs_dir, exist_ok=True)
    
    out_path = os.path.join(docs_dir, "data.json")
    
    data = generate_mock_data()
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    
    print(f"Generated Tana Basin mock data at {out_path}")
