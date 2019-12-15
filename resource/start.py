import os

os.system("python3 receive.py fromapptovmqueue")
tmpFile = open("./data.txt", "r")
data = (tmpFile.read()).split(" ")
res = int(data[0]) + int(data[1])
os.system("python3 send.py fromvmtoappqueue "+str(res))
