## Description
**Problem 4:**
This scripts creates a maya file and a camera within it that is selected from a CSV list of shots. The camera and maya file will be named according to the shot name, and the focal length and filmback size will be set from the CSV file.
**Extra Credit Feature:** A framing chart image plane is added to the camera and a test image is rendered. 

## Arguments
The arguments taken by this script are as follows:
- `-h` :   This is recommened before each use as it displays to the user all the possible shots that they can choose from.
- `shot_num` : Type: int, This value is the shot number that the user would like to select.

## Example
Open command prompt and run `mayapy [python_file_path] -h `. This will run the help command. To select the first shot in the list, you would run `mayapy [python_file_path] 1 `.
