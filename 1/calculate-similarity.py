import os

# Initial solution to the problem
# if __name__ == "__main__":
#     # read contents from input.txt file

#     root_dir = os.path.dirname(os.path.abspath(__file__))
#     parent_dir = os.path.abspath(os.path.join(root_dir, os.pardir))
#     input_file = os.path.join(parent_dir, "inputs/1.txt")
    
#     with open(input_file, "r") as file:
#         data = [line.split() for line in file]
#         left = [int(line[0]) for line in data]
#         right = [int(line[1]) for line in data]

#     similarity_score = 0
#     for number in left:
#         similarity_score += number * right.count(number)

#     print(f"Total similarity score: {similarity_score}")

# Simplified version from copilot
if __name__ == "__main__":
    # read contents from input.txt file
    root_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(root_dir, os.pardir))
    input_file = os.path.join(parent_dir, "inputs/1.txt")
    
    with open(input_file, "r") as file:
        data = [line.split() for line in file]

    # split the data into left and right, convert to integers
    left = [int(line[0]) for line in data]
    right = [int(line[1]) for line in data]

    # calculate the total similarity score
    similarity_score = sum(number * right.count(number) for number in left)

    print(f"Total similarity score: {similarity_score}")