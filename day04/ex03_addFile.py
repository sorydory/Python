# ex03_addFile.py
f = open("test.txt", "a", encoding="utf-8")
for i in range(5,9):
    data = "%d 번째 줄입니다. \n" %i
    f.write(data)
f.close()