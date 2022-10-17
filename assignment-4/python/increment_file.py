import os
import maya.cmds as cmds

save_file_format = "{asset}.{task}.{artist}.{version}.{ext}"

# take version number and extension and returns filename
def createSaveFile(versionInc, extension):
    fileName = cmds.file(q=True, sn=True)
    asset, task, artist, version, ext = fileName.split(".")
    asset_info = {
        "asset": asset,
        "task" : task,
        "artist": os.getenv('USER'),
        "version": versionInc,
        "ext": extension
    }

    filename = save_file_format.format(**asset_info)
    return filename

#increments the current version number by 1
def increment():
    fileName = cmds.file(q=True, sn=True, shn=True)
    asset, task, artist, version, ext = fileName.split(".")

    return (int(version) + 1)


print(createSaveFile(increment(), "ma"))

#saving the file using the filename from the createSaveFile function and using the increment function as the "versionInc" arguement
cmds.file(rename=createSaveFile(increment(), "ma"))
cmds.file(save=True, type="mayaAscii")