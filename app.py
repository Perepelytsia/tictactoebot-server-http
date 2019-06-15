import json
import logic

def application(env, start_response):

    choose = 9

    if env['REQUEST_METHOD'] == 'POST':

        # the environment variable CONTENT_LENGTH may be empty or missing
        try:
            request_body_size = int(env.get('CONTENT_LENGTH', 0))
        except (ValueError):
            request_body_size = 0
        
        request_body = env['wsgi.input'].read(request_body_size)
        command = json.loads(request_body)

        if command['cmd'] == 'moveResponse':
            
            handle = open("commands.log", "a")
            handle.write(request_body.decode('utf-8'))
            handle.write("\n")
            handle.close()

            data = command['data']
            choose = logic.do(data)

    choose = str(choose)
    response = '{"cmd":"moveRequest", "owner":"bot", "data":{"choose":'+choose+'}}'

    handle = open("commands.log", "a")
    handle.write(response)
    handle.write("\n")
    handle.close()

    start_response('200 OK', [('Content-Type','application/json')])
    response = response.encode('utf-8')
    return [response]
