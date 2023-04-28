import os
import requests
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def styled_print(text, header=False):
    """Custom Print Function"""

    class style:
        BOLD = "\033[1m"
        UNDERLINE = "\033[4m"
        END = "\033[0m"

    if header:
        print(f"{style.BOLD}› {style.UNDERLINE}{text}{style.END}")
    else:
        print(f"    {text}")


def process_timestamp(dataframe, column, drop=True):
    dataframe[column] = pd.to_datetime(dataframe[column])
    dataframe["hour"] = dataframe[column].dt.hour
    dataframe["day"] = dataframe[column].dt.day
    dataframe["month"] = dataframe[column].dt.month
    dataframe["year"] = dataframe[column].dt.year
    dataframe["dayofweek"] = dataframe[column].dt.dayofweek
    dataframe["dayofyear"] = dataframe[column].dt.dayofyear
    if drop:
        dataframe = dataframe.drop(column, axis=1)
    return dataframe


def plot_box_plot_hist_plot(
    df,
    column,
    title="Distribution Plot",
    figsize=(16, 16),
    dpi=300,
    save_flag=False,
    file_path=None,
):
    fig, (ax_box, ax_hist) = plt.subplots(
        nrows=2,
        sharex=True,
        figsize=figsize,
        gridspec_kw={"height_ratios": (0.20, 0.80)},
        dpi=dpi,
        constrained_layout=False,
    )
    sns.boxplot(data=df, x=column, ax=ax_box)
    sns.histplot(data=df, x=column, ax=ax_hist, kde=True, bins="sqrt")
    ax_box.set(xlabel="")
    ax_box.set_facecolor("white")
    ax_hist.set_facecolor("white")
    plt.title(title)
    if save_flag:
        fig.savefig(file_path, dpi=dpi, facecolor="white")
        plt.close()


def plot_box_plot_dis_plot(
    df,
    column,
    title="Distribution Plot",
    figsize=(16, 16),
    dpi=300,
    save_flag=False,
    file_path=None,
):
    fig, (ax_box, ax_dis) = plt.subplots(
        nrows=2,
        sharex=True,
        figsize=figsize,
        gridspec_kw={"height_ratios": (0.20, 0.80)},
        dpi=dpi,
        constrained_layout=False,
    )
    sns.boxplot(data=df, x=column, ax=ax_box)
    sns.kdeplot(data=df, x=column, ax=ax_dis)
    ax_box.set(xlabel="")
    ax_box.set_facecolor("white")
    ax_dis.set_facecolor("white")
    plt.title(title)
    if save_flag:
        fig.savefig(file_path, dpi=dpi, facecolor="white")
        plt.close()
