def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        links = [line.strip().split()[0] for line in lines]
        rechts = [line.strip().split()[1] for line in lines]
    return links, rechts

if __name__ == "__main__":
    input_file = 'input'
    links, rechts = read_input(input_file)

    result = 0
    for number in links:
        count = rechts.count(number)
        result += (int(number) * count)
    
    print(result)