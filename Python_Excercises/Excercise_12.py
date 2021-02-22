with open("ascii.txt", "r") as f:
    file_contents = f.read().splitlines()
list = []
for i in file_contents:
    x = ord(i)
    list.append(x)
num = []
for y in list:
        mirror_file = 128  - int(y)
        if mirror_file > 0:
            d = mirror_file 
            num.append(d)
        else:
            print("Has no mirror caharacter")
num.reverse()
char =[]
for b in num:
    c = chr(b)
    char.append(c)
print (*char)