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

def main():
    data = read_data("sequential.json", "unordered_numbers")
    result = binary_search(data, 9)

    print(result)




if __name__ == "__main__":
    main()

