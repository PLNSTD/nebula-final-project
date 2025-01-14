import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import io

def plot_population_trends(dataframe, country):
    fig = plt.figure(figsize=(10, 5))
    plt.plot(dataframe['population_year'], dataframe['population'], marker='o')
    
    # Disable scientific notation
    ax = plt.gca() # Get the current axis
    ax.ticklabel_format(style='plain', axis='y')

    # Add commas to the y-axis labels
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))
    
    # Drawing a vertical line at year 2024
    population_2024 = dataframe[dataframe['population_year'] == 2024]['population'].values[0]
    # Draw a vertical line for the year 2024
    # plt.axvline(x=2024, color='r', linestyle='--', label='Year 2024')
    plt.plot([2024, 2024], [0, population_2024], color='r', linestyle='--', label='Year 2024')

    # Plot the population value for 2024
    plt.scatter(2024, population_2024, color='red', zorder=5)  # Dot on the line

    plt.title(f'{country} Population Projection by Year')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.grid(True)
    plt.legend()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)

    return buf

def plot_population_comparison_trends(dataframes, countries):
    fig = plt.figure(figsize=(10, 5))

    for country in countries:
        dataframe = dataframes[country]  # Get the dataframe for the country
        plt.plot(dataframe['population_year'], dataframe['population'], marker='o', label=country)
        
        # Disable scientific notation
        ax = plt.gca()  # Get the current axis
        ax.yaxis.set_major_formatter(ticker.ScalarFormatter())
        ax.ticklabel_format(style='plain', axis='y')

        # Add commas to the y-axis labels
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

        # Drawing a vertical line at year 2024
        if 2024 in dataframe['population_year'].values:
            population_2024 = dataframe[dataframe['population_year'] == 2024]['population'].values[0]
            plt.plot([2024, 2024], [0, population_2024], color='r', linestyle='--', label=f'{country} - Year 2024')

            # Plot the population value for 2024
            plt.scatter(2024, population_2024, color='red', zorder=5)  # Dot on the line

    plt.title('Comparison Population Projection by Year')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.grid(True)
    plt.legend()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)

    return buf
