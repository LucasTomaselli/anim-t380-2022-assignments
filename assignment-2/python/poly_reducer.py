from pathlib import Path
import maya.standalone
import argparse
maya.standalone.initialize()

import maya.cmds as cmds

parser = argparse.ArgumentParser(description='This script creates a bunch of cubes.')
parser.add_argument('folder_path', type=str, help="This is the folder that contains all your .ma files")
parser.add_argument('reduction_percentage', type=float, help="This is the percentage of poly reduction")

args = parser.parse_args()

filePaths = Path(args.folder_path)
percentReduct = args.reduction_percentage
files = cmds.getFileList(folder=filePaths)
print(len(files))

for x in range(len(files)):

    print("Importing file:", x)

    cmds.file(filePaths.joinpath(f'{str(x)}.ma') , o=True)    

    cmds.select(all=True)

    print("Reducing...")
    cmds.polyReduce(percentage = percentReduct, kqw = 1, triangulate = 0)
    
    cmds.file(save=True, type="mayaAscii")



