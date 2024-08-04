import os
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime


# 日志目录及文件轮转器
class LogDataRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, base_filename, *args, **kwargs):
        self.base_filename = base_filename
        super().__init__(self._get_filename(), *args, **kwargs)

    def _get_filename(self):
        # 获取当前日期，并格式化为YYYYMMDD
        today = datetime.now().strftime("%Y%m%d")
        # 创建包含日期的目录路径
        directory = os.path.join(os.path.dirname(self.base_filename), today)
        # 确保目录存在
        if not os.path.exists(directory):
            os.makedirs(directory)
        # 返回包含日期的完整日志文件路径
        return os.path.join(directory, os.path.basename(self.base_filename))

    def emit(self, record):
        # 每次日志记录时更新文件路径
        self.baseFilename = self._get_filename()
        # 检查文件是否存在，如果不存在则重新打开文件
        if not os.path.exists(self.baseFilename):
            self.stream = self._open()
        super().emit(record)
