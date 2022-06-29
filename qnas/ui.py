from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui
import sys
from nastool import csv

import nastool.bdf as bdf
import nastool.mass_point as mp

# Create a class of GUI, containing a path line edit and two buttons.
# The path line edit is used to input the path of the .bdf file.
# One button is to browse the file and the other button is to handle the file.
class GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.ui = loadUi("./qnas/qnas.ui", self)
        self.ui.browse.clicked.connect(self.browse_file)
        self.ui.handle.clicked.connect(self.handle_file)

        self.show()

    def browse_file(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', './', filter="*.csv")
        self.path_line.setText(path[0])

    def handle_file(self):
        model = bdf.create_bdf()

        file_path = self.path_line.text()
        file_name = file_path.split('/')[-1]
        path = file_path.replace(file_name, '')

        massmap = csv.read_mass_point_from_csv(file_path)
        # print(massmap)
        model = mp.massmap_to_bdf(massmap, model)
        bdf.write_bdf(model, path + 'massmap.bdf')

        # messagebox.showinfo('Info', 'Done!')
        QtWidgets.QMessageBox.information(self, 'Info', 'Done!')

# Run the GUI.
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec_())