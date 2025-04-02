from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def main():
    gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy = load("life_expectancy_years.csv")
    if gdp is None or life_expectancy is None:
        print("Error: file not found")
        exit(1)

    gdp_filtered = gdp["1900"]
    le_filtered = life_expectancy["1900"]

    fig, ax = plt.subplots()
    ax.scatter(gdp_filtered, le_filtered)

    ax.set_title('1900')
    ax.set_ylabel('Life Expectancy')
    ax.set_xlabel('Gross domestic product')

    ax.set_xscale('log')
    ax.xaxis.set_major_locator(ticker.FixedLocator([300, 1e3, 1e4]))
    ax.set_xlim(left=300)
    ax.xaxis.set_major_formatter(to_str)

    plt.show()


def to_str(n: float, pos) -> str:
    """Converts large floats into readable strings"""
    if n > 1e6:
        return f'{n/1e6:.0f}M'
    elif n > 1e3:
        return f'{n/1e3:.0f}k'
    else:
        return str(int(n))


if __name__ == "__main__":
    main()
