# pinnger-2.0
an application that sends pings for end point devices and checks if they are alive

**Table of Contents**

[TOCM]

[TOC]

## Features
Pinnger - an application (exe file) that sends pings for end point devices in hierarchy using threding and checks if they are alive. in the repository example there is ~180 end point devices

the user can add and change the end point devices from a xlsx file or Json file as they wish.

### user interface image 

the application comes with fully functional GUI. written in python with tkinter.

![](https://github.com/David-Elkabas/pinnger-2.0/blob/main/rsz_user_interface.png)
> example of the ui


### ⚙️ setting
the user can change all the setting for the program via the setting.json file.
the setting include:
* colors of the GUI
* font_size
* send ping time
* intervals between updates 
* read the data from json file to xlsx file
* json file name
* xl file name
* use sound or not



### runnig the program

the test the program download the files: 
* Classes.py
* data.json (or data.xlsx)
* setting.json
* main.py

and run the file main.py

or dowload the exe file with data.json & setting.json

## License

This project is open source and available under the [MIT License](LICENSE).

