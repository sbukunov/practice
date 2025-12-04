
from PySide6 import QtWidgets
from PySide6.QtWidgets import QLabel, QLineEdit, QVBoxLayout
from aTreads import SystemInfo

class SystemInfoWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        self.initThread()
    def initUI(self) -> None:
        layoutMain=QVBoxLayout()

        layoutMain.addWidget(QLabel("Задержка:"))
        self.delayEditLine = QLineEdit()
        self.delayEditLine.setText("1")
        layoutMain.addWidget(self.delayEditLine)

        self.cpuLabel = QLabel("CPU INFO")
        self.ramLabel = QLabel("RAM INFO")
        layoutMain.addWidget(self.cpuLabel)
        layoutMain.addWidget(self.ramLabel)

        self.delayEditLine.textChanged.connect(self.changeValueDelay)
        self.setLayout(layoutMain)
    def initThread(self):
        self.mainThread = SystemInfo()
        self.mainThread.systemInfoReceived.connect(self.updateInfo)
        try:
            self.mainThread.delay = int(self.delayEditLine.text())
        except:
            self.mainThread.delay = 1

        self.mainThread.start()

    def updateInfo(self,info):
        self.cpuLabel.setText(f'CPU INFO {info[0]} %')
        self.ramLabel.setText(f'RAM INFO {info[1]} %')

    def changeValueDelay(self,value):
        if value and value.isdigit():
            self.mainThread.delay = int(value)

    def stopThread(self):
        self.mainThread.stop()
        self.mainThread.quit()
        self.mainThread.wait()


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = SystemInfoWidget()
    window.show()
    app.exec()






