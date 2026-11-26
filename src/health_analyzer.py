
import numpy as np


class HealthAnalyzer:
    """
    En klass som utför analyser av hälsodata.
    """

    def __init__(self, df):
        self.df = df

    def calculate_average(self, column):
        """
        Beräknar medelvärdet för en vald kolumn.
        """
        return self.df[column].mean()

    def calculate_median(self, column):
        """
        Beräknar medianen för en vald kolumn.
        """
        return self.df[column].median()

    def calculate_standard_deviation(self, column):
        """
        Beräknar standardavvikelsen för en vald kolumn.
        """
        return self.df[column].std()

    def predict_blood_pressure(self):
        """
        Beräknar en linjär regression för att uppskatta systoliskt blodtryck utifrån ålder.

        Returnerar lutningen och interceptet för modellen.
        """
        ages = self.df["age"].values
        blood_pressure = self.df["systolic_bp"].values
        X = np.column_stack((ages, np.ones(len(ages))))

        coefficients = np.linalg.lstsq(X, blood_pressure, rcond=None)[0]

        return coefficients

    def predict_for_age(self, age):
        """
        Uppskattar det systoliska blodtrycket för en viss ålder.

        Parametrar:
            age: Åldern som blodtrycket ska uppskattas för.

        Returnerar:
            Det uppskattade systoliska blodtrycket.
        """
        slope, intercept = self.predict_blood_pressure()
        predicted = slope * age + intercept

        return predicted
