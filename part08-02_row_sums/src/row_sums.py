# Write your solution here
def row_sums(my_matrix: list) -> None:
    i = 0
    for row in my_matrix:
        my_matrix[i].append(sum(my_matrix[i]))
        i += 1

    return None


if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)    
