# Day One, Task Two
from collections import Counter


def main():
    left = []
    right = []
    sum = 0

    with open("task_1_inputs.txt") as fp:
        for line in fp.readlines():
            l, r = line.split()
            l = int(l.strip())
            r = int(r.strip())
            left.append(l)
            right.append(r)

    counter = Counter(right)

    for val in left:
        sum += (val * counter[val])
    
    print("Sum: ", sum)


if __name__ == '__main__':
    main()
