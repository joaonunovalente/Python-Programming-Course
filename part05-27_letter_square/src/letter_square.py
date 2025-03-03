# Write your solution here
def layers(number):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    my_list = []

    for i in range(0,number):
        my_list.append(i) = alphabet[i]
        print(i)
        print(my_list[i])

        


    return my_list


if __name__ == "__main__":
    layers(3)