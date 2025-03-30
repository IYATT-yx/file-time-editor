from timemodule import TimeModule
from commontools import CommonTools
from buildtime import buildTime

import tkinter as tk
from tkinter import filedialog
import os
import sys
import datetime

class MainUI(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.master = master
        self.pack()

    def updateCreateDays(self):
        """
        根据创建时间的年月调整天数的上限
        """
        days = CommonTools.getDaysOfMonth(self.createYearVar.get(), self.createMonthVar.get())
        self.createDaySpinbox.config(to=days)

    def updateModifyDays(self):
        """
        跟据修改时间的年月调整天数的上限
        """
        days = CommonTools.getDaysOfMonth(self.modifyYearVar.get(), self.modifyMonthVar.get())
        self.modifyDaySpinbox.config(to=days)

    def updateAccessDays(self):
        """
        根据访问时间的年月调整天数的上限
        """
        days = CommonTools.getDaysOfMonth(self.accessYearVar.get(), self.accessMonthVar.get())
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
        self.createYearVar = tk.IntVar()
        self.createMonthVar = tk.IntVar()
        self.createDayVar = tk.IntVar()
        self.createHourVar = tk.IntVar()
        self.createMinuteVar = tk.IntVar()
        self.createSecondVar = tk.IntVar()
        self.createMicrosecondVar = tk.IntVar()
        tk.Spinbox(self, from_=1980, to=2099, increment=1, textvariable=self.createYearVar, width=yearWidth, command=self.updateCreateDays) \
        .grid(row=2, column=1)
        tk.Spinbox(self, from_=1, to=12, increment=1, textvariable=self.createMonthVar, width=monthWidth, command=self.updateCreateDays) \
        .grid(row=2, column=2)
        self.createDaySpinbox = tk.Spinbox(self, from_=1, to=31, increment=1, textvariable=self.createDayVar, width=dayWidth, command=self.updateCreateDays)
        self.createDaySpinbox.grid(row=2, column=3)
        tk.Spinbox(self, from_=0, to=23, increment=1, textvariable=self.createHourVar, width=hourWidth) \
        .grid(row=2, column=4)
        tk.Spinbox(self, from_=0, to=59, increment=1, textvariable=self.createMinuteVar, width=minuteWidth) \
        .grid(row=2, column=5)
        tk.Spinbox(self, from_=0, to=59, increment=1, textvariable=self.createSecondVar, width=secondWidth) \
        .grid(row=2, column=6)
        tk.Spinbox(self, from_=0, to=999999, increment=1, textvariable=self.createMicrosecondVar, width=microsecondWidth) \
        .grid(row=2, column=7)

        # 修改时间
        self.modifyYearVar = tk.IntVar()
        self.modifyMonthVar = tk.IntVar()
        self.modifyDayVar = tk.IntVar()
        self.modifyHourVar = tk.IntVar()
        self.modifyMinuteVar = tk.IntVar()
        self.modifySecondVar = tk.IntVar()
        self.modifyMicrosecondVar = tk.IntVar()
        tk.Spinbox(self, from_=1980, to=2099, increment=1, textvariable=self.modifyYearVar, width=yearWidth, command=self.updateModifyDays) \
        .grid(row=3, column=1)
        tk.Spinbox(self, from_=1, to=12, increment=1, textvariable=self.modifyMonthVar, width=monthWidth, command=self.updateModifyDays) \
        .grid(row=3, column=2)
        self.modifyDaySpinbox = tk.Spinbox(self, from_=1, to=31, increment=1, textvariable=self.modifyDayVar, width=dayWidth, command=self.updateModifyDays)
        self.modifyDaySpinbox.grid(row=3, column=3)
        tk.Spinbox(self, from_=0, to=23, increment=1, textvariable=self.modifyHourVar, width=hourWidth) \
        .grid(row=3, column=4)
        tk.Spinbox(self, from_=0, to=59, increment=1, textvariable=self.modifyMinuteVar, width=minuteWidth) \
        .grid(row=3, column=5)
        tk.Spinbox(self, from_=0, to=59, increment=1, textvariable=self.modifySecondVar, width=secondWidth) \
        .grid(row=3, column=6)
        tk.Spinbox(self, from_=0, to=999999, increment=1, textvariable=self.modifyMicrosecondVar, width=microsecondWidth) \
        .grid(row=3, column=7)

        # 访问时间
        self.accessYearVar = tk.IntVar()
        self.accessMonthVar = tk.IntVar()
        self.accessDayVar = tk.IntVar()
        self.accessHourVar = tk.IntVar()
        self.accessMinuteVar = tk.IntVar()
        self.accessSecondVar = tk.IntVar()
        self.accessMicrosecondVar = tk.IntVar()
        tk.Spinbox(self, from_=1980, to=2099, increment=1, textvariable=self.accessYearVar, width=yearWidth, command=self.updateAccessDays) \
        .grid(row=4, column=1)
        tk.Spinbox(self, from_=1, to=12, increment=1, textvariable=self.accessMonthVar, width=monthWidth, command=self.updateAccessDays) \
        .grid(row=4, column=2)
        self.accessDaySpinbox = tk.Spinbox(self, from_=1, to=31, increment=1, textvariable=self.accessDayVar, width=dayWidth, command=self.updateAccessDays)
        self.accessDaySpinbox.grid(row=4, column=3)
        tk.Spinbox(self, from_=0, to=23, increment=1, textvariable=self.accessHourVar, width=hourWidth) \
        .grid(row=4, column=4)
        tk.Spinbox(self, from_=0, to=59, increment=1, textvariable=self.accessMinuteVar, width=minuteWidth) \
        .grid(row=4, column=5)
        tk.Spinbox(self, from_=0, to=59, increment=1, textvariable=self.accessSecondVar, width=secondWidth) \
        .grid(row=4, column=6)
        tk.Spinbox(self, from_=0, to=999999, increment=1, textvariable=self.accessMicrosecondVar, width=microsecondWidth) \
        .grid(row=4, column=7)

        tk.Button(self, text='打开文件', command=self.onOpenFile).grid(row=0, column=8)
        tk.Button(self, text='修改时间', command=self.onModifyTime).grid(row=2, column=8, rowspan=3, sticky=tk.NSEW)

        tk.Label(self, text=f'IYATT-yx iyatt@iyatt.com 版本：{buildTime}').grid(row=5, column=0, columnspan=10, sticky=tk.W)

    def updateTimeSpinbox(self, valueObj: tk.IntVar, value):
        """
        更新时间控件值

        Args:
            spinboxObj (tk.Spinbox): 时间控件
            value (int): 时间值
        """
        valueObj.set(value)

    def showTime(self, timeDict: dict[str, datetime.datetime]):
        """
        实现时间

        Args:
            timeDict (dict[str, datetime.datetime]): 时间字典：创建、修改、访问
        """
        createDt = timeDict[TimeModule.CREATE]
        modifyDt = timeDict[TimeModule.MODIFY]
        accessDt = timeDict[TimeModule.ACCESS]
        
        self.updateTimeSpinbox(self.createYearVar, createDt.year)
        self.updateTimeSpinbox(self.createMonthVar, createDt.month)
        self.updateTimeSpinbox(self.createDayVar, createDt.day)
        self.updateTimeSpinbox(self.createHourVar, createDt.hour)
        self.updateTimeSpinbox(self.createMinuteVar, createDt.minute)
        self.updateTimeSpinbox(self.createSecondVar, createDt.second)
        self.updateTimeSpinbox(self.createMicrosecondVar, createDt.microsecond)

        self.updateTimeSpinbox(self.modifyYearVar, modifyDt.year)
        self.updateTimeSpinbox(self.modifyMonthVar, modifyDt.month)
        self.updateTimeSpinbox(self.modifyDayVar, modifyDt.day)
        self.updateTimeSpinbox(self.modifyHourVar, modifyDt.hour)
        self.updateTimeSpinbox(self.modifyMinuteVar, modifyDt.minute)
        self.updateTimeSpinbox(self.modifySecondVar, modifyDt.second)
        self.updateTimeSpinbox(self.modifyMicrosecondVar, modifyDt.microsecond)

        self.updateTimeSpinbox(self.accessYearVar, accessDt.year)
        self.updateTimeSpinbox(self.accessMonthVar, accessDt.month)
        self.updateTimeSpinbox(self.accessDayVar, accessDt.day)
        self.updateTimeSpinbox(self.accessHourVar, accessDt.hour)
        self.updateTimeSpinbox(self.accessMinuteVar, accessDt.minute)
        self.updateTimeSpinbox(self.accessSecondVar, accessDt.second)
        self.updateTimeSpinbox(self.accessMicrosecondVar, accessDt.microsecond)

    def onOpenFile(self):
        """
        打开文件
        """
        filepath = os.path.normpath(filedialog.askopenfilename(initialdir=os.path.dirname(sys.argv[0])))
        if filepath == '.': # 点击了取消
            return
        self.filepathEntry.delete(0, tk.END)
        self.filepathEntry.insert(0, filepath)
        timeDict = TimeModule.getFileTime(self.filepathEntry.get())
        self.showTime(timeDict)        

    def onModifyTime(self):
        """
        修改时间
        """
        filepath = os.path.normpath(self.filepathEntry.get())
        createDt = datetime.datetime(
            self.createYearVar.get(),
            self.createMonthVar.get(),
            self.createDayVar.get(),
            self.createHourVar.get(),
            self.createMinuteVar.get(),
            self.createSecondVar.get(),
            self.createMicrosecondVar.get()
        )
        modifyDt = datetime.datetime(
            self.modifyYearVar.get(),
            self.modifyMonthVar.get(),
            self.modifyDayVar.get(),
            self.modifyHourVar.get(),
            self.modifyMinuteVar.get(),
            self.modifySecondVar.get(),
            self.modifyMicrosecondVar.get()
        )
        accessDt = datetime.datetime(
            self.accessYearVar.get(),
            self.accessMonthVar.get(),
            self.accessDayVar.get(),
            self.accessHourVar.get(),
            self.accessMinuteVar.get(),
            self.accessSecondVar.get(),
            self.accessMicrosecondVar.get()
        )

        timeDict = {TimeModule.CREATE: createDt, TimeModule.MODIFY: modifyDt, TimeModule.ACCESS: accessDt}
        TimeModule.modifyTime(filepath, timeDict)
        
        timeDict = TimeModule.getFileTime(filepath)
        self.showTime(timeDict)  
