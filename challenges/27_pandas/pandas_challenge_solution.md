# Pandas Challenge Solutions! 

# Part A: Load in the data

Turns out, you actually have the data on your computer! It lives in `jtc_class_code/datasets/billboard_1978.csv`

1. First, make a new folder called `27_pandas` inside your `jtc_class_code/challenges` folder
    * Then make a new jupyter notebook inside this folder called `pandas_challenge.ipynb`
2. Load it in using `pd.read_csv()` and save it into a variable called songs_1978. 
    * **NOTE:** Since the data file is in a different folder, you'll need to use the `../` syntax to specify exactly where your data live


```python
# import pandas
import pandas as pd
df = pd.read_csv('../../datasets/billboard_1978.csv')
```

# Part B: Inspect the data 

Take a look at the whole DataFrame
### 3. Use `head()` and `tail()` to check out the first and last few rows. Which song ranked #94 on the chart?


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




```python
df.tail(7)
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
      <th>93</th>
      <td>1978</td>
      <td>94</td>
      <td>"Turn to Stone"</td>
      <td>Electric Light Orchestra</td>
      <td>Rock</td>
      <td>15</td>
      <td>13</td>
      <td>Maj</td>
      <td>138</td>
    </tr>
    <tr>
      <th>94</th>
      <td>1978</td>
      <td>95</td>
      <td>"I Can't Stand the Rain"</td>
      <td>Eruption</td>
      <td>Pop</td>
      <td>22</td>
      <td>18</td>
      <td>Maj</td>
      <td>108</td>
    </tr>
    <tr>
      <th>95</th>
      <td>1978</td>
      <td>96</td>
      <td>"Ebony Eyes"</td>
      <td>Bob Welch</td>
      <td>Rock</td>
      <td>17</td>
      <td>14</td>
      <td>Maj</td>
      <td>118</td>
    </tr>
    <tr>
      <th>96</th>
      <td>1978</td>
      <td>97</td>
      <td>"The Name of the Game"</td>
      <td>ABBA</td>
      <td>Pop</td>
      <td>16</td>
      <td>12</td>
      <td>Maj</td>
      <td>76</td>
    </tr>
    <tr>
      <th>97</th>
      <td>1978</td>
      <td>98</td>
      <td>"We're All Alone"</td>
      <td>Rita Coolidge</td>
      <td>Pop</td>
      <td>20</td>
      <td>7</td>
      <td>Maj</td>
      <td>66</td>
    </tr>
    <tr>
      <th>98</th>
      <td>1978</td>
      <td>99</td>
      <td>"Hollywood Nights"</td>
      <td>Bob Seger &amp; The Silver Bullet Band</td>
      <td>Rock</td>
      <td>13</td>
      <td>12</td>
      <td>Maj</td>
      <td>150</td>
    </tr>
    <tr>
      <th>99</th>
      <td>1978</td>
      <td>100</td>
      <td>"Deacon Blues"</td>
      <td>Steely Dan</td>
      <td>Rock</td>
      <td>16</td>
      <td>19</td>
      <td>Maj</td>
      <td>114</td>
    </tr>
  </tbody>
</table>
</div>



'Turn to stone' is ranked 94 on the chart

### 4. How many rows and columns are in this DataFrame?


```python
df.shape
```




    (100, 9)



100 rows, 9 columns

### 5. Which columns have numeric (integer or float) data? 


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 100 entries, 0 to 99
    Data columns (total 9 columns):
     #   Column               Non-Null Count  Dtype 
    ---  ------               --------------  ----- 
     0   Year                 100 non-null    int64 
     1   Hot_Singles_Rank     100 non-null    int64 
     2   Title                100 non-null    object
     3   Artist               100 non-null    object
     4   Genre                100 non-null    object
     5   Weeks_On_Chart       100 non-null    object
     6   Peak_Chart_Position  100 non-null    int64 
     7   Maj_Min              100 non-null    object
     8   BPM                  100 non-null    int64 
    dtypes: int64(4), object(5)
    memory usage: 7.2+ KB


Numeric data in `Year`, `Hot_Singles_Rank`, `Peak_Chart_Position`, `BPM`

### 6. Which columns have strings (listed as 'object' when you run `info()`)?

`Title`, `Artist`, `Genre`, `Weeks_On_Chart`, `Maj_Min`

### 7. What is slowest tempo (minimum BPM) and fastest tempo (maximum BPM) this year?


```python
df.describe()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Hot_Singles_Rank</th>
      <th>Peak_Chart_Position</th>
      <th>BPM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>100.0</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1978.0</td>
      <td>50.500000</td>
      <td>6.940000</td>
      <td>107.700000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.0</td>
      <td>29.011492</td>
      <td>5.112512</td>
      <td>20.396821</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1978.0</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>64.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1978.0</td>
      <td>25.750000</td>
      <td>3.000000</td>
      <td>96.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1978.0</td>
      <td>50.500000</td>
      <td>6.000000</td>
      <td>110.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1978.0</td>
      <td>75.250000</td>
      <td>11.000000</td>
      <td>122.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1978.0</td>
      <td>100.000000</td>
      <td>21.000000</td>
      <td>156.000000</td>
    </tr>
  </tbody>
</table>
</div>



Slowest tempo is 64 and fastest is 156 beats per minute

# Part C: Access specific cells of the dataframe

### 8. The 2nd ranking song in 1978 was called 'Night Fever'. Print out the contents of the cell storing the artist for that song using `.iloc()`
    
    


```python
# the second row (index 1) and the 4th column (index 3)
df.iloc[1,3]
```




    'Bee Gees'



#### Now, print out the contents of the cell storing the genre for that song



```python
# this column is one more to the right (the 5th column), so it is index 4
df.iloc[1,4]
```




    'Pop'



### 9. Print out the name of song ranking 50 on the chart 
    * (hint: which row of the dataframe will this be?)


```python
# tricky because the 50th song is at row index 49 since indexing starts at 0
df.iloc[49, 2]
```




    '"Thunder Island"'


