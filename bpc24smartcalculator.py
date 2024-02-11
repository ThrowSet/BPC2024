def main():
    n1, n2 = input().split()

    # Get length of each number
    n1len = len(n1)
    n2len = len(n2)

    # If number lengths are different then autofill with zeroes to left
    n1str, n2str = "", ""
    if n1len != n2len:
        # Determine which number is smaller to autofill with zeroes
        if n1len > n2len:
            # Autofill n2 with zeroes
            n1str = str(n1)
            n2str = str(n2)
            fill = n1len - n2len
            n2str = (fill * "0") + n2str

        else:
            # Autofill n1 with zeroes
            n2str = str(n2)
            n1str = str(n1)
            fill = n2len - n1len
            n1str = (fill * "0") + n1str
    else:
        # Convert both to strings
        n1str = str(n1)
        n2str = str(n2)

    # Add each column, persisting the carry until carry == 0. R->L
    columns = len(n2str) - 1
    carry = 0
    for i in range(columns + 1):
        # Get element from each column
        tempn1 = n1str[columns - i]
        tempn2 = n2str[columns - i]

        # Convert both to ints
        intn1 = int(tempn1)
        intn2 = int(tempn2)

        # Addition operation
        sum = intn1 + intn2
        if carry == 1:
            # Increment sum
            sum += 1
            carry = 0

        if sum >= 10:
            # Extract rightmost digit and increment carry
            tempsum = str(sum)
            sum = tempsum[1]
            carry = 1
        print(str(sum) + " " + str(carry))
        sum = 0
    if carry == 1:
        print("1 0")


if __name__ == "__main__":
    main()
