import winsound
winsound.Beep(3000,2000)

# import tkinter as tk
# from tkinter import ttk
#
# # colors:
# BLACK1 = '#252525'
# BLACK2 = '#404040'
# RED = '#c00002'
# GREEN = '#82c829'
# WHITE = '#FFFFFF'
# GREY = '#5a5956'
#
#
# class NewWindow(tk.Toplevel):
#
#     def __init__(self, master=None):
#         super().__init__(master=master)
#         self.title("New Window")
#         self.big_frame = tk.Frame(self, bg=BLACK2)
#         self.big_frame.pack()
#         # set minimum window size value
#         self.minsize(250, 180)
#         # set maximum window size value
#         self.maxsize(250, 180)
#         padding_left= tk.Label(self.big_frame, font='Helvetica 12 bold', text=" לא עובד בנתיים", bg=BLACK2, fg="red")
#         padding_left.grid(row = 0, column= 0, sticky=tk.W)
#         title_label = tk.Label(self.big_frame, bg=BLACK2, font='Helvetica 10 bold', text="אנא בחר את קצב שליחת" + "\n"+ "הפינג ואת זמן הסריקה")
#         title_label.grid(row = 0, column= 1, sticky=tk.E, columnspan = 2, pady= 20)
#
#         entry_ping = tk.Entry(self.big_frame,  width=11)
#         entry_ping.grid(row=1, column=0, sticky=tk.E)
#         ping_label= tk.Label(self.big_frame, text=":קצב שליחת פינג", width=12, bg=BLACK2, font='Helvetica 10 bold')
#         ping_label.grid(row = 1, column= 1, sticky=tk.E, columnspan = 2)
#
#         entry_scan = tk.Entry(self.big_frame,  width=11)
#         entry_scan.grid(row=2, column=0, sticky=tk.E)
#         scan_time_label = tk.Label(self.big_frame, text=":קצב סריקה",font='Helvetica 10 bold', width=12, bg=BLACK2)
#         scan_time_label.grid(row = 2, column= 1, sticky=tk.E, columnspan = 2)
#
#         ok_button = tk.Button(self.big_frame, text="אישור", bg=BLACK1, fg=WHITE,
#                               font='Helvetica 8 bold', width=10)
#         ok_button.grid(row=3, column=0, sticky=tk.W, padx=15, pady=20)
#
#         cancel_button = tk.Button(self.big_frame, text="ביטול", bg=BLACK1, fg=WHITE,
#                               font='Helvetica 8 bold', width=10)
#         cancel_button.grid(row=3, column=1, sticky=tk.W, padx=10, pady=20)
#
#
#
# # creates a Tk() object
# master = tk.Tk()
#
# # sets the geometry of
# # main root window
# master.geometry("200x200")
#
# label = tk.Label(master, text="This is the main window")
# label.pack(side=tk.TOP, pady=10)
#
# # a button widget which will
# # open a new window on button click
# btn = tk.Button(master,
#              text="Click to open a new window")
#
# # Following line will bind click event
# # On any click left / right button
# # of mouse a new window will be opened
# btn.bind("<Button>",
#          lambda e: NewWindow(master))
#
# btn.pack(pady=10)
#
# # mainloop, runs infinitely
# master.mainloop()