"""
Created on Sat May 18 2019

@author: Nodar Okroshiashvili
"""





"""
Data link:
    https://www.kaggle.com/zynicide/wine-reviews
    
"""




import pandas as pd



df = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)



# Start plotting

from plotnine import *
from plotnine import options



top_wines = df[df['variety'].isin(df['variety'].value_counts().head(5).index)]


###      Scatter Plot     ###

f = top_wines.head(1000).dropna()

(ggplot(f)
 + aes('points', 'price')
 + geom_point())


# We can add a regression line with a stat_smooth layer:

(ggplot(f)
 + aes('points', 'price')
 + geom_point()
 + stat_smooth())


# Add color

(ggplot(f)
 + aes(color='points')
 + aes('points', 'price')
 + geom_point()
 + stat_smooth())



# Apply faceting, use facet_wrap


(ggplot(f)
+ aes('points','price')
+ aes(color='points')
+ geom_point()
+ stat_smooth()
+ facet_wrap('~variety'))




# Bar chart

(ggplot(top_wines)
+ aes('points')
+ geom_bar())




# Hexplot or two-dimensional histogram

(ggplot(top_wines)
+ aes('points', 'variety')
+ geom_bin2d(bins=20))



# Prettify plot
options.figure_size=(10,10)
(ggplot(top_wines)
+ aes('points', 'variety')
+ geom_bin2d(bins=20)
+ coord_fixed(ratio=1)
+ ggtitle('Top Five Most Common Wine Variety Points Awarded'))



