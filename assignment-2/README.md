This script opens maya files in a given folder and runs the a polygon reduction operation on the mesh that each file contains. This script currently only runs if the maya file contains a single mesh and if the maya files are named with integer values starting from 0.

The script takes two arguments. The first is a string argument which points to the folder where the user stores their maya files and the second is an float which determines what percentage of polygon reduction occurs on the mesh.

Here is an example of how to run the script: mayapy poly_reducer.py C:\Users\lucas\Documents\T380\anim-t380-2022-assignments\assignment-2\bin 70