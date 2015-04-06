# coding=utf-8
from django.http import HttpResponse
from django_websocket import accept_websocket,require_websocket
from common.mymako import render_mako_context

def modify_message(message):
    return message.lower()

@require_websocket
def lower_case(request):
    if not request.is_websocket():
        message = request.GET['message']
        message = modify_message(message)
        return HttpResponse(message)
    else:
        for message in request.websocket:
            message = modify_message(message)
            request.websocket.send(message)
            
def test_page(request):
    return render_mako_context(request, 'test.html', {})
            