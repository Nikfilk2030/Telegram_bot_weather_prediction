import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor


def predict(data: pd.DataFrame, regressor: RandomForestRegressor) -> np.ndarray:
    x = data.drop(['tempC'], axis=1)
    return regressor.predict(x).tolist()
