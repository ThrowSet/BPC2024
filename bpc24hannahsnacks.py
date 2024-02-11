def main():
    n = int(input())

    # n lines: Calories of each pack of snacks
    cals = []
    for i in range(n):
        cals.append(int(input()))
    # Sum from n lines
    sum = 0
    for x in cals:
        sum += x

    # Evaluate if cals are divisible by n
    div = sum / 3

    # Iterate sequentially through elements
    play = True
    canDivide = True
    ct = 0
    day = 0
    while play and ct < n:
        day += cals[ct]
        if day == div:
            # One set of elements can be added to div, keep working through remaining elements
            day = 0

        elif day > div:
            # not possible for elements to be sequential -> false
            canDivide = False
            play = False
        ct += 1

    if canDivide:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
