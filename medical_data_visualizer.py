import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = ((df['weight']/(df['height']/100)**2)>25).astype(int)

# 3
df['cholesterol'].values[df['cholesterol'].values == 1] = 0
df['cholesterol'].values[df['cholesterol'].values > 1] = 1
df['gluc'].values[df['gluc'].values == 1] = 0
df['gluc'].values[df['gluc'].values > 1] = 1

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, value_vars = ['cholesterol','gluc','smoke','alco','active','overweight'], id_vars = 'cardio')

    # 6
    
    # 7
    df_cat = pd.DataFrame(df_cat.groupby('cardio').value_counts()).reset_index().sort_values(by = 'variable')
    df_cat['value'] = df_cat['value'].astype(str)

    # 8
    fig = sns.catplot(df_cat, 
            x = 'variable', y = 'count', 
            kind = 'bar', 
            errorbar = None, 
            col = 'cardio', 
            hue = 'value').figure

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.copy()
    df_heat = df_heat[(df_heat['height'] >= df_heat['height'].quantile(0.025)) & (df_heat['height'] <= df_heat['height'].quantile(0.975))]
    df_heat = df_heat[(df_heat['weight'] >= df_heat['weight'].quantile(0.025)) & (df_heat['weight'] <= df_heat['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()
    corr.drop('id', axis = 1, inplace = True)
    corr.drop('id', axis = 0, inplace = True)

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize = (14,13))

    # 15
    sns.heatmap(data = corr, mask = mask, linewidths = 0.5)

    # 16
    fig.savefig('heatmap.png', bbox_inches = 'tight')
    return fig
