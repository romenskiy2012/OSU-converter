import os
from subprocess import call
#Ubuntu  sudo apt-get install unzip
#Arch  sudo pacman -S zip
m2 = 0
qm1 = input("Путь до папки с картами: ")
qm2 = input("Путь куда выводить готовое: ")
q = os.listdir(path= qm1)
q.append ("001")
Cycle = 0
while Cycle < 30:
    m2 = m2 + 1
    if q[m2 - 1] != "001":
        lol = qm1 + q[m2 - 1]
        lol2 = qm2 + q[m2 - 1] + ".osz"
        call(["zip", "-r", lol2, lol])
    else:
        Cycle = 50
