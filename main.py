from threading import Thread
from time import sleep
from tkinter import Tk, N, E, W, S, BOTTOM, TOP, SOLID, RIGHT, LEFT, Y, X
from tkinter.ttk import *
from PyQt5.QtWidgets import QApplication
from libraries.CalculatorTab import CalculatorTab
import darkdetect
import sv_ttk as Style
import ctypes as ct
import os
import sys

app = QApplication(sys.argv)


class MainApp:
    def __init__(self) -> None:
        self.thread = Thread(target=self.create)
        self.thread.start()

    def darkTitleBar(self):
        """
        MORE INFO:
        https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
        """
        try:
            self.root.update()
            if os.name == "nt":
                ct.windll.dwmapi.DwmSetWindowAttribute(
                    ct.windll.user32.GetParent(
                        self.root.winfo_id()
                    ),
                    20,
                    ct.byref(
                        ct.c_int(2)
                    ),
                    ct.sizeof(
                        ct.c_int(2)
                    )
                )
        except:
            pass

    def setTheme(self) -> None:
        try:
            if darkdetect.isDark():
                self.darkTitleBar()
                Style.set_theme("dark")
            else:
                Style.set_theme("light")
        except:
            Style.set_theme("light")

    def buildWidgets(self):
        # Navigation Bar
        self.topBar = Frame(self.root)
        self.topBar.pack(side=TOP, fill=X)
        CalculatorTab(self.topBar)
        

    def onClose(self):
        for i in range(4, 10):
            self.root.attributes("-alpha", 1-(i/10))
            sleep(.01)
            self.root.update()
        self.root.iconify()
        self.root.withdraw()
        sys.exit()

    def create(self):
        self.root = Tk()
        self.root.geometry("{}x{}".format(
            int(self.root.winfo_screenheight()/2.5), int(self.root.winfo_screenheight()/2)))
        self.root.iconbitmap("./Assets/icon.ico")

        self.root.wm_resizable(False,False)
        self.setTheme()
        self.buildWidgets()

        self.root.title("JSimple - 1.0")
        self.root.protocol("WM_DELETE_WINDOW", self.onClose)
        self.root.mainloop()


if __name__ == "__main__":
    MainApp()
