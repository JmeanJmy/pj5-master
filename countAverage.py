import sys

if __name__ == '__main__':
    file = sys.argv[1]
    fp = open(file)
    totalTS = 0
    totalTJ = 0
    count = 0

    for line in fp:
        line = line.rstrip("\n")
        number = line.split(" ")
        lenNumber = len(number)
        char1 = number[0]
        if (lenNumber != 3 or (char1 != 'T')):
            continue
        TS = float(number[1])
        TJ = float(number[2])
        totalTJ = totalTJ + TJ
        totalTS = totalTS + TS
        count = count + 1

    print("TS: ",totalTS/count, "TJ: ", totalTJ/count, "Total query: ", count)
    fp.close()