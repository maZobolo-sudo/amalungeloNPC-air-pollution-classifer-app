import json
from pathlib import Path
def config_path(workspace: str):
    p = Path(f"tenants/{workspace}/config"); p.mkdir(parents=True, exist_ok=True)
    return p / "air_params.json"
DEFAULTS = {
    "thresholds": {"PM25": 25.0, "PM10": 75.0, "SO2": 125.0, "NO2": 200.0, "O3": 120.0, "CO": 10.0},
    "station_company_map": {}
}
def load_config(workspace: str):
    p = config_path(workspace)
    if not p.exists():
        return DEFAULTS.copy()
    try:
        return json.loads(p.read_text())
    except Exception:
        return DEFAULTS.copy()
def save_config(workspace: str, cfg: dict):
    p = config_path(workspace)
    p.write_text(json.dumps(cfg, indent=2))
    return p
