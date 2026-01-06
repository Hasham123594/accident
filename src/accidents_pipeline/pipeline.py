from __future__ import annotations

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA = Path("data/accidents_2017_to_2023_english.csv")
OUT = Path("outputs")


def load_data() -> pd.DataFrame:
    return pd.read_csv(DATA)


def accidents_by_cause(df: pd.DataFrame) -> pd.DataFrame:
    out = (
        df.groupby("cause_of_accident")["total_injured"]
        .sum()
        .reset_index()
        .sort_values("total_injured", ascending=False)
        .head(10)
    )
    return out


def accidents_by_weekday(df: pd.DataFrame) -> pd.DataFrame:
    return df["week_day"].value_counts().reset_index(
        name="count"
    ).rename(columns={"index": "week_day"})


def plot_top_causes(df: pd.DataFrame, path: Path) -> None:
    plt.figure(figsize=(10, 6))
    plt.barh(df["cause_of_accident"], df["total_injured"])
    plt.xlabel("Total Injuries")
    plt.ylabel("Cause of Accident")
    plt.title("Top 10 Causes of Accidents by Total Injuries")
    plt.gca().invert_yaxis()
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def plot_weekdays(df: pd.DataFrame, path: Path) -> None:
    plt.figure(figsize=(8, 5))
    plt.bar(df["week_day"], df["count"])
    plt.xlabel("Week Day")
    plt.ylabel("Number of Accidents")
    plt.title("Accidents by Week Day")
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def run_pipeline() -> dict[str, Path]:
    OUT.mkdir(exist_ok=True)

    df = load_data()

    top_causes = accidents_by_cause(df)
    weekdays = accidents_by_weekday(df)

    clean_csv = OUT / "top_causes_by_injuries.csv"
    top_causes.to_csv(clean_csv, index=False)

    fig_causes = OUT / "top_causes.png"
    fig_weekdays = OUT / "accidents_by_weekday.png"

    plot_top_causes(top_causes, fig_causes)
    plot_weekdays(weekdays, fig_weekdays)

    return {
        "data": clean_csv,
        "top_causes_plot": fig_causes,
        "weekday_plot": fig_weekdays,
    }


def main() -> None:
    outputs = run_pipeline()
    for k, v in outputs.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
