def read_file(filename, length):
    f = open(filename, "r")
    if f.mode == 'r':
        f1 = f.readlines()
        index = 0
        a = [None] * length
        for x in f1:
            a[index] = x
            print(a[index])
            index = index + 1


if __name__ == "__main__":
    read_file(r"C:\Users\Aliyah\OSDC\greetings.txt", 3)
    print("thanks conor :D")
