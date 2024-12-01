# Day One, Task One


def main():
    left = []
    right = []
    differences = []
    sum = 0

    with open("task_1_inputs.txt") as fp:
        for line in fp.readlines():
            l, r = line.split()
            l = int(l.strip())
            r = int(r.strip())
            left.append(l)
            right.append(r)
    left = sorted(left)
    right = sorted(right)

    assert len(left) == len(right)
    for i in range(len(left)):
        differences.append(abs(left[i] - right[i]))

    assert len(left) == len(differences)
    for val in differences:
        sum += val
    
    print("Sum :", sum)


if __name__ == '__main__':
    main()
