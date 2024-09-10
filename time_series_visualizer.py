import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = read_csv('fcc-forum-pageviews.csv', index_col = 'date', parse_dates = True)

# Clean data
df = df[(df.value >= df.value.quantile(0.025)) & (df.value <= df.value.quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize = (16,5))
    ax.plot(df, color = '#990a0a')
    ax.set_ylabel('Page Views')
    ax.set_xlabel('Date')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace = True)
    df_bar['Month'] = df_bar.date.dt.month_name()
    df_bar['Year'] = df_bar.date.dt.year
    df_bar['Month_No'] = df_bar.date.dt.month
    df_bar = df_bar.groupby(['Month', 'Year']).mean().reset_index().sort_values('Month_No')

    # Draw bar plot
    fig = sns.catplot(data = df_bar, kind = 'bar', x = 'Year', y = 'value', hue = 'Month', palette = 'tab10', height = 5, aspect = 8/5, facet_kws=dict(despine=False))
    fig.set_axis_labels('Years','Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month_no'] = [d.month for d in df_box.date]
    df_box = df_box.sort_values('month_no')

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(ncols = 2, figsize = (17, 8))

    ax[0] = sns.boxplot(df_box, x ='year', y = 'value', fliersize = 2, ax = ax[0]) 
    ax[0].set_ylabel('Page Views')
    ax[0].set_xlabel('Year')
    ax[0].set_title('Year-wise Box Plot (Trend)')
    
    ax[1] = sns.boxplot(df_box, x = 'month', y = 'value', fliersize = 2, ax = ax[1])
    ax[1].set_ylabel('Page Views')
    ax[1].set_xlabel('Month')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
