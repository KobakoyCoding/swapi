#!/usr/bin/env python3
"""A single positional argument"""

import argparse
import json
import requests


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Star Wars API',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('search',
                        metavar='str',
                        type=str,
                        help='''Enter your search: people,
                              planet, or starships.''')

    parser.add_argument('number',
                        metavar='int',
                        type=int,
                        help="""A number range for your search,
                                People 1-83,
                                Planets 1-60,
                                Starships 1-29.""")

    return parser.parse_args()


def main():

    args = get_args()
    # response = requests.get(f"http://swapi.dev/api/planets/{args.number}")
    # json_data = response.text
    # json_load = json.loads(json_data)

    try:
        if args.search == 'planets':
            response = requests.get(f"""http://swapi.dev/api/planets/
                                        {args.number}""")
            json_data = response.text
            json_load = json.loads(json_data)

            print(f"Name: {json_load['name']}")
            print(f"Rotation_period: {json_load['rotation_period']}")
            print(f"Orbital_period: {json_load['orbital_period']}")
            print(f"Diameter: {json_load['diameter']}")
            print(f"Climate: {json_load['climate']}")
            print(f"Gravity: {json_load['gravity']}")
            print(f"Terrain: {json_load['terrain']}")
            print(f"Surface_Water: {json_load['surface_water']}")
            print(f"Population: {json_load['population']}")

        elif args.search == 'people':
            response = requests.get(f"""http://swapi.dev/api/people/
                                        {args.number}""")
            json_data = response.text
            json_load = json.loads(json_data)

            print(f"Name: {json_load['name']}")
            print(f"Gender: {json_load['name']}")
            print(f"BirthYear: {json_load['birth_year']}")
            print(f"EyeColor: {json_load['eye_color']}")
            print(f"HairColor: {json_load['hair_color']}")
            print(f"Height: {json_load['height']}")
            print(f"SkinColor: {json_load['skin_color']}")

        elif args.search == 'starships':
            response = requests.get(f"""http://swapi.dev/api/starships/
                                      {args.number}""")
            json_data = response.text
            json_load = json.loads(json_data)

            print(f"Name: {json_load['name']}")
            print(f"Model: {json_load['model']}")
            print(f"Class: {json_load['starship_class']}")
            print(f"Hyperdrive: {json_load['hyperdrive_rating']}")
            print(f"CreditsCost: {json_load['cost_in_credits']}")
            print(f"Crew: {json_load['crew']}")
            print(f"Length: {json_load['length']}")
            print(f"Manufacturer: {json_load['manufacturer']}")
            print(f"Passengers: {json_load['passengers']}")
            print(f"Consumables: {json_load['consumables']}")
            print(f"""MaxAtmospheringSpeed:
                      {json_load['max_atmosphering_speed']}""")
        else:
            print("Check the help page with the -h or --help option.")
    except KeyError:
        print("Check the number range of your search.")


if __name__ == '__main__':
    main()
