import matplotlib.pyplot as plt
import pandas as pd

def plot_population_trends(dataframe):
    plt.figure(figsize=(10, 5))
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

    # Optionally add text annotation for the population value
    #plt.text(2024, population_2024, f'{population_2024}', horizontalalignment='right', verticalalignment='bottom')
    
    plt.title('Population Projection by Year')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.grid(True)
    plt.legend()
    plt.show()