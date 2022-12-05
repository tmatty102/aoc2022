
"""
 Prepare a list of alphabet for enumerate() to map prority.
 Perhaps import the "string" module to generate the list with "list(string.ascii_letters)"
"""
item_type = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def get_data(thefile):
    with open(thefile, "r", encoding="utf-8") as f:
        content = f.read().splitlines()
        #print(content)
        return content

# part 1
def split_string(n):
    first_comp = n[0:len(n)//2]
    second_comp = n[len(n)//2:]
    return first_comp, second_comp

# get common letter from splited string
def compare_compartments(first_comp, second_comp):
    common_char = []
    for char_in_one in first_comp:
        if char_in_one in second_comp:
            common_char.append(char_in_one)
    return common_char

# get priority by using enumeration        
def get_pri(rucksacks):
    for rucksack in rucksacks:
        for i, v in enumerate(item_type, start=1):
            if rucksack == v:
                #print(f"{i}: {v}")               
                return i

# part two
# split elves into group and return items and the group list
def split_group(n):
    elves_group= []
    for line in n:
        if len(elves_group) < 3:
            #print(line)
            elves_group.append(line)
    a = elves_group[0]
    b = elves_group[1]
    c = elves_group[2]
    return a, b, c, elves_group

# get priority letter from group
def part_two_compare_compartments(first_comp, second_comp, third_comp):
    common_char = []
    for char_in_one in first_comp:
        if char_in_one in second_comp and char_in_one in third_comp:
            common_char.append(char_in_one)
    return common_char

def part_one(data):
    sum_list = []
    for n in get_data(data):
        refined_content_01, refined_content_02 = split_string(n)
        rucksacks = compare_compartments(refined_content_01, refined_content_02)
        pri = get_pri(rucksacks)
        sum_list.append(pri)
    sum_p = sum(sum_list)
    return sum_p

def part_two(data):
    n = get_data(data)
    i = 0 
    sum_list = []
    #print(len(n))
    
    while len(n):
        
        a, b, c, elves_group = split_group(n)
        #print(elves_group)
        rucksacks = part_two_compare_compartments(a,b,c)
        #print(rucksacks)
        pri = get_pri(rucksacks)
        sum_list.append(pri)
        for x in elves_group:
            n.remove(x)
        #print(len(n))
        i += 1
    final_answer = sum(sum_list)
    return final_answer


if __name__ == "__main__":
    data = "data.txt"
    partone = part_one(data)
    parttwo = part_two(data)
    print(f"The answer for part1 is: {partone}")
    print(f"The answer for part2 is: {parttwo}")