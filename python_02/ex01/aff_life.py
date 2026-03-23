import load_csv
import matplotlib.pyplot as pyplot


def aff_life():
    data = load_csv.load("../life_expectancy_years.csv")
    if (data is None) :
        print("Failed loading \"../life_expectancy_years.csv\"")
        return
    
    # filter and rearrange data
    data_france = data[data["country"] == "France"]
    data_france.set_index('country', inplace=True)
    data_france = data_france.T

    try:
        data_france.plot(xlabel='Year', ylabel='Life expectancy', title="France life expectency Projections", legend=False)
    except Exception as error:
        print(error)
        return
    pyplot.show()


def main():
    aff_life()


if (__name__ == "__main__"):
    main()
