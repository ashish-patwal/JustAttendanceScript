URL = 'http://45.116.207.79/moodle/login/index.php'

CLNDRURL = 'http://45.116.207.79/moodle/calendar/view.php?view=upcoming'

MARKATTENDANCEURL = 'http://45.116.207.79/moodle/mod/attendance/attendance.php'

ATTENDANCEURL_REG = '^http://45\.116\.207\.79/moodle/mod/attendance/view\.php\?id=[0-9]*$'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

params = {'logintoken': 'Leave this as it is','username': 'Your_Username', 'password': 'Your_Password'}

