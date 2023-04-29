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


def plot_count_plot(
    df,
    column,
    hue=None,
    title="Count Plot",
    figsize=(24, 24),
    dpi=300,
    save_flag=False,
    file_path=None,
):
    fig, axs = plt.subplots(1, 1, figsize=figsize, dpi=dpi, constrained_layout=False)
    pt = sns.countplot(data=df, x=column, hue=hue, palette=sns.color_palette("Set2"))
    pt.set_xticklabels(pt.get_xticklabels(), rotation=30)
    if hue is not None:
        axs.legend(loc="upper right", title=hue)
    axs.set_facecolor("white")
    plt.title(title)
    if save_flag:
        fig.savefig(file_path, dpi=dpi, facecolor="white")
        plt.close()


def plot_categorical_feature_one_way(
    df,
    column,
    target,
    order=None,
    title="OneWay Plot",
    figsize=(16, 16),
    dpi=300,
    save_flag=False,
    file_path=None,
):
    """
    Plots the trend plots for categorical features.
    Arguments:
        df: DataFrame. Pandas dataframe of the dataset under analysis.
        column: String. Name of the column or feature to create one way plot.
        target: String. Name of the column for target feature.
        title: String. Title for the plot.
        figsize: Tuple. Size of figure.
        dpi: Integer. DPI of saved image of graph.
        save_flag: Boolean. Whether to save the plot as image or not.
        file_path: String. Image path to save the plot as image.
    """
    df[column] = df[column].astype("category")
    if order == None:
        order = df[column].value_counts().index
        categories = list(order)
    else:
        categories = list(order)
    ind = np.array([x for x, _ in enumerate(categories)])

    # TO DO : Replace mean with other statistics
    mean_target = df.groupby(column)[target].mean()
    y = np.array([mean_target[cat] for cat in categories])

    fig, axs = plt.subplots(1, 1, figsize=figsize, dpi=dpi, constrained_layout=False)
    axs = sns.countplot(data=df, x=column, order=categories)
    axs.set_xticklabels(axs.get_xticklabels(), rotation=30)

    axs2 = axs.twinx()
    sns.lineplot(x=ind, y=y, ax=axs2, marker="D", markersize=12)

    axs.set_facecolor("white")
    axs2.set_facecolor("white")
    plt.title(title)
    if save_flag:
        fig.savefig(file_path, dpi=dpi, facecolor="white")
        plt.close()


def plot_correlation(
    corr,
    mask,
    title="Correlation Heatmap",
    figsize=(16, 16),
    save_flag=False,
    file_path=None,
):
    fig = plt.figure(figsize=figsize)
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    sns.heatmap(corr, mask=mask, annot=True, cmap=cmap, fmt=".2f", vmin=-1.0, vmax=1.0)
    plt.title(title)
    if save_flag:
        fig.savefig(file_path)
        plt.close()


def correlation_analysis(
    df,
    method="pearson",
    save_flag=False,
    plot_dir="plots",
    title=None,
    prefix="Correlation_Matrix",
    postfix="",
    figsize=(24, 24),
):
    # Calculate correlation matrix.
    corr = df.corr(method=method, numeric_only=True)
    plot_correlation(
        corr=corr,
        mask=np.triu(np.ones_like(corr, dtype=bool)),
        title=f"{prefix}{title}{postfix}",
        figsize=figsize,
        save_flag=save_flag,
    )
    return corr
