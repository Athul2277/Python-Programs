
import pandas as pd
from scipy.stats import ks_2samp

baseline = pd.read_csv("baseline_data.csv")
current = pd.read_csv("current_data.csv")
for column in baseline.select_dtypes(include="number").columns:
    if column in current.columns:
        result = ks_2samp(baseline[column].dropna(), current[column].dropna())
        print(column, "Drift detected:", result.pvalue < 0.05)
