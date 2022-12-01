def read_input():
    f = open("input.txt", "r")
    content = f.readlines()
    return content


# part 1, get the greatest cal
total = 0
all_cal = []
for line in read_input():
    if line != "\n":
        int_line = int(line)
        total += int_line
    elif line == "\n":
        all_cal.append(total)
        total = 0
max_cal = max(all_cal)
print(max_cal)

# part 2,  get the total of top 3 cal numbers
all_cal.sort(reverse=True)
top_three = []
t = 0
for y in range(3):
    top_three.append(all_cal[y])
    t += all_cal[y]

print(top_three)
print(t)
