


"""
Data Link:
    https://www.kaggle.com/zynicide/wine-reviews
    
"""



import pandas as pd
import seaborn as sns


df = pd.read_csv('winemag-data_first150k.csv', index_col=0)



# Bar chart
sns.countplot(df['points'])


# Seabor does not have direct analogue of Pandas line or area chart
# but have "kdeplot"

sns.kdeplot(df.query('price < 200').price)


# Two-dimensional KDE plot
sns.kdeplot(df[df['price'] < 20].loc[:,['price','points']].dropna().sample(5000))


# Histogram
sns.distplot(df['points'], bins=10, kde=False)


# Joinplot
sns.jointplot(x='price', y='points', data=df[df['price'] < 100])

sns.jointplot(x='price', y='points', data=df[df['price'] < 100], kind='hex', 
              gridsize=20)



# Box and Violin plot
new_df = df[df.variety.isin(df.variety.value_counts().head(5).index)]

sns.boxplot(x='variety', y='points', data=new_df)

sns.violinplot(x='variety', y='points', data=new_df)



