# Before class

* Make sure you have downloaded the 'musical_instrument_reviews.csv' data file. This is a dataset containing reviews for a product on Amazon (taken from [a larger dataset on Kaggle](https://www.kaggle.com/eswarchandt/amazon-music-reviews)), and we'll be cleaning the data so we can see if customers liked the product or not.


# Outline of class agenda

During this class you'll:

1. Learn how to select data in DataFrames by columns and by rows
2. Learn how to change DataFrame column names
3. Learn how to make new columns and remove columns
4. Learn how to spot missing data in DataFrames and replace it
5. Learn how to sort data in DataFrames
6. Learn how to export data from a DataFrame back to a csv file
7. Feel more comfortable with how data cleaning can fit into your workflow

# Class

Today we're going to focus on 'data cleaning'. But, what is data cleaning, exactly?
* Any operations you need to do to get your data in shape for analysis, graphs, or presentations
* Typically involves checking the data for correctness, fixing errors, and dealing with missing data
* Might involve selecting only certain parts of larger datasets, or combining multiple datasets

Data cleaning might not always be the most exciting aspect of working with data, but it is *super important* for any projects where you're working with data! It also is something most data scientists spend a [lot of time](https://businessoverbroadway.com/2019/02/19/how-do-data-professionals-spend-their-time-on-data-science-projects/) on


To get started for today, we'll import pandas as usual, then read in a daset on musical instrument reviews from a .csv file

First import pandas


```python
import pandas as pd
```

Then, read in the csv file using `pd.read_csv()`


```python
reviews = pd.read_csv('../../datasets/musical_instrument_reviews.csv')

```

Now, let's take a quick look at it:


```python
reviews.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>reviewerID</th>
      <th>reviewerName</th>
      <th>reviewText</th>
      <th>overall</th>
      <th>summary</th>
      <th>reviewTime</th>
      <th>reviewWords</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>A2IBPI20UZIR0U</td>
      <td>cassandra tu "Yeah, well, that's just like, u...</td>
      <td>Not much to write about here, but it does exac...</td>
      <td>5.0</td>
      <td>good</td>
      <td>02 28, 2014</td>
      <td>51</td>
    </tr>
    <tr>
      <td>1</td>
      <td>A14VAT5EAX3D9S</td>
      <td>Jake</td>
      <td>The product does exactly as it should and is q...</td>
      <td>5.0</td>
      <td>Jake</td>
      <td>03 16, 2013</td>
      <td>104</td>
    </tr>
    <tr>
      <td>2</td>
      <td>A195EZSQDW3E21</td>
      <td>Rick Bennette "Rick Bennette"</td>
      <td>The primary job of this device is to block the...</td>
      <td>5.0</td>
      <td>It Does The Job Well</td>
      <td>08 28, 2013</td>
      <td>77</td>
    </tr>
    <tr>
      <td>3</td>
      <td>A2C00NNG1ZQQG2</td>
      <td>RustyBill "Sunday Rocker"</td>
      <td>Nice windscreen protects my MXL mic and preven...</td>
      <td>5.0</td>
      <td>GOOD WINDSCREEN FOR THE MONEY</td>
      <td>02 14, 2014</td>
      <td>35</td>
    </tr>
    <tr>
      <td>4</td>
      <td>A94QU4C90B1AX</td>
      <td>SEAN MASLANKA</td>
      <td>This pop filter is great. It looks and perform...</td>
      <td>5.0</td>
      <td>No more pops when I record my vocals.</td>
      <td>02 21, 2014</td>
      <td>28</td>
    </tr>
  </tbody>
</table>
</div>



Before we get started on data cleaning, we can check out a few things about this DataFrame. This contains 500 reviews of a product on Amazon (musical instruments), so with this analysis we can imagine we're trying to figure out whether people seem to like this product, or whether there are certain reasons why people give it negative reviews. 

We have several pieces of data on each review, stored in each column:
* **reviewerID:** a unique ID for each Amazon user who reviewed this product
* **reviewerName:** the username for each reviewer
* **reviewText:** a string containing the text of the entire review
* **overall:** the user's overall rating of the product on a scale from 1-5 stars
* **summary:** the user's summary of their review
* **reviewTime:** the date of the review [day month year]
* **reviewWords:** the number of words in the user's entire review (i.e. number of words in the entry in the `reviewText` column)

## 1. Selecting data in a DataFrame by columns and by rows

Last class, we learned how to select specific cells of DataFrame objects using numeric indexing with `iloc()`, but often it is much more useful to be able to work with columns and rows in different ways. We'll learn a few of those here:

### Selecting columns

There are two methods that are useful for selecting certain columns in a DataFrame.

**Method 1**

The first is using brackets with the column labels inside. This method is really flexible, because we can either select just one column as a Pandas Series object

`reviews['reviewerID']`

Or, we can one or more columns as an entire DataFrame object by using two sets of brackets (so the column labels are a list object


`reviews[['reviewerID']]`

`reviews[['reviewerID', 'overall']]`

**Method 2**

The second method is using `.` to reference a column as an attribute of a DataFrame. This always only gets 1 column of the data frame as a Pandas Series:

`reviews.reviewerID` (this is equivalent to `reviews['reviewerID']`)

The only thing to be aware of for Method 2 is that you can't make *new* columns this way. Colummns referenced with the `.` have to already exist in the DataFrame

**Mini-challenge 1:** 
1. Select the `overall` column of the `reviews` DataFrame, and save if to the variable 'overall_rating'. Then run `type()` to see what kind of object you get.
2. Make a new DataFrame of the columns `overall` and `reviewWords` and save it into a variable called `df2`. Confirm that it is a DataFrame using `type()`

**Solution:** 



```python
# part 1
overall_rating = reviews.overall
type(overall_rating)
```




    pandas.core.series.Series




```python
# part 2
df2 = reviews[['overall', 'reviewWords']]
type(df2)
```




    pandas.core.frame.DataFrame



One more quick trick is that you can also make a list of column names, and then use this list to create a DataFrame with only these columns, for example:


```python
column_list = ['overall', 'reviewText', 'summary']
df3 = reviews[column_list]
df3.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>overall</th>
      <th>reviewText</th>
      <th>summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>5.0</td>
      <td>Not much to write about here, but it does exac...</td>
      <td>good</td>
    </tr>
    <tr>
      <td>1</td>
      <td>5.0</td>
      <td>The product does exactly as it should and is q...</td>
      <td>Jake</td>
    </tr>
    <tr>
      <td>2</td>
      <td>5.0</td>
      <td>The primary job of this device is to block the...</td>
      <td>It Does The Job Well</td>
    </tr>
    <tr>
      <td>3</td>
      <td>5.0</td>
      <td>Nice windscreen protects my MXL mic and preven...</td>
      <td>GOOD WINDSCREEN FOR THE MONEY</td>
    </tr>
    <tr>
      <td>4</td>
      <td>5.0</td>
      <td>This pop filter is great. It looks and perform...</td>
      <td>No more pops when I record my vocals.</td>
    </tr>
  </tbody>
</table>
</div>



Because `column_list` in this example is already a list, we only need 1 set of brackets here to make a DataFrame with these specified columns

### Selecting or 'filtering' rows (based on their content)

So, we've learned how to select only certain columns from a DataFrame. Great! 

One other thing that might be really helpful is only selecting certain *rows*. We saw how to do that last time with `iloc()`, but what might often be more useful is only including rows that with data in them that *fit certain criteria*. Often, we might call this **filtering** the data.

For example, when we're going through these product reviews, we might want to 
* filter the data for reviews that were longer than 50 words
* filter the data for reviews in the year 2014

Generally, we filter rows by applying a [conditional statement](https://www.python-course.eu/python3_conditional_statements.php#:~:text=statements%20in%20Python.-,Conditional%20statements%20in%20Python,should%20be%20executed%20or%20not.&text=The%20indented%20block%20is%20only,condition%20'condition'%20is%20True.) (a logical statement that can return `True` or `False` for each entry) related to a column of the DataFrame

For example, one conditional statement to check if reviews are longer than 50 words could be:


```python
reviews.reviewWords > 50
```




    0       True
    1       True
    2       True
    3      False
    4      False
           ...  
    495    False
    496    False
    497     True
    498    False
    499    False
    Name: reviewWords, Length: 500, dtype: bool



If we do the conditional statement *by itself* like this, it returns a pandas Series full of `True` and `False` values. For each review, we get `True` if the condition is met (the review was longer than 50 words, or `reviewWords > 50`) and `False` if not.

Now, the *fancy part* comes in when we use this Series of `True` and `False` values to select which rows of whole DataFrame we want. We can use this to take **only the rows of the DataFrame where the condition is met, where the value is `True`** with the following syntax:


```python
reviews_above_50_words = reviews[reviews.reviewWords > 50]
```

This is a *bunch* of steps in one line of code, but to summarise, what this does is to apply a **condition** to the `reviewWords` column of the DataFrame, which only returns `True` if the numeric value for an entry in that column is above 50. Then, the bracket indexing selects *only* the rows with a value of `True` from `reviews`, and we save that into a new DataFrame object. Let's take a look to confirm that we're only getting rows where the review is over 50 words:


```python
reviews_above_50_words.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>reviewerID</th>
      <th>reviewerName</th>
      <th>reviewText</th>
      <th>overall</th>
      <th>summary</th>
      <th>reviewTime</th>
      <th>reviewWords</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>A2IBPI20UZIR0U</td>
      <td>cassandra tu "Yeah, well, that's just like, u...</td>
      <td>Not much to write about here, but it does exac...</td>
      <td>5.0</td>
      <td>good</td>
      <td>02 28, 2014</td>
      <td>51</td>
    </tr>
    <tr>
      <td>1</td>
      <td>A14VAT5EAX3D9S</td>
      <td>Jake</td>
      <td>The product does exactly as it should and is q...</td>
      <td>5.0</td>
      <td>Jake</td>
      <td>03 16, 2013</td>
      <td>104</td>
    </tr>
    <tr>
      <td>2</td>
      <td>A195EZSQDW3E21</td>
      <td>Rick Bennette "Rick Bennette"</td>
      <td>The primary job of this device is to block the...</td>
      <td>5.0</td>
      <td>It Does The Job Well</td>
      <td>08 28, 2013</td>
      <td>77</td>
    </tr>
    <tr>
      <td>7</td>
      <td>AJNFQI3YR6XJ5</td>
      <td>Fender Guy "Rick"</td>
      <td>I now use this cable to run from the output of...</td>
      <td>3.0</td>
      <td>Didn't fit my 1996 Fender Strat...</td>
      <td>11 16, 2012</td>
      <td>167</td>
    </tr>
    <tr>
      <td>10</td>
      <td>A2NYK9KWFMJV4Y</td>
      <td>Mike Tarrani "Jazz Drummer"</td>
      <td>Monster makes a wide array of cables, includin...</td>
      <td>5.0</td>
      <td>One of the best instrument cables within the b...</td>
      <td>04 19, 2012</td>
      <td>190</td>
    </tr>
  </tbody>
</table>
</div>



**Mini-challenge 2:**

In a similar way to what we just did, filter `reviews` to make a new DataFrame called `good_reviews` with only `overall` scores of 4 or higher.

**Solution**


```python
good_reviews = reviews[reviews.overall >= 4]
```

We can use the describe() function to check that the minumum value in the overall column is a 4


```python
good_reviews.describe()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>overall</th>
      <th>reviewWords</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>count</td>
      <td>451.000000</td>
      <td>451.000000</td>
    </tr>
    <tr>
      <td>mean</td>
      <td>4.725055</td>
      <td>86.119734</td>
    </tr>
    <tr>
      <td>std</td>
      <td>0.446982</td>
      <td>107.781997</td>
    </tr>
    <tr>
      <td>min</td>
      <td>4.000000</td>
      <td>7.000000</td>
    </tr>
    <tr>
      <td>25%</td>
      <td>4.000000</td>
      <td>30.000000</td>
    </tr>
    <tr>
      <td>50%</td>
      <td>5.000000</td>
      <td>49.000000</td>
    </tr>
    <tr>
      <td>75%</td>
      <td>5.000000</td>
      <td>90.500000</td>
    </tr>
    <tr>
      <td>max</td>
      <td>5.000000</td>
      <td>915.000000</td>
    </tr>
  </tbody>
</table>
</div>



## 2. Changing DataFrame column names

To update the column names, we can use the [`rename()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html). To specify which columns we want to rename and what the new names should be, we add a `columns` argument in the form of a dictionary. In this dictionary object, each column name is formatted as `{'old name':'new name'}`

So, if we wanted to change the `summary` column to be called `review_summary`:


```python
reviews.rename(columns = {'summary':'review_summary'}, inplace = True)
```

Here, we also can add the `inplace = True` arguement so that the column is renamed 'inplace' and the DataFrame is modified without us having to assign it to a variable. The colum name is now changed:


```python
reviews.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>reviewerID</th>
      <th>reviewerName</th>
      <th>reviewText</th>
      <th>overall</th>
      <th>review_summary</th>
      <th>reviewTime</th>
      <th>reviewWords</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>A2IBPI20UZIR0U</td>
      <td>cassandra tu "Yeah, well, that's just like, u...</td>
      <td>Not much to write about here, but it does exac...</td>
      <td>5.0</td>
      <td>good</td>
      <td>02 28, 2014</td>
      <td>51</td>
    </tr>
    <tr>
      <td>1</td>
      <td>A14VAT5EAX3D9S</td>
      <td>Jake</td>
      <td>The product does exactly as it should and is q...</td>
      <td>5.0</td>
      <td>Jake</td>
      <td>03 16, 2013</td>
      <td>104</td>
    </tr>
    <tr>
      <td>2</td>
      <td>A195EZSQDW3E21</td>
      <td>Rick Bennette "Rick Bennette"</td>
      <td>The primary job of this device is to block the...</td>
      <td>5.0</td>
      <td>It Does The Job Well</td>
      <td>08 28, 2013</td>
      <td>77</td>
    </tr>
  </tbody>
</table>
</div>



We can also change multiple columns at once with the same syntax:


```python
reviews.rename(columns = {'reviewerName':'username',
                          'reviewerID': 'user_id'}, inplace = True)
```


```python
reviews.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>username</th>
      <th>reviewText</th>
      <th>overall</th>
      <th>review_summary</th>
      <th>reviewTime</th>
      <th>reviewWords</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>A2IBPI20UZIR0U</td>
      <td>cassandra tu "Yeah, well, that's just like, u...</td>
      <td>Not much to write about here, but it does exac...</td>
      <td>5.0</td>
      <td>good</td>
      <td>02 28, 2014</td>
      <td>51</td>
    </tr>
    <tr>
      <td>1</td>
      <td>A14VAT5EAX3D9S</td>
      <td>Jake</td>
      <td>The product does exactly as it should and is q...</td>
      <td>5.0</td>
      <td>Jake</td>
      <td>03 16, 2013</td>
      <td>104</td>
    </tr>
    <tr>
      <td>2</td>
      <td>A195EZSQDW3E21</td>
      <td>Rick Bennette "Rick Bennette"</td>
      <td>The primary job of this device is to block the...</td>
      <td>5.0</td>
      <td>It Does The Job Well</td>
      <td>08 28, 2013</td>
      <td>77</td>
    </tr>
  </tbody>
</table>
</div>



## 3. Adding and removing DataFrame columns

Often we'll want to add new columns to our DataFrame to make new useful variables, or remove columns we're not using. Let's learn how to do both here!

**Adding a new column**

In general, we can add new columns using the `df['column_name']` syntax just as if we were working with existing columns. 

As an example, maybe we want to make a new column that indicates if a review was especially long (over 500 words) called `long_review`. 


```python
reviews['long_review'] = reviews.reviewWords > 100
```

We can also make columns where all of the values are exactly the same by assigning an integer, float, string, or boolean value to a column:


```python
# make a column indicating the name of the data analyst
reviews['data_analyst'] = 'Paul Bloom'

# make a column with all zeros
reviews['zeros'] = 0
```

Now we can check that those columns are there:


```python
reviews.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>username</th>
      <th>reviewText</th>
      <th>overall</th>
      <th>review_summary</th>
      <th>reviewTime</th>
      <th>reviewWords</th>
      <th>long_review</th>
      <th>data_analyst</th>
      <th>zeros</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>A2IBPI20UZIR0U</td>
      <td>cassandra tu "Yeah, well, that's just like, u...</td>
      <td>Not much to write about here, but it does exac...</td>
      <td>5.0</td>
      <td>good</td>
      <td>02 28, 2014</td>
      <td>51</td>
      <td>False</td>
      <td>Paul Bloom</td>
      <td>0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>A14VAT5EAX3D9S</td>
      <td>Jake</td>
      <td>The product does exactly as it should and is q...</td>
      <td>5.0</td>
      <td>Jake</td>
      <td>03 16, 2013</td>
      <td>104</td>
      <td>True</td>
      <td>Paul Bloom</td>
      <td>0</td>
    </tr>
    <tr>
      <td>2</td>
      <td>A195EZSQDW3E21</td>
      <td>Rick Bennette "Rick Bennette"</td>
      <td>The primary job of this device is to block the...</td>
      <td>5.0</td>
      <td>It Does The Job Well</td>
      <td>08 28, 2013</td>
      <td>77</td>
      <td>False</td>
      <td>Paul Bloom</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



**Removing Columns**

We can remove columns using the `drop()` function as follows:


```python
reviews.drop(columns = ['data_analyst', 'zeros'], inplace = True)
```

So here with `drop()`, we specify a `columns` argument as a list of the column names we want to remove. If we only wanted to drop one column, we could also use a list with just 1 element.

You might wonder be wondering what `inplace = True` does. This argument saves the DataFrame with the columns dropped *back* into the original one, so we don't have to reassign it to a variable again. If we don't include this, we'd have to assign to a variable to save the changes.

If you have a DataFrame with a LOT of columns and you want to get rid of most of them, it is often easier to select the columns you *do* want rather than the ones you *don't*. (see #1 for selecting columns)

**Mini-challenge 3**

* Add a column called 'my_name' to `reviews` with your name in each row
* Add a column called 'my_integer' to `reviews` with the same integer in each row
* Then, remove both columns uding `inplace = True`

**Solution**


```python
# adding the columns
reviews['my_name'] = 'Paul Bloom'
reviews['my_integer'] = 8
reviews.head(2)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>username</th>
      <th>reviewText</th>
      <th>overall</th>
      <th>review_summary</th>
      <th>reviewTime</th>
      <th>reviewWords</th>
      <th>long_review</th>
      <th>my_name</th>
      <th>my_integer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>A2IBPI20UZIR0U</td>
      <td>cassandra tu "Yeah, well, that's just like, u...</td>
      <td>Not much to write about here, but it does exac...</td>
      <td>5.0</td>
      <td>good</td>
      <td>02 28, 2014</td>
      <td>51</td>
      <td>False</td>
      <td>Paul Bloom</td>
      <td>8</td>
    </tr>
    <tr>
      <td>1</td>
      <td>A14VAT5EAX3D9S</td>
      <td>Jake</td>
      <td>The product does exactly as it should and is q...</td>
      <td>5.0</td>
      <td>Jake</td>
      <td>03 16, 2013</td>
      <td>104</td>
      <td>True</td>
      <td>Paul Bloom</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
# drop the new columns
reviews.drop(columns=['my_name', 'my_integer'], inplace = True)
```


```python
reviews.head(2)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>username</th>
      <th>reviewText</th>
      <th>overall</th>
      <th>review_summary</th>
      <th>reviewTime</th>
      <th>reviewWords</th>
      <th>long_review</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>A2IBPI20UZIR0U</td>
      <td>cassandra tu "Yeah, well, that's just like, u...</td>
      <td>Not much to write about here, but it does exac...</td>
      <td>5.0</td>
      <td>good</td>
      <td>02 28, 2014</td>
      <td>51</td>
      <td>False</td>
    </tr>
    <tr>
      <td>1</td>
      <td>A14VAT5EAX3D9S</td>
      <td>Jake</td>
      <td>The product does exactly as it should and is q...</td>
      <td>5.0</td>
      <td>Jake</td>
      <td>03 16, 2013</td>
      <td>104</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## 4. Finding & dealing with missing data

Often the data we're working with has missing values we'll need to deal with before analysis or graphing. 

One way to check for these values in the entire DataFrame is with the `isnull()` function. For example, if we call this on the entire dataframe, the function returns a DataFrame where each cell is `True` if that same cell in the original dataframe contained a null (or missing) value, and `False` if there was data in that cell.


```python
reviews.isnull()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>username</th>
      <th>reviewText</th>
      <th>overall</th>
      <th>review_summary</th>
      <th>reviewTime</th>
      <th>reviewWords</th>
      <th>long_review</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
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
    </tr>
    <tr>
      <td>495</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>496</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>497</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>498</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>499</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>500 rows × 8 columns</p>
</div>



This might be hard to read by itself, but then if we combine this with the `sum()` function, we can get a quick summary of how many missing values are in each column:


```python
reviews.isnull().sum()
```




    user_id           0
    username          4
    reviewText        0
    overall           4
    review_summary    3
    reviewTime        0
    reviewWords       0
    long_review       0
    dtype: int64



Here we can see that the `username` and `overall` columns are both missing 4 values, and `review_summary` is missing 3

But, what if we wanted to actually check out what's going on in the rows missing data? For this, we can use the same process we used earlier to *select rows*, but here, we can select the rows where a certain column contains missing values. For example, let's select only the rows where `overall` is null:


```python
# This is the same process as in section 1! Inside the brackets is a conditional argument
# The code inside the brackets gives True for every null value in the column `overall` and false otherwise
# Then we filter the whole DataFrame for only the rows where this returned True
reviews[reviews.overall.isnull()]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>username</th>
      <th>reviewText</th>
      <th>overall</th>
      <th>review_summary</th>
      <th>reviewTime</th>
      <th>reviewWords</th>
      <th>long_review</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>137</td>
      <td>AFLRU6952DEFX</td>
      <td>S.</td>
      <td>These have a lower profile and can fit and ben...</td>
      <td>NaN</td>
      <td>Possibly better than the metal ended ones</td>
      <td>06 24, 2014</td>
      <td>20</td>
      <td>False</td>
    </tr>
    <tr>
      <td>140</td>
      <td>AQFOCVEBDCYU9</td>
      <td>Jazzgryl52</td>
      <td>I purchased this to work with my ION system an...</td>
      <td>NaN</td>
      <td>No problems</td>
      <td>07 31, 2013</td>
      <td>22</td>
      <td>False</td>
    </tr>
    <tr>
      <td>245</td>
      <td>A37AQI4AU3JWSR</td>
      <td>Joshua</td>
      <td>Donr be fooled by the imitations... should be ...</td>
      <td>NaN</td>
      <td>Best rack screws for your money.</td>
      <td>12 18, 2012</td>
      <td>28</td>
      <td>False</td>
    </tr>
    <tr>
      <td>246</td>
      <td>AUK79PXTAOJP9</td>
      <td>~ Kyle</td>
      <td>Great rack mount screws. Rubber washers are pe...</td>
      <td>NaN</td>
      <td>Great</td>
      <td>07 8, 2013</td>
      <td>44</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



**Removing missing values**

A lot of the time we might want to remove rows where a certain column is missing data. This will often show up as `NaN`, which stands for 'not a number'. 

Here, we can't really do much without the `overall` ratings of the product, so we'll remove the 4 rows with NaNs in this column. We can do this by putting a minus sign in front of the `reviews.overal.isnull()` which will return True for all **non-null** rows. Then, we select only those, and save into a new DataFrame called `reviews_no_null_ratings`


```python
reviews_no_null_ratings = reviews[-reviews.overall.isnull()]
```

Now, this new DataFrame has no nulls in the `overall` column, and we can see it is 4 rows smaller than before (only 496 columns now)


```python
print(reviews_no_null_ratings.isnull().sum())
print(reviews_no_null_ratings.shape)
```

    user_id           0
    username          4
    reviewText        0
    overall           0
    review_summary    3
    reviewTime        0
    reviewWords       0
    long_review       0
    dtype: int64
    (496, 8)


**Replacing Missing Values**

Instead of removing data, sometimes we might want to replace it with something meaningful. 

Here, we want to replace the NaN values in the `username` column with the username 'unknown user'. First, we can take a look at these:


```python
reviews[reviews.username.isnull()]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>username</th>
      <th>reviewText</th>
      <th>overall</th>
      <th>review_summary</th>
      <th>reviewTime</th>
      <th>reviewWords</th>
      <th>long_review</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>41</td>
      <td>AA5TINW2RJ195</td>
      <td>NaN</td>
      <td>Good quality cable and sounds very good</td>
      <td>5.0</td>
      <td>Five Stars</td>
      <td>07 15, 2014</td>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <td>263</td>
      <td>A14VAT5EAX3D9S</td>
      <td>NaN</td>
      <td>It is exactly what you need in a capo! You can...</td>
      <td>5.0</td>
      <td>Great</td>
      <td>04 2, 2013</td>
      <td>82</td>
      <td>False</td>
    </tr>
    <tr>
      <td>264</td>
      <td>A2RVY2GDMZHH4</td>
      <td>NaN</td>
      <td>Love these capos and nice that you can get the...</td>
      <td>5.0</td>
      <td>Always great Kyser</td>
      <td>12 28, 2012</td>
      <td>23</td>
      <td>False</td>
    </tr>
    <tr>
      <td>432</td>
      <td>A3BMYEA3J6RBVV</td>
      <td>NaN</td>
      <td>Bought it as a gift. Friend loved it very much.</td>
      <td>5.0</td>
      <td>Friend loved it very much</td>
      <td>07 13, 2014</td>
      <td>10</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



Now, we use these to reassign values to `reviews.username` 


```python
reviews.username[reviews.username.isnull()] = 'unknown user'
```

Now if we look for nulls in this column, there aren't any:


```python
# returns no data!
reviews[reviews.username.isnull()]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>username</th>
      <th>reviewText</th>
      <th>overall</th>
      <th>review_summary</th>
      <th>reviewTime</th>
      <th>reviewWords</th>
      <th>long_review</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>



But, if we look for values of 'unknown user' in this column, we find them where the NaNs used to be 


```python
reviews[reviews.username == 'unknown user']
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>username</th>
      <th>reviewText</th>
      <th>overall</th>
      <th>review_summary</th>
      <th>reviewTime</th>
      <th>reviewWords</th>
      <th>long_review</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>41</td>
      <td>AA5TINW2RJ195</td>
      <td>unknown user</td>
      <td>Good quality cable and sounds very good</td>
      <td>5.0</td>
      <td>Five Stars</td>
      <td>07 15, 2014</td>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <td>263</td>
      <td>A14VAT5EAX3D9S</td>
      <td>unknown user</td>
      <td>It is exactly what you need in a capo! You can...</td>
      <td>5.0</td>
      <td>Great</td>
      <td>04 2, 2013</td>
      <td>82</td>
      <td>False</td>
    </tr>
    <tr>
      <td>264</td>
      <td>A2RVY2GDMZHH4</td>
      <td>unknown user</td>
      <td>Love these capos and nice that you can get the...</td>
      <td>5.0</td>
      <td>Always great Kyser</td>
      <td>12 28, 2012</td>
      <td>23</td>
      <td>False</td>
    </tr>
    <tr>
      <td>432</td>
      <td>A3BMYEA3J6RBVV</td>
      <td>unknown user</td>
      <td>Bought it as a gift. Friend loved it very much.</td>
      <td>5.0</td>
      <td>Friend loved it very much</td>
      <td>07 13, 2014</td>
      <td>10</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



**Removing ALL missing values**

So far we've been targeting missing values in each column one-by-one. But, what if we wanted to remove ALL the missing data from the DataFrame in one step? We can use the `dropna()` function for this!

If we want to remove each *row* that has any missing values, we can run as follows:


```python
reviews_clean = reviews.dropna(axis = 0)
```

Here `axis = 0` specifies that we removing rows (because rows are axis 0 and columns are axis 1)


```python
reviews_clean.isnull().sum()
```




    user_id           0
    username          0
    reviewText        0
    overall           0
    review_summary    0
    reviewTime        0
    reviewWords       0
    long_review       0
    dtype: int64



If we use `shape` here, we can also see that more rows have been removed from the DataFrame (now we only have 493)


```python
reviews_clean.shape
```




    (493, 8)



**Mini-challenge 4:**

Instead of removing *rows* with missing data, we might want to remove all *columns* with any missing values. Use the [documentation for the `dropna()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html) to find out how to do this. Save the output DataFrame to a variable called `reviews_clean_columns`

**Solution**

We use the `axis = 1` argument to specificy that we want to drop *columns*


```python
reviews_clean_columns = reviews.dropna(axis = 1)
```


```python
# The resulting dataframe is still 500 rows, but fewer columns now
reviews_clean_columns.shape
```




    (500, 6)



## 5. Sorting DataFrames

One very handy thing about DataFrames is that we can sort the data using any column using `sort_values()`

For example, we can sort the data by the `overall` column. By default this goes from least-greatest for integer/float variables 


```python
reviews.sort_values('overall')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>username</th>
      <th>reviewText</th>
      <th>overall</th>
      <th>review_summary</th>
      <th>reviewTime</th>
      <th>reviewWords</th>
      <th>long_review</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>413</td>
      <td>A3KBFCPNQ58YK4</td>
      <td>Sam</td>
      <td>Here's the deal with this pedal. It is inexpen...</td>
      <td>1.0</td>
      <td>Beginners Beware</td>
      <td>02 21, 2014</td>
      <td>68</td>
      <td>False</td>
    </tr>
    <tr>
      <td>408</td>
      <td>A2B58VXLLOFQKR</td>
      <td>James Moulton</td>
      <td>This is a cheap piece of junk that does what i...</td>
      <td>1.0</td>
      <td>It distorts</td>
      <td>11 13, 2009</td>
      <td>85</td>
      <td>False</td>
    </tr>
    <tr>
      <td>52</td>
      <td>A1L7M2JXN4EZCR</td>
      <td>David G</td>
      <td>It hums, crackles, and I think I'm having prob...</td>
      <td>1.0</td>
      <td>I have bought many cables and this one is the ...</td>
      <td>02 9, 2014</td>
      <td>46</td>
      <td>False</td>
    </tr>
    <tr>
      <td>224</td>
      <td>A27DR1VO079F1V</td>
      <td>Dan Edman</td>
      <td>These things are terrible. One wouldn't fit in...</td>
      <td>1.0</td>
      <td>Crap</td>
      <td>02 19, 2014</td>
      <td>27</td>
      <td>False</td>
    </tr>
    <tr>
      <td>223</td>
      <td>A3AOB0VF6H0IF4</td>
      <td>Daits</td>
      <td>Received it in time, standard blister packagin...</td>
      <td>1.0</td>
      <td>DIED after 45 days of use</td>
      <td>01 27, 2013</td>
      <td>35</td>
      <td>False</td>
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
    </tr>
    <tr>
      <td>251</td>
      <td>A7TRK2GG6BHWD</td>
      <td>Johnny Pasta "Johnny Pasta"</td>
      <td>Why drive a Pinto when you can drive a Cadilla...</td>
      <td>5.0</td>
      <td>Best All Around Mic For Live Applications</td>
      <td>01 13, 2013</td>
      <td>65</td>
      <td>False</td>
    </tr>
    <tr>
      <td>137</td>
      <td>AFLRU6952DEFX</td>
      <td>S.</td>
      <td>These have a lower profile and can fit and ben...</td>
      <td>NaN</td>
      <td>Possibly better than the metal ended ones</td>
      <td>06 24, 2014</td>
      <td>20</td>
      <td>False</td>
    </tr>
    <tr>
      <td>140</td>
      <td>AQFOCVEBDCYU9</td>
      <td>Jazzgryl52</td>
      <td>I purchased this to work with my ION system an...</td>
      <td>NaN</td>
      <td>No problems</td>
      <td>07 31, 2013</td>
      <td>22</td>
      <td>False</td>
    </tr>
    <tr>
      <td>245</td>
      <td>A37AQI4AU3JWSR</td>
      <td>Joshua</td>
      <td>Donr be fooled by the imitations... should be ...</td>
      <td>NaN</td>
      <td>Best rack screws for your money.</td>
      <td>12 18, 2012</td>
      <td>28</td>
      <td>False</td>
    </tr>
    <tr>
      <td>246</td>
      <td>AUK79PXTAOJP9</td>
      <td>~ Kyle</td>
      <td>Great rack mount screws. Rubber washers are pe...</td>
      <td>NaN</td>
      <td>Great</td>
      <td>07 8, 2013</td>
      <td>44</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>500 rows × 8 columns</p>
</div>



If we choose a column with strings in it, by default it will be sorted alphabetically: 


```python
reviews.sort_values('username').head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>username</th>
      <th>reviewText</th>
      <th>overall</th>
      <th>review_summary</th>
      <th>reviewTime</th>
      <th>reviewWords</th>
      <th>long_review</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>497</td>
      <td>A3EZEP0FX5BC1P</td>
      <td>A Conrad "Ask Conrad"</td>
      <td>This is for theKyser Banjo/Mandolin CapoThis i...</td>
      <td>5.0</td>
      <td>A very good ukulele capo</td>
      <td>02 8, 2010</td>
      <td>140</td>
      <td>True</td>
    </tr>
    <tr>
      <td>266</td>
      <td>A3EZEP0FX5BC1P</td>
      <td>A Conrad "Ask Conrad"</td>
      <td>The title says it all.  I got it for $16 (free...</td>
      <td>4.0</td>
      <td>It's cheap, easy, sturdy, and works</td>
      <td>01 19, 2010</td>
      <td>67</td>
      <td>False</td>
    </tr>
    <tr>
      <td>467</td>
      <td>A2C2TKHICAZ4RS</td>
      <td>A. Castillo</td>
      <td>My first wah was a Morley Steve Vai Bad Horsie...</td>
      <td>5.0</td>
      <td>Great affordable Wah wah pedal</td>
      <td>05 13, 2009</td>
      <td>150</td>
      <td>True</td>
    </tr>
    <tr>
      <td>42</td>
      <td>ABC68JUCPTVOE</td>
      <td>A. Fabbri "afabbri"</td>
      <td>Zero issues with this cable so far.  It feels ...</td>
      <td>5.0</td>
      <td>Pretty cheap cable that has lasted so far</td>
      <td>03 31, 2012</td>
      <td>35</td>
      <td>False</td>
    </tr>
    <tr>
      <td>203</td>
      <td>AXABTEYS7A4A8</td>
      <td>A. Garza "Amazon Addict"</td>
      <td>I bought this for my teen son for Christmas. H...</td>
      <td>5.0</td>
      <td>This Shure is a great mic</td>
      <td>01 10, 2014</td>
      <td>67</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



There are many other ways to sort that we won't go over right now, but you can [check out the docs](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html) for options!

## 6. Exporting data out to a csv file


**Non-destructive editing:**
* With pandas DataFrame objects, we are only working with the data *within the python environment* unless we write out to a csv or other file format. This is helpful because this means that even with all the manipulation of our DataFrame objects, we are doing "non-destructive editing" -- aka not touching the original files.
* *Exporting csv files is a little different though,* since now we are saving files on the computer's file system again. Be careful! If you save to a certain file name that already exists, the new file with *overwrite* the old one!

Now that we've cleaned our data, let's save it to a file called 'clean_instrument_reviews.csv'. We can do this with the `to_csv()` function, remembering to specify the path to the output csv file in quotes (file paths always use quotes in python)


```python
reviews_clean.to_csv('clean_instrument_reviews.csv')
```

Check the directory where your jupyter notebook is located and you should see the new csv file! The working directory for saving files is always the *directory where the jupyter notebook is located*. However, we can specificy other directories to save data to, for example:


```python
# In this example, we also set index=False so that it doesn't save out a # for each row
reviews_clean.to_csv('../../datasets/clean_instrument_reviews.csv', index=False)
```

## 7. The data cleaning workflow

We've gone over a *lot* of different things in this lesson, but to tie it all together, here's a summary of the kind of workflow we used:

* Import the data and inspect what's there
* Change the column names, add any new columnes needed, remove unnecessary columns
* Selecting and filtering only the desired rows
* Dealing with any missing values
* Sorting the data
* Exporting to a csv file

This kind of workflow of reading data in, doing a BUNCH of things to 'clean' it, then exporting it, is an important set of steps in many workflows, and one you'll practice a few more times during this class

# Challenge: which product do people like best?

In this challenge, you will take the role of a data scientist. You'll be given some data on customer reviews for 3 products (Products A, B, and C) and you'll have to clean it to be able to run your company's graphing code to see which product is best.

##### Necessary files:
* There is a file in the datasets folder called 'product_tests.csv'. This contains data from 100 customer ratings each of Products A, B, and C. Each customer has a unique user id and rated one of the products on a scale from 0-5. 
* There is a script that runs your company's graphing code called 'compare_products.py'. This script will make a graph to help figure out which product customers like best. **This script reads in a file called 'products_clean.csv' in the datasets folder. Your job is to clean the data to make this file!**


##### Your data cleaning goals:

Your goal is to make this 'products_clean.csv' file a cleaned datafile. Here are the steps you should take to make sure the data are clean

* Remove any rows where ratings (values in the `rating` column) are below 0 or above 5. These would be impossible scores so these should be removed.
* There are some rows where the user_id is missing. Replace these with 'unknown user' for each missing user_id. We don't know the user id, but maybe we can still analyze these data points!
* Filter out any rows where `product` or `rating` are missing. We can't analyze data if we don't know which product it was, or what the rating was!
* Rename the `rating` column to `user_rating` and the `product` column to `product_id`. The company's code is built to use these standardized column names

Once you've done all these steps, export the data to the 'products_clean.csv' file in the datasets folder!

#### Comparing the products

Once you've finished, run `$ python compare_products.py` from the command line, and if the code runs smoothly, you'll see a file called 'product_chart.png' pop up to help you decide which product customers like best. 

Which product do you think is highest-rated?

If you don't get it on the first try, don't worry! Try to use the error messages you see, and take a look at your 'products_clean.csv' file to see what is being output to help you guide your data cleaning process 
