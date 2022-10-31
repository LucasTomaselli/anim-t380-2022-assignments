import maya.cmds as cmds
import csv
import argparse
import os
import re
from collections import defaultdict
import maya.standalone

#Initializing Maya standalone
maya.standalone.initialize()

#Creating an "empty" defaultdict that can be populated by the data in the CSV file
total = defaultdict(list)

#Storing assignment folder path
project_path = os.path.dirname(os.path.dirname(__file__))

#Opening csv and and reading with csv.DictReader to create a dict for each row that uses column headers as keys and each row in that column as a value
with open(project_path+'/bin/camera_list.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

#Iterating over each row and then iterating over the key and value pairs within the row. The defaultdict is populated as values are appended to the corresponding keys to create one dictionary of all the data in the csv file.
    for row in csv_reader:
        for key, value in row.items():
            total[key].append(value)

#Looping through all the value with the 'Camera' key and adding them to a string
shots = ''
for i in range(len(total['Camera'])):
    shots += str(i+1) + '.' + total['Camera'][i]
    shots += ',\n'
shots = shots[:-2]
args_descr = 'Welcome. Here is the shot list:\n' + shots

#Using the generated string as the help description for argparse so that the user can see all the available shots that they can select from
parser = argparse.ArgumentParser(description= args_descr)
parser.add_argument('shot_num', type=int, help="Please type the integer value of the shot you would like to select.")

args = parser.parse_args()
shot_num = args.shot_num

#Stroing the user argument in a variable that determine which camera is selected. creating a renamed string variable of the "shot" variable where certain special characters are replaced with '_' for maya naming compatability
row = shot_num - 1
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
cmds.renderWindowEditor(camera = rename_shot, writeImage =  project_path + '/bin/render.png')
cmds.ogsRender(camera = rename_shot)

#Here all the specs of the selected camera are printed
print('Camera: ' + str(shot) + ', Focal Length: ' + str(focal_length) + ', Horizontal Filmback: ' + str(hor_filmback) + 'in, Vertical Filmback: ' + str(vert_filmback) + 'in')

#File is named according the shot, and saved.
cmds.file(rename= project_path + '/bin/' + rename_shot + '.ma')
cmds.file(save=True, type='mayaAscii')

print('File ' + rename_shot + '.ma saved!')