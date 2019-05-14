import argparse
import json

def main(name, score, location):
    with open("restaurants.json", "r") as jsonFile:
        restaurants = json.load(jsonFile)
        restaurants[name] = {
            "score": score,
            "location": location
        }

    with open("restaurants.json", "w") as jsonFile:
        json.dump(restaurants, jsonFile)
    print(name + "has been updated!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add a restaurant to the pool.')
    parser.add_argument('-n', '--name', help='Name of the restaurant', required=True)
    parser.add_argument('-s', '--score', help='Score of the restaurant', required=True)
    parser.add_argument('-l', '--loc', help='Location of the restaurant', required=True)
    args = vars(parser.parse_args())

    main(args['name'], args['score'], args['loc'])




