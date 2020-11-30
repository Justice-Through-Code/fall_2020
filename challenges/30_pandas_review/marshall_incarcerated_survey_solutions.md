<img src="https://dw9zmd5y2p1va.cloudfront.net/TheMarshallProject_Logo_Primary_TrueBlack.png" width="800">

# Marshall Project Survey of Incarcerated People: pandas review challenge


In today's challenge, you'll be importing data [collected by the Marshall Project from a survey that over 8000 incarcerated people responded to](https://github.com/themarshallproject/incarcerated_survey). In this survey, incarcerated individuals responded to a set of questions about their experiences and political views. For more information about this survey, [see here](https://www.themarshallproject.org/2020/03/11/what-do-we-really-know-about-the-politics-of-people-behind-bars). One key piece is that protecting the identities and privacy of the survey respondents is **very important** here -- that is why there are no names, exact ages, or specific prison locations contained here. 

The challenge will involve 4 main parts:
1. Importing the survey responses directly from online (Github) into a Pandas dataframe 
2. Cleaning the survey response data in pandas
3. Using pandas to pull out a few key statistics from the survey responses
4. Saving the cleaned data to csv files on your computer

# Part 1: Importing the data

It turns out that the `read_csv()` function from pandas works whether a csv file lives on your own computer or on the internet.  In this case, we'll pull the dataset [located here](https://github.com/themarshallproject/incarcerated_survey/blob/master/data/incarcerated_survey_responses-marshallproject_slate-march_2019.csv) on a Marshall Project Github repo. 

## 1A. Load pandas, then read in the csv file

* Import pandas
* To import the csv file, go to the [link on github to for the file](https://github.com/themarshallproject/incarcerated_survey/blob/master/data/incarcerated_survey_responses-marshallproject_slate-march_2019.csv), then click 'view raw'. This will take you to a link to the csv file itself. 
* Copy this link, and paste it (in quotes) as an argument to the `read_csv()` function.
* Read in the csv from this link and assign it to a variable


```python
import pandas as pd
```


```python
df = pd.read_csv('https://raw.githubusercontent.com/themarshallproject/incarcerated_survey/master/data/incarcerated_survey_responses-marshallproject_slate-march_2019.csv')
```

## 1B. Check out the data

* How many rows & columns are in the dataframe?
* What are the names of all the columns?
* Check to make sure you can figure out what type of data is in each column (i.e. numeric, strings, etc)


```python
df.shape
```




    (8266, 37)




```python
df.columns
```




    Index(['age', 'identifies_as_man', 'identifies_as_woman',
           'identifies_as_hispanic_or_latinx', 'identifies_as_black',
           'identifies_as_white', 'highest_education_level',
           'length_in_this_facility', 'state', 'party',
           'how_often_discuss_politics', 'how_get_news', 'ever_voted',
           'direction_country_headed',
           'how_often_officials_acting_in_your_interest',
           'which_party_for_cj_reform', 'stance_on_assault_weapons_ban',
           'stance_on_marijuana_legalization',
           'stance_on_tightening_border_security', 'stance_on_raise_min_wage',
           'race_affects_politics', 'should_incarcerated_vote',
           'incarceration_impacts_motivation_to_vote',
           'politics_changed_since_incarcerated',
           'cj_important_issue_eliminating_mandatory_mins',
           'cj_important_issue_reducing_racial_bias',
           'cj_important_issue_abolishing_death_penalty',
           'cj_important_issue_lowering_incarceration_rates_rural_communities',
           'cj_important_issue_improving_prison_conds',
           'cj_important_issue_restoring_voting_rights',
           'cj_important_issue_reducing_prison_pop',
           'cj_important_issue_ending_war_on_drugs',
           'cj_important_issue_ending_private_prisons',
           'cj_important_issue_lowering_sentences_violent_crimes',
           'cj_important_issue_raising_wages_incarcerated_workers', 'who_vote_for',
           'approve_disapprove_trump'],
          dtype='object')




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 8266 entries, 0 to 8265
    Data columns (total 37 columns):
     #   Column                                                             Non-Null Count  Dtype 
    ---  ------                                                             --------------  ----- 
     0   age                                                                5618 non-null   object
     1   identifies_as_man                                                  6240 non-null   object
     2   identifies_as_woman                                                6240 non-null   object
     3   identifies_as_hispanic_or_latinx                                   6240 non-null   object
     4   identifies_as_black                                                6240 non-null   object
     5   identifies_as_white                                                6240 non-null   object
     6   highest_education_level                                            5618 non-null   object
     7   length_in_this_facility                                            5618 non-null   object
     8   state                                                              2936 non-null   object
     9   party                                                              7617 non-null   object
     10  how_often_discuss_politics                                         8265 non-null   object
     11  how_get_news                                                       8210 non-null   object
     12  ever_voted                                                         8070 non-null   object
     13  direction_country_headed                                           8043 non-null   object
     14  how_often_officials_acting_in_your_interest                        8005 non-null   object
     15  which_party_for_cj_reform                                          7973 non-null   object
     16  stance_on_assault_weapons_ban                                      7956 non-null   object
     17  stance_on_marijuana_legalization                                   7953 non-null   object
     18  stance_on_tightening_border_security                               7943 non-null   object
     19  stance_on_raise_min_wage                                           7933 non-null   object
     20  race_affects_politics                                              7822 non-null   object
     21  should_incarcerated_vote                                           7833 non-null   object
     22  incarceration_impacts_motivation_to_vote                           7741 non-null   object
     23  politics_changed_since_incarcerated                                7733 non-null   object
     24  cj_important_issue_eliminating_mandatory_mins                      8266 non-null   int64 
     25  cj_important_issue_reducing_racial_bias                            8266 non-null   int64 
     26  cj_important_issue_abolishing_death_penalty                        8266 non-null   int64 
     27  cj_important_issue_lowering_incarceration_rates_rural_communities  8266 non-null   int64 
     28  cj_important_issue_improving_prison_conds                          8266 non-null   int64 
     29  cj_important_issue_restoring_voting_rights                         8266 non-null   int64 
     30  cj_important_issue_reducing_prison_pop                             8266 non-null   int64 
     31  cj_important_issue_ending_war_on_drugs                             8266 non-null   int64 
     32  cj_important_issue_ending_private_prisons                          8266 non-null   int64 
     33  cj_important_issue_lowering_sentences_violent_crimes               8266 non-null   int64 
     34  cj_important_issue_raising_wages_incarcerated_workers              8266 non-null   int64 
     35  who_vote_for                                                       7564 non-null   object
     36  approve_disapprove_trump                                           7637 non-null   object
    dtypes: int64(11), object(26)
    memory usage: 2.3+ MB



```python
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>identifies_as_man</th>
      <th>identifies_as_woman</th>
      <th>identifies_as_hispanic_or_latinx</th>
      <th>identifies_as_black</th>
      <th>identifies_as_white</th>
      <th>highest_education_level</th>
      <th>length_in_this_facility</th>
      <th>state</th>
      <th>party</th>
      <th>...</th>
      <th>cj_important_issue_lowering_incarceration_rates_rural_communities</th>
      <th>cj_important_issue_improving_prison_conds</th>
      <th>cj_important_issue_restoring_voting_rights</th>
      <th>cj_important_issue_reducing_prison_pop</th>
      <th>cj_important_issue_ending_war_on_drugs</th>
      <th>cj_important_issue_ending_private_prisons</th>
      <th>cj_important_issue_lowering_sentences_violent_crimes</th>
      <th>cj_important_issue_raising_wages_incarcerated_workers</th>
      <th>who_vote_for</th>
      <th>approve_disapprove_trump</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 37 columns</p>
</div>



# Part 2: Clean the data

## 2A: Make a dataframe with only the specific columns in `col_list` below


```python
col_list = ['identifies_as_woman', 'identifies_as_hispanic_or_latinx', 'identifies_as_black',
            'identifies_as_white', 'highest_education_level', 'state', 'direction_country_headed',
            'should_incarcerated_vote', 'incarceration_impacts_motivation_to_vote']
```


```python
df = df[col_list]
```

## 2B. Convert string columns to boolean

There are several columns where all of the non-missing values are either 'True' or 'False', but the data are stored as strings, not booleans. 
* Convert the 4 `identifies_as...` columns to booleans using the `.astype('boolean')` method for each Pandas series. [Check out the documentation](https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html) if you're wondering how to go about doing this. 
    * **Hint:** you'll probably want to figure this out with 1 column first, then apply the same code 3 more times to the other columns
* Then, check to make sure that these columns are boolean datatype

Solution (will likely draw warnings from Pandas but will work)
```python
df['identifies_as_woman'] = df['identifies_as_woman'].astype('boolean')
df['identifies_as_hispanic_or_latinx'] = df['identifies_as_hispanic_or_latinx'].astype('boolean')
df['identifies_as_black'] = df['identifies_as_black'].astype('boolean')
df['identifies_as_white'] = df['identifies_as_white'].astype('boolean')
```


```python
# Solution using .loc()
df.loc[:, 'identifies_as_woman'] = df['identifies_as_woman'].astype('boolean')
df.loc[:, 'identifies_as_hispanic_or_latinx'] = df['identifies_as_hispanic_or_latinx'].astype('boolean')
df.loc[:, 'identifies_as_black'] = df['identifies_as_black'].astype('boolean')
df.loc[:, 'identifies_as_white'] = df['identifies_as_white'].astype('boolean')
```


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 8266 entries, 0 to 8265
    Data columns (total 9 columns):
     #   Column                                    Non-Null Count  Dtype  
    ---  ------                                    --------------  -----  
     0   identifies_as_woman                       6240 non-null   boolean
     1   identifies_as_hispanic_or_latinx          6240 non-null   boolean
     2   identifies_as_black                       6240 non-null   boolean
     3   identifies_as_white                       6240 non-null   boolean
     4   highest_education_level                   5618 non-null   object 
     5   state                                     2936 non-null   object 
     6   direction_country_headed                  8043 non-null   object 
     7   should_incarcerated_vote                  7833 non-null   object 
     8   incarceration_impacts_motivation_to_vote  7741 non-null   object 
    dtypes: boolean(4), object(5)
    memory usage: 387.6+ KB


## 2C: Deal the missing data

* First, identify how many missing datapoints there are in each column. 
* For now, let's say we only want to work with data where the participant has shared whether they identify as a woman (i.e. remove rows where `identifies_as_woman` is missing)


```python
# check number of nulls in each column
df.isnull().sum()
```




    identifies_as_woman                         2026
    identifies_as_hispanic_or_latinx            2026
    identifies_as_black                         2026
    identifies_as_white                         2026
    highest_education_level                     2648
    state                                       5330
    direction_country_headed                     223
    should_incarcerated_vote                     433
    incarceration_impacts_motivation_to_vote     525
    dtype: int64




```python
# remove nulls for that column
df = df[-df['identifies_as_woman'].isnull()]
```


```python
# check it again
df.isnull().sum()
```




    identifies_as_woman                            0
    identifies_as_hispanic_or_latinx               0
    identifies_as_black                            0
    identifies_as_white                            0
    highest_education_level                      622
    state                                       3304
    direction_country_headed                     222
    should_incarcerated_vote                     431
    incarceration_impacts_motivation_to_vote     522
    dtype: int64



# 3. Get some descriptive statistics

Now that we've cleaned the data just a little bit, let's start to understand who is included in this dataset and how they answered some of the questions. 

## 3A. Who are the survey respondents?
Your goal for this part is to fill in all the blank pieces of info:

* Number of survey respondents who identify as a woman:
* **Percent** of survey respondents who identify as a woman:
* Percent of survey respondents who identify as Black:
* Percent of survey respondents who identify as White:
* Percent of survey respondents who identify as Hispanic or Latinx:
* From which state are the most survey respondents from:
* Percent of survey respondents where the information on their state is missing:


**Hint1:** you can use the `.value_counts()` method on each DataFrame column to get this info. Check out [the documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html) for more info, and **make sure to set `dropna=False`** so you can see how many missing datapoints there are

**Hint2:** To convert numbers of respondents to percentages, you can divide by the total number of respondents (which is the total number of rows in the DataFrame). Then multiply this by 100



```python
df['identifies_as_woman'].value_counts(dropna=False)
```




    False    5800
    True      440
    NaN         0
    Name: identifies_as_woman, dtype: Int64




```python
# to get as percentages/divide by number of rows in the dataframe
# multiplying by 100 to get percentages from proportions
num_respondents = df.shape[0]
100*df['identifies_as_woman'].value_counts(dropna=False)/num_respondents
```




    False    92.948718
    True      7.051282
    NaN       0.000000
    Name: identifies_as_woman, dtype: float64




```python
100*df['identifies_as_black'].value_counts(dropna=False)/num_respondents
```




    False    84.391026
    True     15.608974
    NaN       0.000000
    Name: identifies_as_black, dtype: float64




```python
100*df['identifies_as_white'].value_counts(dropna=False)/num_respondents
```




    True     62.067308
    False    37.932692
    NaN       0.000000
    Name: identifies_as_white, dtype: float64




```python
100*df['identifies_as_hispanic_or_latinx'].value_counts(dropna=False)/num_respondents
```




    False    93.028846
    True      6.971154
    NaN       0.000000
    Name: identifies_as_hispanic_or_latinx, dtype: float64




```python
100*df['state'].value_counts(dropna=False)/num_respondents
```




    NaN    52.948718
    KS     23.060897
    AR     18.012821
    MT      3.413462
    CA      1.714744
    ME      0.432692
    IL      0.416667
    Name: state, dtype: float64



* Number of survey respondents who identify as a woman: 440
* **Percent** of survey respondents who identify as a woman: 7%
* Percent of survey respondents who identify as Black: 15.6%
* Percent of survey respondents who identify as White: 62.1%
* Percent of survey respondents who identify as Hispanic or Latinx: 6.97%
* From which state are the most survey respondents from: Kansas (KS) (23.1%)
* Percent of survey respondents where the information on their state is missing: 52.9%

## 3B. How do views on voting and policy vary among survey respondents?

For each of the questions below, use the `.value_counts(dropna=False)` method to come up with your own answer. Back it up with specific proportions or percentages from the data!

#### Do most of the survey respondents think that people who are incarcerated should be able to vote? (use the `should_incarcerated_vote` column)

*These are responses to the question, 'Should people who are currently incarcerated be allowed to vote, no matter their crime?'*


```python
100*df['should_incarcerated_vote'].value_counts(dropna=False)/num_respondents
```




    Yes                        71.330128
    No                         11.586538
    Don't know / No opinion    10.176282
    NaN                         6.907051
    Name: should_incarcerated_vote, dtype: float64



Yes, 71% said yes to this question. Of the remaining respondents, the a large proportion of them either had no opinion or the response was missing. 

#### Do most of the survey respondents think that the country is headed in the right direction? (use the `direction_country_headed` column)

*Responses to the question, 'In general, do you think things in our country are headed in the right direction or do you feel things are headed down the wrong track?'*


```python
100*df['direction_country_headed'].value_counts(dropna=False)/num_respondents
```




    In between         35.144231
    Wrong track        34.759615
    Right direction    15.769231
    No opinion         10.769231
    NaN                 3.557692
    Name: direction_country_headed, dtype: float64



It seems like opinions vary a lot here. The largest proportion of people (35%) said 'In Between'. However, almost as many said 'Wrong track' (34.7%), which is much more than 'Right direction' (15.7%). So, overall more people felt that the country was headed in the wrong direction than the right direction, but there were also a lot of people who felt that it wasn't exactly one or another, or who had no opinion. 

#### Does incarceration change motivation to vote? If so, how? (use the `incarceration_impacts_motivation_to_vote` column)

*Responses to the question, 'What impact has incarceration had on your motivation to vote?	'*


```python
100*df['incarceration_impacts_motivation_to_vote'].value_counts(dropna=False)/num_respondents
```




    No impact                                   36.121795
    Increased my motivation to vote             33.317308
    Slightly increased my motivation to vote    11.538462
    NaN                                          8.365385
    Decreased my motivation to vote              7.243590
    Slightly decreased my motivation to vote     3.413462
    Name: incarceration_impacts_motivation_to_vote, dtype: float64



Again, responses vary a lot here. The largest group (36.1%) said 'No impact', but apart from that, a far higher percent of respondents said 'increased' or 'slightly increased' (33.3% and 11.6%), as opposed to 'decreased' or 'slightly decreased' (7.2% and 3.4%). Overall in this group of respondents, it seems like incarceration doesn't always impact motivation to vote, but if it does, it more often increases motivation. 

# Part 4: Save the data to csv

Save the DataFrame you cleaned for later use to the `jtc_class_code/datasets` folder on your computer. Give it a clear file name so you know what it is. (use `index=False`) if you don't want the extra column


```python
df.to_csv('../../datasets/marshall_incarcerated_survey_clean.csv', index = False)
```

# Wrap-up

Nice job with this challenge! You reviewed a lot of key pandas concepts, and practiced a lot of core data science skills in inspecting & cleaning the data and extracting relevant information.

Remember to comment your code and push to your Github repo!


```python

```
