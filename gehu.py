from bs4 import BeautifulSoup
import requests
from const import URL, params, headers
from util import calendarWrapper 

# payload = {
#        'sessid': '2542',
#        'sesskey': 'LAKRb1WMNT',
#        '_qf__mod_attendance_student_attendance_form': '1',
#        'mform_isexpanded_id_session': '1',
#        'status': '3365',
#        'submitbutton': 'Save changes'}


with requests.Session() as session:
    html = session.get(URL, verify=False, headers=headers)
    soup = BeautifulSoup(html.content, 'html5lib')
    params['logintoken'] = soup.find('input', {'name': 'logintoken'})['value']

    print()
    print('Authenticating with Moodle')
    print('-'*20)
    html2 = session.post(URL, verify=False, headers=headers, data=params)
    headers.update(session.cookies.get_dict())
    print('updated cookies for moodle session')
    print('-'*20)
    print('Submitting attendance if any in calender')
    print('-'*20)
    calendarWrapper(session, headers)

