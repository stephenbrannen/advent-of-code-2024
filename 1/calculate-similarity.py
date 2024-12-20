import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from common.files import get_file_data

# Initial solution to the problem
# if __name__ == "__main__":
#     # read contents from input.txt file

#     data = get_file_data("1.txt")
#     left = [int(line[0]) for line in data]
#     right = [int(line[1]) for line in data]

#     similarity_score = 0
#     for number in left:
#         similarity_score += number * right.count(number)

#     print(f"Total similarity score: {similarity_score}")

# Simplified version from copilot
if __name__ == "__main__":
    # read contents from input.txt file
    data = get_file_data("1.txt")

    # split the data into left and right, convert to integers
    left = [int(line[0]) for line in data]
    right = [int(line[1]) for line in data]

    # calculate the total similarity score
    similarity_score = sum(number * right.count(number) for number in left)

    print(f"Total similarity score: {similarity_score}")