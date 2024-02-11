def main():
    n = int(input())

    # Get all inputs from user (int, float)
    values = {}
    for i in range(n):
        k, v = input().split()
        k = int(k)
        v = float(v)
        values[k] = v

    # Sort dictionary by value
    justValues = values.values()
    sortedList = sorted(justValues, reverse=True)
    justKeys = []

    for i in range(3):
        # Check dictionary to find the first 3 keys (IDs)
        x = sortedList[i]

        for y in values:
            if values[y] == x:
                justKeys.append(y)
                break

    justKeys = sorted(justKeys)

    # Print first three values
    for i in range(3):
        print(justKeys[i])


if __name__ == "__main__":
    main()
