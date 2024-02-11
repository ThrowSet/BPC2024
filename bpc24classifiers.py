def main():
    n, m = input().split()
    # n and m instantiated as strings
    n = int(n)
    m = int(m)

    # Get classifiers as inputs from user
    classifierWeights = input().split()
    for i in range(len(classifierWeights)):
        classifierWeights[i] = int(classifierWeights[i])

    # Get values for each variable
    values = []
    for i in range(m):
        line = input().split()
        for x in range(len(line)):
            line[x] = int(line[x])

        values.append(line)

    # Evaluate all values and return good or bad
    for i in range(m):
        tempsum = 0

        # Get first list from values
        tempList = values[i]
        for x in range(n):
            tempsum += classifierWeights[x] * tempList[x]

        if tempsum > 0:
            print("good")
        else:
            print("bad")


if __name__ == "__main__":
    main()
