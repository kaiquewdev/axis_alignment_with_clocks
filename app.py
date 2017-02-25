'''Axis alignment with clock app'''
from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route('/')
async def index(request):
    return json({'version':'0.0.1'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
