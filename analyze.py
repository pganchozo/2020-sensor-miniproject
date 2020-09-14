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

    # Task 2 part d
    dates = data["temperature"].index

    # find the time interval between each batch of data being sent
    seconds = dates[1:]-dates[:-1]
    interval = [t.total_seconds() for t in seconds]
    interval_series = pandas.Series(interval)

    # Find mean and variance of the time interval
    interval_mean = interval_series.mean()
    interval_var = interval_series.var()

    interval_series.plot.kde()

    print("The mean of the time interval is " + str(interval_mean))
    print("The variance of the time interval is " + str(interval_var))


    for k in data:

        print("time index:")

        # Task 2 part a
        print("Median for the temperature:")
        print(data["temperature"].median())

        print("Variance for the temperature:")
        print(data["temperature"].var())

        # Task 2 part b
        print("Median for the occupancy:")
        print(data["occupancy"].median())

        # find variance of each sensor
        print("Variance for the occupancy:")
        print(data["occupancy"].var())

        
    #     data[k].plot()
    #     time = data[k].index
    #     data[k].hist()
    #     plt.figure()
    #     plt.hist(np.diff(time.values).astype(np.int64) // 1000000000)
    #     plt.xlabel("Time (seconds)")

          # Task 2 part c
    #     # plot pdf of each sensor
    #     data[k].plot.kde()



    plt.show()
