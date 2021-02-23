'''
This module helps to navigate
in json-file
'''

import json

def read_file(name: str) -> dict:
    '''
    Read json file
    '''
    with open(name, "r", encoding='utf-8') as input_file:
        data = json.load(input_file)

    return data

def print_available_data(data) -> None:
    '''
    Prints data that can be accessed by user
    '''
    if isinstance(data, dict):
        for i in data:
            if isinstance(data[i], dict):
                print(f'💖 {i}')
            elif isinstance(data[i], list):
                print(f'🍏 {i}')
            else:
                print(f'🌻 {i}')

def output_dict_info(data, key):
    '''
    Gets information from a dict
    '''
    if isinstance(data[key], dict):
        print_available_data(data[key])
        the_end = False
        print("")
    elif isinstance(data[key], list):
        return False
    else:
        print(data[key])
        the_end = True  # becomes True when user reaches non-collection value
        print("")

    return the_end

def main():
    '''
    Main function
    '''
    the_end = False

    print("Hi! I'm json navigator! I will help you find infornation you need!\n")
    print("I will print you what information you can access.\n")
    print("If you see there '💖' symbol, this is a dictionary.")
    print("If you see there '🍏' symbol, this is a list.")
    print("If you see there '🌻' symbol, this is not a collection\n")

    file_name = input("Input file name: ")
    print("")

    data = read_file(file_name)

    while True:
        if isinstance(data, list):
            if len(data) == 0:
                print("That's an empty list!\n")
                the_end = True
            else:
                print(f"That is a list with {len(data)} elements.\n")
                ind = int(input(f"Type index of an element you want to get (0-{len(data)-1}): "))
                print("")
                data = data[ind]
                continue

        if the_end:
            answr = input("Do you want to start again? (Y/n): ")
            print("")
            if answr == "n":
                break
            data = read_file(file_name)
            the_end = False
            continue

        print_available_data(data)
        print("")

        key = input("Please enter information you want to get: ")
        print("")
        the_end = output_dict_info(data, key)
        data = data[key]


if __name__ == "__main__":
    main()
