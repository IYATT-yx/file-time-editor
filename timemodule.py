import os
import datetime
import time
import pywintypes
import win32file
import win32con

class TimeModule:
    YEAR = 'year'
    MONTH = 'month'
    DAY = 'day'
    HOUR = 'hour'
    MINUTE = 'minute'
    SECOND = 'second'
    MICROSECOND = 'microsecond'
    CREATE = 'create'
    ACCESS = 'access'
    MODIFY = 'modify'

    @staticmethod
    def getFileTime(filepath: str) -> dict:
        """
        获取文件的创建、访问、修改时间

        Args:
            filepath (str): 文件路径

        Returns:
            dict: (创建时间, 访问时间, 修改时间)。
            每段时间为一个字典结构，由 (年，月，日，时，分，秒，微秒) 组成。
        """
        fileStats = os.stat(filepath)

        createTime = datetime.datetime.fromtimestamp(fileStats.st_birthtime)
        accessTime = datetime.datetime.fromtimestamp(fileStats.st_atime)
        modifyTime = datetime.datetime.fromtimestamp(fileStats.st_mtime)

        createTimeDict = {
            TimeModule.YEAR: createTime.year,
            TimeModule.MONTH: createTime.month,
            TimeModule.DAY: createTime.day,
            TimeModule.HOUR: createTime.hour,
            TimeModule.MINUTE: createTime.minute,
            TimeModule.SECOND: createTime.second,
            TimeModule.MICROSECOND: createTime.microsecond
        }

        accessTimeDict = {
            TimeModule.YEAR: accessTime.year,
            TimeModule.MONTH: accessTime.month,
            TimeModule.DAY: accessTime.day,
            TimeModule.HOUR: accessTime.hour,
            TimeModule.MINUTE: accessTime.minute,
            TimeModule.SECOND: accessTime.second,
            TimeModule.MICROSECOND: accessTime.microsecond
        }

        modifyTimeDict = {
            TimeModule.YEAR: modifyTime.year,
            TimeModule.MONTH: modifyTime.month,
            TimeModule.DAY: modifyTime.day,
            TimeModule.HOUR: modifyTime.hour,
            TimeModule.MINUTE: modifyTime.minute,
            TimeModule.SECOND: modifyTime.second,
            TimeModule.MICROSECOND: modifyTime.microsecond
        }

        return {
            TimeModule.CREATE: createTimeDict,
            TimeModule.ACCESS: accessTimeDict,
            TimeModule.MODIFY: modifyTimeDict
        }
    
    @staticmethod
    def timeDict2Win(timeDict: dict) -> pywintypes.Time:
        """
        将年、月、日、时、分、秒、微秒的时间字典转为 Windows 时间秒
        """
        TimeSecond = time.mktime((
            timeDict[TimeModule.YEAR],
            timeDict[TimeModule.MONTH],
            timeDict[TimeModule.DAY],
            timeDict[TimeModule.HOUR],
            timeDict[TimeModule.MINUTE],
            timeDict[TimeModule.SECOND],
            0, 0, 0
        ))
        return pywintypes.Time(TimeSecond + timeDict[TimeModule.MICROSECOND] / 1e6)

    @staticmethod
    def modifyTime(filepath: str, timeDict: dict):
        createTime = TimeModule.timeDict2Win(timeDict[TimeModule.CREATE])
        accessTime = TimeModule.timeDict2Win(timeDict[TimeModule.ACCESS])
        modifyTime = TimeModule.timeDict2Win(timeDict[TimeModule.MODIFY])

        # 文件句柄
        handle = win32file.CreateFile(
            filepath,
            win32con.GENERIC_WRITE, # 写入
            win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
            None, # 默认的安全属性
            win32con.OPEN_EXISTING, # 文件不存在则失败
            0, # 不修改属性
            None
        )

        win32file.SetFileTime(
            handle,
            createTime,
            accessTime,
            modifyTime,
            False # 设置为本地时间，而不是 UTC
        )

        handle.close()