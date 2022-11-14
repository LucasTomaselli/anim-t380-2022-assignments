## Description
This scripts generates a GUI that creates a camera within the user's maya scene based on a selction from a drop-down menu of shot names. This drop-down menu is populated by a CSV file containg a list of shots. The camera will be named according to the shot name, and the focal length and filmback size will be set from the CSV file. A framing chart image plane is added the camera.
## Arguments
This GUI contains a drop-down menu that is populated with the shot names that the user can choose from.
## Note
Before running this script, the user must first set their maya project. Within the project folder the user should have a folder titled `bin` which must containt the `camera_list.csv` and the `framing_chart.jpg`.