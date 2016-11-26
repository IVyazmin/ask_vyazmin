#def application(environ, start_response):
#    status = '200 OK'
#    response_headers = [('Content-type', 'text/plain')]
#    start_response(status, response_headers)
#    return ['Hello world!\n']


from pprint import pformat
from cgi import parse_qsl, escape

def application(environ, start_response):
    output = b'<p>Hello World!</p>'

    output += 'Post:'
    output+= '<form method="post">'
    output+= '<input type="text" name = "test">'
    output+= '<input type="submit" value="Send">'
    output+= '</form>'

    d = parse_qsl(environ['QUERY_STRING'])
    if environ['REQUEST_METHOD'] == 'POST':
        output+= '<h1>Post  data:</h1>'
        output += (pformat(environ['wsgi.input'].read()))

    if environ['REQUEST_METHOD'] == 'GET':
        if environ['QUERY_STRING'] != '':
            output+= '<h1>Get data:</h1>'
            for ch in d:
                output+= ' = '.join(ch)
                output+= '<br>'

    
    start_response('200 OK', [('Content-type', 'text/html')])
    return output