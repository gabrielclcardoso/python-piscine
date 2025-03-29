from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def main():
    data = load("life_expectancy_years.csv")
    data.set_index('country', inplace=True)
    points = data.loc['Brazil']
    print(points)

    fig, ax = plt.subplots()
    ax.plot(points)

    ax.set_xlabel('Year')
    ax.set_ylabel('Life expectancy')
    ax.set_title('Brazil Life expectancy Projections')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(40))

    plt.show()


if __name__ == "__main__":
    main()
