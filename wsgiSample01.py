from wsgiref import simple_server

def application(env, res):
    status = "200 OK"
    header =  [("Content-type", "text/plain")]
    res(status,header)
    return ["Hello wsgi application\n"]

if __name__ == "__main__":
    sv = simple_server.make_server("", 8080, application) #host , port , application
    sv.serve_forever()
