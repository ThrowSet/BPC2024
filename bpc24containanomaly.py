def main():
    anomaly_x, anomaly_y = map(int, input().split())

    n = int(input())

    # Get tower coordinates
    towers = []
    for i in range(n):
        tower_x, tower_y = map(int, input().split())
        x = [tower_x, tower_y]
        towers.append(x)

    # Check each edge created by towers
    contained = True
    for i in range(len(towers)):
        tower1 = towers[i]
        tower2 = towers[(i + 1) % len(towers)]

        crossProduct = (anomaly_x - tower1[0]) * (tower2[1] - tower1[1]) - (anomaly_y - tower1[1]) * (
                    tower2[0] - tower1[0])

        if crossProduct < 0:
            contained = False
            break

    if contained:
        print("CONTAINED")
    else:
        print("NOT CONTAINED")


if __name__ == "__main__":
    main()
