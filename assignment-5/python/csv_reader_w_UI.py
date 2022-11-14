import maya.cmds as cmds
import csv
import os
import re
from collections import defaultdict
from maya import OpenMayaUI as omui 
from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance 


#Creating an "empty" defaultdict that can be populated by the data in the CSV file
total = defaultdict(list)

#Storing folder path of maya project
project_path = cmds.workspace(q=True, rd=True)

#Opening csv and and reading with csv.DictReader to create a dict for each row that uses column headers as keys and each row in that column as a value
with open(project_path+'/bin/camera_list.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

#Iterating over each row and then iterating over the key and value pairs within the row. The defaultdict is populated as values are appended to the corresponding keys to create one dictionary of all the data in the csv file.
    for row in csv_reader:
        for key, value in row.items():
            total[key].append(value)

#Looping through all the value with the 'Camera' key and adding them to a string
shots = []
for i in range(len(total['Camera'])):
    shots.append(total['Camera'][i])


#Referencing main Maya application window
mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QWidget) 


class MyMayaWidget(QWidget):    
    def __init__(self, *args, **kwargs):        
        super(MyMayaWidget, self).__init__(*args, **kwargs)
               
        self.setParent(mayaMainWindow)        
        self.setWindowFlags(Qt.Window)   
        
        #GUI Window 
        self.setWindowTitle('Shot Selecter')        
        self.setGeometry(100, 100, 300, 250)
        
        #My Widgets
        self.title_label = QLabel('Shot Selecter', self)
        self.title_label.move(5, 10)
        
        self.my_button = QPushButton('Create Camera', self)
        self.my_button.move(5,200)
        
        self.options_label = QLabel('Shot:', self)
        self.options_label.move(5, 50)

        self.my_options = QComboBox(self)
        self.my_options.addItems(shots)
        self.my_options.move(50,50)
        

        #On Click
        self.my_button.clicked.connect(self.button_onClicked)

    def button_onClicked(self):
        self.create_camera()  

    def create_camera(self):

        #Stroing the user argument in a variable that determine which camera is selected. creating a renamed string variable of the "shot" variable where certain special characters are replaced with '_' for maya naming compatability
        row = self.my_options.currentIndex()
        shot = total['Camera'][row]
        rename_shot = re.sub('[ -]', '_', str(shot))

        #Storing the value from the csv file into variables to be sued when creating the camera. the convention for filmback size is in mm but maya uses inches for this feature. The csv file contains mm so these values are converted to inches
        focal_length = (float)(total['Focal Length'][row])
        hor_filmback = round(((float)(total['Filmback Size Horizontal'][row]))/25.24, 2)
        vert_filmback = round(((float)(total['Filmback Size Vertical'][row]))/25.24, 2)

        print('Creating', shot, '...\n')

        #Creating the camera, renaming it, adding an image plane with the framing chart, and rendering an image
        cmds.camera(focalLength = focal_length, horizontalFilmAperture = hor_filmback, verticalFilmAperture = vert_filmback)
        cmds.rename(rename_shot)
        cmds.imagePlane(camera = rename_shot, fileName = project_path + '/bin/framing_chart.jpg')

        #Here all the specs of the selected camera are printed
        print('Camera: ' + str(shot) + ', Focal Length: ' + str(focal_length) + ', Horizontal Filmback: ' + str(hor_filmback) + 'in, Vertical Filmback: ' + str(vert_filmback) + 'in')

my_widget = MyMayaWidget()     
my_widget.show()