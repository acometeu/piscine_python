from load_csv import load


def main():
    print(load("../life_expectancy_years.csv"))
    data = "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    print(load(data))
    print(load("../population_total.csv"))
    print(load("../ouioui.csv"))


if (__name__ == "__main__"):
    main()
