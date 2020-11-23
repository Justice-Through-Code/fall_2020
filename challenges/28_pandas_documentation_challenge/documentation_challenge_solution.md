# 1. Import pandas and load the `billboard_1978.csv` dataset into a DataFrame

As a reminder, `billboard_1978.csv` is in your `jtc_class_code/datasets` folder


```python
import pandas as pd
df = pd.read_csv('../../datasets/billboard_1978.csv')
```

# 2. Print out the top 7 rows of the DataFrame


```python
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Hot_Singles_Rank</th>
      <th>Title</th>
      <th>Artist</th>
      <th>Genre</th>
      <th>Weeks_On_Chart</th>
      <th>Peak_Chart_Position</th>
      <th>Maj_Min</th>
      <th>BPM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1978</td>
      <td>1</td>
      <td>"Shadow Dancing"</td>
      <td>Andy Gibb</td>
      <td>Pop</td>
      <td>25</td>
      <td>1</td>
      <td>Min</td>
      <td>102</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1978</td>
      <td>2</td>
      <td>"Night Fever"</td>
      <td>Bee Gees</td>
      <td>Pop</td>
      <td>20</td>
      <td>1</td>
      <td>Min</td>
      <td>110</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1978</td>
      <td>3</td>
      <td>"You Light Up My Life"</td>
      <td>Debby Boone</td>
      <td>Country</td>
      <td>25</td>
      <td>1</td>
      <td>Maj</td>
      <td>78</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1978</td>
      <td>4</td>
      <td>"Stayin' Alive"</td>
      <td>Bee Gees</td>
      <td>Pop</td>
      <td>27</td>
      <td>1</td>
      <td>Min</td>
      <td>103</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1978</td>
      <td>5</td>
      <td>"Kiss You All Over"</td>
      <td>Exile</td>
      <td>Country</td>
      <td>23</td>
      <td>1</td>
      <td>Maj</td>
      <td>104</td>
    </tr>
  </tbody>
</table>
</div>



# 3. Use the pandas docs to figure out how to sort the DataFrame so the fastest songs are at the top. Also, sort the DataFrame 'in place' without having to assign to a variable

Solution:
* df.[sort_values()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html) page of docs
* add the `ascending = False` argument to switch to descending order
* add the `inplace = True` argument to sort in place


```python
df.sort_values(by = 'BPM', ascending = False, inplace = True)
```

# 4. Use the pandas docs to find out how to remove the `Genre` and `Maj_Min` columns from the DataFrame (while keeping the rest)

Make sure you save the resulting DataFrame, either in place, or by assigning a new variable

Hint: one way to phrase this is 'dropping' columns

Solution:
* [df.drop()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html#pandas.DataFrame.drop) in docs


Two straightforward ways:
* `df.drop(columns = ['Genre', 'Maj_Min'])`
* `df.drop(labels = ['Genre', 'Maj_Min'], axis = 1)`



```python
# method 1 ()
df.drop(columns = ['Genre', 'Maj_Min'], inplace = True)
```

# 5. Using [this page from the Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.lower.html) as a starting point, find a way to make song titles all lower case and song artists all caps.

Remember, each column in a DataFrame object is a data type called `Series` (or `pandas.Series`)

Solution: This one is a little tricky! 
* First, remember that how we can get a column of a DataFrame (or a `Series`) 
* Then we can use `df['Title'].str.lower()` to access the strings in the column and make them lower case
* Then we save them back into `df['Title']` again


```python
df['Title'] = df['Title'].str.lower()
```


```python
df['Artist'] = df['Artist'].str.upper()
```


```python
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Hot_Singles_Rank</th>
      <th>Title</th>
      <th>Artist</th>
      <th>Weeks_On_Chart</th>
      <th>Peak_Chart_Position</th>
      <th>BPM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>74</th>
      <td>1978</td>
      <td>75</td>
      <td>"always and forever"</td>
      <td>HEATWAVE</td>
      <td>20</td>
      <td>18</td>
      <td>156</td>
    </tr>
    <tr>
      <th>98</th>
      <td>1978</td>
      <td>99</td>
      <td>"hollywood nights"</td>
      <td>BOB SEGER &amp; THE SILVER BULLET BAND</td>
      <td>13</td>
      <td>12</td>
      <td>150</td>
    </tr>
    <tr>
      <th>76</th>
      <td>1978</td>
      <td>77</td>
      <td>"serpentine fire"</td>
      <td>EARTH, WIND &amp; FIRE</td>
      <td>18</td>
      <td>13</td>
      <td>140</td>
    </tr>
    <tr>
      <th>69</th>
      <td>1978</td>
      <td>70</td>
      <td>"what's your name"</td>
      <td>LYNYRD SKYNYRD</td>
      <td>18</td>
      <td>13</td>
      <td>138</td>
    </tr>
    <tr>
      <th>93</th>
      <td>1978</td>
      <td>94</td>
      <td>"turn to stone"</td>
      <td>ELECTRIC LIGHT ORCHESTRA</td>
      <td>15</td>
      <td>13</td>
      <td>138</td>
    </tr>
  </tbody>
</table>
</div>



# 6. Using the Pandas docs, find a way to export your finished DataFrame to a new csv file called `billboard_1978_cleaned.csv`

#### Bonus: can you get this file to be output right back into the `jtc_class_code/datasets/` folder?

Solution:
* A great place to start here is the [IO tools](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html) section of the pandas docs
* Or, the [df.to_csv()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html) page in the API reference section
* For the bonus: the key is in realizing that just like with *reading* the csv, we can specify full file paths outside the working directory using Unix-like syntax for writing files

Tip: you can add the `index = False` argument when saving to avoid writing an additional column of indexes


```python
df.to_csv('../../datasets/billboard_1978_cleaned.csv', index= False)
```

# 7. Wrap-up: comment your code (including pasting in any links to the docs where you found solutions) and push your .ipynb file to github

Congrats on finishing this challenge!
