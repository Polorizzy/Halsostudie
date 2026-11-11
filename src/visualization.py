import matplotlib.pyplot as plt


def plot_age_distribution(df):
    plt.figure()
    df["age"].hist()

    plt.xlabel("Age (in years)")
    plt.ylabel("Number of People")
    plt.title("Age Distribution")
    plt.show()


def plot_age_counts(df):
    plt.figure(figsize=(16, 6))

    df["age"].value_counts().sort_index().plot(
        kind="bar",
        title="Age Distribution",
        xlabel="Age",
        ylabel="Count",
        rot=45
    )

    plt.xticks(fontsize=8)
    plt.tight_layout()
    plt.show()


def plot_sex_distribution(df):
    plt.figure(figsize=(8, 6))

    df["sex"].value_counts().plot(
        kind="bar",
        title="Sex Distribution",
        xlabel="Sex",
        ylabel="Count",
        rot=0
    )

    plt.xticks(fontsize=8)
    plt.tight_layout()
    plt.show()

def plot_height_distribution(df):
    plt.figure(figsize=(8, 6))

    df["height"].hist()

    plt.xlabel("Height (in cm)")
    plt.ylabel("Number of people")
    plt.title("Height Distribution")

    plt.tight_layout()
    plt.show()

def plot_weight_distribution(df):
    plt.figure(figsize=(8, 6))

    df["weight"].hist()

    plt.xlabel("Weight (in kg)")
    plt.ylabel("Number of people")
    plt.title("Weight Distribution")

    plt.tight_layout()
    plt.show()

def plot_systolic_bp_distibution(df):
    plt.figure(figsize=(8, 6))

    df["systolic_bp"].hist()

    plt.xlabel("Systolic Blood Pressure (in mmHg)")
    plt.ylabel("Number of people")
    plt.title("Systolic Blood Pressure Distribution")

    plt.tight_layout()
    plt.show()

def plot_cholesterol_distribution(df):
    plt.figure(figsize=(8, 6))

    df["cholesterol"].hist()

    plt.xlabel("Cholesterol in (mg/dL)")
    plt.ylabel("Number of people")
    plt.title("Cholesterol Distribution")

    plt.tight_layout()
    plt.show()

def plot_smoker_distribution(df):
    plt.figure(figsize=(8, 6))

    df["smoker"].value_counts().plot(
        kind="bar",
        title="Smoker Distribution",
        xlabel="Smoker",
        ylabel="Count",
        rot=0
    )

    plt.xticks(fontsize=8)
    plt.tight_layout()
    plt.show()

def plot_disease_distribution(df):
    plt.figure(figsize=(8, 6))

    df["disease"].value_counts().plot(
        kind="bar",
        title="Disease Distribution",
        xlabel="Disease",
        ylabel="Count",
        rot=0
    )

    plt.xticks(fontsize=8)
    plt.tight_layout()
    plt.show()