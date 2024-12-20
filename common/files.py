import os
from typing import List

def get_file_data(file_name) -> List[List[int]]:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(root_dir, os.pardir))
    input_file = os.path.join(parent_dir, "inputs", file_name)

    with open(input_file, "r") as file:
        return [line.split() for line in file]
    