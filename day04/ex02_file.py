#ex02_file.py

f = open("test.txt", "w", encoding="utf-8")
students = ["또리","망이","솔이","원이"]
scores = [98,80,77,65]
for i in range(4):
    data = "%s님은 %s점입니다. \n" %(students[i],scores[i])
    f.write(data)
f.close()
d = open("text.txt","r",encoding="utf-8")
readData = d.readline()
print(readData)
# for i in readData:
#     print(i)
d.close()