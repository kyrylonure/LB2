"""from bottle import route, run, request, response
@route('/')
def hello():
    return "Hello world!"

@route('/currency')
def get_currency():
    if 'today' in request.query:
        return "Today exchange rate is 41,5"
    if 'yesterday' in request.query:
        return "Yesterday exchange rate is 41,7"

    return "Unknown query. Suported queries are /currency?today or /currency?yesterday"





if __name__ == '__main__':
    run(port=8000),
"""
    from bottle import route, run, request, response


    @route('/')
    def hello():
        # Отримати значення заголовка Content-Type
        content_type = request.get_header('Content-Type')

        if content_type == 'application/json':
            # Встановити відповідний заголовок Content-Type для JSON
            response.content_type = 'application/json'
            return {"message": "Hello, JSON!"}  # Повертаємо JSON

        elif content_type == 'application/xml':
            # Встановити відповідний заголовок Content-Type для XML
            response.content_type = 'application/xml'
            return """<?xml version="1.0" encoding="UTF-8"?>
    <response>
        <message>Hello, XML!</message>
    </response>"""  # Повертаємо XML

        else:
            # За замовчуванням повертати звичайний текст
            response.content_type = 'text/plain'
            return "Hello, Plain Text!"


    if __name__ == '__main__':
        run(host='localhost', port=8000)
