def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def checkSafe(list):
    # print(list)
    # Parse list to integers
    list = list.split(" ")
    list = [int(i) for i in list]
    # print(list)

    # Check if only increasing or decreasing and no consecutive numbers
    if list[0] > list[1] & list[1] > list[2] & list[2] > list[3] & list[3] > list[4]:
        print(f"List {list}: Strictly decreasing")
        # Check if only decreasing by 1-3
        if all(1 <= list[i] - list[i+1] <= 3 for i in range(len(list) - 1)):
            print(f"List {list}: Decreasing by 1-3")
            print(f"List {list}: Safe\n")
            return True
        else:
            print(f"List {list}: Not decreasing by 1-3\n")
            return False

    elif list[0] < list[1] & list[1] < list[2] & list[2] < list[3] & list[3] < list[4]:
        print(f"List {list}: Strictly increasing")
        # Check if only increasing by 1-3
        if all(1 <= list[i+1] - list[i] <= 3 for i in range(len(list) - 1)):
            print(f"List {list}: Increasing by 1-3")
            print(f"List {list}: Safe\n")
            return True
        else:
            print(f"List {list}: Not increasing by 1-3\n")
            return False
    else:
        print(f"List {list}: Neither strictly increasing nor strictly decreasing")
        print(f"List {list}: Not safe\n")
        # Return false
        return False


# file = fr"./example"
file = fr"./input"
list = read_input(file)

# print(list)

countedsafe = 0
for row in list:
    if checkSafe(row):
        countedsafe += 1

print(f"Counted safe: {countedsafe}")