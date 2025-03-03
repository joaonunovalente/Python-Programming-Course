# write your solution here

def row_sums() -> list:
    row_sum_list = []
    with open("matrix.txt") as new_file:
        for line in new_file:
            numbers = line.split(",")
            row_list = []
            for number in numbers:
                row_list.append(int(number))
            row_sum_list.append(sum(row_list))
    return row_sum_list

def matrix_sum():
    row_sum_list = []
    with open("matrix.txt") as new_file:
        for line in new_file:
            numbers = line.split(",")
            row_list = []
            for number in numbers:
                row_list.append(int(number))
            row_sum_list.append(sum(row_list))

    return sum(row_sum_list)

def matrix_max():
    maximum = 0
    row_sum_list = []
    with open("matrix.txt") as new_file:
        for line in new_file:
            numbers = line.split(",")
            row_list = []
            for number in numbers:
                row_list.append(int(number))
            row_sum_list.append(max(row_list))

    return max(row_sum_list)


    return maximum


if __name__ == "__main__":
    row_sums()
