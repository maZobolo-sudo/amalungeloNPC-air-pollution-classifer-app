import streamlit as st, pandas as pd
from pathlib import Path
st.title("📥 Data Intake")
up = st.file_uploader("Upload station-day CSV with columns PM25, PM10, SO2, NO2, O3, CO, Temp, RH, Wind, exceedance, station", type=["csv"])
if not up: st.stop()
df = pd.read_csv(up)
WORKSPACE = st.secrets.get("workspace_key","default")
p = Path(f"tenants/{WORKSPACE}/data/air.csv"); p.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(p, index=False); st.success(f"Saved to {p}"); st.dataframe(df.head())
