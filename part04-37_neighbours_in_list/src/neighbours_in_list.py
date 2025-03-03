def longest_series_of_neighbours(my_list: list) -> int:
    count = 0
    longest = 0
    for index in range(0,len(my_list) - 1):
        diff = my_list[index + 1] - my_list[index]
        print(diff, end = " ")
        if diff == 1 or diff == -1:
            if count <= 0:
                count = 0
            count += 1
            if count > longest:
                longest = count

        else:
            count = 0


        
    return longest + 1



if __name__ == "__main__":
    my_list = [1, 2, 3, 5, 6, 7, 6, 5, 6, 7, 10, 11, 10]
    longest_series_of_neighbours(my_list)