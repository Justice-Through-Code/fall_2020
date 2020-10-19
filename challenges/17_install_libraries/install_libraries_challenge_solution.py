print("Challenge 1: Install wikipedia and sportsreference Python packages.")
# TODO: Install wikipedia python package - Link to documentation (https://pypi.org/project/wikipedia/)
# TODO: Install sportsreference python package - Link to documentation (https://pypi.org/project/sportsreference/)

print()

print("Challenge 2: Import both packages.")
# TODO: Once you have successfully installed these 2 packages, import both of them

import wikipedia
import sportsreference
from sportsreference.nfl.teams import Teams

print()

print("Challenge 3: Use wikipedia package in a function")
# TODO: Write a function that takes the name of the page you want to search on Wikipedia as an argument and use the wikipedia package to fetch the page of Columbia University. You can find an example for how to do this on the documentation page given above. Print the title of the page, its url and its summary.

def use_wikipedia(page_name):
    # Write code here
    columbia = wikipedia.page(page_name)

    print(columbia.title)
    print(columbia.url)
    print(columbia.summary)

    return

print()

print("Challenge 4: Use sportsreference package in a function")

# TODO: Write a function that uses the sportsreference package to print every NFL team's name and abbreviation. You can find an example for how to do this on the documentation page given above.

def use_sportsreference():
    # Write code here

    teams = Teams()
    for team in teams:
        print(team.name, team.abbreviation)

    return

print()

# Calling both the functions here
use_wikipedia("Columbia University")

print()

use_sportsreference()

