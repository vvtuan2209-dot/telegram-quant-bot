import xgboost as xgb
import numpy as np

def train(X,y):

    model = xgb.XGBClassifier(
        n_estimators=120,
        max_depth=4,
        learning_rate=0.1
    )

    model.fit(X,y)
    return model


def predict(model,X):

    p = model.predict_proba(X)[0]

    return {str(i).zfill(2): float(p[i]) for i in range(len(p))}
