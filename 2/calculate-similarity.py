import os

# Initial solution to the problem
# if __name__ == "__main__":
#     # read contents from input.txt file
#     working_dir = os.path.dirname(os.path.abspath(__file__))
#     parent_dir = os.path.abspath(os.path.join(working_dir, os.pardir))
#     input_file = os.path.join(parent_dir, "input.txt")

#     with open(input_file, "r") as file:
#         data = [line.split() for line in file]
#         left = [int(line[0]) for line in data]
#         right = [int(line[1]) for line in data]
#         # This time, you'll need to figure out exactly how often each number from the left list appears in 
#         # the right list. Calculate a total similarity score by adding up each number in the left list after 
#         # multiplying it by the number of times that number appears in the right list.

#     similarity_score = 0
#     for number in left:
#         similarity_score += number * right.count(number)

#     print(f"Total similarity score: {similarity_score}")

# Simplified version from copilot
if __name__ == "__main__":
    # get the root directory of the current file
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    # get the parent directory
    parent_dir = os.path.abspath(os.path.join(ROOT_DIR, os.pardir))

    # read contents from input.txt file in the parent directory
    input_file_path = os.path.join(parent_dir, "input.txt")
    with open(input_file_path, "r") as file:
        data = [line.split() for line in file]

    # split the data into left and right, convert to integers
    left = [int(line[0]) for line in data]
    right = [int(line[1]) for line in data]

    # calculate the total similarity score
    similarity_score = sum(number * right.count(number) for number in left)

    print(f"Total similarity score: {similarity_score}")