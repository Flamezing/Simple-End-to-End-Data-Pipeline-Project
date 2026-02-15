import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def load_data():
    return pd.read_csv("background_noise_focus_dataset.csv")


def clean_data(df):
    df = df.drop_duplicates()
    return df


def transform_participant_id(df):

    df = df.copy()

    # parse
    series = pd.to_numeric(
        df["participant_id"], errors="coerce"
    )
    
    if series.isna().any():
        raise ValueError("participant_id contains invalid value")

    series = series.astype(int)

    if not series.is_unique:
        raise ValueError("participant_id must be unique")
    
    # normalize
    df["participant_id"] = series

    df = df.sort_values("participant_id")
    
    if not df["participant_id"].is_monotonic_increasing:
        raise ValueError("participant_id must be monotonic_increasing")

    return df


def transform_age(df):

    df = df.copy()

    # parse
    series = pd.to_numeric(
        df["age"], errors="coerce"
    )
    
    if series.isna().any():
        raise ValueError("age contains invalid value")

    # normalize
    df["age"] = series
    return df


def transform_noise_volume_level(df):

    df = df.copy()

    series = pd.to_numeric(
        df["noise_volume_level"], errors="coerce"
    )
    
    if series.isna().any():
        raise ValueError("noise_volume_level contains invalid value")
    
    if not series.between(1, 10).all():
        raise ValueError("noise_volume_level must be between 1 and 10")
    
    df["noise_volume_level"] = series
    return df


def transform_focus_duration_minutes(df):

    df = df.copy()

    series = pd.to_numeric(
        df["focus_duration_minutes"], errors="coerce"
    )
    
    if series.isna().any():
        raise ValueError("focus_duration_minutes contains invalid value")
    
    if not series.between(10, 120).all():
        raise ValueError("focus_duration_minutes must be between 10 and 120")
    
    df["focus_duration_minutes"] = series
    return df


def transform_perceived_focus_score(df):

    df = df.copy()

    series = pd.to_numeric(
        df["perceived_focus_score"], errors="coerce"
    )
    
    if series.isna().any():
        raise ValueError("perceived_focus_score contains invalid value")
    
    if not series.between(1, 10).all():
        raise ValueError("perceived_focus_score must be between 1 and 10")
    
    df["perceived_focus_score"] = series
    return df


def transform_task_completion_quality(df):

    df = df.copy()

    series = pd.to_numeric(
        df["task_completion_quality"], errors="coerce"
    )
    
    if series.isna().any():
        raise ValueError("task_completion_quality contains invalid value")
    
    if not series.between(1, 10).all():
        raise ValueError("task_completion_quality must be between 1 and 10")
    
    df["task_completion_quality"] = series
    return df


def transform_mental_fatigue_after_task(df):

    df = df.copy()

    series = pd.to_numeric(
        df["mental_fatigue_after_task"], errors="coerce"
    )
    
    if series.isna().any():
        raise ValueError("mental_fatigue_after_task contains invalid value")
    
    if not series.between(1, 10).all():
        raise ValueError("mental_fatigue_after_task must be between 1 and 10")
    
    df["mental_fatigue_after_task"] = series
    return df

def main():
    df = load_data()
    df = clean_data(df)
    df = transform_participant_id(df)
    df = transform_age(df)
    df = transform_noise_volume_level(df)
    df = transform_focus_duration_minutes(df)
    df = transform_perceived_focus_score(df)
    df = transform_task_completion_quality(df)
    df = transform_mental_fatigue_after_task(df)

    df.to_csv("clean_data.csv", index=False)

    print("Pipeline success")


if __name__ == "__main__":
    main()