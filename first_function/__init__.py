import logging
import azure.functions as func

def main(request: func.HttpRequest):
    logging.info(f'Requested method: {request.method}')

    if request.method == "GET":
        return func.HttpResponse("Hello!")
    elif request.method == "POST":
        
        try:
            name = request.get_json()['name']
        except (ValueError, KeyError):
            return func.HttpResponse("Wrong JSon")
        
        return func.HttpResponse(f'Hello, {name}')