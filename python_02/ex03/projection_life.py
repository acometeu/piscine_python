import pandas as pd
import load_csv
import matplotlib.pyplot as pyplot


def projection_life():
    life_expectancy = load_csv.load("../life_expectancy_years.csv")
    income = load_csv.load("../income_per_person_gdppercapita"
                           "_ppp_inflation_adjusted.csv")
    life_expectancy = life_expectancy[["country", "1900"]]
    life_expectancy.set_index("country", inplace=True)
    life_expectancy.rename(columns={"1900": "Life Expectancy"}, inplace=True)
    income = income[["country", "1900"]]
    income.set_index("country", inplace=True)
    income.rename(columns={"1900": "Gross domestic Product"}, inplace=True)

    data = pd.concat([life_expectancy, income], axis="columns")
    try:
        data.plot.scatter(x="Gross domestic Product", y="Life Expectancy",
                          c="#0080FE", title="1900", logx=True)
    except Exception as error:
        print(error)
        return

    pyplot.show()


def main():
    projection_life()


if (__name__ == "__main__"):
    main()
