# Crop the first word of each line of a list file

fl = "ru.txt"9gag.com

line = 0
with open("ru2.txt", 'w+') as f:
    for a in open(fl):
        f.write(a[0:a.find(" ")]+"\n")
        line+=1
        if line == 50000:
            f.close()
            exit()
