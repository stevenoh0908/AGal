# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

'''
{ AGal - main.pyw }

AGal is GUI Application for analyzing complex data, which is dedicated to Galaxy H II Section Analysis Team,
developed by Stephen Oh.

Latest Modification Date: 2020-06-12 Fri, KST
Developed by Stephen Oh, Chief Developer of Trendous Development Alliance & Studio.Chem
Email Address: stevenoh0908@gmail.com

> Warning
This Code uses PyQt and ba2cc for execution, please make sure that you've installed them already,
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from exdatabaseparser import ExDBManager
import subprocess, os


class Ui_MainWindow(object):

    offset = 10

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 0, 1, 1, 1)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.menuAnalysis = QtWidgets.QMenu(self.menubar)
        self.menuAnalysis.setObjectName("menuAnalysis")
        self.menuSave_Load = QtWidgets.QMenu(self.menubar)
        self.menuSave_Load.setObjectName("menuSave_Load")
        self.menuSave_Load_2 = QtWidgets.QMenu(self.menubar)
        self.menuSave_Load_2.setObjectName("menuSave_Load_2")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionH_II_Section_Analysis = QtWidgets.QAction(MainWindow)
        self.actionH_II_Section_Analysis.setObjectName("actionH_II_Section_Analysis")
        self.actionExclude_Extremes = QtWidgets.QAction(MainWindow)
        self.actionExclude_Extremes.setObjectName("actionExclude_Extremes")
        self.actionSave_Current_Status = QtWidgets.QAction(MainWindow)
        self.actionSave_Current_Status.setObjectName("actionSave_Current_Status")
        self.actionSave_to_AGal_Dataset_agal = QtWidgets.QAction(MainWindow)
        self.actionSave_to_AGal_Dataset_agal.setObjectName("actionSave_to_AGal_Dataset_agal")
        self.actionGet_Ex_Database_via_its_name = QtWidgets.QAction(MainWindow)
        self.actionGet_Ex_Database_via_its_name.setObjectName("actionGet_Ex_Database_via_its_name")
        self.actionLoad_Ex_Database_from_file = QtWidgets.QAction(MainWindow)
        self.actionLoad_Ex_Database_from_file.setObjectName("actionLoad_Ex_Database_from_file")
        self.actionExport_Ex_Database_to_Agal_Ex_Database_set_agaldb = QtWidgets.QAction(MainWindow)
        self.actionExport_Ex_Database_to_Agal_Ex_Database_set_agaldb.setObjectName("actionExport_Ex_Database_to_Agal_Ex_Database_set_agaldb")
        self.actionDisplay_Settings = QtWidgets.QAction(MainWindow)
        self.actionDisplay_Settings.setObjectName("actionDisplay_Settings")
        self.actionClear_All = QtWidgets.QAction(MainWindow)
        self.actionClear_All.setObjectName("actionClear_All")
        self.actionAuto_Border_Calculation = QtWidgets.QAction(MainWindow)
        self.actionAuto_Border_Calculation.setObjectName("actionAuto_Border_Calculation")
        self.actionCompare_Galaxies = QtWidgets.QAction(MainWindow)
        self.actionCompare_Galaxies.setObjectName("actionCompare_Galaxies")
        self.actionDisplay_Galaxy_s_Attributes = QtWidgets.QAction(MainWindow)
        self.actionDisplay_Galaxy_s_Attributes.setObjectName("actionDisplay_Galaxy_s_Attributes")
        self.actionCompare = QtWidgets.QAction(MainWindow)
        self.actionCompare.setObjectName("actionCompare")
        self.actionImage_Analysis_Settings = QtWidgets.QAction(MainWindow)
        self.actionImage_Analysis_Settings.setObjectName("actionImage_Analysis_Settings")
        self.actionExtreme_Offset_Settings = QtWidgets.QAction(MainWindow)
        self.actionExtreme_Offset_Settings.setObjectName("actionExtreme_Offset_Settings")
        self.actionAuto_Border_Calculation_Settings = QtWidgets.QAction(MainWindow)
        self.actionAuto_Border_Calculation_Settings.setObjectName("actionAuto_Border_Calculation_Settings")
        self.actionChart_Displaying_Settings = QtWidgets.QAction(MainWindow)
        self.actionChart_Displaying_Settings.setObjectName("actionChart_Displaying_Settings")
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")

        self.actionH_II_Section_Analysis.triggered.connect(self.actionHIISectionAnalysisClicked)
        self.actionExclude_Extremes.triggered.connect(self.actionExcludeExtremesClicked)
        self.actionSave_Current_Status.triggered.connect(self.actionSaveCurrentStatusClicked)
        self.actionGet_Ex_Database_via_its_name.triggered.connect(self.actionGetExDatabaseClicked)
        self.actionExport_Ex_Database_to_Agal_Ex_Database_set_agaldb.triggered.connect(self.actionExportExDatabaseClicked)
        self.actionDisplay_Settings.triggered.connect(self.actionDisplaySettingsClicked)
        self.actionClear_All.triggered.connect(self.actionClearAllClicked)
        self.actionAuto_Border_Calculation.triggered.connect(self.actionAutoBorderCalculationClicked)
        self.actionCompare_Galaxies.triggered.connect(self.actionCompareGalaxiesClicked)
        self.actionDisplay_Galaxy_s_Attributes.triggered.connect(self.actionDisplayGalaxyAttributeClicked)
        self.actionImage_Analysis_Settings.triggered.connect(self.actionImageAnalysisSettingsClicked)
        self.actionExtreme_Offset_Settings.triggered.connect(self.actionExtremeOffsetSettingsClicked)
        self.actionAuto_Border_Calculation_Settings.triggered.connect(self.actionAutoBorderCalculationSettingsClicked)
        self.actionChart_Displaying_Settings.triggered.connect(self.actionChartDisplayingSettingsClicked)
        self.actionLicense.triggered.connect(self.actionLicenseClicked)
        
        self.menuAnalysis.addAction(self.actionH_II_Section_Analysis)
        self.menuAnalysis.addSeparator()
        self.menuAnalysis.addAction(self.actionExclude_Extremes)
        self.menuAnalysis.addAction(self.actionAuto_Border_Calculation)
        self.menuAnalysis.addSeparator()
        self.menuAnalysis.addAction(self.actionDisplay_Galaxy_s_Attributes)
        self.menuAnalysis.addAction(self.actionCompare)
        self.menuSave_Load.addAction(self.actionGet_Ex_Database_via_its_name)
        self.menuSave_Load.addSeparator()
        self.menuSave_Load.addAction(self.actionExport_Ex_Database_to_Agal_Ex_Database_set_agaldb)
        self.menuSave_Load_2.addAction(self.actionSave_Current_Status)
        self.menuSave_Load_2.addAction(self.actionSave_to_AGal_Dataset_agal)
        self.menuSettings.addAction(self.actionImage_Analysis_Settings)
        self.menuSettings.addAction(self.actionExtreme_Offset_Settings)
        self.menuSettings.addAction(self.actionAuto_Border_Calculation_Settings)
        self.menuSettings.addAction(self.actionChart_Displaying_Settings)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionLicense)
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuSave_Load.menuAction())
        self.menubar.addAction(self.menuSave_Load_2.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AGal"))
        self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis"))
        self.menuSave_Load.setTitle(_translate("MainWindow", "Ex-Database"))
        self.menuSave_Load_2.setTitle(_translate("MainWindow", "Import/Export"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionH_II_Section_Analysis.setText(_translate("MainWindow", "Start H II Image Analysis"))
        self.actionExclude_Extremes.setText(_translate("MainWindow", "Exclude Extremes"))
        self.actionSave_Current_Status.setText(_translate("MainWindow", "Import from AGal Dataset(.agal)"))
        self.actionSave_to_AGal_Dataset_agal.setText(_translate("MainWindow", "Export to AGal Dataset(.agal)"))
        self.actionGet_Ex_Database_via_its_name.setText(_translate("MainWindow", "Get Ex-Database via its name(WEB)"))
        self.actionExport_Ex_Database_to_Agal_Ex_Database_set_agaldb.setText(_translate("MainWindow", "Export Galaxy Properties to Txt File"))
        self.actionDisplay_Settings.setText(_translate("MainWindow", "Display Settings"))
        self.actionClear_All.setText(_translate("MainWindow", "Clear All"))
        self.actionAuto_Border_Calculation.setText(_translate("MainWindow", "Auto-Border Calculation"))
        self.actionCompare_Galaxies.setText(_translate("MainWindow", "Compare..."))
        self.actionDisplay_Galaxy_s_Attributes.setText(_translate("MainWindow", "Display Galaxy\'s Attributes"))
        self.actionCompare.setText(_translate("MainWindow", "Compare..."))
        self.actionImage_Analysis_Settings.setText(_translate("MainWindow", "Image Analysis Settings"))
        self.actionExtreme_Offset_Settings.setText(_translate("MainWindow", "Extreme Offset Settings"))
        self.actionAuto_Border_Calculation_Settings.setText(_translate("MainWindow", "Auto-Border Calculation Settings"))
        self.actionChart_Displaying_Settings.setText(_translate("MainWindow", "Chart Displaying Settings"))
        self.actionLicense.setText(_translate("MainWindow", "License"))
        pass

    def actionHIISectionAnalysisClicked(self):
        pass

    def actionExcludeExtremesClicked(self):
        pass

    def actionSaveCurrentStatusClicked(self):
        pass

    def actionGetExDatabaseClicked(self):
        subprocess.Popen('python exdatabaseparser.py', creationflags=subprocess.CREATE_NEW_CONSOLE)
        pass

    def actionExportExDatabaseClicked(self):
        name, ok = QtWidgets.QInputDialog.getText(MainWindow, "AGal", "Input Name of Exporting Extra-Galatic Object")
        if ok:
            if not os.path.isdir('Ex-Database'):
                os.mkdir('Ex-Database')
                pass
            with open('Ex-Database\\'+str(name)+'.txt', 'w') as datafile:
                manager = ExDBManager(str(name))
                datafile.write('<Information Table Of ' + manager.galaxyname + '>')
                datafile.write('\n')
                datafile.write('--------------------------')
                datafile.write('\n')
                datafile.write('Info URL: ' + manager.url)
                datafile.write('\n')
                datafile.write('--------------------------')
                datafile.write('\n')
                datafile.write('[Cross-Identifications]')
                datafile.write('\n')
                for item in manager.CrossIdent:
                    datafile.write('- ' + item)
                    datafile.write('\n')
                datafile.write('')
                datafile.write('\n')
                datafile.write('[Coordinates for Preferred Position]')
                datafile.write('\n')
                datafile.write('> Equatorial (J2000)')
                datafile.write('\n')
                datafile.write('RA: ' + manager.RA)
                datafile.write('\n')
                datafile.write('Dec: ' + manager.Dec)
                datafile.write('\n')
                datafile.write('RA(in Deg): ' + manager.RA_DEG)
                datafile.write('\n')
                datafile.write('Dec(in Deg): ' + manager.Dec_DEG)
                datafile.write('\n')
                datafile.write('')
                datafile.write('\n')
                datafile.write('[Preferred Redshift & Derived Quantities] - H0 = 67.8 km/s/Mpc')
                datafile.write('\n')
                datafile.write('z: ' + manager.Z[0] + ' +/- ' + manager.Z[1])
                datafile.write('\n')
                datafile.write('V(Helio, km/s): ' + manager.VHelio[0] + ' +/- ' + manager.VHelio[1])
                datafile.write('\n')
                datafile.write('V(CMB, km/s): ' + manager.VCMB[0] + ' +/- ' + manager.VCMB[1])
                datafile.write('\n')
                datafile.write('')
                datafile.write('\n')
                datafile.write('[Classifications]')
                datafile.write('\n')
                datafile.write('Object Type: ' + manager.ObjectType)
                datafile.write('\n')
                datafile.write('Morphology: ' + manager.Morphoogy)
                datafile.write('\n')
                datafile.write('Other: ' + manager.OtherClassification)
                datafile.write('\n')
                datafile.write('')
                datafile.write('\n')
                datafile.write('[Angular & Physical Diameters]')
                datafile.write('\n')
                datafile.write('Passband: ' + manager.Passband)
                datafile.write('\n')
                datafile.write('Diameter(kpc): ' + manager.Diameter)
                datafile.write('\n')
                datafile.write('')
                datafile.write('\n')
                datafile.write('[Foreground Galatic Extinction]')
                datafile.write('\n')
                datafile.write('A_lambda [mag] V: ' + manager.A_lambdaV)
                datafile.write('\n')
                datafile.write('A_lambda [mag] K: '+ manager.A_lambdaK)
                datafile.write('\n')
                pass
            pass
        pass

    def actionDisplaySettingsClicked(self):
        pass

    def actionClearAllClicked(self):
        pass

    def actionAutoBorderCalculationClicked(self):
        pass

    def actionCompareGalaxiesClicked(self):
        pass

    def actionDisplayGalaxyAttributeClicked(self):
        pass

    def actionImageAnalysisSettingsClicked(self):
        pass

    def actionExtremeOffsetSettingsClicked(self):
        offset, ok = QtWidgets.QInputDialog.getDouble(MainWindow, 'Extreme Offset Option', 'Input offset for excluding extremes.', 10, -2147483647, 2147483647, 5)
        if ok:
            if offset > 0:
                self.offset = offset
                pass
            pass
        pass

    def actionAutoBorderCalculationSettingsClicked(self):
        pass

    def actionChartDisplayingSettingsClicked(self):
        pass

    def actionLicenseClicked(self):
        subprocess.Popen('pythonw license.pyw', shell=True)
        pass

    pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
