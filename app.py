import json

def application(env, start_response):

    if env['REQUEST_METHOD'] == 'POST':

        # the environment variable CONTENT_LENGTH may be empty or missing
        try:
            request_body_size = int(env.get('CONTENT_LENGTH', 0))
        except (ValueError):
            request_body_size = 0
        
        request_body = env['wsgi.input'].read(request_body_size)
        data = json.loads(request_body)
        l = json.dumps(data)
        handle = open("log", "w")
        handle.write(l)
        handle.close()

    start_response('200 OK', [('Content-Type','application/json')])
    test = '{"ret":some}'
    test = test.encode('utf-8')
    return [test]
