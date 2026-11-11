import numpy as np
from scipy.stats import ttest_ind

def calculate_average(df, column):
    return df[column].mean()

def simulate_disease_probability(df, n=1000):
    disease_probability = df["disease"].mean()
    np.random.seed(42)
    simulated_disease = np.random.binomial(1, disease_probability, n)

    return simulated_disease.mean()

def calculate_confidence_interval(df, column):
    data = df[column]

    mean = data.mean()
    std = data.std()
    n = len(data)

    standard_error = std / np.sqrt(n)
    margin = 1.96 * standard_error

    lower = mean - margin
    upper = mean + margin

    return lower, upper

def test_smoker_blood_pressure(df):
    smokers = df[df["smoker"] == "Yes"]["systolic_bp"]
    non_smokers = df[df["smoker"] == "No"]["systolic_bp"]

    t_stat, p_value = ttest_ind(smokers, non_smokers, equal_var=False, alternative="greater")

    return t_stat, p_value