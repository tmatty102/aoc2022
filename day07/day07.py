from collections import defaultdict

# look for pattern
# useful lines  "$ cd <dir>" to get the directory
# eliminiate wasetful lines dir or $
# create dict for dir and size


def get_data(thefile):
    with open(thefile, "r", encoding="utf-8") as f:
        content = f.readlines()
        # print(content)
        return content


def solution(part):
    data = get_data("data.txt")
    ds = defaultdict(int)
    dir_path = []
    for line in data:
        idx = line.strip().split(" ")
        # print(idx)
        # get directory and path
        if idx[0] == "$" and idx[1] == "cd":
            if idx[2] == "/":
                dir_path = ["/"]
            elif idx[2] == "..":
                dir_path.pop()
            else:
                dir_path.append(idx[2])

        elif idx[0] == "$" or idx[0] == "dir":
            pass
        else:
            #
            size = int(idx[0])
            for i in range(0, len(dir_path)):
                # print(dir_path[i])
                ds["".join(dir_path[: i + 1])] += size
        # print(ds)

    if part == "part1":
        print(sum(v for v in ds.values() if v <= 100000))

    disk_size = 70000000
    free_space_needed = 30000000
    delete = free_space_needed - (disk_size - ds["/"])

    if part == "part2":
        print(min(v for v in ds.values() if v >= delete))


def part1():
    # solve part1
    solution("part1")


def part2():
    solution("part2")


if __name__ == "__main__":
    part1()
    part2()
