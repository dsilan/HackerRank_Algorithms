import sys
ar = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
arr = [[0, -4, -6, 0, -7, -6], [-1, -2, -6, -8, -3, -1], [-8, -4, -2, -8, -8, -6], [-3, -1, -2, -5, -7, -4], [-3, -5, -3, -6, -6, -6], [-3, -6, 0, -8, -6, -7]]
max_value, sum_value = int(-sys.float_info.max-1), 0
for i in range (0, 4):
    for j in range (0, 4):
        sum_value += arr[i][j] + arr[i][j+1] + arr[i][j+2]
        sum_value += arr[i+1][j+1]
        sum_value += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if sum_value > max_value:
            max_value = sum_value
        sum_value = 0
print(max_value)