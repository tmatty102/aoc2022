from collections import defaultdict


def get_data(thefile):
    with open(thefile, "r", encoding="utf-8") as f:
        content = f.read()
        # print(content)
    return content


def part1():
    # solve part1
    data = get_data("data.txt")
    org_crate, moves = data.rstrip().split("\n\n")

    crates01 = defaultdict(list)
    crates02 = defaultdict(list)
    for n in org_crate.split("\n")[:-1][::-1]:
        i = 1
        while i < len(n):
            if n[i] != " ":
                crates01[(i + 3) // 4].append(n[i])
                crates02[(i + 3) // 4].append(n[i])
            i += 4
    print(crates01)
    print(crates02)

    for move in moves.split("\n"):
        _, num, _, start, _, dest = move.split(" ")
        num, start, dest = int(num), int(start), int(dest)

        for i in range(num):
            crates01[dest].append(crates01[start].pop())
        crates02[dest].extend(crates02[start][-num:])
        crates02[start] = crates02[start][:-num]

    part1 = "".join(c[-1] for c in crates01.values())
    print(f"Part 1: {part1}")

    part2 = "".join(c[-1] for c in crates02.values())
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    part1()
