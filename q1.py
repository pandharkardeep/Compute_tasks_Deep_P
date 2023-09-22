n, x = map(int,input().split())
arrScores=[list(map(float,input().split())) for _ in range(x)]
[print(round(sum(i)/len(i),1)) for i in zip(*arrScores)]



