from pyautogui import *
from Settings import *

def __Selecter__(Line:int) -> str:
    #constant
    __stop:int = 0 
    __DataBase__ = ... 
    with open(FileDataBase,'rt') as texter:
        __DataBase__ = texter.readlines()
        for x in __DataBase__: 
            lines = x.splitlines()
            for reader in lines: 
                __stop = __stop +1
                if (__stop < Line +1 and __stop > Line-1): 
                    return reader 

class Spam:
    def __init__(self,text,times):
        self.text = text
        self.times = times
        self.config()
    
    def config(self):
        press('win')
        self.timer(1500)
        write('Bloco De Notas')
        self.timer(1500)
        press('Enter')
        self.timer(2500)
        write(self.text)
        self.timer(2000)
        keyDown('Ctrl')
        self.timer(2000)
        press('a')
        self.timer(2000)
        press('c')
        self.timer(2000)
        self.spam()
    
    def timer(self,t):
        for x in range(t):
            x =+ 1
            print(x)
    
    def spam(self):
        for spam in range(0,self.times):
            keyDown('Ctrl')
            press('v')
            keyUp('Ctrl')
            press('Enter')
            spam =+ 1
try:
    Bot_Spam = Spam((__Selecter__(2)),NumberOfTimes)
except:
    print("[ERROR]: It didn't work! So, We're just going use default mode, with 50 times in NumberOfTimes.")
    import os
    os.system('pause')
    Bot_Spam = Spam((__Selecter__(2)),50)