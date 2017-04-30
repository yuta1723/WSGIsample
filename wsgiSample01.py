# -*- coding: utf-8 -*-
from wsgiref import simple_server
from cgi import parse_qs

def application(env, res):
    status = "200 OK"
    get_info = parse_qs(env['QUERY_STRING'])
    body = 'year=' + get_info['year'][0] + '<br>'
    body += 'month=' + get_info['month'][0] + '<br>'
    body += 'day=' + get_info['day'][0] + '<br>'
    #body = makeString()
    header =  [("Content-type", "text/html;charset=UTF-8"),("Content-Length",str(len(body)))]
    res(status,header)
    return [body]

def makeString():

    discription = """
    <html><body>
        <table width='300' border='1'>
            <caption>テストテーブル</caption>
            <tr>
                <th>1</th>
                <th>2</th>
                <th>3</th>
            </tr>
            <tr>
                <th>4</th>
                <th>5</th>
                <th>6</th>
            </tr>
            <tr>
                <th>7</th>
                <th>8</th>
                <th>9</th>
            </tr>
        </table>
    </body></html>

    """
    #body = "Hello wsgi application\n"
    print discription
    return discription

if __name__ == "__main__":
    sv = simple_server.make_server("", 8080, application) #host , port , application
    sv.serve_forever()
