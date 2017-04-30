# -*- coding: utf-8 -*-
from wsgiref import simple_server
from cgi import parse_qs
import calendar

def application(env, res):
    status = "200 OK"
    get_info = parse_qs(env['QUERY_STRING'])
    year = get_info['year'][0]
    month = get_info['month'][0]
    day = get_info['day'][0]

    weekdayStr = getWeekDay(year,month,day)

    body = '%s年%s月%s日は%s曜日です' % (year,month,day,weekdayStr)

    header =  [("Content-type", "text/html;charset=UTF-8"),("Content-Length",str(len(body)))]
    res(status,header)
    return [body]

def getWeekDay(year,month,day):
    weekdayStr = ""
    weekday = calendar.weekday(int(year),int(month),int(day))
    if weekday == 0:
        return 'Monday'
    elif weekday == 1:
        return 'Thuesday'
    elif weekday == 2:
        return 'Wednesday'
    elif weekday == 3:
        return 'Thursday'
    elif weekday == 4:
        return 'Friday'
    elif weekday == 5:
        return 'Satuaday'
    elif weekday == 6:
        return 'Sunday'

if __name__ == "__main__":
    sv = simple_server.make_server("", 8080, application) #host , port , application
    sv.serve_forever()
