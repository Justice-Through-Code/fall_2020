# Before class

* Make sure the [pandas library](https://pandas.pydata.org/) is installed and working on your computer
    * Mostly likely if you have Anaconda installed, you're all set. To confirm this, open up a jupyter notebook and run `import pandas` in a python cell. If you get no error message, you're all set!
    * If you do get an error message, run `$ pip install pandas` from your command line to install it. After installing, repeat the previous step to check if the installation worked
* Download the [spotify_top_tens.csv file](https://github.com/Justice-Through-Code/fall_2020) from Github, and put this file in a folder called `datasets` inside your jtc course folder on your computer

# Outline of class agenda

During this class you'll:

1. Learn how to import data from a .csv file into a dataframe object
2. Learn what a dataframe is, and why it is useful
3. Get comfortable working the the [pandas documentation & user guide](https://pandas.pydata.org/docs/user_guide/index.html#user-guide) for working with dataframes
4. Get accustomed to inspecting dataframes
    * Printing out the contents of dataframes
    * Looking at the first (`head()`) or last (`tail()`) few rows of dataframes
    * Inspecting the shape (rows and columns) of dataframes with `shape()`
    * Getting summaries of the dataframe contents using `info()` and `describe()`
5. Learn how to access specific cells of DataFrame objects with `iloc()` and bracket indexing

# Class

## 1) Importing data from a csv file into a dataframe

Often in python, we'll want to work with data from files already stored on our computer or on the internet, such as csv files. Pandas will give us a way to do this!

First, let's import the pandas library. We'll do this every time we use pandas. Most often, we abbreviate it as 'pd'


```python
import pandas as pd
```

Now, we can read in a csv file. To do this, we use `pd.read_csv()`, with the path to our csv file as an input argument. In this case, let's read the 'spotify_top_tens.csv' file that you put in your datasets folder.

**Importantly**, when we read csv files (or any other files) with python, there are a few things to remember:
* File paths are always formatted as strings (i.e. they should have quotes around them)
* File paths work basically the same way we learned in bash, where the `/` character indicates going into a folder, and `../` means going 'up' one level out of a folder


```python
pd.read_csv('../../datasets/spotify_top_tens.csv')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>artist</th>
      <th>top genre</th>
      <th>year</th>
      <th>bpm</th>
      <th>nrgy</th>
      <th>dnce</th>
      <th>dB</th>
      <th>live</th>
      <th>val</th>
      <th>dur</th>
      <th>acous</th>
      <th>spch</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Hey, Soul Sister</td>
      <td>Train</td>
      <td>neo mellow</td>
      <td>2010</td>
      <td>97</td>
      <td>89</td>
      <td>67</td>
      <td>-4</td>
      <td>8</td>
      <td>80</td>
      <td>217</td>
      <td>19</td>
      <td>4</td>
      <td>83</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Love The Way You Lie</td>
      <td>Eminem</td>
      <td>detroit hip hop</td>
      <td>2010</td>
      <td>87</td>
      <td>93</td>
      <td>75</td>
      <td>-5</td>
      <td>52</td>
      <td>64</td>
      <td>263</td>
      <td>24</td>
      <td>23</td>
      <td>82</td>
    </tr>
    <tr>
      <td>2</td>
      <td>TiK ToK</td>
      <td>Kesha</td>
      <td>dance pop</td>
      <td>2010</td>
      <td>120</td>
      <td>84</td>
      <td>76</td>
      <td>-3</td>
      <td>29</td>
      <td>71</td>
      <td>200</td>
      <td>10</td>
      <td>14</td>
      <td>80</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Bad Romance</td>
      <td>Lady Gaga</td>
      <td>dance pop</td>
      <td>2010</td>
      <td>119</td>
      <td>92</td>
      <td>70</td>
      <td>-4</td>
      <td>8</td>
      <td>71</td>
      <td>295</td>
      <td>0</td>
      <td>4</td>
      <td>79</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Just the Way You Are</td>
      <td>Bruno Mars</td>
      <td>pop</td>
      <td>2010</td>
      <td>109</td>
      <td>84</td>
      <td>64</td>
      <td>-5</td>
      <td>9</td>
      <td>43</td>
      <td>221</td>
      <td>2</td>
      <td>4</td>
      <td>78</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>598</td>
      <td>Find U Again (feat. Camila Cabello)</td>
      <td>Mark Ronson</td>
      <td>dance pop</td>
      <td>2019</td>
      <td>104</td>
      <td>66</td>
      <td>61</td>
      <td>-7</td>
      <td>20</td>
      <td>16</td>
      <td>176</td>
      <td>1</td>
      <td>3</td>
      <td>75</td>
    </tr>
    <tr>
      <td>599</td>
      <td>Cross Me (feat. Chance the Rapper &amp; PnB Rock)</td>
      <td>Ed Sheeran</td>
      <td>pop</td>
      <td>2019</td>
      <td>95</td>
      <td>79</td>
      <td>75</td>
      <td>-6</td>
      <td>7</td>
      <td>61</td>
      <td>206</td>
      <td>21</td>
      <td>12</td>
      <td>75</td>
    </tr>
    <tr>
      <td>600</td>
      <td>No Brainer (feat. Justin Bieber, Chance the Ra...</td>
      <td>DJ Khaled</td>
      <td>dance pop</td>
      <td>2019</td>
      <td>136</td>
      <td>76</td>
      <td>53</td>
      <td>-5</td>
      <td>9</td>
      <td>65</td>
      <td>260</td>
      <td>7</td>
      <td>34</td>
      <td>70</td>
    </tr>
    <tr>
      <td>601</td>
      <td>Nothing Breaks Like a Heart (feat. Miley Cyrus)</td>
      <td>Mark Ronson</td>
      <td>dance pop</td>
      <td>2019</td>
      <td>114</td>
      <td>79</td>
      <td>60</td>
      <td>-6</td>
      <td>42</td>
      <td>24</td>
      <td>217</td>
      <td>1</td>
      <td>7</td>
      <td>69</td>
    </tr>
    <tr>
      <td>602</td>
      <td>Kills You Slowly</td>
      <td>The Chainsmokers</td>
      <td>electropop</td>
      <td>2019</td>
      <td>150</td>
      <td>44</td>
      <td>70</td>
      <td>-9</td>
      <td>13</td>
      <td>23</td>
      <td>213</td>
      <td>6</td>
      <td>6</td>
      <td>67</td>
    </tr>
  </tbody>
</table>
<p>603 rows × 14 columns</p>
</div>



Great! We've read the csv into a DataFrame object. But *what is* a DataFrame?

## 2) What are pandas DataFrames and why are they useful?

So, if you look at what printed out when you read in the csv file above, you'll notice that it looks a bit like the .csv file if you were to open it in Excel or Numbers. It shows up as a table, with rows and columns, just like a spreadsheet. But what is the DataFrame exactly?

### At one level, pandas DataFrames are a [python class](https://docs.python.org/3/tutorial/classes.html)

We learned about classes a little while ago, and pandas DataFrames are their own class under the hood. This means that they can be instantiated as objects, and they come with their own available functions.

### DataFrames are 2-dimensional, rectangular, labeled datastructures

So far we've spent a lot of time with both lists and dictionaries, and we've talked about how they each have strenghts and weaknesses. DataFrames share some helpful features of both dictionaries and lists, such as:
* Like dictionaries, pandas DataFrames are **labeled**. That means that the data stored inside them is organized so that you can see what each piece means
* Like lists, pandas DataFrames are **ordered**. Pieces of data inside DataFrames have locations that can be indexed numerically. This means, that also like lists, it is possible to use **loops** to iterate through data inside dataframes

**What does it mean that DataFrames are 2-dimensional?**

This means that DataFrames look like spreadsheets, or tables (i.e. 'tabular data'). Dataframes have rows (horizontal slices) and columns (vertical slices), which contain the data inside. 

<img src="https://media.geeksforgeeks.org/wp-content/uploads/finallpandas.png" width="500">


### DataFrames are really useful for data analysis

The table-like shape of DataFrames makes them super useful for working with data, including:
* Organizing, storing, and manipulating data
* Doing statistical analyses
* Making figures and charts
* Machine learning and AI

We'll get into a bunch of these soon!

<img src="https://miro.medium.com/max/666/1*DadyHI0auADUxl5-ft4uSQ.jpeg" width="300">

## 3) The pandas documentation and user guide

We're going to get started learning to work with DataFrames now, but before we do, it is important to know where to go if you want to find features for DataFrames, debug, and learn more.

One great place for all of this is the [pandas documentation](https://pandas.pydata.org/docs/user_guide/index.html#user-guide)! This is essentially a codebook that you can use to look up everything that pandas DataFrames can do.

For example, [here](https://pandas.pydata.org/docs/user_guide/io.html#csv-text-files) is the documetation for the `read_csv()` function we just learned. The page for this function tells us all about the different arguments that can be used for the function, what outputs to expect, and even has example use cases.

When you're trying to figure out how to do something new with DataFrames, or how to debug code using a function you've used before, the documentation is a great resources for figuring things out! 

## 4) Getting accustomed to working with DataFrames

So, when you loaded in the data from the csv file before using `pd.read_csv()`, it printed out. However, most often we'll want to save DataFrames as variables to work with them, as below:


```python
songs = pd.read_csv('../../datasets/spotify_top_tens.csv')
```

Now `songs` is a variable containing the DataFrame

### Printing out the contents of a DataFrame

Often, we'll want to print out the DataFrame to take a quick look at it, or to see what kind of data is stored inside it. *Specifically in jupyter notebooks*, we can view the DataFrame just by typing the variable name as the last line (or only line) in a cell:


```python
songs
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>artist</th>
      <th>top genre</th>
      <th>year</th>
      <th>bpm</th>
      <th>nrgy</th>
      <th>dnce</th>
      <th>dB</th>
      <th>live</th>
      <th>val</th>
      <th>dur</th>
      <th>acous</th>
      <th>spch</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Hey, Soul Sister</td>
      <td>Train</td>
      <td>neo mellow</td>
      <td>2010</td>
      <td>97</td>
      <td>89</td>
      <td>67</td>
      <td>-4</td>
      <td>8</td>
      <td>80</td>
      <td>217</td>
      <td>19</td>
      <td>4</td>
      <td>83</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Love The Way You Lie</td>
      <td>Eminem</td>
      <td>detroit hip hop</td>
      <td>2010</td>
      <td>87</td>
      <td>93</td>
      <td>75</td>
      <td>-5</td>
      <td>52</td>
      <td>64</td>
      <td>263</td>
      <td>24</td>
      <td>23</td>
      <td>82</td>
    </tr>
    <tr>
      <td>2</td>
      <td>TiK ToK</td>
      <td>Kesha</td>
      <td>dance pop</td>
      <td>2010</td>
      <td>120</td>
      <td>84</td>
      <td>76</td>
      <td>-3</td>
      <td>29</td>
      <td>71</td>
      <td>200</td>
      <td>10</td>
      <td>14</td>
      <td>80</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Bad Romance</td>
      <td>Lady Gaga</td>
      <td>dance pop</td>
      <td>2010</td>
      <td>119</td>
      <td>92</td>
      <td>70</td>
      <td>-4</td>
      <td>8</td>
      <td>71</td>
      <td>295</td>
      <td>0</td>
      <td>4</td>
      <td>79</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Just the Way You Are</td>
      <td>Bruno Mars</td>
      <td>pop</td>
      <td>2010</td>
      <td>109</td>
      <td>84</td>
      <td>64</td>
      <td>-5</td>
      <td>9</td>
      <td>43</td>
      <td>221</td>
      <td>2</td>
      <td>4</td>
      <td>78</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>598</td>
      <td>Find U Again (feat. Camila Cabello)</td>
      <td>Mark Ronson</td>
      <td>dance pop</td>
      <td>2019</td>
      <td>104</td>
      <td>66</td>
      <td>61</td>
      <td>-7</td>
      <td>20</td>
      <td>16</td>
      <td>176</td>
      <td>1</td>
      <td>3</td>
      <td>75</td>
    </tr>
    <tr>
      <td>599</td>
      <td>Cross Me (feat. Chance the Rapper &amp; PnB Rock)</td>
      <td>Ed Sheeran</td>
      <td>pop</td>
      <td>2019</td>
      <td>95</td>
      <td>79</td>
      <td>75</td>
      <td>-6</td>
      <td>7</td>
      <td>61</td>
      <td>206</td>
      <td>21</td>
      <td>12</td>
      <td>75</td>
    </tr>
    <tr>
      <td>600</td>
      <td>No Brainer (feat. Justin Bieber, Chance the Ra...</td>
      <td>DJ Khaled</td>
      <td>dance pop</td>
      <td>2019</td>
      <td>136</td>
      <td>76</td>
      <td>53</td>
      <td>-5</td>
      <td>9</td>
      <td>65</td>
      <td>260</td>
      <td>7</td>
      <td>34</td>
      <td>70</td>
    </tr>
    <tr>
      <td>601</td>
      <td>Nothing Breaks Like a Heart (feat. Miley Cyrus)</td>
      <td>Mark Ronson</td>
      <td>dance pop</td>
      <td>2019</td>
      <td>114</td>
      <td>79</td>
      <td>60</td>
      <td>-6</td>
      <td>42</td>
      <td>24</td>
      <td>217</td>
      <td>1</td>
      <td>7</td>
      <td>69</td>
    </tr>
    <tr>
      <td>602</td>
      <td>Kills You Slowly</td>
      <td>The Chainsmokers</td>
      <td>electropop</td>
      <td>2019</td>
      <td>150</td>
      <td>44</td>
      <td>70</td>
      <td>-9</td>
      <td>13</td>
      <td>23</td>
      <td>213</td>
      <td>6</td>
      <td>6</td>
      <td>67</td>
    </tr>
  </tbody>
</table>
<p>603 rows × 14 columns</p>
</div>



Notice that *if the dataframe is very big*, only the first few and last few rows actually display, with a '...' separating them

If you *aren't* using a jupyter notebook (i.e. just working with a python script), this won't work, however. What works in either setting is using the `print()` function. This might not look as nice in a jupyter notebook, but if you're running a .py script from the command line, you'll see the same output.


```python
print(songs)
```

                                                     title            artist  \
    0                                     Hey, Soul Sister             Train   
    1                                 Love The Way You Lie            Eminem   
    2                                              TiK ToK             Kesha   
    3                                          Bad Romance         Lady Gaga   
    4                                 Just the Way You Are        Bruno Mars   
    ..                                                 ...               ...   
    598                Find U Again (feat. Camila Cabello)       Mark Ronson   
    599      Cross Me (feat. Chance the Rapper & PnB Rock)        Ed Sheeran   
    600  No Brainer (feat. Justin Bieber, Chance the Ra...         DJ Khaled   
    601    Nothing Breaks Like a Heart (feat. Miley Cyrus)       Mark Ronson   
    602                                   Kills You Slowly  The Chainsmokers   
    
               top genre  year  bpm  nrgy  dnce  dB  live  val  dur  acous  spch  \
    0         neo mellow  2010   97    89    67  -4     8   80  217     19     4   
    1    detroit hip hop  2010   87    93    75  -5    52   64  263     24    23   
    2          dance pop  2010  120    84    76  -3    29   71  200     10    14   
    3          dance pop  2010  119    92    70  -4     8   71  295      0     4   
    4                pop  2010  109    84    64  -5     9   43  221      2     4   
    ..               ...   ...  ...   ...   ...  ..   ...  ...  ...    ...   ...   
    598        dance pop  2019  104    66    61  -7    20   16  176      1     3   
    599              pop  2019   95    79    75  -6     7   61  206     21    12   
    600        dance pop  2019  136    76    53  -5     9   65  260      7    34   
    601        dance pop  2019  114    79    60  -6    42   24  217      1     7   
    602       electropop  2019  150    44    70  -9    13   23  213      6     6   
    
         pop  
    0     83  
    1     82  
    2     80  
    3     79  
    4     78  
    ..   ...  
    598   75  
    599   75  
    600   70  
    601   69  
    602   67  
    
    [603 rows x 14 columns]


### Viewing the first few rows of the DataFrame with head()

If we want to visualize just the first few rows of the DataFrame, we can use the `head()` function. The syntax for this is:


```python
songs.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>artist</th>
      <th>top genre</th>
      <th>year</th>
      <th>bpm</th>
      <th>nrgy</th>
      <th>dnce</th>
      <th>dB</th>
      <th>live</th>
      <th>val</th>
      <th>dur</th>
      <th>acous</th>
      <th>spch</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Hey, Soul Sister</td>
      <td>Train</td>
      <td>neo mellow</td>
      <td>2010</td>
      <td>97</td>
      <td>89</td>
      <td>67</td>
      <td>-4</td>
      <td>8</td>
      <td>80</td>
      <td>217</td>
      <td>19</td>
      <td>4</td>
      <td>83</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Love The Way You Lie</td>
      <td>Eminem</td>
      <td>detroit hip hop</td>
      <td>2010</td>
      <td>87</td>
      <td>93</td>
      <td>75</td>
      <td>-5</td>
      <td>52</td>
      <td>64</td>
      <td>263</td>
      <td>24</td>
      <td>23</td>
      <td>82</td>
    </tr>
    <tr>
      <td>2</td>
      <td>TiK ToK</td>
      <td>Kesha</td>
      <td>dance pop</td>
      <td>2010</td>
      <td>120</td>
      <td>84</td>
      <td>76</td>
      <td>-3</td>
      <td>29</td>
      <td>71</td>
      <td>200</td>
      <td>10</td>
      <td>14</td>
      <td>80</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Bad Romance</td>
      <td>Lady Gaga</td>
      <td>dance pop</td>
      <td>2010</td>
      <td>119</td>
      <td>92</td>
      <td>70</td>
      <td>-4</td>
      <td>8</td>
      <td>71</td>
      <td>295</td>
      <td>0</td>
      <td>4</td>
      <td>79</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Just the Way You Are</td>
      <td>Bruno Mars</td>
      <td>pop</td>
      <td>2010</td>
      <td>109</td>
      <td>84</td>
      <td>64</td>
      <td>-5</td>
      <td>9</td>
      <td>43</td>
      <td>221</td>
      <td>2</td>
      <td>4</td>
      <td>78</td>
    </tr>
  </tbody>
</table>
</div>



So, here we've just printed out the first few rows of `songs`. How many total rows were printed here?

**Mini-challenge:** It turns out that `head()` can be run with optional arguments to print out a different number of rows. Use the [pandas documentation for this function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html) to find this out, and use it to print out 3 rows.

### Viewing the last few rows of the DataFrame with tail()

As you might suspect, `tail()` works the same way that `head()` does, just with the last rows of the DataFrame instead of the first. Try using this function to print out the last 6 rows of `songs`


```python
songs.tail(n = 6)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>artist</th>
      <th>top genre</th>
      <th>year</th>
      <th>bpm</th>
      <th>nrgy</th>
      <th>dnce</th>
      <th>dB</th>
      <th>live</th>
      <th>val</th>
      <th>dur</th>
      <th>acous</th>
      <th>spch</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>597</td>
      <td>Con Calma - Remix</td>
      <td>Daddy Yankee</td>
      <td>latin</td>
      <td>2019</td>
      <td>94</td>
      <td>87</td>
      <td>74</td>
      <td>-3</td>
      <td>4</td>
      <td>61</td>
      <td>181</td>
      <td>17</td>
      <td>5</td>
      <td>76</td>
    </tr>
    <tr>
      <td>598</td>
      <td>Find U Again (feat. Camila Cabello)</td>
      <td>Mark Ronson</td>
      <td>dance pop</td>
      <td>2019</td>
      <td>104</td>
      <td>66</td>
      <td>61</td>
      <td>-7</td>
      <td>20</td>
      <td>16</td>
      <td>176</td>
      <td>1</td>
      <td>3</td>
      <td>75</td>
    </tr>
    <tr>
      <td>599</td>
      <td>Cross Me (feat. Chance the Rapper &amp; PnB Rock)</td>
      <td>Ed Sheeran</td>
      <td>pop</td>
      <td>2019</td>
      <td>95</td>
      <td>79</td>
      <td>75</td>
      <td>-6</td>
      <td>7</td>
      <td>61</td>
      <td>206</td>
      <td>21</td>
      <td>12</td>
      <td>75</td>
    </tr>
    <tr>
      <td>600</td>
      <td>No Brainer (feat. Justin Bieber, Chance the Ra...</td>
      <td>DJ Khaled</td>
      <td>dance pop</td>
      <td>2019</td>
      <td>136</td>
      <td>76</td>
      <td>53</td>
      <td>-5</td>
      <td>9</td>
      <td>65</td>
      <td>260</td>
      <td>7</td>
      <td>34</td>
      <td>70</td>
    </tr>
    <tr>
      <td>601</td>
      <td>Nothing Breaks Like a Heart (feat. Miley Cyrus)</td>
      <td>Mark Ronson</td>
      <td>dance pop</td>
      <td>2019</td>
      <td>114</td>
      <td>79</td>
      <td>60</td>
      <td>-6</td>
      <td>42</td>
      <td>24</td>
      <td>217</td>
      <td>1</td>
      <td>7</td>
      <td>69</td>
    </tr>
    <tr>
      <td>602</td>
      <td>Kills You Slowly</td>
      <td>The Chainsmokers</td>
      <td>electropop</td>
      <td>2019</td>
      <td>150</td>
      <td>44</td>
      <td>70</td>
      <td>-9</td>
      <td>13</td>
      <td>23</td>
      <td>213</td>
      <td>6</td>
      <td>6</td>
      <td>67</td>
    </tr>
  </tbody>
</table>
</div>



### Determining the number of rows and columns with `shape`

Often, it's very helpful to know the exact dimensions of the DataFrame. We can use the `shape` function to do this, the same way we use `head()`, except without the parenthesis:


```python
songs.shape
```




    (603, 14)



The output from `shape` always comes in this format, as (# of rows, # of columns). 
* How many rows does `songs` have?
* How many columns does `songs` have?

One thing to keep in mind going forward is that when we are thinking about rows and columns in DataFrames, **rows are always considered the first dimension (or axis 0), and columns are the second dimension (or axis 1)**. We'll come back to why this general rule is helpful soon!

### Summarizing the DataFrame contents with `info()`

Sometiems, we might want to get a summary of a DataFrame that tells us what the names of all the columns are, and what type of data is stored in each column. We can do this with `info()`:


```python
songs.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 603 entries, 0 to 602
    Data columns (total 14 columns):
    title        603 non-null object
    artist       603 non-null object
    top genre    603 non-null object
    year         603 non-null int64
    bpm          603 non-null int64
    nrgy         603 non-null int64
    dnce         603 non-null int64
    dB           603 non-null int64
    live         603 non-null int64
    val          603 non-null int64
    dur          603 non-null int64
    acous        603 non-null int64
    spch         603 non-null int64
    pop          603 non-null int64
    dtypes: int64(11), object(3)
    memory usage: 66.1+ KB


This shows us all of the columns in `songs`. For each one, we can see the number of entries (603) that are not-null (i.e. each column has 603 entries with actual data). `int64` indicates that the data in these columns (for example, year, bpm, and nrgy) are integers, and `object` indicates strings.

If we want just a printout of the column labels (without all the info of what is stored inside), we can run:


```python
songs.columns
```




    Index(['title', 'artist', 'top genre', 'year', 'bpm', 'nrgy', 'dnce', 'dB',
           'live', 'val', 'dur', 'acous', 'spch', 'pop'],
          dtype='object')



This might not give as much info, but it does allow us to index the columns:


```python
songs.columns[3]
```




    'year'



### Summarizing the DataFrame contents with describe()

`info()` gives a summary of what data is stored in each column, but another way to access info about each column that can be especially useful if the data are numeric (intgers, floats), is the `describe()` function. When we call this function on a DataFrame, it will show us a bunch of useful metrics for each numeric variable:
* The count (how many non-null pieces of data there are in the column)
* The mean of the column 
* The standard deviation (std) of the column
* The 25th, 50th (median), and 75th percentiles of the column
* The minumum and maximum values in the column


```python
songs.describe()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>bpm</th>
      <th>nrgy</th>
      <th>dnce</th>
      <th>dB</th>
      <th>live</th>
      <th>val</th>
      <th>dur</th>
      <th>acous</th>
      <th>spch</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>count</td>
      <td>603.000000</td>
      <td>603.000000</td>
      <td>603.000000</td>
      <td>603.000000</td>
      <td>603.000000</td>
      <td>603.000000</td>
      <td>603.000000</td>
      <td>603.000000</td>
      <td>603.000000</td>
      <td>603.000000</td>
      <td>603.000000</td>
    </tr>
    <tr>
      <td>mean</td>
      <td>2014.592040</td>
      <td>118.545605</td>
      <td>70.504146</td>
      <td>64.379768</td>
      <td>-5.578773</td>
      <td>17.774461</td>
      <td>52.225539</td>
      <td>224.674959</td>
      <td>14.326700</td>
      <td>8.358209</td>
      <td>66.520730</td>
    </tr>
    <tr>
      <td>std</td>
      <td>2.607057</td>
      <td>24.795358</td>
      <td>16.310664</td>
      <td>13.378718</td>
      <td>2.798020</td>
      <td>13.102543</td>
      <td>22.513020</td>
      <td>34.130059</td>
      <td>20.766165</td>
      <td>7.483162</td>
      <td>14.517746</td>
    </tr>
    <tr>
      <td>min</td>
      <td>2010.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>-60.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>134.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <td>25%</td>
      <td>2013.000000</td>
      <td>100.000000</td>
      <td>61.000000</td>
      <td>57.000000</td>
      <td>-6.000000</td>
      <td>9.000000</td>
      <td>35.000000</td>
      <td>202.000000</td>
      <td>2.000000</td>
      <td>4.000000</td>
      <td>60.000000</td>
    </tr>
    <tr>
      <td>50%</td>
      <td>2015.000000</td>
      <td>120.000000</td>
      <td>74.000000</td>
      <td>66.000000</td>
      <td>-5.000000</td>
      <td>12.000000</td>
      <td>52.000000</td>
      <td>221.000000</td>
      <td>6.000000</td>
      <td>5.000000</td>
      <td>69.000000</td>
    </tr>
    <tr>
      <td>75%</td>
      <td>2017.000000</td>
      <td>129.000000</td>
      <td>82.000000</td>
      <td>73.000000</td>
      <td>-4.000000</td>
      <td>24.000000</td>
      <td>69.000000</td>
      <td>239.500000</td>
      <td>17.000000</td>
      <td>9.000000</td>
      <td>76.000000</td>
    </tr>
    <tr>
      <td>max</td>
      <td>2019.000000</td>
      <td>206.000000</td>
      <td>98.000000</td>
      <td>97.000000</td>
      <td>-2.000000</td>
      <td>74.000000</td>
      <td>98.000000</td>
      <td>424.000000</td>
      <td>99.000000</td>
      <td>48.000000</td>
      <td>99.000000</td>
    </tr>
  </tbody>
</table>
</div>



What are the minumum and maxumim values stored in the `year` column of `songs`? What about the mean `bpm` (beats per minute)? 

### Accessing specific cells of the DataFrame with bracket indexing and `iloc()`

In this class, we've used hard brackets a bunch to index lists. Lucikly, DataFrames basically work the same way, except that they have 2 dimensions instead of 1. As we saw before with `shape`, with DataFrame objects, indices are always expressed as `[rows, columns]`.

To access DataFrame cells using the same kind of integer-based indexing that we use for lists, we can use the `iloc()` function. This always follows the syntax of `<DataFrame name>.iloc[rows, columns]`

For example, `songs.iloc[0,2]` should give us the data in the cell at the 1st row and the 3rd column of the DataFrame. Let's check this now


```python
songs.iloc[0,2]
```




    'neo mellow'




```python
songs.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>artist</th>
      <th>top genre</th>
      <th>year</th>
      <th>bpm</th>
      <th>nrgy</th>
      <th>dnce</th>
      <th>dB</th>
      <th>live</th>
      <th>val</th>
      <th>dur</th>
      <th>acous</th>
      <th>spch</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Hey, Soul Sister</td>
      <td>Train</td>
      <td>neo mellow</td>
      <td>2010</td>
      <td>97</td>
      <td>89</td>
      <td>67</td>
      <td>-4</td>
      <td>8</td>
      <td>80</td>
      <td>217</td>
      <td>19</td>
      <td>4</td>
      <td>83</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Love The Way You Lie</td>
      <td>Eminem</td>
      <td>detroit hip hop</td>
      <td>2010</td>
      <td>87</td>
      <td>93</td>
      <td>75</td>
      <td>-5</td>
      <td>52</td>
      <td>64</td>
      <td>263</td>
      <td>24</td>
      <td>23</td>
      <td>82</td>
    </tr>
    <tr>
      <td>2</td>
      <td>TiK ToK</td>
      <td>Kesha</td>
      <td>dance pop</td>
      <td>2010</td>
      <td>120</td>
      <td>84</td>
      <td>76</td>
      <td>-3</td>
      <td>29</td>
      <td>71</td>
      <td>200</td>
      <td>10</td>
      <td>14</td>
      <td>80</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Bad Romance</td>
      <td>Lady Gaga</td>
      <td>dance pop</td>
      <td>2010</td>
      <td>119</td>
      <td>92</td>
      <td>70</td>
      <td>-4</td>
      <td>8</td>
      <td>71</td>
      <td>295</td>
      <td>0</td>
      <td>4</td>
      <td>79</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Just the Way You Are</td>
      <td>Bruno Mars</td>
      <td>pop</td>
      <td>2010</td>
      <td>109</td>
      <td>84</td>
      <td>64</td>
      <td>-5</td>
      <td>9</td>
      <td>43</td>
      <td>221</td>
      <td>2</td>
      <td>4</td>
      <td>78</td>
    </tr>
  </tbody>
</table>
</div>



Can you confirm that `iloc()` is pulling out data from the cell in the 1st row and 3rd column?

Try doing this a few more times to see if you can get:
* The 3rd row and the 5th column
* The 2nd row and the first column
* The last row and the second column (a little trickier!)

# Challenge

For this challenge, we're going to explore some data in a different csv file, the one called 'billboard_1978.csv'. This file contains data on the [Billboard Hot 100](https://www.billboard.com/charts/hot-100) songs from 1978. 

For this challenge, try to do the following things with this data, as if you were just starting to work on it for a larger project and you wanted to get accustomed to it:

1. Load it in using `pd.read_csv()` and save it into a variable called songs_1978. To do this, you'll first want to make sure it is in your datasets folder
2. Take a look at the whole DataFrame
3. Use `head()` and `tail()` to check out the first and last few rows. Which song ranked #94 on the chart?
4. How many rows and columns are in this DataFrame?
5. Which columns have numeric (integer or float) data? 
6. Which columns have strings (listed as 'object' when you run `info()`)?
7. What is slowest tempo (minimum BPM) and fastest tempo (maximum BPM) this year?
8. Have songs gotten faster on average since 1978? Are the songs in `songs` on average faster than the songs in the `songs_1978` dataset? Compare the mean BPM across both DataFrames?

**Recap**: Nice job! We've learned a lot about working with DataFrames today. Next time, we'll learn how to 'clean' the data and work with DataFrames in more detail. 
