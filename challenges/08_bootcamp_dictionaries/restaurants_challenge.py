print("Challenge: Favoruite Restuarants")

print()

print("Question 1")

print("Below is a dictionary of restaurants fetched from the Yelp. Go through the dictionary and figure print out the following 3 pieces of information about the restaurant: \n1. The latitude and longitude of Four Barrel Coffee \n2. The complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code. \n3. The website of Four Barrel Coffee.")

restaurants = {
    "total": 8228,
    "businesses": [
        {
            "rating": 4,
            "price": "$",
            "phone": "+14152520800",
            "id": "E8RJkjfdcwgtyoPMjQ_Olg",
            "alias": "four-barrel-coffee-san-francisco",
            "is_closed": False,
            "categories": [
                            {
                                "alias": "coffee",
                                "title": "Coffee & Tea"
                            }
                        ],
            "review_count": 1738,
            "name": "Four Barrel Coffee",
            "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
            "coordinates": {
                            "latitude": 37.7670169511878,
                            "longitude": -122.42184275
                            },
            "image_url": "http://s3-media2.fl.yelpcdn.com/bphoto/MmgtASP3l_t4tPCL1iAsCg/o.jpg",
            "location": {
                            "city": "San Francisco",
                            "country": "US",
                            "address2": "",
                            "address3": "",
                            "state": "CA",
                            "address1": "375 Valencia St",
                            "zip_code": "94103"
                        },
            "distance": 1604.23,
            "transactions": ["pickup", "delivery"]
        }
        # ... (More restaurants)
        ],
    "region": {
                "center":
                     {
                        "latitude": 37.767413217936834,
                        "longitude": -122.42820739746094
                    }
                }
    }

# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.
# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
# TODO: Write code to print the URL of the website of Four Barrel Coffee.


print()

print("Question 2")

# TODO: Create a new empty dictionary called fav_restaurants.
# TODO: Choose 3 of your most favourite restaurants in NYC and add the following information for those restaurants inside fav_restaurants:
#         1. Name of the restaurant
#         2. Address of the restaurant
#         3. Favourite dish in that restaurant
#         4. Opening and closing hours of that restaurant
# TODO: Print the dictionary.

# The dictionary should look like this


'''
fav_restaurants =
{
    "restaurant 1":
        {
            "name": "Subway",
            "address": "116th & Broadway, NY 10016",
            "fav_dish": "Pizza Sub",
            "hours": "12 PM - 12 AM"
        },
    "restaurant 2": ....and so on
}
'''

print()

print("Question 3")

print("Imagine that any 1 of your most favourite restaurants closed down during the Covid. Remove the details of that restaurant from the dictionary fav_restaurants.")

# TODO: Remove 1 restaurant from the dictionary fav_restaurants.
# TODO: Print the new dictionary. The new dictionary should contain only 2 restaurants.

print()

print("Question 4")

print("Imagine that another one of your most favourite restaurants modified its opening and closing hours during Covid. Update just the hours field for 1 restaurant in the dictionary fav_restaurants.")

# TODO: Update the hours field of 1 restaurant in the dictionary fav_restaurants.
# TODO: Print the old and new open hours of the restaurant by accessing those fields from the dictionary.

print()
