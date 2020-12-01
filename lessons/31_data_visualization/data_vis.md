# Data Visualization: Pandas + Seaborn

Today is the last lesson for the data science unit, and we will be doing **data visualization!** Data visualization is all about **communicating** things about the data. For example, data visualization can:
* Tell a story
* Make a comparison between things
* Show relationships or patterns
* Show changes over time


Today's lesson will be using a library called [seaborn](https://seaborn.pydata.org/) with pandas to make graphs. Seaborn is **very** flexible, so it is worth browsing the documentation to come up with ideas for lots of beautiful graphs you can make. 



## Setup

First we'll import pandas and seaborn. Usually, we import seaborn as `sns`


```python
import pandas as pd
import seaborn as sns
import numpy as np
```

    /Users/paul/anaconda3/lib/python3.7/site-packages/statsmodels/tools/_testing.py:19: FutureWarning: pandas.util.testing is deprecated. Use the functions in the public API at pandas.testing instead.
      import pandas.util.testing as tm


We also do 2 more things:
* `import matplotlib.pyplot as plt` -- this is another plotting software that seaborn is built on. We'll need it when we save our plots at the end ([docs](https://matplotlib.org/))
* run this command `%matplotlib inline` to ensure that our plots all show up in our jupyter notebooks 


```python
import matplotlib.pyplot as plt
%matplotlib inline
```

### Loading in 2017 census data

For today's lesson we'll use data from the 2017 census. Let's load it in and explore the columns.
* Each row describes **one county**


```python
df = pd.read_csv('../../datasets/census.csv')
df.head(4)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FIPS</th>
      <th>Geography</th>
      <th>population</th>
      <th>median_age</th>
      <th>total_households</th>
      <th>median_household_income</th>
      <th>avg_household_size</th>
      <th>total_families</th>
      <th>avg_family_size</th>
      <th>pct_owner_occupied_units</th>
      <th>pop_16_years_or_older</th>
      <th>unemployment_pct</th>
      <th>population_group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10100</td>
      <td>Aberdeen, SD Micro Area</td>
      <td>42608</td>
      <td>37.8</td>
      <td>17907</td>
      <td>54533</td>
      <td>2.29</td>
      <td>11172</td>
      <td>2.89</td>
      <td>67.5</td>
      <td>33671</td>
      <td>1.8</td>
      <td>Low Population</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10140</td>
      <td>Aberdeen, WA Micro Area</td>
      <td>71454</td>
      <td>43.5</td>
      <td>28070</td>
      <td>45483</td>
      <td>2.44</td>
      <td>17782</td>
      <td>3.00</td>
      <td>66.1</td>
      <td>58156</td>
      <td>10.1</td>
      <td>Low Population</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10180</td>
      <td>Abilene, TX Metro Area</td>
      <td>169000</td>
      <td>33.9</td>
      <td>60369</td>
      <td>48156</td>
      <td>2.57</td>
      <td>39949</td>
      <td>3.12</td>
      <td>62.4</td>
      <td>133221</td>
      <td>4.4</td>
      <td>Low Population</td>
    </tr>
    <tr>
      <th>3</th>
      <td>10220</td>
      <td>Ada, OK Micro Area</td>
      <td>38289</td>
      <td>35.5</td>
      <td>14512</td>
      <td>46689</td>
      <td>2.54</td>
      <td>9459</td>
      <td>3.07</td>
      <td>64.0</td>
      <td>30079</td>
      <td>5.1</td>
      <td>Low Population</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 917 entries, 0 to 916
    Data columns (total 13 columns):
     #   Column                    Non-Null Count  Dtype  
    ---  ------                    --------------  -----  
     0   FIPS                      917 non-null    int64  
     1   Geography                 917 non-null    object 
     2   population                917 non-null    int64  
     3   median_age                917 non-null    float64
     4   total_households          917 non-null    int64  
     5   median_household_income   917 non-null    int64  
     6   avg_household_size        917 non-null    float64
     7   total_families            917 non-null    int64  
     8   avg_family_size           917 non-null    float64
     9   pct_owner_occupied_units  917 non-null    float64
     10  pop_16_years_or_older     917 non-null    int64  
     11  unemployment_pct          917 non-null    float64
     12  population_group          917 non-null    object 
    dtypes: float64(5), int64(6), object(2)
    memory usage: 93.3+ KB


# Continuous vs. Categorical

Before we make any graphs, it is important to know when a variable is **continuous vs. categorical** (check out [this resource](https://support.minitab.com/en-us/minitab-express/1/help-and-how-to/modeling-statistics/regression/supporting-topics/basics/what-are-categorical-discrete-and-continuous-variables/#:~:text=Categorical%20variables%20contain%20a%20finite,not%20have%20a%20logical%20order.&text=Continuous%20variables%20are%20numeric%20variables,be%20numeric%20or%20date%2Ftime.)) We won't spend a ton of time on this but:
* Continuous variables are ones that exist on a continuum (like a spectrum). 
    * For example, age (years) or height (inches). 
    * Continuous variables are usually **int** or **float** data types
* Categorical variables are ones that can only fall into certain categories. 
    * For example, state ('New York', 'California', etc) or political party ('Democrat', 'Republican', 'Independent') 
    * Categorical variables are usually **strings**, although a categorical variable with only 2 possibilieis (i.e. 'tumor' vs' no tumor') could be a **boolean**

# Histograms

Histograms are a great way to see how a **continuous** variable is distribued. Let's try it out with the `sns.distplot()` function:


```python
sns.distplot(df['median_age'])
```




    <matplotlib.axes._subplots.AxesSubplot at 0x128112310>




![](images/output_10_1.png)



```python
sns.distplot(df['avg_household_size'])
```




    <matplotlib.axes._subplots.AxesSubplot at 0x128b5e090>




![](images/output_11_1.png)


# Categorical plots

Now, let's say we want to do the equivalent, but a variable is categorical? What can we do?

We can use something called `sns.catplot()` for this, or a 'categorical plot'. Here, we can compare and see how many counties there were in each population group:


```python
sns.catplot(x="population_group", kind="count", data=df)
```




    <seaborn.axisgrid.FacetGrid at 0x128c617d0>




![](images/output_13_1.png)


So, here we can see that there are many more counties in the 'High Population' group compared to the 'Low Population' one

# Scatter plots

Now, it can be helpful to know the relationship between **multiple** variables. If both are continuous, a scatterplot is a great way to do this. We can use `sns.scatterplot()`

* Notice that now we have to define the `data`, `x`, and `y` parameters to specify where each piece of the graph goes


```python
sns.scatterplot(data = df, x = 'median_household_income', y = 'unemployment_pct')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x128d9d710>




