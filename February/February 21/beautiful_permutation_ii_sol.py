import sys

res = []
ele = []

def backtrack():
    if not ele:
        print(*res)
        sys.exit(0)

    for i in range(len(ele) - 1, -1, -1):
        x = ele[i]

        if not res or abs(res[-1] - x) != 1:
            ele.pop(i)
            res.append(x)
            backtrack()
            res.pop()
            ele.insert(i, x)

def main():
    n = int(input())

    if n == 2 or n == 3:
        print("NO SOLUTION")
        return

    for i in range(n, 0, -1):
        ele.append(i)

    backtrack()

if __name__ == "__main__":
    main()