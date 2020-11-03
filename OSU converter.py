import sys
from PySide2.QtUiTools import QUiLoader #pip3 install PySide2
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile, QIODevice
from PySide2.QtWidgets import QFileDialog
from PySide2.QtCore import QStringListModel
from threading import Thread
import time
from time import strftime, localtime, sleep #Для (Time)

import os
from subprocess import call
#Ubuntu  sudo apt-get install unzip
#Arch  sudo pacman -S zip
language = "RU"

put = os.path.dirname(os.path.realpath(__file__)) + "/"#Путь- (part-1)

q = []
llm_2 = ()
qm1 = ()
qm2 = ()
d = ()
llm_10 = ()
r = ()


def functt(haha):
    global llm_2, q, llm_10, r
    Cycle = 0
    llm_2_D = llm_2
    m2 = llm_10
    print(llm_2_D)
    while Cycle < 30:
        r = r + d
        window.progressBar.setValue(r)
        
        if q[m2] != "001" and llm_2_D != 0:
            lol = qm1 + "/" + q[m2]
            lol2 = qm2 + "/" + q[m2] + ".osz"
            call(["zip", "-r", lol2, lol])
            #RAR = f'zip -r {lol2} {lol}'
            #os.system(RAR)
            #print(llm_2_D)
            llm_2_D = llm_2_D - 1
            m2 = m2 + 1
        else:
            Cycle = 50
            window.pushButton_2.setEnabled(True)



def ButtonWay():
    qm1 = QFileDialog.getExistingDirectory(window, "Заголовок", "/home/")
    window.lineEdit.setText(qm1)

def ButtonWay_2():
    qm2 = QFileDialog.getExistingDirectory(window, "Заголовок", "/home/")
    window.lineEdit_2.setText(qm2)


def sas():
    global qm1, qm2
    qm1 = window.lineEdit.text()#Путь откуда
    qm2 = window.lineEdit_2.text()#Путь куда

    if os.path.exists(qm1) == True and os.path.exists(qm2) == True:
        print("Путь одобрен!!!")
        sas3(qm1,qm2)
    else:
        if language == "RU":
            window.label_3.setText("Incorrect path!!!")
        else:
            window.label_3.setText("Некорректный путь!!!")
        print("Путь не одобрен!!!")

def sas3(qm1,qm2):
    global llm_2, q, d, llm_10, r
    window.progressBar.setValue(0)
    window.pushButton_2.setEnabled(False)
    m2 = 0
    q = os.listdir(path= qm1)
    q.append ("001")
    Cycle2 = 0
    x = 0
    llm_10 = (0)
    while Cycle2 < 30:
        if q[x] == "001":
            Cycle2 = 50
        else:
            x = x + 1
    
    d = 100 / x
    r = 0
    llm = os.cpu_count()
    llm = llm - 1
    if llm <= x:
        llm_2 = x / llm
        llm_2 = round(llm_2)
        print(llm_2)
        print(llm)
        print(x)
        while llm > 0:
            variable = Thread(target=functt, args=('ahhah',))
            variable.start()
            time.sleep(0.02)#Остановка на 0.10 сек.
            llm = llm - 1
            llm_10 = llm_10 + llm_2

    else:
        print(llm)
        print(x)
        Cycle = 0
        while Cycle < 30:
            r = r + d
            window.progressBar.setValue(r)
            m2 = m2 + 1
            if q[m2 - 1] != "001":
                lol = qm1 + "/" + q[m2 - 1]
                lol2 = qm2 + "/" + q[m2 - 1] + ".osz"
                call(["zip", "-r", lol2, lol])
            else:
                Cycle = 50
def sas2():
    global language
    if language == "RU":
        window.label.setText("Папка с картами")
        window.label_2.setText("Папка куда складировать карты")
        window.label_3.setText("Требуется установить zip или unzip!!!")
        window.pushButton.setText("English")
        window.pushButton_2.setText("Старт")
        language = "US"
    elif language == "US":
        window.label.setText("Folder with maps")
        window.label_2.setText("Folder where to store cards")
        window.label_3.setText("Zip or unzip required !!!")
        window.pushButton.setText("Русский")
        window.pushButton_2.setText("Start")
        language = "RU"

if __name__ == "__main__":
    global window    

    app = QApplication(sys.argv)

    ui_file_name = put + "222.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print("Cannot open {}: {}".format(ui_file_name, ui_file.errorString()))
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    sas2()
    window.show()
    window.pushButton_2.clicked.connect(sas)
    window.pushButton.clicked.connect(sas2)
    window.progressBar.setValue(0)

    window.pushButton_3.clicked.connect(ButtonWay)
    window.pushButton_4.clicked.connect(ButtonWay_2)

    sys.exit(app.exec_())








os.cpu_count()

variable = Thread(target=functt, args=('ahhah',))
variable.start()
