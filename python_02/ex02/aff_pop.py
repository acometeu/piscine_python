import load_csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot


def aff_pop():
    data = load_csv.load("../population_total.csv")
    if (data is None) :
        print("Failed loading \"../life_expectancy_years.csv\"")
        return
    
    # filter and rearrange data
    countries = ["Jamaica", "France"]
    data = data[data["country"].isin(countries)]
    data.set_index('country', inplace=True)
    data = data.T

    for col in countries :
        # making masks
        mask_thousands = data.loc[:, col].str.endswith('k')
        mask_million = data.loc[:, col].str.endswith('M')
        mask_billion = data.loc[:, col].str.endswith('B')

        # applying conversion to float
        data.loc[mask_thousands, col] = data.loc[mask_thousands, col].str.rstrip('k').astype(float) * 1000
        data.loc[mask_million, col] = data.loc[mask_million, col].str.rstrip('M').astype(float) * 1000000
        data.loc[mask_billion, col] = data.loc[mask_billion, col].str.rstrip('B').astype(float) * 1000000000

    
    try:
        data.plot(xlabel='Year', ylabel='Population', title="Population Projections", legend=True)
    except Exception as error:
        print(error)
        return

    pyplot.show()


def main():
    aff_pop()


if (__name__ == "__main__"):
    main()
