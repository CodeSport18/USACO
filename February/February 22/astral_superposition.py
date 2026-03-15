t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    superimposed = [input() for _ in range(n)]

    allStars = sum(1 for x in range(n) for y in range(n) if superimposed[x][y] != 'W')

    if a == 0 and b == 0:
        stars = allStars
    else:
        image2 = [[False] * n for _ in range(n)]

        for x in range(n):
            for y in range(n):
                if superimposed[y][x] == 'W' or image2[x][y]:
                    continue

                nx = x + a
                ny = y + b

                if ny < n and nx < n and superimposed[ny][nx] != 'W':
                    if superimposed[ny][nx] != 'B':
                        image2[nx][ny] = True

        invalid = False
        for x in range(n):
            for y in range(n):
                if superimposed[y][x] != 'B':
                    continue

                nx = x - a
                ny = y - b

                if nx < 0 or ny < 0 or superimposed[ny][nx] == 'W':
                    invalid = True
                    break

                if image2[nx][ny]:
                    image2[nx][ny] = False
            if invalid:
                break

        image2numstars = sum(image2[x][y] for x in range(n) for y in range(n))

        stars = -1 if invalid else allStars - image2numstars

    print(stars)