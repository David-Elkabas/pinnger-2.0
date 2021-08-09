from tkinter import *

# colors:
BLACK1 = '#252525'
BLACK2 = '#404040'
RED = '#c00002'
GREEN = '#82c829'
WHITE = '#FFFFFF'

# files name
xl_file = "input.xlsx"

# measures
WIDTH = 600
HEIGHT = 500
MAIN_WINDOW_SIZE = str(WIDTH)+'x'+str(HEIGHT)

right_WIDTH = 280
right_HEIGHT = 400

SERVER_FRAME_WIDTH = 280
SERVER_FRAME_HEIGHT = 120

TAKASH_FRAME_WIDTH = 280
TAKASH_FRAME_HEIGHT = 240

TAKASH_WIDTH = 80
TAKASH_HEIGHT = 150

class Right_frame():
    def __init__(self, parent):
        self.parent = parent
        self.right_frame = Frame(self.parent, bg=RED, width=right_WIDTH, height=right_HEIGHT)
        self.right_frame.grid(column=1, row=1, padx=5, pady=5,sticky="NSEW")

class Left_frame():
    def __init__(self, parent):
        self.parent = parent
        self.left_frame = Frame(self.parent, bg=GREEN, width=right_WIDTH, height=right_HEIGHT)
        self.left_frame.grid(column=0, row=1, padx=5, pady=5,sticky="NSEW")
        self.left_frame.pack_propagate(0)

class window(Frame):
    def __init__(self, master):
        self.master = master
        self.main_frame = Frame(master, bg=BLACK2)
        self.main_frame.pack(fill=BOTH, expand=True)
        setting_button = Button(self.main_frame, text=" הגדרות", bg=BLACK1, fg=WHITE, font='Helvetica 8 bold', width=6)
        setting_button.grid(row=0, column=0, sticky=W,padx=5, pady=5)

        Grid.rowconfigure(self.main_frame, 0, weight=1)
        Grid.columnconfigure(self.main_frame, 0, weight=1)
        Grid.columnconfigure(self.main_frame, 1, weight=1)
        Grid.rowconfigure(self.main_frame, 1, weight=1)

        self.create_inner_windows()

    def create_inner_windows(self):
        self.left_frame = Left_frame(self.main_frame)
        self.right_frame = Right_frame(self.main_frame)

'''             ELIAV 

        self.create_top_title("ליבות ואתרים ניידים", self.left_frame, False)
        self.create_top_title("bla bla 36", self.right_frame, True)


    def create_top_title(self, title_name, frame_to_add_to, buttons):
        self.upper_frame = Frame(frame_to_add_to, bg=BLACK2)
        self.upper_frame.pack(fill=X, pady=2, padx=5)

        if buttons == True:
            self.setting_button = Button(self.upper_frame, text=" הגדרות", bg=BLACK1, fg=WHITE, font='Helvetica 8 bold', width=6)
            self.setting_button.grid(row=0, column=0, sticky=W)
            self.statistics_button = Button(self.upper_frame, text="סטיסטיקה", bg=BLACK1, fg=WHITE, font='Helvetica 8 bold',
                                       width=6)
            self.statistics_button.grid(row=1, column=0, sticky=W)

        self.title_bottom = Label(self.upper_frame, text=title_name, bg=BLACK2, fg=WHITE, font='Helvetica 18 bold')
        self.title_bottom.grid(row=0, column=1, rowspan=2)
        self.upper_frame.grid_rowconfigure(1, weight=1)
        self.upper_frame.grid_columnconfigure(1, weight=1)

        span = Frame(frame_to_add_to, bg=BLACK1, height=2)
        span.pack(fill=X, padx=15)
        '''



root = Tk()
root.title('Pingger')
root.geometry(MAIN_WINDOW_SIZE)

my_window = window(root)
# my_window.create_inner_windows()
root.mainloop()