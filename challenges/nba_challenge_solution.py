print("Challenge 2.1 Solution:")
print("Create a variable for the number of 3pt shots made by Fred VanVleet")
print("Create a variable for the number of 3 pt shots made by James Harden")
jamal_murray_3pts_made = 46
fred_vanvleet_3pts_made = 43
james_harden_3pts_made = 37
print()

print("Challenge 2.2 Solution:")
print("Print the variables that track the number of 3 pt shots made by each of the three players")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_vanvleet_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots")
print()

print("Challenge 2.3 Solution: Store the number of three point shot attempts in variables for each player")
jamal_murray_3pts_attempts = 93
fred_vanvleet_3pts_attempts = 110
james_harden_3pts_attempts = 109
print()

print("Challenge 2.4 Solution: Build on your print statement")
# TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
# the number of three point shots for each player. E.g., output should be similar to
# "In the 2020 NBA playoffs, player X made Y 3 point shots and Z 3 point shot attempts."
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} "
      f"3 point shots and attempted {jamal_murray_3pts_attempts} 3 point shots")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_vanvleet_3pts_made} "
      f"3 point shots and attempted {fred_vanvleet_3pts_attempts} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} "
      f"3 point shots and attempted {james_harden_3pts_attempts} 3 point shots")
print()

print("Challenge 2.5 Solution: Calculate, store, and print the three point percentage for each player")
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
jamal_murray_3pts_percentage = jamal_murray_3pts_made/jamal_murray_3pts_attempts
fred_vanvleet_3pts_percentage = fred_vanvleet_3pts_made/fred_vanvleet_3pts_attempts
james_harden_3pts_percentage = james_harden_3pts_made/james_harden_3pts_attempts
print(f"In the 2020 NBA playoffs, Jamal Murray's 3 point percentage was {jamal_murray_3pts_percentage}")
print(f"In the 2020 NBA playoffs, Fred VanVleet's 3 point percentage was {fred_vanvleet_3pts_percentage}")
print(f"In the 2020 NBA playoffs, James Harden's 3 point percentage was {james_harden_3pts_percentage}")

print("Challenge 3.1 Solution: Calculate, store, and print total points scored")
# In the 2020 WNBA season, Seattle Storm player Breanna Stewart played 20 games and averaged 19.7 points per-game.
# TODO: Calculate the total number of points Breanna Stewart scored in the 2020 WNBA season
# TODO: Cast the calculated number to an integer using `int()` and save to a new variable
# TODO: Print the cast variable as part of a string explaining the statistic for Breanna Stewart,
# e.g. "In the 2020 WNBA season, ... Player X scored Y points total"
breanna_stewart_total_points_scored = 20 * 19.7
total_points_scored_int = int(breanna_stewart_total_points_scored)
print(f"In the 2020 WNBA season, Seattle Storm player Breanna Stewart scored a total of {total_points_scored_int}")
print()

print("Challenge 3.2: Average defensive rebounds")
# In the 2020 WNBA season, the Seattle Storm's top 3 defensive rebounders were
# 1. Breanna Stewart with 7.3 defensive rebounds per-game
# 2. Natasha Howard with 4.7 defensive rebounds per-game
# 3. Alysha Clark with 3.4 defensive rebounds per-game
# TODO: Calculate the average defensive rebounds per-game among these three players for the Seattle Storm and
# save it to a variable
average_defensive_rebounds = (7.3 + 4.7 + 3.4)/3
# TODO: Print the saved variable as a floating point number
print("In the 2020 WNBA season, Breanna Stewart, Natasha Howard, and Alysha Clark of the Seattle Storm averaged"
      f"{average_defensive_rebounds} per-game")
print()
