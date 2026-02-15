import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def load_data():
    return pd.read_csv("clean_data.csv")


def role_count_plot(df):

    role_count = df["role"].value_counts()

    y = np.array([0, 50, 100, 150, 200])

    plt.figure()

    plt.title("Role Count",
              fontsize=20,
              family="Arial",
              fontweight="bold")

    plt.bar(role_count.index, role_count.values)

    plt.yticks(y)

    plt.tick_params(axis="both")

    plt.show()


def noise_focus_plot(df):

    # return the series of unique elements in df["noise_type"] and get its length
    noise_types = df["background_noise_type"].unique()
    n = len(noise_types)

    fig, axes = plt.subplots(
        n, 1,
        figsize=(8, 6*n),
        constrained_layout=True
    )

    # if axes only contains one plot, convert itself into a list for consistency
    if n == 1:
        axes = [axes]

    grouped = df.groupby("background_noise_type")

    for ax, noise in zip(axes, noise_types):

        # seperate df by "background_noise_type" into subsets
        subset = grouped.get_group(noise)

        # .value_counts() : count the value of "perceived_focus_score", default sorted by count
        # .sort_index() : sort the series by index
        scores = subset["perceived_focus_score"] \
                    .value_counts() \
                    .sort_index()

        ax.plot(scores.index, scores.values)

        ax.set_title(f"{noise} - Focus Score")
        ax.set_xlabel("Perceived Focus Score")
        ax.set_ylabel("Count")

    plt.show()
    

def main():
    df = load_data()
    role_count_plot(df)
    noise_focus_plot(df)


if __name__ == "__main__":
    main()