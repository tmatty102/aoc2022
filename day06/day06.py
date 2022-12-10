def get_data(thefile):
    with open(thefile, "r", encoding="utf-8") as f:
        content = f.read()
        # print(content)
        return content


def find_marker(marker):
    data = get_data("data.txt")
    x = marker
    while x < len(data):
        if len(set(data[x - x : x])) == 4:
            print(x)
            break
    x += 1


def part1():
    # solve part1
    find_marker(4)


def part2():
    # solve part2
    find_marker(14)


if __name__ == "__main__":
    part1()
    part2()
