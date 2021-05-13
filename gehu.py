from bs4 import BeautifulSoup
import sys
import argparse
import requests
from const import URL, params, headers
from util import submitAttendance, calenderEvents

# payload = {
#        'sessid': '2542',
#        'sesskey': 'LAKRb1WMNT',
#        '_qf__mod_attendance_student_attendance_form': '1',
#        'mform_isexpanded_id_session': '1',
#        'status': '3365',
#        'submitbutton': 'Save changes'}

parser = argparse.ArgumentParser()
parser.add_argument('--events','-e', dest='show_events', action='store_true', help='displays the upcoming events')
parser.add_argument('--attendance', '-a', dest='mark_attendance', action='store_true', help='marks attendance')

args = parser.parse_args()

if len(sys.argv) == 1:
    print('Please provide arguments')

else:
    with requests.Session() as session:
        html = session.get(URL, verify=False, headers=headers)
        soup = BeautifulSoup(html.content, 'html5lib')
        params['logintoken'] = soup.find('input', {'name': 'logintoken'})['value']

        print()
        print('Authenticating with Moodle')
        print('-'*20)
        html2 = session.post(URL, verify=False, headers=headers, data=params)
        if html2.url == URL:
            print('Wrong Credentials')
        else:
            headers.update(session.cookies.get_dict())
            print('updated cookies for moodle session')
            print('-'*20)

            if args.mark_attendance and args.show_events:
                calenderEvents(session, headers)
                submitAttendance(session, headers)

            elif args.mark_attendance:
                submitAttendance(session, headers)
            
            elif args.show_events:
                calenderEvents(session, headers)

                

