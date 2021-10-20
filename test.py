import tkinter as tk
from tkinter import filedialog



def upload_file():
    file = tk.filedialog.askopenfilename()
    fob = open(file , 'r')
    print(fob.read())

def main():
    root = tk.Tk()
    root.geometry("400x300")  # Size of the window
    root.title('Pingger 2.0')
    my_font1 = ('times', 18, 'bold')
    l1 = tk.Label(root, text='Upload File & read', width=30, font=my_font1)
    l1.grid(row=1, column=1)
    b1 = tk.Button(root, text='Upload File',
                   width=20, command=lambda: upload_file())
    b1.grid(row=2, column=1)
    root.mainloop()  # Keep the window open


if __name__ == '__main__':
    main()