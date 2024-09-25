m,n = list(map(int,input().split()))
matrix = [input().split() for item in range(m)]

area = [[0 for i in range(n+1)] for j in range(m+1)]
get_len = 0
for i in range(1, len(area)):
    for j in range(1, len(area[0])):
        if matrix [i-1][j-1] == "X":
            area[i][j] = min(area[i][j-1], area[i-1][j], area[i-1][j-1])+1 
            get_len = max(get_len, area[i][j])
            
print(get_len*get_len)   
