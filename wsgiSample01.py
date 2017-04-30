from wsgiref import simple_server

def application(env, res):
    status = "200 OK"
    body = "Hello wsgi application\n"
    header =  [("Content-type", "text/plain"),("Content-Length",str(len(body)))]
    res(status,header)
    return [body]

if __name__ == "__main__":
    sv = simple_server.make_server("", 8080, application) #host , port , application
    sv.serve_forever()
