# Data cleaning challenge: which product do people like best?

In this challenge, you will take the role of a data scientist. You'll be given some data on customer reviews for 3 products (Products A, B, and C) and you'll have to clean it to be able to run your company's graphing code to see which product is best.

### Necessary files:
* There is a file in the `datasets` folder called 'product_tests.csv'. This contains data from 100 customer ratings each of Products A, B, and C. Each customer has a unique user id and rated one of the products on a scale from 0-5. (0 is the worst, 5 is the best) 
* There is a script that runs your company's graphing code called `compare_products.py`. This script will make a graph to help figure out which product customers like best. **This script reads in a file called 'products_clean.csv' in the datasets folder. Your overall job is to clean the data to make this file!**


**First, import the `product_tests.csv` file using pandas and assign it to a variable** (remember to import pandas too)


```python
import pandas as pd
products = pd.read_csv('../../datasets/product_tests.csv')
print(products.shape)
products.head()
```

    (300, 4)





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>product</th>
      <th>rating</th>
      <th>user_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Product A</td>
      <td>4.340998</td>
      <td>Y5JgC1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Product A</td>
      <td>NaN</td>
      <td>GRHQYF</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Product A</td>
      <td>2.363216</td>
      <td>EZ96Fa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Product A</td>
      <td>NaN</td>
      <td>MzRCo4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Product A</td>
      <td>4.987896</td>
      <td>VnVWvM</td>
    </tr>
  </tbody>
</table>
</div>



### Your data cleaning goals:

Your goal is to make this 'products_clean.csv' file a cleaned datafile. Here are the steps you should take to make sure the data are clean

1. Remove any rows where ratings (values in the `rating` column) are below 0 or above 5. These would be impossible scores so these should be removed.


```python
# using brackets to specify a condition to filter the dataframe
products = products[products.rating >=0]
products = products[products.rating <= 5]
```

2. There are some rows where the user_id is missing. Replace these with the string 'unknown user' for each missing user_id. We don't know the user id, but maybe we can still analyze these data points!


```python
# this is a tricky one! 
# on the left of the brackets, we need to specificy the COLUMN, and inside the brackets goes the condition. 
# So we're applying a condition specifically to a column
products.user_id[products.user_id.isnull()] = 'unknown user'
```

    /Users/paul/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      """Entry point for launching an IPython kernel.


3. Filter out any rows where `product` or `rating` are missing. We can't analyze data if we don't know which product it was, or what the rating was!


```python
# use the minus sign to say that we want all rows that are NOT null for these columns
products = products[-products['product'].isnull()]
products = products[-products['rating'].isnull()]
```

4. Rename the `rating` column to `user_rating` and the `product` column to `product_id`. The company's code is built to use these standardized column names


```python
# columns to rename go in a dictionary with syntax {old_name:new_name} for all key-value pairs
products.rename(columns = {'rating':'user_rating', 'product':'product_id'}, inplace = True)
```

5. Once you've done all these steps, export the data to `jtc_class_code/datasets/products_clean.csv`

Make sure that the csv is named exactly this way in your folder, because the graphing code relies on this exact file path!


```python
products.to_csv('../../datasets/products_clean.csv', index = False)
```

### Comparing the products

Once you've finished, run `$ python compare_products.py` from the command line, and if the code runs smoothly, you'll see a file called `product_chart.png` pop up to help you decide which product customers like best. 

Which product do you think is highest-rated?

If you don't get it on the first try, don't worry! Try to use the error messages you see, and take a look at your `products_clean.csv` file to see what is being output to help you guide your data cleaning process 

## Finished and got the plot? Decided which product is highest-rated? 

#### Congrats on finishing the data cleaning challenge! Data cleaning is not easy! 

So, remember to comment all your code and push this notebook to Github
