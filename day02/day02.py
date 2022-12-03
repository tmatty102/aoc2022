"""
A = rock 1
B = paper 2 
C = scissors 3
X = rock 1 
Y = paper 2 
Z = scissors 3

score per shape
rock = 1
paper = 2
scissors = 3

score per round
lose = 0
draw = 3
win = 6

score =  shape_score + round_status
"""
win_map = {
    "A": "B",
    "B": "C",
    "C": "A",
}

lose_map = {
    "A": "C",
    "B": "A",
    "C": "B",    
}
score_map = {
    "A": 1,
    "B": 2,
    "C": 3,
    "lose": 0,
    "draw": 3,
    "win": 6
}


def read_file(thefile):
    with open(thefile, "r", encoding="utf-8") as f:
        content = f.readlines()
        return content

def part_one_conversion(file):
    # convert all x,y,z to a,b,c for easy evaluation   
    rounds = []
    data = read_file(file)
    for line in data:
        if "X" in line:
            line = line.replace("X", "A")
        elif "Y" in line:
            line = line.replace("Y", "B")
        elif "Z" in line:
            line = line.replace("Z", "C")
        rounds.append(line.rstrip())
    return rounds

def part_two_conversion(file):
    data = read_file(file)
    rounds = []
    for line in data:
        if "X" in line:
            line = line.replace("X", lose_map[line[0]])
        elif "Y" in line:
            line = line.replace("Y", line[0])
        elif "Z" in line:
            line = line.replace("Z", win_map[line[0]])
        rounds.append(line.rstrip())
    
    return rounds
# evaluate match, get score per match and add the score to score_list
def evaluation(data):
    scores = 0
    score_list = []
    for line in data:
        if line[0] == line[2]:
            print("draw")
            scores = score_map[line[2]] + score_map["draw"]
            score_list.append(scores)
        elif line[0] == "A":
            if line[2] == "C":
                print("lose")
                scores = score_map[line[2]] + score_map["lose"]
                score_list.append(scores)
            else:
                print("win")
                scores =  score_map[line[2]] + score_map["win"]
                score_list.append(scores)
        elif line[0] == "B":
            if line[2] == "A":
                print("lose")
                scores = score_map[line[2]] + score_map["lose"]
                score_list.append(scores)
            else:
                print("win")
                scores =  score_map[line[2]] + score_map["win"]
                score_list.append(scores)
        elif line[0] == "C":
            if line[2] == "B":
                print("lose")
                scores = score_map[line[2]] + score_map["lose"]
                score_list.append(scores)
            else:
                print("win")
                scores =  score_map[line[2]] + score_map["win"]
                score_list.append(scores)
    
    # get total score
    total_score = sum(score_list)          
    return total_score

def part_one(file):    
    data01 = part_one_conversion(file)
    answer = evaluation(data01)
    return answer

def part_two(file):
    data02 = part_two_conversion(file)
    answer = evaluation(data02)
    return answer
        

if __name__ == "__main__":
    file = "data.txt"
    partone = part_one(file)
    parttwo = part_two(file)

    print(partone)
    print(parttwo)
