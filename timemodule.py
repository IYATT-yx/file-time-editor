import os
import datetime
import pywintypes
import win32file
import win32con

class TimeModule:
    CREATE = 'create'
    MODIFY = 'modify'
    ACCESS = 'access'

    @staticmethod
    def getFileTime(filepath: str) -> dict[str, datetime.datetime]:
        """
        获取文件的创建、访问、修改时间

        Args:
            filepath (str): 文件路径

        Returns:
            dict: 创建时间、修改时间、访问时间
        """
        fileStats = os.stat(filepath)
        return {
            TimeModule.CREATE: datetime.datetime.fromtimestamp(fileStats.st_birthtime),
            TimeModule.MODIFY: datetime.datetime.fromtimestamp(fileStats.st_mtime),
            TimeModule.ACCESS: datetime.datetime.fromtimestamp(fileStats.st_atime)
        }
    
    @staticmethod
    def timeDt2Win(timeDt: datetime.datetime) -> pywintypes.Time:
        """
        将 datetime 对象转为 Windows 时间
        """
        return pywintypes.Time(timeDt)
    
    @staticmethod
    def timeDt2Second(timeDt: datetime.datetime) -> float:
        """
        将 datetime 对象转为秒
        """
        return timeDt.timestamp()

    @staticmethod
    def modifyTime(filepath: str, timeDict: dict):
        createTime = TimeModule.timeDt2Win(timeDict[TimeModule.CREATE])
        modifyTime = TimeModule.timeDt2Second(timeDict[TimeModule.MODIFY])
        accessTime = TimeModule.timeDt2Second(timeDict[TimeModule.ACCESS])

        # 创建时间只能使用 Windows API 修改
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
            UTCTimes = False # 设置为本地时间，而不是 UTC
        )
        handle.close()

        # # 修改访问时间和修改时间
        os.utime(filepath, (accessTime, modifyTime))
