import tkinter as tk
from MainMenu import MainMenu

def main():
    root = tk.Tk()
    MainMenu(root)
    root.geometry("800x600")
    root.mainloop()

if __name__ == "__main__":
    main()
