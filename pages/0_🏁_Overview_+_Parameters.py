import streamlit as st, pandas as pd
from pathlib import Path
from src.config import load_config, save_config, DEFAULTS

st.title("🏁 Overview + Parameters")
st.markdown("""
This app predicts **air quality exceedance risk** and lets you map **stations → firms/companies** for compliance grouping.
- Set **thresholds** (context only).
- Upload a **station→company** CSV so we can aggregate compliance by company.
""")
WORKSPACE = st.secrets.get("workspace_key","default")
cfg = load_config(WORKSPACE)

st.subheader("Thresholds (context)")
polls = ["PM25","PM10","SO2","NO2","O3","CO"]
cols = st.columns(len(polls))
for i,p in enumerate(polls):
    cfg["thresholds"][p] = cols[i].number_input(p, value=float(cfg["thresholds"].get(p, DEFAULTS["thresholds"][p])))

st.markdown("---")
st.subheader("Station → Company mapping")
st.caption("Upload CSV with columns: station,company")
up = st.file_uploader("Upload mapping CSV", type=["csv"])
if "map_df" not in st.session_state:
    st.session_state["map_df"] = pd.DataFrame(list(cfg.get("station_company_map", {}).items()), columns=["station","company"])
if up:
    df = pd.read_csv(up)
    if {"station","company"}.issubset(df.columns):
        st.session_state["map_df"] = df[["station","company"]].dropna()
    else:
        st.error("CSV must contain 'station' and 'company' headers.")
st.dataframe(st.session_state["map_df"] if not st.session_state["map_df"].empty else pd.DataFrame({"station":[], "company":[]}))
if st.button("💾 Save Parameters"):
    cfg["station_company_map"] = dict(zip(st.session_state["map_df"]["station"], st.session_state["map_df"]["company"])) if not st.session_state["map_df"].empty else {}
    p = save_config(WORKSPACE, cfg)
    st.success(f"Saved parameters to {p}")
