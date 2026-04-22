import numpy as np
import pandas as pd
from pathlib import Path


# Создаем папку data, если её нет
Path("data").mkdir(exist_ok=True)

np.random.seed(42)
n_points = 2000
dates = pd.date_range("2022-01-01", periods=n_points, freq="h")
trend = np.linspace(50, 80, n_points)
daily = 10 * np.sin(2 * np.pi * np.arange(n_points)/24)
weekly = 5 * np.sin(2 * np.pi * np.arange(n_points)/168)
noise = np.random.normal(0, 2, n_points)
outliers = np.zeros(n_points)
outlier_idx = np.random.choice(n_points, size=int(0.02*n_points), replace=False)
outliers[outlier_idx] = np.random.uniform(30, 60, size=len(outlier_idx))
value = trend + daily + weekly + noise + outliers
value = np.clip(value, 10, 50)
df = pd.DataFrame({"timestamp": dates, "value": np.round(value, 2)})
df.to_csv("data/sensor_data.csv", index=False)
print("Generated data/sensor_data.csv")
