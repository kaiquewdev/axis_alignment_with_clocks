'''Axis alignment with clock app'''

from sanic import Sanic
from sanic.response import json

from model import Plan
from model import HorizontalVision
from model import VerticalVision

app = Sanic()

@app.route('/')
async def index(request):
    return json({'version':'0.0.1','name':'axis_alignment_with_clocks'})

@app.route('/plan')
async def plan(request):
    plan = Plan()
    return json({'x':plan.axis('x').position(),'y':plan.axis('y').position(),'axis':plan.axis_count()})

@app.route('/alignment')
async def horizontal_vision(request):
    hv = HorizontalVision()
    vv = VerticalVision()
    return json({'x':[hv.axis('x').position(),vv.axis('x').position()],'y':[hv.axis('x').position(),vv.axis('y').position()],'axis':hv.axis_count()+vv.axis_count()})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
