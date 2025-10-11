matrix = [[1,2,3],[4,5,6],[7,8,9]]
end_index = len(matrix) - 1
diagonal = [matrix[i][i] for i in range(len(matrix))]
next_diagonal =[matrix[i][end_index -i]for i in range(len(matrix))]
print(diagonal)
print(next_diagonal)