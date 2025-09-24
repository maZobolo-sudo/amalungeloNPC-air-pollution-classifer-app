import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score, precision_recall_fscore_support
FEATURES = ["PM25","PM10","SO2","NO2","O3","CO","Temp","RH","Wind"]
TARGET = "exceedance"
def train(df: pd.DataFrame):
    X, y = df[FEATURES], df[TARGET].astype(int)
    Xtr,Xte,ytr,yte = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)
    m = GradientBoostingClassifier(random_state=42).fit(Xtr,ytr)
    proba = m.predict_proba(Xte)[:,1]; pred = (proba>=0.5).astype(int)
    auc = roc_auc_score(yte, proba)
    prec,rec,f1,_ = precision_recall_fscore_support(yte, pred, average="binary")
    return m, {"auc":float(auc),"precision":float(prec),"recall":float(rec),"f1":float(f1)}
def predict(model, df: pd.DataFrame):
    return model.predict_proba(df[FEATURES])[:,1]
