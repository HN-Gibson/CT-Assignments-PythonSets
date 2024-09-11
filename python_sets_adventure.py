# Objective: The aim of this assignment is to deepen your understanding and application of Python sets.

# Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# 1. Destinations that both airlines fly to.

shared_destinations = our_routes.intersection(competitor_routes)
print(f"Both airlines fly to:\n{", ".join(str(d)for d in shared_destinations)}")

# 2. Destinations unique to your airline.

unique_to_us = our_routes.difference(competitor_routes)
print(f"Our unique destinations include:\n{", ".join(str(d) for d in unique_to_us)}")

# 3. Whether there are any destinations that neither airline shares.

unique_to_each = our_routes.symmetric_difference(competitor_routes)
print(f"Unique destinations to both airlines:\n{", ".join(str(d) for d in unique_to_each)}")