![](images/output_16_1.png)


### Scatterplot + line of best fit

We aren't going to talk about the stats behind this much, but it can be really helpful to add a line visualizing the best fit of a **linear relationship** between two continuous variables. We can do this by using the same syntax as a scatterplot, but using `sns.lmplot()` instead (the lm stands for 'linear model'). Check out the [docs here](https://seaborn.pydata.org/generated/seaborn.lmplot.html)


```python
sns.lmplot(data = df, x = 'median_household_income', y = 'unemployment_pct')
```




    <seaborn.axisgrid.FacetGrid at 0x128cb0d90>




![](images/output_18_1.png)


# Scatterplot + groups

We can break up the scatterplot into different colors by groups too, using the `hue` argument


```python
sns.lmplot(data = df, x = 'median_household_income', y = 'unemployment_pct', hue = 'population_group')
```




    <seaborn.axisgrid.FacetGrid at 0x128fa29d0>




![](images/output_20_1.png)


# Comparing categories

What if we want to compare different groups (categorical variable) to each other? Seaborn lets us do that too in a few different ways, with the categorical variable on the x-axis and a continuous one on the y axis

## Barplots

We can do these with `sns.barplot()`. Again, we specify, `data`, `x`, and `y`, only x is categorical now.
* So, here we compare the median household income in counties with low vs. high population


```python
sns.barplot(data = df, x = 'population_group', y = 'median_household_income')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1292e9150>




![](images/output_22_1.png)


What is the barplot showing exactly? Well, the **height** of the bar is, by default, the **average** household income in each group, and the little lines show the [standard error](https://en.wikipedia.org/wiki/Standard_error), or a measure of how certain we are about that average. 

## Boxplots

Boxplots are very similar in syntax to bar graphs, but they show the data a little differently. The inside box shows the 25% quantile, the median (50% quantile), and the 75% quantile. So, we can think about this as showing the box where **half** the data points fall. The points show outliers


```python
sns.boxplot(data = df, x = 'population_group', y = 'median_household_income')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x129069e10>




