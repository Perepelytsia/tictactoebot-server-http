import json
import logic
import psycopg2

def application(env, start_response):

    conn = psycopg2.connect(dbname='tictactoe', user='tictactoe', password='tictactoe', host='localhost')
    cursor = conn.cursor()
    choose = 9

    if env['REQUEST_METHOD'] == 'POST':

        # the environment variable CONTENT_LENGTH may be empty or missing
        try:
            request_body_size = int(env.get('CONTENT_LENGTH', 0))
        except (ValueError):
            request_body_size = 0
        
        request_body = env['wsgi.input'].read(request_body_size)
        command = json.loads(request_body)

        if command['cmd'] == 'state':
            
            handle = open("commands.log", "a")
            handle.write(request_body.decode('utf-8'))
            handle.write("\n")
            handle.close()

            postgres_insert_query = """ INSERT INTO commands (type, cmd, owner, data) VALUES (%s,%s,%s,%s)"""
            record_to_insert = ('req', command['cmd'], command['owner'], json.dumps(command['data']))
            cursor.execute(postgres_insert_query, record_to_insert)
            conn.commit()

            data = command['data']
            choose = logic.do(data)

    data = {"choose":choose}
    command = {"cmd":"move", "owner":"bot", "data":data}

    postgres_insert_query = """ INSERT INTO commands (type, cmd, owner, data) VALUES (%s,%s,%s,%s)"""
    record_to_insert = ('res', command['cmd'], command['owner'], json.dumps(command['data']))
    cursor.execute(postgres_insert_query, record_to_insert)
    conn.commit()

    response = json.dumps(command)

    handle = open("commands.log", "a")
    handle.write(response)
    handle.write("\n")
    handle.close()

    start_response('200 OK', [('Content-Type','application/json')])
    response = response.encode('utf-8')
    return [response]
