for i in range(5, 0, -1):
    line = " " * (i - 1) * 2 + " ".join(str(j) for j in range(i, 6))
    print(line)