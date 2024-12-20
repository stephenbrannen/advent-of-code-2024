import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from common.files import get_file_data

# Add the parent directory to the Python path


# Initial solution to the problem
if __name__ == "__main__":
    data = get_file_data("2.txt")
    print(data)