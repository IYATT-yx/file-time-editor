from timemodule import TimeModule
from commontools import CommonTools
from buildtime import buildTime

import tkinter as tk
from tkinter import filedialog
import os
import sys

class MainUI(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.master = master
        self.pack()

    def updateCreateDays(self):
        """
        根据创建时间的年月调整天数的上限
        """
        days = CommonTools.getDaysOfMonth(self.createYearSpinbox.get(), self.createMonthSpinbox.get())
        self.createDaySpinbox.config(to=days)

    def updateModifyDays(self):
        """
        跟据修改时间的年月调整天数的上限
        """
        days = CommonTools.getDaysOfMonth(self.modifyYearSpinbox.get(), self.modifyMonthSpinbox.get())
        self.modifyDaySpinbox.config(to=days)

    def updateAccessDays(self):
        """
        根据访问时间的年月调整天数的上限
        """
        days = CommonTools.getDaysOfMonth(self.accessYearSpinbox.get(), self.accessMonthSpinbox.get())
        self.accessDaySpinbox.config(to=days)

    def initUI(self):
        tk.Label(self, text='文件：').grid(row=0, column=0)
        tk.Label(self, text='创建时间：').grid(row=2, column=0)
        tk.Label(self, text='修改时间：').grid(row=3, column=0)
        tk.Label(self, text='访问时间：').grid(row=4, column=0)

        tk.Label(self, text='年').grid(row=1, column=1)
        tk.Label(self, text='月').grid(row=1, column=2)
        tk.Label(self, text='日').grid(row=1, column=3)
        tk.Label(self, text='时').grid(row=1, column=4)
        tk.Label(self, text='分').grid(row=1, column=5)
        tk.Label(self, text='秒').grid(row=1, column=6)
        tk.Label(self, text='微秒').grid(row=1, column=7)

        self.filepathEntry = tk.Entry(self)
        self.filepathEntry.grid(row=0, column=1, columnspan=7, sticky=tk.NSEW)

        yearWidth = 5
        monthWidth = 3
        dayWidth = 3
        hourWidth = 3
        minuteWidth = 3
        secondWidth = 3
        microsecondWidth = 7

        # 创建时间
        self.createYearSpinbox = tk.Spinbox(self, from_=1980, to=2099, increment=1, width=yearWidth, command=self.updateCreateDays)
        self.createYearSpinbox.grid(row=2, column=1)
        self.createMonthSpinbox = tk.Spinbox(self, from_=1, to=12, increment=1, width=monthWidth, command=self.updateCreateDays)
        self.createMonthSpinbox.grid(row=2, column=2)
        self.createDaySpinbox = tk.Spinbox(self, from_=1, to=31, increment=1, width=dayWidth)
        self.createDaySpinbox.grid(row=2, column=3)
        self.createHourSpinbox = tk.Spinbox(self, from_=0, to=23, increment=1, width=hourWidth)
        self.createHourSpinbox.grid(row=2, column=4)
        self.createMinuteSpinbox = tk.Spinbox(self, from_=0, to=59, increment=1, width=minuteWidth)
        self.createMinuteSpinbox.grid(row=2, column=5)
        self.createSecondSpinbox = tk.Spinbox(self, from_=0, to=59, increment=1, width=secondWidth)
        self.createSecondSpinbox.grid(row=2, column=6)
        self.createMicrosecondSpinbox = tk.Spinbox(self, from_=0, to=999, increment=1, width=microsecondWidth)
        self.createMicrosecondSpinbox.grid(row=2, column=7)

        # 修改时间
        self.modifyYearSpinbox = tk.Spinbox(self, from_=1980, to=2099, increment=1, width=yearWidth, command=self.updateModifyDays)
        self.modifyYearSpinbox.grid(row=3, column=1)
        self.modifyMonthSpinbox = tk.Spinbox(self, from_=1, to=12, increment=1, width=monthWidth, command=self.updateModifyDays)
        self.modifyMonthSpinbox.grid(row=3, column=2)
        self.modifyDaySpinbox = tk.Spinbox(self, from_=1, to=31, increment=1, width=dayWidth)
        self.modifyDaySpinbox.grid(row=3, column=3)
        self.modifyHourSpinbox = tk.Spinbox(self, from_=0, to=23, increment=1, width=hourWidth)
        self.modifyHourSpinbox.grid(row=3, column=4)
        self.modifyMinuteSpinbox = tk.Spinbox(self, from_=0, to=59, increment=1, width=minuteWidth)
        self.modifyMinuteSpinbox.grid(row=3, column=5)
        self.modifySecondSpinbox = tk.Spinbox(self, from_=0, to=59, increment=1, width=secondWidth)
        self.modifySecondSpinbox.grid(row=3, column=6)
        self.modifyMicrosecondSpinbox = tk.Spinbox(self, from_=0, to=999, increment=1, width=microsecondWidth)
        self.modifyMicrosecondSpinbox.grid(row=3, column=7)

        # 访问时间
        self.accessYearSpinbox = tk.Spinbox(self, from_=1980, to=2099, increment=1, width=yearWidth, command=self.updateAccessDays)
        self.accessYearSpinbox.grid(row=4, column=1)
        self.accessMonthSpinbox = tk.Spinbox(self, from_=1, to=12, increment=1, width=monthWidth, command=self.updateAccessDays)
        self.accessMonthSpinbox.grid(row=4, column=2)
        self.accessDaySpinbox = tk.Spinbox(self, from_=1, to=31, increment=1, width=dayWidth)
        self.accessDaySpinbox.grid(row=4, column=3)
        self.accessHourSpinbox = tk.Spinbox(self, from_=0, to=23, increment=1, width=hourWidth)
        self.accessHourSpinbox.grid(row=4, column=4)
        self.accessMinuteSpinbox = tk.Spinbox(self, from_=0, to=59, increment=1, width=minuteWidth)
        self.accessMinuteSpinbox.grid(row=4, column=5)
        self.accessSecondSpinbox = tk.Spinbox(self, from_=0, to=59, increment=1, width=secondWidth)
        self.accessSecondSpinbox.grid(row=4, column=6)
        self.accessMicrosecondSpinbox = tk.Spinbox(self, from_=0, to=999, increment=1, width=microsecondWidth)
        self.accessMicrosecondSpinbox.grid(row=4, column=7)

        tk.Button(self, text='打开文件', command=self.onOpenFile).grid(row=0, column=8)
        tk.Button(self, text='修改时间', command=self.onModifyTime).grid(row=2, column=8, rowspan=3, sticky=tk.NSEW)

        tk.Label(self, text=f'IYATT-yx iyatt@iyatt.com 版本：{buildTime}').grid(row=5, column=0, columnspan=10, sticky=tk.W)

    def updateTimeSpinbox(self, spinboxObj: tk.Spinbox, value):
        """
        更新时间控件值

        Args:
            spinboxObj (tk.Spinbox): 时间控件
            value (int): 时间值
        """
        spinboxObj.delete(0, tk.END)
        spinboxObj.insert(0, value)

    def showTime(self, timeDict: dict):
        createTimeDict = timeDict[TimeModule.CREATE]
        modifyTimeDict = timeDict[TimeModule.MODIFY]
        accessTimeDict = timeDict[TimeModule.ACCESS]
        
        self.updateTimeSpinbox(self.createYearSpinbox, createTimeDict[TimeModule.YEAR])
        self.updateTimeSpinbox(self.createMonthSpinbox, createTimeDict[TimeModule.MONTH])
        self.updateTimeSpinbox(self.createDaySpinbox, createTimeDict[TimeModule.DAY])
        self.updateTimeSpinbox(self.createHourSpinbox, createTimeDict[TimeModule.HOUR])
        self.updateTimeSpinbox(self.createMinuteSpinbox, createTimeDict[TimeModule.MINUTE])
        self.updateTimeSpinbox(self.createSecondSpinbox, createTimeDict[TimeModule.SECOND])
        self.updateTimeSpinbox(self.createMicrosecondSpinbox, createTimeDict[TimeModule.MICROSECOND])

        self.updateTimeSpinbox(self.modifyYearSpinbox, modifyTimeDict[TimeModule.YEAR])
        self.updateTimeSpinbox(self.modifyMonthSpinbox, modifyTimeDict[TimeModule.MONTH])
        self.updateTimeSpinbox(self.modifyDaySpinbox, modifyTimeDict[TimeModule.DAY])
        self.updateTimeSpinbox(self.modifyHourSpinbox, modifyTimeDict[TimeModule.HOUR])
        self.updateTimeSpinbox(self.modifyMinuteSpinbox, modifyTimeDict[TimeModule.MINUTE])
        self.updateTimeSpinbox(self.modifySecondSpinbox, modifyTimeDict[TimeModule.SECOND])
        self.updateTimeSpinbox(self.modifyMicrosecondSpinbox, modifyTimeDict[TimeModule.MICROSECOND])

        self.updateTimeSpinbox(self.accessYearSpinbox, accessTimeDict[TimeModule.YEAR])
        self.updateTimeSpinbox(self.accessMonthSpinbox, accessTimeDict[TimeModule.MONTH])
        self.updateTimeSpinbox(self.accessDaySpinbox, accessTimeDict[TimeModule.DAY])
        self.updateTimeSpinbox(self.accessHourSpinbox, accessTimeDict[TimeModule.HOUR])
        self.updateTimeSpinbox(self.accessMinuteSpinbox, accessTimeDict[TimeModule.MINUTE])
        self.updateTimeSpinbox(self.accessSecondSpinbox, accessTimeDict[TimeModule.SECOND])
        self.updateTimeSpinbox(self.accessMicrosecondSpinbox, accessTimeDict[TimeModule.MICROSECOND])

    def onOpenFile(self):
        """
        打开文件
        """
        file = os.path.normpath(filedialog.askopenfilename(initialdir=os.path.dirname(sys.argv[0])))
        self.filepathEntry.delete(0, tk.END)
        self.filepathEntry.insert(0, file)
        timeDict = TimeModule.getFileTime(file)
        self.showTime(timeDict)        

    def onModifyTime(self):
        """
        修改时间
        """
        filepath = os.path.normpath(self.filepathEntry.get())
        createTimeDict = {
            TimeModule.YEAR: int(self.createYearSpinbox.get()),
            TimeModule.MONTH: int(self.createMonthSpinbox.get()),
            TimeModule.DAY: int(self.createDaySpinbox.get()),
            TimeModule.HOUR: int(self.createHourSpinbox.get()),
            TimeModule.MINUTE: int(self.createMinuteSpinbox.get()),
            TimeModule.SECOND: int(self.createSecondSpinbox.get()),
            TimeModule.MICROSECOND: int(self.createMicrosecondSpinbox.get())
        }
        modifyTimeDict = {
            TimeModule.YEAR: int(self.modifyYearSpinbox.get()),
            TimeModule.MONTH: int(self.modifyMonthSpinbox.get()),
            TimeModule.DAY: int(self.modifyDaySpinbox.get()),
            TimeModule.HOUR: int(self.modifyHourSpinbox.get()),
            TimeModule.MINUTE: int(self.modifyMinuteSpinbox.get()),
            TimeModule.SECOND: int(self.modifySecondSpinbox.get()),
            TimeModule.MICROSECOND: int(self.modifyMicrosecondSpinbox.get())
        }
        accessTimeDict = {
            TimeModule.YEAR: int(self.accessYearSpinbox.get()),
            TimeModule.MONTH: int(self.accessMonthSpinbox.get()),
            TimeModule.DAY: int(self.accessDaySpinbox.get()),
            TimeModule.HOUR: int(self.accessHourSpinbox.get()),
            TimeModule.MINUTE: int(self.accessMinuteSpinbox.get()),
            TimeModule.SECOND: int(self.accessSecondSpinbox.get()),
            TimeModule.MICROSECOND: int(self.accessMicrosecondSpinbox.get())
        }
        timeDict = {TimeModule.CREATE: createTimeDict, TimeModule.MODIFY: modifyTimeDict, TimeModule.ACCESS: accessTimeDict}
        TimeModule.modifyTime(filepath, timeDict)
