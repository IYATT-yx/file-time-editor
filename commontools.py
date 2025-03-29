import calendar

class CommonTools:
    @staticmethod
    def getDaysOfMonth(year: str, month: str):
        """
        计算年月对应的天数
        """
        year = int(year)
        month = int(month)
        return calendar.monthrange(year, month)[1]