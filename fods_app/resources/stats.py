"""Statistical functions for data analysis."""

import numpy as np
import pandas as pd


# Functions for loading the dataset
def root_dir() -> str:
    """Return the root directory for the dataset.

    Returns:
        str: The root directory path.
    """
    return "../data"


def data_path(filename: str) -> str:
    """Return the directory for a given filename.

    Args:
        filename (str): The name of the file.

    Returns:
        str: The directory path for the file.
    """
    return root_dir() + "/" + filename


def load_data(filename: str, chunk_size: int = -1) -> pd.DataFrame | list[pd.DataFrame]:
    """Load the healthcare dataset from a specified file path.

    Args:
        filename (str): The name of the file containing the dataset.
        chunk_size (int, optional): The number of rows in each chunk (default is -1).
    Returns:
        pd.DataFrame | list[pd.DataFrame]: A DataFrame containing the loaded dataset,
        or a list of DataFrame chunks when `chunk_size > 0`.
    """
    path = data_path(filename)
    _df = pd.read_csv(path)

    if chunk_size > 0:
        return choping(pd.read_csv(path), chunk_size=chunk_size)
    return _df


# Chopping data into smaller pieces
def choping(_df, chunk_size=1000):
    """Chop a DataFrame into smaller pieces.
    Args:
        _df (pd.DataFrame): The DataFrame to chop.
        chunk_size (int, optional): The number of rows in each chunk (default is 1000).
    Returns:
        list: A list of DataFrame chunks.
    """
    df_list = []
    for chunk in _df.groupby(_df.index // chunk_size):
        df_list.append(chunk[1])
    return df_list


# Grouping and Aggregating Data
def summarize(_df, group_by, value_col, agg="mean", sort=True):
    """Summarize a DataFrame by grouping and aggregating values.

    Args:
        _df (pd.DataFrame): The DataFrame to summarize.
        group_by (str): The column name to group by.
        value_col (str): The column name to aggregate.
        agg (str, optional): The aggregation function to use (default is "mean").
        sort (bool, optional): Whether to sort the results by the aggregated values (default is True).
    Returns:
        pd.DataFrame: A summarized DataFrame with the aggregated values.
    """
    results = _df.groupby(group_by)[value_col].agg(agg)
    if sort:
        results = results.sort_values(ascending=False)
    return results


# Identify Outliers in the Dataset
def above_percentile(_df, group_by, value_col, q=0.9) -> pd.DataFrame:
    """Identify rows in a DataFrame where the value in a specified column is above a certain percentile.

    Args:
        _df (pd.DataFrame): The DataFrame to analyze.
        group_by (str): The column name to group by.
        value_col (str): The column name to evaluate for outliers.
        q (float, optional): The percentile threshold to use for identifying outliers (default is 0.9).
    Returns:
        pd.DataFrame: A DataFrame containing rows where the value in the specified column is above the given percentile.
    """
    results = summarize(_df, group_by, value_col, agg="mean", sort=False)
    threshold = results.quantile(q)
    return _df[_df[value_col] > threshold]
