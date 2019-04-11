from PyQt5 import QtCore, QtGui, QtWidgets
import dejarNota


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.notaBtn = QtWidgets.QPushButton(self.centralwidget)
        self.notaBtn.setGeometry(QtCore.QRect(10, 250, 101, 31))
        self.notaBtn.setObjectName("notaBtn")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 250, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.usuarioCuit = QtWidgets.QLineEdit(self.centralwidget)
        self.usuarioCuit.setGeometry(QtCore.QRect(10, 120, 221, 31))
        self.usuarioCuit.setObjectName("usuarioCuit")
        self.morcillaEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.morcillaEdit.setGeometry(QtCore.QRect(10, 190, 221, 31))
        self.morcillaEdit.setObjectName("morcillaEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(590, 560, 191, 16))
        self.label_4.setObjectName("label_4")
        self.cuadroProg = QtWidgets.QListWidget(self.centralwidget)
        self.cuadroProg.setGeometry(QtCore.QRect(360, 10, 421, 541))
        self.cuadroProg.setObjectName("cuadroProg")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.notaBtn.clicked.connect(self.iniciarProceso)
        self.pushButton_2.clicked.connect(self.detenerProceso)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AutoNota 0.2"))
        self.notaBtn.setText(_translate("MainWindow", "Dejar Nota"))
        self.pushButton_2.setText(_translate("MainWindow", "Detener"))
        self.label.setText(_translate("MainWindow", "Auto Nota"))
        self.label_2.setText(_translate("MainWindow", "Usuario (CUIT)"))
        self.label_3.setText(_translate("MainWindow", "Contraseña"))
        self.label_4.setText(_translate("MainWindow", "Desarrollado por Martín Ezequiel Toledo"))

    # funcion para el boton de dejar nota
    def iniciarProceso(self):
        usuario = str(self.usuarioCuit.text())
        morcilla = str(self.morcillaEdit.text())
        dejarNota.dejar_nota(user= usuario, psw= morcilla)
        return True

    #funcion para el boton Detener
    def detenerProceso(self):
        # placeholder, invocar funcion de detener
        print ("detener")

    def agregar_valor(self,msj):
        self.cuadroProg.addItem(msj)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




