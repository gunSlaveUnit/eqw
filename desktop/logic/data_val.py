import time
from datetime import datetime

class DateChecker:
    def check_date(self, date_string):
        try:
            date_obj = datetime.strptime(date_string, '%Y-%m-%d')
            timestamp = int(time.mktime(date_obj.timetuple()))
            return timestamp
        except ValueError:
            return None
