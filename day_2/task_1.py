# Day Two, Task One


def check_levels(levels):
    previous = -1
    increasing = False

    for i, l in enumerate(levels):
        if i == 0:
            previous = l
            continue
        if i == 1:
            increasing = l > previous
        if i > 1:
            if (l > previous) != increasing:
                return False
        difference = abs(l - previous)
        if difference < 1 or difference > 3:
            return False
        previous = l

    return True



def main():
    total_true = 0

    with open("input.txt") as fp:
        for line in fp.readlines():
            levels = line.split()
            levels = [int(l) for l in levels]
            if check_levels(levels):
                total_true += 1
    
    print("Total True: ", total_true)







if __name__ == '__main__':
    main()
