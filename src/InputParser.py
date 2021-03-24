

def readFile():
    f = open (r"C:\Users\Aliyah\OSDC\greetings.txt", "r")
    if f.mode == 'r':
        f1=f.readlines()
        index = 0
        a = [None] * 5
        for x in f1:
            #print (x)
            a[index] = x
            print (a[index])
            index = index+1
readFile()