# Initial solution to the problem

# if __name__ == "__main__":
#     # read contents from input.txt file
#     with open("input.txt", "r") as file:
#         data = file.readlines()

#         # split the data into left and right
#         left = []
#         right = []

#         for line in data:
#             temp = line.split()
#             left.append(int(temp[0]))
#             right.append(int(temp[1]))

#         # sort the lists
#         left = sorted(left)
#         right = sorted(right)

#         # calculate the distance between the smallest two points from each list
#         distance = 0

#         for i in range(len(left)):
#             # Find distance between the smallest two points and add the distance to the total distance
#             distance += abs(left[i] - right[i])

#         print(distance)

# Simplified version from copilot
if __name__ == "__main__":
    # read contents from input.txt file
    with open("input.txt", "r") as file:
        data = [line.split() for line in file]

    # split the data into left and right, convert to integers, and sort
    left = sorted(int(line[0]) for line in data)
    right = sorted(int(line[1]) for line in data)

    # calculate the distance between the smallest two points from each list
    distance = sum(abs(l - r) for l, r in zip(left, right))

    print(distance)