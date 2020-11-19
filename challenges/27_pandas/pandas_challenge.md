# Pandas Intro Challenge

For this challenge, we're going to explore some data in a different csv file, the one called `billboard_1978.csv`. This file contains data on the [Billboard Hot 100](https://www.billboard.com/charts/hot-100) songs from 1978. 

For this challenge, try to do the following things with this data, as if you were just starting to work on it for a larger project and you wanted to get accustomed to it:

# Part A: Load in the data

Turns out, you actually have the data on your computer! It lives in `jtc_class_code/datasets/billboard_1978.csv`

1. First, make a new folder called `27_pandas` inside your `jtc_class_code/challenges` folder
    * Then make a new jupyter notebook inside this folder called `pandas_challenge.ipynb`
2. Load it in using `pd.read_csv()` and save it into a variable called songs_1978. 
    * **NOTE:** Since the data file is in a different folder, you'll need to use the `../` syntax to specify exactly where your data live

# Part B: Inspect the data 

Take a look at the whole DataFrame
3. Use `head()` and `tail()` to check out the first and last few rows. Which song ranked #94 on the chart?
4. How many rows and columns are in this DataFrame?
5. Which columns have numeric (integer or float) data? 
6. Which columns have strings (listed as 'object' when you run `info()`)?
7. What is slowest tempo (minimum BPM) and fastest tempo (maximum BPM) this year?


# Part C: Access specific cells of the dataframe

8. The 2nd ranking song in 1978 was called 'Night Fever'. Print out the contents of the cell storing the artist for that song
    * Now, print out the contents of the cell storing the genre for that song
9. Print out the name of song ranking 50 on the chart 
    * (hint: which row of the dataframe will this be?)

# Part D: Make sure your jupyter notebook is clean

* Add markdown chunks with headers or text in them explaining what each section of the notebook does
* Select 'Restart Kernel and Run All' from the 'Kernel' tab to make sure your notebook runs cleanly from start to finish

# Part E: Add, push, and commit your notebook to github

Check out out on Github, you should be able to view the file there!

**Recap**: Nice job! We've learned a lot about working with DataFrames today. Next time, we'll learn how to 'clean' the data and work with DataFrames in more detail. 
