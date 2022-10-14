def row_counter(n, row = [1]):
    if n == 1:
        return ""
    else:
        actual_row = row
        next_row = [] 
        for i in range(len(actual_row)-1):
            next_row.append(actual_row[i] + actual_row[i + 1])
        next_row = [1] + next_row + [1]
        print(next_row)
        return row_counter(n-1, next_row,)


# row_counter(N rows)
row_counter(10)

# result
#                  [1, 1]
#                 [1, 2, 1]
#                [1, 3, 3, 1]
#              [1, 4, 6, 4, 1]
#             [1, 5, 10, 10, 5, 1]
#          [1, 6, 15, 20, 15, 6, 1]
#         [1, 7, 21, 35, 35, 21, 7, 1]
#       [1, 8, 28, 56, 70, 56, 28, 8, 1]
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]