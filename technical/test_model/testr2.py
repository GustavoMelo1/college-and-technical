import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score

df = pd.read_csv("dados_analise_process_seletivo.csv")  
df["period"] = pd.to_datetime(df["period"])
df = df.sort_values("period").reset_index(drop=True)
 
df["mes"] = df["period"].dt.month
df["trimestre"] = df["period"].dt.quarter
df["ano"] = df["period"].dt.year
 
features = ["mes", "trimestre", "ano"]
X = df[features]
y = df["target"]
 
teste = df["prediction"].notna()
X_treino, y_treino = X[~teste], y[~teste]
X_teste, y_teste = X[teste], y[teste]


#model testtttttttttttttttt
modelo = GradientBoostingRegressor(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=2,
    random_state=42,
)
modelo.fit(X_treino, y_treino)       
pred_gb = modelo.predict(X_teste)   

r2_gb = r2_score(y_teste, pred_gb)

y_prev = df.loc[teste, "prediction"]
r2_prediction = r2_score(y_teste, y_prev)

#results

print("results column prediction:", round(r2_prediction, 3))
print("training model results:", round(r2_gb, 3))