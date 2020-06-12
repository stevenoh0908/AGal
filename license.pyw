# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'license.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LisenceWindow(object):
    def setupUi(self, LisenceWindow):
        LisenceWindow.setObjectName("LisenceWindow")
        LisenceWindow.resize(300, 200)
        LisenceWindow.setMinimumSize(QtCore.QSize(300, 200))
        LisenceWindow.setMaximumSize(QtCore.QSize(300, 200))
        LisenceWindow.setBaseSize(QtCore.QSize(300, 200))
        self.verticalLayout = QtWidgets.QVBoxLayout(LisenceWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(LisenceWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(LisenceWindow)
        QtCore.QMetaObject.connectSlotsByName(LisenceWindow)

    def retranslateUi(self, LisenceWindow):
        _translate = QtCore.QCoreApplication.translate
        LisenceWindow.setWindowTitle(_translate("LisenceWindow", "AGal - License"))
        self.label_2.setText(_translate("LisenceWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">License</span></p><p align=\"center\">AGal,  Analysis Tools for the research of extra-galaxy with its image, was Developed by <a href=\"https://github.com/stevenoh0908\"><span style=\" text-decoration: underline; color:#0000ff;\">Stephen Oh</span></a>, Published Under GPL v3.0 License.</p><p align=\"center\">For troubleshooting, please contact <a href=\"mailto:stevenoh0908@gmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">stevenoh0908@gmail.com</span></a>.</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LisenceWindow = QtWidgets.QWidget()
    ui = Ui_LisenceWindow()
    ui.setupUi(LisenceWindow)
    LisenceWindow.show()
    sys.exit(app.exec_())
