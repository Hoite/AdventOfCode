def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        links = [line.strip().split()[0] for line in lines]
        rechts = [line.strip().split()[1] for line in lines]
    return links, rechts

if __name__ == "__main__":
    input_file = 'input'
    links, rechts = read_input(input_file)

    # Omzetten van strings naar integers
    for i in range(len(links)):
        links[i] = int(links[i])
        rechts[i] = int(rechts[i])

    # Sorteren lijsten van klein naar groot
    links.sort()
    rechts.sort()

    som = 0
    for i in range(len(links)):
        distance = abs(links[i] - rechts[i])
        som += distance
    
    print(som)