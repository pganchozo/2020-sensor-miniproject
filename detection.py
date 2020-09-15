#!/usr/bin/env python3
"""
This example assumes the JSON data is saved one line per timestamp (message from server).

It shows how to read and process a text file line-by-line in Python, converting JSON fragments
to per-sensor dictionaries indexed by time.
These dictionaries are immediately put into Pandas DataFrames for easier processing.

Feel free to save your data in a better format--I was just showing what one might do quickly.
"""
import pandas
from pathlib import Path
import argparse
import json
from datetime import datetime
from scipy import stats
import typing as T
import matplotlib.pyplot as plt
import numpy as np
import statistics


def load_data(file: Path) -> T.Dict[str, pandas.DataFrame]:

    temperature = {}
    occupancy = {}
    co2 = {}

    with open(file, "r") as f:
        for line in f:
            r = json.loads(line)
            room = list(r.keys())[0]
            time = datetime.fromisoformat(r[room]["time"])

            temperature[time] = {room: r[room]["temperature"][0]}
            occupancy[time] = {room: r[room]["occupancy"][0]}
            co2[time] = {room: r[room]["co2"][0]}

    data = {
        "temperature": pandas.DataFrame.from_dict(temperature, "index").sort_index(),
        "occupancy": pandas.DataFrame.from_dict(occupancy, "index").sort_index(),
        "co2": pandas.DataFrame.from_dict(co2, "index").sort_index(),
    }

    return data



if __name__ == "__main__":

    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    file = Path(P.file).expanduser()
    data = load_data(file)
    temperature = data["temperature"]
    total_outliers = []

    # iterate through every room that has temperature data

    for k in temperature:

        current_mean = temperature[k].mean()
        current_std = temperature[k].std()

        # lower and upper limits are three standard deviations away from the mean
        lower_limit = current_mean - (current_std*3)
        upper_limit = current_mean + (current_std*3)
        outliers = []

        # if the value being analyzed is above/below the limits defined above
        # those values are saved to an array "total_outliers"
        for i in temperature[k]:
            if i > upper_limit or i < lower_limit:
                outliers.append(i)

        total_outliers.append({k: outliers})
        

    print(total_outliers)
  

