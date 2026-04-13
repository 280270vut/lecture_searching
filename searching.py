from pathlib import Path
import json


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    import json

    allowed = ["unordered_numbers", "ordered_numbers", "dna_sequence"]

    if field not in allowed:
        return None

    with open(file_name, "r") as file:
        data = json.load(file)
    return data[field]


    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name

def linear_search(sequence, target):
    positions = []
    count = 0

    for i in range (len(sequence)):
        if sequence[i] == target:
            positions.append(i)
            count += 1
    return {"positions": positions, "count": count}


def binary_search(seznam, hledane):
    levy_okraj = 0
    pravy_okraj = len(seznam) -1

    while levy_okraj <= pravy_okraj:
        stred = (levy_okraj + pravy_okraj) // 2

        if seznam[stred] == hledane:
            return stred

        elif seznam[stred] < hledane:
            levy_okraj = stred + 1

        else:
            pravy_okraj = stred - 1


    return None


import time
import matplotlib.pyplot as plt
from generators import unordered_sequence, ordered_sequence


def main():
    vlastnosti = [100, 500, 1000, 5000, 10000]
    casy_sekvencni = []
    casy_binarni = []

    for vlastnost in vlastnosti:

        neserazeny = unordered_sequence(max_len=100)
        serazeny = ordered_sequence(max_len=100)

        hledane = serazeny[len(serazeny) // 2]

        start = time.perf_counter()
        linear_search(neserazeny, hledane)
        end = time.perf_counter()
        casy_sekvencni.append(end - start)

        start = time.perf_counter()
        binary_search(serazeny, hledane)
        end = time.perf_counter()
        casy_binarni.append(end - start)

        print("Velikosti:", velikosti)
        print("Sekvencni:", casy_sekvencni)
        print("Binarni:", casy_binarni)

        plt.plot(velikosti, casy_sekvencni, label = "sekvencni")
        plt.plot(velikosti, casy_binarni, label = "binarni")
        plt.xlabel("Velikost vstupu")
        plt.ylabel("Cas")
        plt.title("porovnani algoritmu")
        plt.legend()
        plt.show()





def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

    linear_result = linear_search(sequential_data, 9)
    print(linear_result)

    ordered_data = read_data("sequential.json", "ordered_numbers")
    binary_result = binary_search(ordered_data, 9)
    print(binary_result)



if __name__ == "__main__":
    main()

