

def get_data(thefile):
    with open(thefile, "r", encoding="utf-8") as f:
        content = f.read().splitlines()
        #print(content)
        return content

def parse_data(content):
    assignment01 = []
    assignment02 = []
    n = content[0].replace(",", "!")
    nn = n.replace("-", ",")
    new_data = nn.split("!")
    #print(new_data)
    pre_assignment01 = new_data[0].split(",")
    pre_assignment02 = new_data[1].split(",")
    #print(int(pre_assignment01[0]))
    #print(int(pre_assignment01[1]))
    for i in range(int(pre_assignment01[0]),int(pre_assignment01[1])+1):
        assignment01.append(i)
    for i in range(int(pre_assignment02[0]),int(pre_assignment02[1])+1):
        assignment02.append(i)    
    return set(assignment01), set(assignment02) 
    

def part1():
    # solve part1
    data = get_data("data.txt")
    #print(len(data))
    count = 0
    while len(data) > 0:
        parsed_data01, parsed_data02 = parse_data(data)
        #print(parsed_data01)
        #print(parsed_data02)

        if parsed_data02.issubset(parsed_data01) or parsed_data01.issubset(parsed_data02):
            #print(parsed_data02.intersection_update())
            count = count + 1    
        data.remove(data[0])
        #print(f"during in while count: {count}")
        
    print(f"Part1: {count}")

def part2():
    # solve part2
    data = get_data("data.txt")
    #print(len(data))
    count = 0
    while len(data) > 0:
        parsed_data01, parsed_data02 = parse_data(data)
        #print(parsed_data01)
        #print(parsed_data02)

        if not parsed_data02.isdisjoint(parsed_data01):
            #print(parsed_data02.intersection_update())
            count = count + 1    
        data.remove(data[0])
        #print(f"during in while count: {count}")
    print(f"Part2: {count}")

if __name__ == "__main__":
    part1()
    part2()
