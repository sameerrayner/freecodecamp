import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig, ax = plt.subplots(figsize = (17,7))
    ax.plot(x, y, 'o', ms = 4)

    # Create first line of best fit
    slope, intercept, rvalue, pvalue, stderr = linregress(x, y)
    full_range = np.arange(1880,2051)
    ax.plot(full_range, slope*full_range + intercept, '--')

    # Create second line of best fit
    slope, intercept, rvalue, pvalue, stderr = linregress(x[120:], y[120:])
    later_range = np.arange(2000,2051)
    ax.plot(later_range, slope*later_range + intercept, 'r--')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend(['Yearly Average Sea Level','Projected Sea Level (based on rates 1880-2013)','Projected Sea Level (based on rates 2000-2013)'])
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()