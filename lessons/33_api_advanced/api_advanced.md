# APIs Continued: Making authorized requests

Last time, we learned how to use `requests` to make web requests directly from python. This time, we'll be learning about using other APIs to make **authorized requests**. 

Unlike with `requests`, these tools will allow us to make requests for **specific data** from authorized sources. These are often websites or online databases that are specifically settting up APIs to allow users to look for certain data or use a program for specific uses.

Today we'll learn about two APIs:
* [newsapi](https://newsapi.org/): which allows for pulling and searching news articles from around the world
* [spotipy](https://spotipy.readthedocs.io/en/2.16.1/): allows for accessing Spotify data and commands using python

We'll also learn about **getting and saving API credentials**

## Use News API to find articles from specific sources, or on specific topics

We'll use this to 

First, we'll need to run this in a blank cell in a jupyter notebook to install the api

```python
!pip install newsapi-python
```

Now that it is installed, we can import the library with:


```python
from newsapi import NewsApiClient
```

### Now, check out the docs
[Check out the News API docs](https://newsapi.org/docs/client-libraries/python) for info on how to get started

# Getting the API keys:

Many APIs require **access keys** so that you are logging in to use the API's resources with certain user credentials. This is so the API can give users limits to the numbers of request they can make, or give different users different access priveleges.

The first step is usually to **sign up for an API account** to get an access key. Most websites for APIs have a link for this kind of signup. You can do this for the News API [here](https://newsapi.org/register)

Once you go through the process, you'll see that you now have access to an **API Key**. This is usually a very long string of characters. 

## Saving the API key to a file

Most often, we want to keep API keys **private** since they correspond with our own user accounts. So, it's a good idea to put them into separate files outside of our code, rather than pasting the key directly into code we might share. 
* One efficient way is to copy the key into a file called something like `news_api_key.txt`, then read in the text from the file with python

For example:


```python
with open('news_api_key.txt') as file:
   api_key = file.read()
```

What this piece is doing is:
* Opening up `news_api_key.txt`
* Reading the contents of the file into a variable called `api_key`
* If we ran `print(api_key)`, it would show us the same long string of text

## Using News API

The first thing we need to do now that we have loaded the api key in is to **start an instance of the api client** using our API key. 


```python
news_api = NewsApiClient(api_key)
```

Here, `newsapi` is now our instance of the api client, and we will use this instantiation to acess more API data. 

As indicated in the [docs](https://newsapi.org/docs/client-libraries/python), we can use `get_everything()` to search for all articles. We can also add search terms if we want. 

For example, we can serach for all articles in English that mention Amazon:


```python
news_results = news_api.get_everything(q='Amazon', language='en')
news_results
```




    {'status': 'ok',
     'totalResults': 59993,
     'articles': [{'source': {'id': 'techcrunch', 'name': 'TechCrunch'},
       'author': 'Jonathan Shieber',
       'title': 'Amazon launches Amazon Pharmacy, a delivery service for prescription medications',
       'description': 'A little over two years after its $753 million acquisition of the prescription medicine delivery service Pillpack, Amazon has finally launched Amazon Pharmacy, its online and mobile prescription medication ordering and fulfillment service. Using a secure phar…',
       'url': 'http://techcrunch.com/2020/11/17/amazon-launches-amazon-pharmacy-its-delivery-service-for-prescription-medications/',
       'urlToImage': 'https://techcrunch.com/wp-content/uploads/2020/03/GettyImages-1160670986.jpg?w=599',
       'publishedAt': '2020-11-17T11:00:03Z',
       'content': 'A little over two years after its $753 million acquisition of the prescription medicine delivery service Pillpack, Amazon has finally launched Amazon Pharmacy, its online and mobile prescription medi… [+5442 chars]'},
      {'source': {'id': 'techcrunch', 'name': 'TechCrunch'},
       'author': 'Jonathan Shieber',
       'title': 'GoodRx, Walgreens, CVS shares all down on Amazon’s Pharmacy news',
       'description': 'Consumer healthcare stocks are plummeting this morning on news that Amazon has finally launched its integrated pharmacy service. Amazon launches Amazon Pharmacy, a delivery service for prescription medications The news, which could dramatically reshape the he…',
       'url': 'http://techcrunch.com/2020/11/17/goodrx-walgreens-cvs-shares-all-down-on-amazons-pharmacy-news/',
       'urlToImage': 'https://techcrunch.com/wp-content/uploads/2019/09/GettyImages-1058454392.jpg?w=600',
       'publishedAt': '2020-11-17T14:19:14Z',
       'content': 'Consumer healthcare stocks are plummeting this morning on news that Amazon has finally launched its integrated pharmacy service.\r\nThe news, which could dramatically reshape the healthcare landscape b… [+1842 chars]'},
      {'source': {'id': 'the-verge', 'name': 'The Verge'},
       'author': 'Loren Grush',
       'title': 'International coalition of activists launches protest against Amazon',
       'description': 'On November 27th, or Black Friday, an international group of Amazon workers and climate activists launched a new campaign called Make Amazon Pay, with stunts planned all over the world. Their goals include better pay for Amazon workers and reducing the compan…',
       'url': 'https://www.theverge.com/2020/11/27/21722421/make-amazon-pay-protest-campaign-black-friday',
       'urlToImage': 'https://cdn.vox-cdn.com/thumbor/bFFK53WuA2FojTJ74IZ1kFEE9Z8=/0x457:4032x2568/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/22125105/002.jpg',
       'publishedAt': '2020-11-27T14:54:36Z',
       'content': 'The “Make Amazon Pay” logo projected onto Amazon’s campus in Hyderabad, India. | Image: Make Amazon Pay campaign\r\n\n \n\n An international group of climate activists and Amazon warehouse workers have la… [+3939 chars]'},
      {'source': {'id': None, 'name': 'New York Times'},
       'author': 'Yiren Lu',
       'title': 'Can Shopify Compete With Amazon Without Becoming Amazon?',
       'description': 'If the key to Amazon’s success has been to put the customer first, for Shopify the key has been to put the merchant first.',
       'url': 'https://www.nytimes.com/2020/11/24/magazine/shopify.html',
       'urlToImage': 'https://static01.nyt.com/images/2020/11/29/magazine/29mag-shopify/29mag-shopify-facebookJumbo.png',
       'publishedAt': '2020-11-25T15:17:39Z',
       'content': 'Similarly, a partnership ethos sounds great and offers flexibility and reach, but there are also real drawbacks in trying to align the incentives and interests of so many parties. Facebook and Shopif… [+5227 chars]'},
      {'source': {'id': None, 'name': 'Lifehacker.com'},
       'author': 'Brendan Hesse',
       'title': 'Is Amazon Sidewalk Safe, or Should You Disable It Now?',
       'description': 'Before the end of 2020, Amazon will launch a new feature called Sidewalk that creates small, public internet networks powered by Echo smart speakers and Ring home security products in your neighborhood.Read more...',
       'url': 'https://lifehacker.com/is-amazon-sidewalk-safe-or-should-you-disable-it-now-1845793859',
       'urlToImage': 'https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/ezpdijuujqbef39osmre.jpg',
       'publishedAt': '2020-12-02T22:15:00Z',
       'content': 'Before the end of 2020, Amazon will launch a new feature called Sidewalk that creates small, public internet networks powered by Echo smart speakers and Ring home security products in your neighborho… [+2781 chars]'},
      {'source': {'id': None, 'name': 'Lifehacker.com'},
       'author': 'Elizabeth Yuko',
       'title': 'Amazon Recalls Ring Doorbells After Reports They Catch on Fire',
       'description': 'In a year where it seems everything is both literally and figuratively on fire, it’s not surprising that we can now add Amazon’s Ring Video Doorbell to the list. Yes, it turns out that the device you purchased and installed for the purpose of making your home…',
       'url': 'https://lifehacker.com/amazon-recalls-ring-doorbells-after-reports-they-catch-1845643691',
       'urlToImage': 'https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/ynubvycah0byafrlnmez.jpg',
       'publishedAt': '2020-11-11T21:00:00Z',
       'content': 'In a year where it seems everything is both literally and figuratively on fire, its not surprising that we can now add Amazons Ring Video Doorbell to the list. Yes, it turns out that the device you p… [+1879 chars]'},
      {'source': {'id': 'techcrunch', 'name': 'TechCrunch'},
       'author': 'Megan Rose Dickey',
       'title': 'Amazon faces lawsuit alleging failure to provide PPE to workers during pandemic',
       'description': 'Christian Smalls, a former Amazon warehouse employee, filed a lawsuit against the company today alleging Amazon failed to provide personal protective equipment to Black and Latinx workers during the COVID-19 pandemic. The class action suit alleges Amazon fail…',
       'url': 'http://techcrunch.com/2020/11/12/amazon-faces-lawsuit-alleging-failure-to-provide-ppe-to-workers-during-pandemic/',
       'urlToImage': 'https://techcrunch.com/wp-content/uploads/2020/11/GettyImages-1228910433.jpg?w=603',
       'publishedAt': '2020-11-12T20:18:35Z',
       'content': 'Christian Smalls, a former Amazon warehouse employee, filed a lawsuit against the company today alleging Amazon failed to provide personal protective equipment to Black and Latinx workers during the … [+3381 chars]'},
      {'source': {'id': 'wired', 'name': 'Wired'},
       'author': 'Tom Simonite',
       'title': 'Congress Is Eyeing Face Recognition, and Companies Want a Say',
       'description': 'Amazon and Microsoft have hired lobbyists. So too have airlines, retailers, wireless carriers, and cruise operators.',
       'url': 'https://www.wired.com/story/congress-eyeing-face-recognition-companies-want-say/',
       'urlToImage': 'https://media.wired.com/photos/5fb8571e73fc49e41208c778/191:100/w_1280,c_limit/Business-Facial-Recognition-1224837570.jpg',
       'publishedAt': '2020-11-23T12:00:00Z',
       'content': 'Daniel Castro, vice president at the Information Technology and Innovation Foundation, a Washington think tank that receives funding from the tech industry, says face recognition rules would fit with… [+4254 chars]'},
      {'source': {'id': 'engadget', 'name': 'Engadget'},
       'author': 'Karissa Bell',
       'title': 'Amazon now lets you interact with Alexa via text on iOS',
       'description': 'Alexa can now respond to commands via text on iOS. Amazon appears to have quietly added the capability\xa0 in the last few days, though the company officially confirmed the feature to The Verge. \r\n Amazon\r\n With the change, users can opt to text commands to Alex…',
       'url': 'https://www.engadget.com/amazon-adds-text-commands-alexa-ios-app-200311384.html',
       'urlToImage': 'https://o.aolcdn.com/images/dims?resize=1200%2C630&crop=1200%2C630%2C0%2C0&quality=95&image_uri=https%3A%2F%2Fs.yimg.com%2Fos%2Fcreatr-uploaded-images%2F2020-11%2Fda126520-2459-11eb-a5f7-87ade3133b11&client=amp-blogside-v2&signature=f330bca37e5193c2bf5e5876bc94068d3dd3a024',
       'publishedAt': '2020-12-03T20:03:11Z',
       'content': 'Alexa can now respond to commands via text on iOS. Amazon appears to have quietly added the capability\xa0 in the last few days, though the company officially confirmed the feature to The Verge.\r\nWith t… [+384 chars]'},
      {'source': {'id': 'engadget', 'name': 'Engadget'},
       'author': 'Valentina Palladino',
       'title': 'Here are the best Amazon devices worth buying on Cyber Monday',
       'description': 'It’s always advisable to wait until the holiday shopping season to buy Amazon devices. Aside from Amazon Prime Day, this is when Echo speakers, Fire tablets, Kindles and the like are almost guaranteed to hit all-time-low prices. Sure, the company has intermit…',
       'url': 'https://www.engadget.com/best-amazon-devices-sale-cyber-monday-2020-124557651.html',
       'urlToImage': 'https://o.aolcdn.com/images/dims?resize=1200%2C630&crop=1200%2C630%2C0%2C0&quality=95&image_uri=https%3A%2F%2Fs.yimg.com%2Fos%2Fcreatr-uploaded-images%2F2020-10%2F20d06bc0-0a55-11eb-8fed-d4d161d274f8&client=amp-blogside-v2&signature=e5345fe65b73d08af71c2246fd2ac0b64b59e2ac',
       'publishedAt': '2020-11-30T12:45:57Z',
       'content': 'Buy Kindle Paperwhite at Amazon - $85Buy Kindle Oasis at Amazon - $175\r\nAll-new Fire TV Stick - $28\r\nThe all-new Fire TV Stick is discounted to $28, which is 30 percent off its normal price. This str… [+7198 chars]'},
      {'source': {'id': 'engadget', 'name': 'Engadget'},
       'author': 'Valentina Palladino',
       'title': 'Amazon knocks $250 off the Samsung Galaxy S20+ 5G',
       'description': 'Almost all of the handsets Samsung announced this year are premium in every way — including price. But Amazon has made it a bit easier to grab the Galaxy S20+ 5G with a new sale that discounts the smartphone by $250, bringing it down to $950. That’s the best …',
       'url': 'https://www.engadget.com/samsung-galaxy-s20-plus-5g-sale-amazon-early-black-friday-144548446.html',
       'urlToImage': 'https://o.aolcdn.com/images/dims?resize=1200%2C630&crop=1200%2C630%2C0%2C0&quality=95&image_uri=https%3A%2F%2Fs.yimg.com%2Fos%2Fcreatr-uploaded-images%2F2020-11%2F02cea870-28e2-11eb-b7ed-d33556290772&client=amp-blogside-v2&signature=0acff5808765603368f6c9bd722be6481ced7e65',
       'publishedAt': '2020-11-17T14:45:48Z',
       'content': 'We gave the Galaxy S20+ a score of 85, and the biggest difference between it and the S20 Ultra is the camera system. While the S20 Ultra has a crazy 108-megapixel camera with 100x Space Zoom and a 4x… [+1245 chars]'},
      {'source': {'id': 'engadget', 'name': 'Engadget'},
       'author': 'Igor Bonifacic',
       'title': 'Amazon discounts the Kindle Paperwhite to $85 for Black Friday',
       'description': 'If the pandemic has helped you rediscover the joy of reading, Amazon’s latest Kindle deal may be exactly what you’re looking for. For Black Friday, the retailer has discounted the base 8GB Paperwhite with ads by $45 to $85. That’s the same price the company s…',
       'url': 'https://www.engadget.com/amazon-kindle-paperwhite-blackfriday-2020-050114855.html',
       'urlToImage': 'https://o.aolcdn.com/images/dims?resize=1200%2C630&crop=1200%2C630%2C0%2C0&quality=95&image_uri=https%3A%2F%2Fs.yimg.com%2Fos%2Fcreatr-uploaded-images%2F2020-11%2F771612d0-2b77-11eb-a6a7-2e343ee46478&client=amp-blogside-v2&signature=e99450129d9e09d203c9cb087a850547ee40bea8',
       'publishedAt': '2020-11-26T05:01:14Z',
       'content': 'We gave the Paperwhite a score of 95 back in 2018 when Amazon updated the device to make it waterproof and add Bluetooth support. With its compelling mix of features and price, we still think it’s th… [+1384 chars]'},
      {'source': {'id': 'engadget', 'name': 'Engadget'},
       'author': 'Jon Fingas',
       'title': 'Walmart Plus drops $35 order minimum to battle Amazon Prime',
       'description': 'Walmart hasn’t been shy about challenging Amazon Prime with its Plus service, and that now includes no-charge shipping. CNBC reports that Walmart Plus is dropping its $35 order minimum for free one- or two-day shipping as of December 4th. You won’t have to ad…',
       'url': 'https://www.engadget.com/walmart-plus-drops-online-order-minimum-150825637.html',
       'urlToImage': 'https://o.aolcdn.com/images/dims?resize=1200%2C630&crop=1200%2C630%2C0%2C0&quality=95&image_uri=https%3A%2F%2Fs.yimg.com%2Fos%2Fcreatr-uploaded-images%2F2020-09%2F02f53730-ef92-11ea-abbf-ebc05e1d2c0c&client=amp-blogside-v2&signature=9aefee13db2dc64e40c0ea1f30a2878fea37edb3',
       'publishedAt': '2020-12-02T15:08:25Z',
       'content': 'Chief Customer Officer Janey Whiteside pitched this as a “life hack” to obtain holiday gifts and treats that much sooner. However, there’s little doubt that this is meant to undermine Amazon’s minimu… [+591 chars]'},
      {'source': {'id': 'engadget', 'name': 'Engadget'},
       'author': 'Mariella Moon',
       'title': 'FTC: Robocallers are now pretending to be Apple and Amazon',
       'description': 'There’s a new robocall scheme that uses Apple’s and Amazon’s name to rip people off, and the Federal Trade Commission has issued a warning to raise awareness about it. The FTC has posted two versions of the scam on its website, so people would know what to ex…',
       'url': 'https://www.engadget.com/ftc-robocalls-apple-amazon-warning-045846581.html',
       'urlToImage': 'https://o.aolcdn.com/images/dims?resize=1200%2C630&crop=1200%2C630%2C0%2C0&quality=95&image_uri=https%3A%2F%2Fs.yimg.com%2Fos%2Fcreatr-images%2F2019-10%2F108fb9f0-eb70-11e9-bfff-74a6c8c93e0e&client=amp-blogside-v2&signature=d69287c7c94af4ecde00d728e7891bcdac4ccc34',
       'publishedAt': '2020-12-04T04:58:46Z',
       'content': 'There’s a new robocall scheme that uses Apple’s and Amazon’s name to rip people off, and the Federal Trade Commission has issued a warning to raise awareness about it. The FTC has posted two versions… [+885 chars]'},
      {'source': {'id': 'engadget', 'name': 'Engadget'},
       'author': 'Nathan Ingraham',
       'title': 'HBO Max is finally coming to Amazon Fire TV',
       'description': 'The launch of HBO Max was not without some confusion, as the company struggled to make it clear how the subscription differed from the old HBO Now service and where HBO Max would be available. More concerning was the fact that HBO Max wasn’t available at all …',
       'url': 'https://www.engadget.com/hbo-max-app-for-amazon-fire-tv-142410194.html',
       'urlToImage': 'https://o.aolcdn.com/images/dims?resize=1200%2C630&crop=1200%2C630%2C0%2C0&quality=95&image_uri=https%3A%2F%2Fs.yimg.com%2Fos%2Fcreatr-uploaded-images%2F2020-11%2F8ef36740-2816-11eb-9759-9b6a105c78d5&client=amp-blogside-v2&signature=0ca18980cb1b2bbbf00720b718191f9f1f75cf77',
       'publishedAt': '2020-11-16T14:24:10Z',
       'content': 'The launch of HBO Max was not without some confusion, as the company struggled to make it clear how the subscription differed from the old HBO Now service and where HBO Max would be available. More c… [+596 chars]'},
      {'source': {'id': 'engadget', 'name': 'Engadget'},
       'author': 'Valentina Palladino',
       'title': 'Amazon Echo devices get steep discounts ahead of Black Friday',
       'description': 'The next round of Amazon Black Friday deals has begun, with most of the company’s Echo speakers receiving heavy discounts. And considering these are the latest Echos with the new spherical design that only became available about one month ago, the deals are t…',
       'url': 'https://www.engadget.com/amazon-echo-speakers-fire-hd-10-black-friday-2020-deals-050109253.html',
       'urlToImage': 'https://o.aolcdn.com/images/dims?resize=1200%2C630&crop=1200%2C630%2C0%2C0&quality=95&image_uri=https%3A%2F%2Fs.yimg.com%2Fos%2Fcreatr-uploaded-images%2F2020-11%2Ff6dc2950-2b4a-11eb-8b3e-ceabac4f7281&client=amp-blogside-v2&signature=625ef8171331801c4328eea004f1da03f6039014',
       'publishedAt': '2020-11-22T05:01:09Z',
       'content': 'Buy Echo Dot at Amazon - $29Buy Echo Dot with clock at Amazon - $39\r\nFire HD 10 - $80\r\nThe most powerful Fire tablet available, the Fire HD 10 is on sale for $80. Even at its normal price of $150, it… [+3908 chars]'},
      {'source': {'id': 'engadget', 'name': 'Engadget'},
       'author': 'Cherlynn Low',
       'title': 'Amazon adds X-Ray features to its music service',
       'description': 'Amazon is bringing over a popular feature from Kindle and Prime Video to its Music service. The company announced today the Music X-Ray experience is now available for tens of millions of songs in its catalog. According to the company, this will “offer a behi…',
       'url': 'https://www.engadget.com/amazon-music-x-ray-164539864.html',
       'urlToImage': 'https://o.aolcdn.com/images/dims?resize=1200%2C630&crop=1200%2C630%2C0%2C0&quality=95&image_uri=https%3A%2F%2Fs.yimg.com%2Fos%2Fcreatr-uploaded-images%2F2020-11%2F1b0ccfc0-2b4e-11eb-a77f-132291d095db&client=amp-blogside-v2&signature=e3e460a125ff865d3f6289fbda1968caa4c4be4d',
       'publishedAt': '2020-11-20T16:45:39Z',
       'content': 'Amazon is bringing over a popular feature from Kindle and Prime Video to its Music service. The company announced today the Music X-Ray experience is now available for tens of millions of songs in it… [+534 chars]'},
      {'source': {'id': 'engadget', 'name': 'Engadget'},
       'author': 'Daniel Cooper',
       'title': 'Amazon reduces the size of its delivery drone team',
       'description': 'Amazon has confirmed that it is laying off a number of people working on its internal drone delivery project. The Financial Times reported that the mega-retailer had opted to shrink its internal team in favor of using external contractors to complete the work…',
       'url': 'https://www.engadget.com/amazon-drone-term-prime-air-layoffs-102029310.html',
       'urlToImage': 'https://o.aolcdn.com/images/dims?resize=1200%2C630&crop=1200%2C630%2C0%2C0&quality=95&image_uri=https%3A%2F%2Fs.yimg.com%2Fos%2Fcreatr-uploaded-images%2F2020-11%2F42916880-2b17-11eb-ae7f-c5e17befb08d&client=amp-blogside-v2&signature=5bc98b6f555d55d03a2d9b3468ac1005d4d0f384',
       'publishedAt': '2020-11-20T10:20:29Z',
       'content': 'Amazon has confirmed that it is laying off a number of people working on its internal drone delivery project. The Financial Times reported that the mega-retailer had opted to shrink its internal team… [+604 chars]'},
      {'source': {'id': 'engadget', 'name': 'Engadget'},
       'author': 'Nicole Lee',
       'title': 'Amazon Sidewalk will be enabled by default on Echo devices',
       'description': 'Last year, Amazon announced Sidewalk, a shared network designed to keep your smart devices connected beyond the reach of the typical WiFi router. In order to do that, it’ll utilize certain devices as “Sidewalk Bridge” connections, such as Ring cameras and Ech…',
       'url': 'https://www.engadget.com/amazon-sidewalk-echo-default-214620200.html',
       'urlToImage': 'https://o.aolcdn.com/images/dims?resize=1200%2C630&crop=1200%2C630%2C0%2C0&quality=95&image_uri=https%3A%2F%2Fs.yimg.com%2Fos%2Fcreatr-uploaded-images%2F2020-11%2Ff7ef59e0-3354-11eb-b7fd-39f78a8f57db&client=amp-blogside-v2&signature=6342a115fd94c74e7d4a4c858fbe71a85306b692',
       'publishedAt': '2020-11-30T21:46:20Z',
       'content': 'The idea behind Amazon Sidewalk is that it uses the 900 MHz spectrum as well as the aforementioned Sidewalk Bridge device connections to extend the reach of WiFi networks so that outdoor gadgets can … [+1046 chars]'},
      {'source': {'id': 'techcrunch', 'name': 'TechCrunch'},
       'author': 'Anthony Ha',
       'title': 'Daily Crunch: Amazon Web Services stumble',
       'description': 'An Amazon Web Services outage has a wide effect, Salesforce might be buying Slack and Pinterest tests new support for virtual events. This is your Daily Crunch for November 25, 2020. And for those of you who celebrate Thanksgiving: Enjoy! There will be no new…',
       'url': 'http://techcrunch.com/2020/11/25/daily-crunch-amazon-web-services-stumble/',
       'urlToImage': 'https://techcrunch.com/wp-content/uploads/2020/11/GettyImages-1085999578.jpg?w=600',
       'publishedAt': '2020-11-25T23:10:22Z',
       'content': 'An Amazon Web Services outage has a wide effect, Salesforce might be buying Slack and Pinterest tests new support for virtual events. This is your Daily Crunch for November 25, 2020.\r\nAnd for those o… [+2648 chars]'}]}



## Narrowing the search

Wow, that's quite a lot of results. Nice! We can also narrow down the search terms with the `sources`, `from_param` (starting date) and `to` (ending date) parameters. 

So, here we narrow our search to news results from only BBC news between 11/11/2020 and 11/12/2020:


```python
news_results = news_api.get_everything(q='amazon', language='en', sources = 'bbc-news',
                                      from_param = '2020-11-11', to='2020-11-12')
news_results
```




    {'status': 'ok',
     'totalResults': 4,
     'articles': [{'source': {'id': 'bbc-news', 'name': 'BBC News'},
       'author': 'https://www.facebook.com/bbcnews',
       'title': "Amazon's Ring video doorbells catch fire because wrong screw used",
       'description': 'There have been dozens of cases of property damage and injuries to owners.',
       'url': 'https://www.bbc.co.uk/news/technology-54903754',
       'urlToImage': 'https://ichef.bbci.co.uk/news/1024/branded_news/D1E9/production/_115373735_ringg.jpg',
       'publishedAt': '2020-11-11T17:37:25Z',
       'content': "image copyrightGetty Images\r\nimage captionThe video doorbells use a screw to keep the faceplate and battery in place\r\nDozens of Amazon's Ring smart doorbells have caught fire or burned their owners a… [+1909 chars]"},
      {'source': {'id': 'bbc-news', 'name': 'BBC News'},
       'author': 'https://www.facebook.com/bbcnews',
       'title': 'China to clamp down on internet monopolies',
       'description': 'The regulations suggest increasing unease in Beijing with the growing influence of digital platforms',
       'url': 'https://www.bbc.co.uk/news/business-54898357',
       'urlToImage': 'https://ichef.bbci.co.uk/news/1024/branded_news/159D8/production/_115363588_gettyimages-1174671524.jpg',
       'publishedAt': '2020-11-11T05:08:48Z',
       'content': 'image copyrightGetty Images\r\nChina has proposed new regulations aimed at curbing the power of its biggest internet companies. \r\nThe regulations suggest increasing unease in Beijing with the growing i… [+2721 chars]'},
      {'source': {'id': 'bbc-news', 'name': 'BBC News'},
       'author': 'https://www.facebook.com/bbcnews',
       'title': 'Coronavirus: M&S expands its scan-and-pay app to all UK stores',
       'description': 'The retailer says it is bringing the service to 573 stores as part of its response to Covid-19.',
       'url': 'https://www.bbc.co.uk/news/technology-54903748',
       'urlToImage': 'https://ichef.bbci.co.uk/news/1024/branded_news/525E/production/_115368012_m-s.jpg',
       'publishedAt': '2020-11-11T13:11:29Z',
       'content': 'image captionM&amp;S says use of the app should mean fewer queues at its checkouts\r\nMarks &amp; Spencer is expanding use of a "scan, pay and go" app-based service to all of its 573 UK grocery stores.… [+2063 chars]'},
      {'source': {'id': 'bbc-news', 'name': 'BBC News'},
       'author': 'https://www.facebook.com/bbcnews',
       'title': 'Climate change: Protecting the rainforest through your shopping basket',
       'description': "Green groups welcome the UK's plan to outlaw the import of food and other goods from protected areas.",
       'url': 'https://www.bbc.co.uk/news/science-environment-54894962',
       'urlToImage': 'https://ichef.bbci.co.uk/news/1024/branded_news/13502/production/_115360197_mediaitem115360195.jpg',
       'publishedAt': '2020-11-11T03:02:28Z',
       'content': 'By Roger HarrabinBBC environment analyst\r\nimage captionA road cuts through burnt Amazon rainforest in Brazil\r\nNew laws should help prevent consumers from buying food grown on rainforest land that has… [+3419 chars]'}]}



# Parsing our API data

This is a lot of data, and it might look confusing at first! However, if we look carefully, we can see that we are getting back a nested dictionary from the API request. Most importantly, there is a value in this outer dictionary called `articles`, which has all articles stored within it.

### Getting the article titles

We can **write a function** to parse this dictionary and pull out the titles of each article as follows:


```python
def get_article_titles(results):
    titles = []
    for article in results['articles']:
        titles.append(article['title'])
    return titles
```

Now, let's run the function on the articles including 'Amazon' and print the titles: 


```python
news_results = news_api.get_everything(q='amazon', language='en')
titles = get_article_titles(news_results)
titles
```




    ['Amazon launches Amazon Pharmacy, a delivery service for prescription medications',
     'GoodRx, Walgreens, CVS shares all down on Amazon’s Pharmacy news',
     'International coalition of activists launches protest against Amazon',
     'Can Shopify Compete With Amazon Without Becoming Amazon?',
     'Is Amazon Sidewalk Safe, or Should You Disable It Now?',
     'Amazon Recalls Ring Doorbells After Reports They Catch on Fire',
     'Amazon faces lawsuit alleging failure to provide PPE to workers during pandemic',
     'Congress Is Eyeing Face Recognition, and Companies Want a Say',
     'Amazon now lets you interact with Alexa via text on iOS',
     'Here are the best Amazon devices worth buying on Cyber Monday',
     'Amazon knocks $250 off the Samsung Galaxy S20+ 5G',
     'Amazon discounts the Kindle Paperwhite to $85 for Black Friday',
     'Walmart Plus drops $35 order minimum to battle Amazon Prime',
     'FTC: Robocallers are now pretending to be Apple and Amazon',
     'HBO Max is finally coming to Amazon Fire TV',
     'Amazon Echo devices get steep discounts ahead of Black Friday',
     'Amazon adds X-Ray features to its music service',
     'Amazon reduces the size of its delivery drone team',
     'Amazon Sidewalk will be enabled by default on Echo devices',
     'Daily Crunch: Amazon Web Services stumble']



## Putting the data into a pandas DataFrame

Often, a large dictionary can be made easier to work with through putting it into a dataframe. Since the `articles` value in this dictionary is a list of dictionaries with 1 nested dictionary per article, we can convert this to a dataframe:


```python
import pandas as pd
```


```python
articles_info = pd.DataFrame(news_results['articles'])
```


```python
articles_info.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>source</th>
      <th>author</th>
      <th>title</th>
      <th>description</th>
      <th>url</th>
      <th>urlToImage</th>
      <th>publishedAt</th>
      <th>content</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>{'id': 'techcrunch', 'name': 'TechCrunch'}</td>
      <td>Jonathan Shieber</td>
      <td>Amazon launches Amazon Pharmacy, a delivery se...</td>
      <td>A little over two years after its $753 million...</td>
      <td>http://techcrunch.com/2020/11/17/amazon-launch...</td>
      <td>https://techcrunch.com/wp-content/uploads/2020...</td>
      <td>2020-11-17T11:00:03Z</td>
      <td>A little over two years after its $753 million...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>{'id': 'techcrunch', 'name': 'TechCrunch'}</td>
      <td>Jonathan Shieber</td>
      <td>GoodRx, Walgreens, CVS shares all down on Amaz...</td>
      <td>Consumer healthcare stocks are plummeting this...</td>
      <td>http://techcrunch.com/2020/11/17/goodrx-walgre...</td>
      <td>https://techcrunch.com/wp-content/uploads/2019...</td>
      <td>2020-11-17T14:19:14Z</td>
      <td>Consumer healthcare stocks are plummeting this...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>{'id': 'the-verge', 'name': 'The Verge'}</td>
      <td>Loren Grush</td>
      <td>International coalition of activists launches ...</td>
      <td>On November 27th, or Black Friday, an internat...</td>
      <td>https://www.theverge.com/2020/11/27/21722421/m...</td>
      <td>https://cdn.vox-cdn.com/thumbor/bFFK53WuA2FojT...</td>
      <td>2020-11-27T14:54:36Z</td>
      <td>The “Make Amazon Pay” logo projected onto Amaz...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>{'id': None, 'name': 'New York Times'}</td>
      <td>Yiren Lu</td>
      <td>Can Shopify Compete With Amazon Without Becomi...</td>
      <td>If the key to Amazon’s success has been to put...</td>
      <td>https://www.nytimes.com/2020/11/24/magazine/sh...</td>
      <td>https://static01.nyt.com/images/2020/11/29/mag...</td>
      <td>2020-11-25T15:17:39Z</td>
      <td>Similarly, a partnership ethos sounds great an...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>{'id': None, 'name': 'Lifehacker.com'}</td>
      <td>Brendan Hesse</td>
      <td>Is Amazon Sidewalk Safe, or Should You Disable...</td>
      <td>Before the end of 2020, Amazon will launch a n...</td>
      <td>https://lifehacker.com/is-amazon-sidewalk-safe...</td>
      <td>https://i.kinja-img.com/gawker-media/image/upl...</td>
      <td>2020-12-02T22:15:00Z</td>
      <td>Before the end of 2020, Amazon will launch a n...</td>
    </tr>
  </tbody>
</table>
</div>



Now, if we wanted to use this data for some kind of analysis, we'd be in great shape!

# The Spotify API (spotipy)

Now, we'll do a really quick intro to the Spotipy API, which will allow us to search and use Spotify features with python. 

To install the API, run in a blank code cell:

```python
!pip install spotipy
```

## Get started: make a spotify developer account

If you don't have a Spotify account already, you'll want to set up one (it is free) to use the API. Then, set up a Developer Account at [this link](https://developer.spotify.com/dashboard/login) to start getting access to API keys

### Check out the docs

Before we begin with the API, let's [check out the docs!](https://spotipy.readthedocs.io/en/2.13.0/) What do we need to do to get started?

## spotify API keys: `client_id` and `client_secret`

Unlike News API, Spotify requres two different keys for using the API:  `client_id` and `client_secret`. You can get these from your developer account, but we'll also need to find a good way to load them into python.

This time, we'll us a json file for this. You can think of a json file as basically a file with a dictionary in -- every item is stored as key-value pairs. So, let's make a file called `spotify_screts.json` in the same directory as this notebook. It should look like this:

```json
{
    "client_id" : "<paste client id here>",
    "client_secret" : "<paste client secret here>"
}
```

Now, we can import the `json` library and import the file as follows to read it in:


```python
import json

with open('spotify_secrets.json') as file:
    secrets = json.load(file)
```

Notice that now the contents of the file are stored as a dictionary in python, with key-value pairs for `client_id` and `client_secret`


```python
print(type(secrets))
print(secrets.keys())
```

    <class 'dict'>
    dict_keys(['client_id', 'client_secret'])


## Load the API and Credential Handler

We need to set up both the spotipy api and a way to give it our client credentials


```python
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# set up the credentials with the client_id and client_secret
creds = SpotifyClientCredentials(secrets['client_id'], secrets['client_secret'])

# instantiate a spotipy client with the credentials
sp = spotipy.Spotify(client_credentials_manager=creds)
```

#### Search for an Artist 

In Spotify, every single artist has a unique `id`, which can be used to search for different things about the artist. Here, we can make a function to search for an artist using `sp.search()` and get their id. 


```python
artist_results = sp.search(q='Kendrick Lamar', type='artist')
artist_results
```




    {'artists': {'href': 'https://api.spotify.com/v1/search?query=Kendrick+Lamar&type=artist&offset=0&limit=10',
      'items': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/2YZyLoL8N0Wb9xBt1NhZWg'},
        'followers': {'href': None, 'total': 15953881},
        'genres': ['conscious hip hop', 'hip hop', 'rap', 'west coast rap'],
        'href': 'https://api.spotify.com/v1/artists/2YZyLoL8N0Wb9xBt1NhZWg',
        'id': '2YZyLoL8N0Wb9xBt1NhZWg',
        'images': [{'height': 640,
          'url': 'https://i.scdn.co/image/3a836196bfb341f736c7fe2704fb75de53f8dfbb',
          'width': 640},
         {'height': 320,
          'url': 'https://i.scdn.co/image/5259c0496329b3f608a1ae0edb799cd2f8451acc',
          'width': 320},
         {'height': 160,
          'url': 'https://i.scdn.co/image/b772a78d4cb192268d6f601a78f21044c17d6dda',
          'width': 160}],
        'name': 'Kendrick Lamar',
        'popularity': 87,
        'type': 'artist',
        'uri': 'spotify:artist:2YZyLoL8N0Wb9xBt1NhZWg'},
       {'external_urls': {'spotify': 'https://open.spotify.com/artist/3M8jTGG0AItu4XYotTlC6M'},
        'followers': {'href': None, 'total': 727},
        'genres': [],
        'href': 'https://api.spotify.com/v1/artists/3M8jTGG0AItu4XYotTlC6M',
        'id': '3M8jTGG0AItu4XYotTlC6M',
        'images': [],
        'name': 'Kendrick Lamar & Jay Rock',
        'popularity': 20,
        'type': 'artist',
        'uri': 'spotify:artist:3M8jTGG0AItu4XYotTlC6M'},
       {'external_urls': {'spotify': 'https://open.spotify.com/artist/47lIHBDQOx2KzAuXujwzj1'},
        'followers': {'href': None, 'total': 7},
        'genres': [],
        'href': 'https://api.spotify.com/v1/artists/47lIHBDQOx2KzAuXujwzj1',
        'id': '47lIHBDQOx2KzAuXujwzj1',
        'images': [],
        'name': 'Kendrick Lamar Cousin',
        'popularity': 0,
        'type': 'artist',
        'uri': 'spotify:artist:47lIHBDQOx2KzAuXujwzj1'}],
      'limit': 10,
      'next': None,
      'offset': 0,
      'previous': None,
      'total': 3}}



Again, this is a really complicated dictionary to parse! How could we get the `id` for Kendrick Lamar specifically?


```python
artist_results['artists']['items'][0]['id']
```




    '2YZyLoL8N0Wb9xBt1NhZWg'



Here, let's make a function to get the `id` for an artist we search, so we can get the `id` for Kendrick Lamar (or another artist) more easily


```python
def get_artist_id(results):
    return results['artists']['items'][0]['id']
```


```python
artist_results = sp.search(q='Kendrick Lamar', type='artist')
artist_id = get_artist_id(artist_results)

print(artist_id)
```

    2YZyLoL8N0Wb9xBt1NhZWg


# Wrapping up

We learned how to start working with both the News API and Spotipy today! In the lesson, you'll go a little further with using each of these to get data. This kind of work should be a big help for learning to work with the kinds of APIs you may use for your WOW projects as well.


```python

```
