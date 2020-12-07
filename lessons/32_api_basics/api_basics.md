# Connecting to other data sources

In previous lessons, we have learned to use data imported from csv files. The data collected in csv files are put together and made available to the public. Today we will learn another way to access data called **APIs**. Let's cover a few definitions first:

# What is an API?
An API, or Application Programming Interface are set of commands that one software can use to interact with another software without having to know it's internal logic. 

For example, in the context of the pandas library, using the API means using data structures like **DataFrame**, **Series** and functions like **read_csv**. These are parts of the pandas library exposed or made available to us for use while their implementation details are hidden from us. 

Similarly, APIs also help us interact with servers over the internet to retrieve and send data. You will often hear the term API used interchangeably to describe this interaction. To understand this interaction, we need to look at how the web works.

# The internet
Visiting a website involves the web browser making multiple **requests** for resources like data, HTML pages, scripts, images, etc from servers. This system of exchanging data is enabled by the **HTTP** protocol. 

Using APIs to interact with servers is similar to visiting a website, we make requests for data to a server and the server responds with data over **HTTP**.

![](https://media.prod.mdn.mozit.cloud/attachments/2016/08/09/13677/d031b77dee83f372ffa4e0389d68108b/Fetching_a_page.png)

# Demo 1: Making a web request

We will be using a popular HTTP library called **requests** that helps Python users make web requests easily. 


```python
!pip install requests
```


```python
import requests
```


```python
response = requests.get('https://www.google.com')
```

Using **requests.get()** we just made a request for the Google web page like a web browser when you type in the URL in the address bar.


```python
response.text
```

Printing **response.text** reveals the HTML code of Google web page.

# Demo 2: Getting jobs data using Github Jobs API

We can also make requests for specific data. Let's explore the [**Github Jobs API**](https://jobs.github.com/api) page. 
- The API page contains instructions to get jobs data using their API.
- Examples show the URL can be manipulated to get specific data back.

# Building the request

### URL

URL/route/endpoint are used to specify the resource being requested. In this case, we get job positions that contain **Python** in the description and based in **New York**


```python
url = 'https://jobs.github.com/positions.json?description=python&location=new+york'
```

### Request Method or HTTP Verb


```python
response = requests.get(url)
```

The **.get()** function doesn't refer to the verb in the english language but something called an **HTTP Verb**. HTTP defines a set of request methods to indicate the desired action to be performed for a given resource. A few popular ones are **GET, POST , PUT  and  DELETE**. 

More on HTTP Verbs [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods).

# Reading the response

### HTTP Response Status Code

The server response always includes HTTP response status code. They indicate whether a specific HTTP request has been successfully completed. Responses are grouped in five classes:
- `100–199` Informational responses,
- `200–299` Successful responses,
- `300–399` Redirects,
- `400–499` Client errors,
- `500–599` and Server errors


```python
response.status_code
```

We got a 200 status code, which means the server responded to our request for data successfully!

### JSON

The response text contains the data. However, it is in a format called JSON (JavaScript Object Notation), which is a common way to represent data sent over a network. It is programming language agnostic, which means requests from  applications built in different programming languages can receive and use it.


```python
response.text
```


```python
type(response.text)
```

Let's convert the JSON into Python data structures


```python
jobs = response.json()
type(jobs)
```

Now can traverse the output safely


```python
for job in jobs:
   print(job['title'])
```


```python

```

# Demo 3: Getting TV show data from TVMAZE API
Let's explore the [TV MAZE API](http://www.tvmaze.com/api) page.
### Finding the names of all episodes of 'Seinfeld'


First we need to find the **id** of the show. Let's use the 'Show search' endpoint to get it.


```python
search_response = requests.get('http://api.tvmaze.com/search/shows?q=seinfeld')
seinfeld_data = search_response.json()
seinfeld_id = seinfeld_data[0]['show']['id']
```

Now that we have the **id** we can use the 'Show episode list' endpoint.


```python
episodes_url = f'http://api.tvmaze.com/shows/{seinfeld_id}/episodes'

episodes_response = requests.get(episodes_url)
episodes = episodes_response.json()

for episode in episodes:
    print(episode['name'])
```
