from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def main():
    data = load("population_total.csv")
    if data is None:
        print("Error: file not found")
        exit(1)

    data.set_index('country', inplace=True)
    data = data.loc[:, :'2050']
    p1 = data.loc['Brazil']
    p2 = data.loc['Thailand']

    fig, ax = plt.subplots()

    ax.plot(p1.apply(to_float), label=p1.name)
    ax.plot(p2.apply(to_float), label=p2.name)

    ax.set_xlabel('Year')
    ax.set_ylabel('Population')
    ax.set_title('Population Projections')
    ax.legend()

    formatter = ticker.FuncFormatter(to_string)
    ax.yaxis.set_major_formatter(formatter)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(40))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(2e7))

    plt.show()


def to_float(string: str) -> float:
    """Transforms a string with a possible letter at the end to a float"""
    scale = 1

    if string[-1] == 'M':
        scale = 1e6
        string = string.removesuffix('M')
    elif string[-1] == 'k':
        scale = 1e3
        string = string.removesuffix('k')

    n = float(string)
    return n * scale


def to_string(n: float, pos) -> str:
    """Transforms a float to a string with a letter at the end for numbers
    bigger than 1000
    """
    if abs(n) > 1e6:
        return f'{n/1e6:.0f}M'
    elif abs(n) > 1e3:
        return f'{n/1e3:.0f}k'
    else:
        return f'{n:.0f}'


if __name__ == "__main__":
    main()
