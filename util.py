from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
from context import RequestURL
from requests import codes
import re
import threading

from const import CLNDRURL, ATTENDANCEURL_REG, MARKATTENDANCEURL


def dateAndTime(soup):
    #return [BeautifulSoup(data.select('div:nth-of-type(3)'), 'html5lib').get_text() for data in soup.select('div:is(.description .card-body)')]
    return (''.join(data.get_text().split()) for data in soup.find('div', {'class': 'calendarwrapper'}).find_all('div', class_=re.         compile('^row$')))

def Links(soup):
    return (data.attrs['href'] for data in soup.find('div', {'class': 'maincalendar'}).find_all('a', href=re.compile(ATTENDANCEURL_REG)))


def submitAttendance(session, headers):
    print('Submitting attendance if any in calender')
    print('-'*20)
    with RequestURL(CLNDRURL, session, headers) as soup:
        for link in Links(soup):
            #submitAttendance(link, session, headers)
            #print(link)
            threading.Thread(target=markAttendance, args=(link, session, headers)).start()
            

def calenderEvents(session, headers):
    print('Showing upcoming events')
    print('-'*20)
    with RequestURL(CLNDRURL, session, headers) as soup:
        for counter, event in enumerate(dateAndTime(soup), 1):
            print(event)
            if(counter%3 == 0):
                print('-'*20)




def markAttendance(targetURL, session, headers):

    payload = {
        'submitbutton': 'Save+changes',
        '_qf__mod_attendance_student_attendance_form': '1',
        'mform_isexpanded_id_session': '1'}

    with RequestURL(targetURL, session, headers) as soup:
        print(soup.title.string)
        try:
            target = soup.find('a', text='Submit attendance')['href']
        except TypeError:
            print('NO Submission Link')
            print('-'*20)
        else:
            for k, v in parse_qs(urlparse(target).query).items():
                    payload[k] = ''.join(v)
            with RequestURL(target, session, headers) as soup2:
                presentValue = soup2.find('input', {'name': 'status', 'type': 'radio'})['value']
                #statusValue = presentValue.find_parent('input',{'name': 'status', 'type': 'radio'}).attrs['value']
                payload.setdefault('status', presentValue)
                
                r = session.post(MARKATTENDANCEURL, verify=False, headers=headers, data=payload)
                if r.status_code == codes['ok']:
                    print('Submitted Attendance successfully')
                else :
                    print("Error happend : " + r.status_code)
                print('-'*20)
                


