import random
import argparse
import json

def main(location):
    restaurantList = list()
    with open("restaurants.json", "r") as jsonFile:
        restaurants = json.load(jsonFile)
        for key, value in restaurants.items():
            if location == "" or location == value['location'] or value['location'] == "both":
                restaurantList += [key] * int(value['score'])

    # print(restaurantList)
    print("Today you will eat at " + random.choice(restaurantList))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pick a restaurant from the pool.')
    parser.add_argument('-l', '--loc', default='', help='Location of the restaurant')
    args = vars(parser.parse_args())

    main(args['loc'])