import streamlit as st, pandas as pd, joblib, matplotlib.pyplot as plt
from pathlib import Path
from src.model import FEATURES, predict
st.title("🧪 Scoring + Compliance")
WORKSPACE = st.secrets.get("workspace_key","default")
mp = Path(f"tenants/{WORKSPACE}/models/air_model.joblib")
if not mp.exists(): st.warning("Train a model first."); st.stop()
model = joblib.load(mp)
up = st.file_uploader("Upload station-day CSV to score", type=["csv"])
thr = st.slider("Exceedance risk threshold", 0.0, 1.0, 0.5, 0.01)
if up:
    df = pd.read_csv(up)
    proba = predict(model, df)
    df["exceed_risk"] = proba; df["flag_exceed"] = (proba>=thr).astype(int)
    st.dataframe(df.head())
    rate = df["flag_exceed"].mean()
    st.metric("Predicted exceedance share", f"{rate:.0%}")
    fig = plt.figure(figsize=(6,3)); df.groupby("station")["flag_exceed"].mean().mul(100).plot(kind="bar"); plt.ylabel("% exceed risk")
    st.pyplot(fig)
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download scored CSV", csv, "air_scored.csv", "text/csv")
