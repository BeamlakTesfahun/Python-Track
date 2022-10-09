markSheet = []
scoreSheet = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        markSheet += [[name, score]]
        scoreSheet += [score]
    ch = sorted(set(scoreSheet))[1]

    for n, s in sorted(markSheet):
        if s == ch:
            print(n)
