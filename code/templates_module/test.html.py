# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1428147731.671
_template_filename='C:\\Users\\Jeremy\\Desktop\\younggo\\code\\mysite\\templates/test.html'
_template_uri='test.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\r\n\t<head>\n\t  <meta http-equiv="Content-type" content="text/html; charset=utf-8"/>\n\t  <title>websocket</title>\r\n\t  <script src="')
        # SOURCE LINE 5
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/jquery-1.11.2.min.js" type="text/javascript" charset="utf-8"></script>\n\t</head>\r\n\t<body id="test" onload="">\n\t\t<input type="text" name="msg" value="" id="msg"/>\n\t\t<button id="send">\u53d1\u9001</button>\r\n\t\t<textarea name="reply" rows="8" cols="40"></textarea>\r\n\t</body>\t\r\n\t<script type="text/javascript" charset="utf-8">\n\t\tvar ws = new WebSocket("ws://localhost:8000/websocket/lower_case/");\r\n\t\t$("#send").click(function(){\r\n\t\t\tvar msg = $("#msg").val();\r\n\t\t\t// ws.send(msg);\r\n\t\t\tvar url = \'/websocket/lower_case/\';\r\n\t\t\t$.get(url,{message:msg},function(res){\r\n\t\t\t\tconsole.log(res);\r\n\t\t\t})\r\n\t\t})\n\t</script>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


