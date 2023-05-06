import pandas as pd

data = pd.read_csv("data/mimic_pulseOx_data.csv")
data = data[(data.SaO2 <= 100) & (data.SpO2 <= 100) & (data.SaO2 >= 65) & (data.SpO2 >= 65)]
data = data[data['delta_SpO2'] >= -10]

data.to_csv("data/solutions/workshop_1.csv", index=False)

