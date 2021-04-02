def swapFiledata():
    input("what is the name of the new file you want to swap: ")
    input("what is the name of the file you want to swap it with: ")

    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file1, 'w') as a:
        a.write(data_b)


swapFiledata()