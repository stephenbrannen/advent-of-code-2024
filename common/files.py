import os
from typing import List

def get_file_data(file_name: str) -> List[List[str]]:
    input_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "inputs", file_name)
    with open(input_file, "r") as file:
        return [line.split() for line in file]