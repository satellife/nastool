import qnas.ui as ui
from qnas.ui import QtWidgets, QtCore, QtGui, sys

#enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, False)
#use highdpi icons
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

app = QtWidgets.QApplication(sys.argv)
gui = ui.GUI()
sys.exit(app.exec_())