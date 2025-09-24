# 🌫️ Air Quality Classifier (with Parameters)
**Model:** GradientBoostingClassifier to predict risk of NAAQS exceedance.  
**Compliance angle:** NEMAQA + NAAQS; group risks by **station** and optionally by **company** via station→company mapping.

## Workflow
1. **🏁 Overview + Parameters**: set context thresholds (optional) and upload a `station,company` mapping CSV (optional).  
2. **📥 Data Intake**: upload **labeled training data** (must contain `exceedance` = 0/1).  
3. **🤖 Model**: train the classifier on your tenant dataset (`tenants/<workspace>/data/air.csv`).  
4. **🧪 Scoring + Compliance**: score new unlabeled data, review exceedance risk by **station** and **company**.

## Sample files
- `samples/sample_training_air.csv` → ready to upload in **Data Intake** (has `exceedance` labels).  
- `samples/sample_station_company_map.csv` → optional mapping for **Overview + Parameters**.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
