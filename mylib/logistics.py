#!/usr/bin/env python3


#build a list of 10 cities in Japan and their coordinates
cities = {
    "Tokyo": (35.6895, 139.6917),
    "Yokohama": (35.4437, 139.6380),
    "Kyoto": (35.0116, 135.7681),
    "Osaka": (34.6937, 135.5023),
    "Sapporo": (43.0618, 141.3545),
    "Nagoya": (35.1815, 136.9066),
    "Fukuoka": (33.5904, 130.4017),
    "Kobe": (34.6901, 135.1955),
    "Kawasaki": (35.5301, 139.7026),
    "Yaita": (36.8552, 139.8722),
}

from geopy.distance import geodesic

# calculate the distance between two coordinates
def calculate_distance(coord1, coord2):
    """
    Calculate the distance between two coordinates in kilometers
    """
    return geodesic(coord1, coord2).km

# calculate the distance between two cities
def distance(city1, city2):
    """
    Calculate the distance between two cities in kilometers
    """
    return calculate_distance(cities[city1], cities[city2])

# calculate the time it takes to travel between two cities at a given speed
def travel_time(city1, city2, speed):
    """
    Calculate the time it takes to travel between two cities at a given speed
    """
    return distance(city1, city2) / speed

#calculate traveling sales person problem

def total_distance(city_list):
    """
    Calculate the total distance traveled by a salesperson visiting a list of cities
    """
    total = 0
    for i in range(len(city_list) - 1):
        total += distance(city_list[i], city_list[i + 1])
    return total

#最適な経路を見つける
def find_best_route(city_list):
    """
    Find the best route for a salesperson visiting a list of cities
    """
    from itertools import permutations

    min_distance = float("inf")
    best_route = None
    for route in permutations(city_list):
        d = total_distance(route)
        if d < min_distance:
            min_distance = d
            best_route = route
    return best_route,min_distance

# city_list = ['Tokyo', 'Osaka', 'Nagoya', 'Sapporo'] 

# print(find_best_route(city_list))