![](images/output_25_1.png)


We can also get rid of the outlier points on the graph by setting `fliersize=0`


```python
sns.boxplot(data = df, x = 'population_group', y = 'median_household_income', fliersize=0)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x12bd45d90>




![](images/output_27_1.png)


# Changing figure size

We can resize a figure with the following code -- the two numbers are `(width, height)`.

This is REALLY helpful for when we are saving figures out to files


```python
sns.set(rc={'figure.figsize':(10,6)})
```


```python
sns.boxplot(data = df, x = 'population_group', y = 'median_household_income', fliersize=0)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x12b467310>




![](images/output_30_1.png)


Another example


```python
sns.set(rc={'figure.figsize':(3,3)})
sns.boxplot(data = df, x = 'population_group', y = 'median_household_income', fliersize=0)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x12c01d890>




![](images/output_32_1.png)


# Labels

It is always good to give our graphs clear labels so we can communicate the point effectively! 

So, let's relabel the x and y axes, and give it a title to make it more clear

To do this, we want to do 2 things:
1. Assign the plot to a variable
2. Use the `.set()` method to set `xlabel`, `ylabel`, and `title` as strings with that variable


```python
sns.set(rc={'figure.figsize':(6,7)})

# assign the plot to a variable
my_plt = sns.boxplot(data = df, x = 'population_group', y = 'median_household_income', fliersize=0)

# set labels
my_plt.set(xlabel='County Size', ylabel='Unemployment %', title='Median income ($) in small vs. large counties')
```




    [Text(0, 0.5, 'Unemployment %'),
     Text(0.5, 0, 'County Size'),
     Text(0.5, 1.0, 'Median income ($) in small vs. large counties')]




![](images/output_34_1.png)


# Style!

This part is fun. We can change the look and feel of a plot by setting the style!

We can also change things like
* font
* palette (the color palette used)
* font size

We can do this by using `sns.set()` with a variety of arguments


```python
sns.set(style="ticks",font="Arial",palette="Pastel1",font_scale=2)
sns.boxplot(data = df, x = 'population_group', y = 'median_household_income', fliersize=0)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x12c9a0650>




![](images/output_36_1.png)



```python
sns.set(style="white",palette="Pastel2",font_scale=1)
sns.boxplot(data = df, x = 'population_group', y = 'median_household_income', fliersize=0)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x12c816750>




![](images/output_37_1.png)


# Saving plots to files!

If we wanted to, we **could** take screenshots of our graphs, but these typically are low-resolution -- not great for presentations, websites, posters, etc. It is much better to save as images or pdf files!

Importantly, it helps to run the plot saving code **in the same cell** as when the plot was created
* We can save most seaborn plots using the `plt.savefig()` command with a file path to the eventual file inside


```python
sns.set(rc={'figure.figsize':(8,8)})
sns.boxplot(data = df, x = 'population_group', y = 'median_household_income')

# save to png file
plt.savefig('my_plot_1.png')

# save to pdf file
plt.savefig('my_plot_1.pdf')
```


![](images/output_39_0.png)


### Another example




```python
# set the plot size
sns.set(rc={'figure.figsize':(10,8)})

# set the style
sns.set(style="whitegrid",font="Arial",palette="Pastel1")

# make the lm plot
ax = sns.lmplot(data = df, x = 'median_household_income', y = 'unemployment_pct', hue = 'population_group')
ax.set(xlabel = 'County Median Household Income ($)', ylabel = 'County Unemployment Rate (%)', 
       title = 'Unemployment as a function of median income')

# save to png file
plt.savefig('my_plot_2.png')

# save to pdf file
plt.savefig('my_plot_2.pdf')
```


![](images/output_41_0.png)


# Wrap-up

This lesson has had a LOT of content, but hopefully will be useful for your data science needs going forward! We learned how to make a lot of different plots, and how to customize them a lot.
* However, this is just the tip of the iceburg. There are a lot more kinds of graphs that you can make, and you can explore them through the [Seaborn gallery](https://seaborn.pydata.org/examples/index.html)
* Plotting is definitely not easy! Often, it can take many tries to get a graph to show up the way you want, or to make a point clearly. If you choose to work on more data science going forward, these will be valuable skills to practice.
