# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1426670212.936
_template_filename=u'C:\\Users\\Jeremy\\Desktop\\younggo\\code\\mysite\\templates/base.html'
_template_uri=u'/base.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = [u'head', u'head_css', u'footer', u'content', u'header', u'head_js']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def head():
            return render_head(context.locals_(__M_locals))
        def head_css():
            return render_head_css(context.locals_(__M_locals))
        def footer():
            return render_footer(context.locals_(__M_locals))
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context.locals_(__M_locals))
        def header():
            return render_header(context.locals_(__M_locals))
        def head_js():
            return render_head_js(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html>\r\n<html>\r\n\t<head>\r\n\t    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head'):
            context['self'].head(**pageargs)
        

        # SOURCE LINE 28
        __M_writer(u'\r\n\t</head>\r\n\t\r\n\t<body>\r\n    \t<!--\u9876\u90e8\u5bfc\u822a Start-->\r\n\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        # SOURCE LINE 33
        __M_writer(u'\r\n\t\t<!--\u9876\u90e8\u5bfc\u822a End--> \r\n\t\r\n\t    <!-- \u56fa\u5b9a\u5bbd\u5ea6\u5c45\u4e2d start -->\r\n\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 37
        __M_writer(u'\r\n\t    <!-- \u56fa\u5b9a\u5bbd\u5ea6\u8868\u5355\u5c45\u4e2d end --> \r\n\t\t\r\n\t    ')
        # SOURCE LINE 40
        __M_writer(unicode(self.body()))
        __M_writer(u'\r\n\t\t\r\n\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        # SOURCE LINE 44
        __M_writer(u'\r\n\t</body>\r\n</html>\r\n<script>\r\n\t$(function(){\r\n\t\tvar a = "";\r\n\t})\r\n\t\r\n</script>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def head():
            return render_head(context)
        def head_js():
            return render_head_js(context)
        def head_css():
            return render_head_css(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\r\n\t        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\r\n\t        <title>Younggo</title>\r\n\t        <meta name="description" content=""/>\r\n\t        <meta name="author" content=""/>\r\n\t        <!-- bootstrap css -->\r\n<!-- \t\t\t<link href="')
        # SOURCE LINE 10
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'bootstrap-3.3.2/css/bootstrap.min.css" rel="stylesheet"> -->\r\n\t\t\t<!-- \u5b9a\u5236ccs\t -->\r\n\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head_css'):
            context['self'].head_css(**pageargs)
        

        # SOURCE LINE 16
        __M_writer(u'\r\n \t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head_js'):
            context['self'].head_js(**pageargs)
        

        # SOURCE LINE 23
        __M_writer(u'\t\t\r\n\t        <!-- \u8fd9\u4e2a\u662f\u5168\u5c40\u914d\u7f6e\uff0c\u5982\u679c\u9700\u8981\u5728js\u4e2d\u4f7f\u7528site_url,\u5219\u8fd9\u4e2ajavascript\u7247\u6bb5\u4e00\u5b9a\u8981\u4fdd\u7559 -->\r\n\t        <script type="text/javascript">\r\n\r\n\t\t    </script>\r\n\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_css(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def head_css():
            return render_head_css(context)
        __M_writer = context.writer()
        # SOURCE LINE 12
        __M_writer(u'\r\n\t \t\t\t<link href="')
        # SOURCE LINE 13
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/comm.css" rel="stylesheet">\r\n\t \t\t\t<link href="')
        # SOURCE LINE 14
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/headcom.css" rel="stylesheet">\r\n\t\t\t\t<link href="')
        # SOURCE LINE 15
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/footer.css" rel="stylesheet">\r\n\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        # SOURCE LINE 42
        __M_writer(u'\r\n\t\t\t')
        # SOURCE LINE 43
        runtime._include_file(context, u'/footer.part', _template_uri)
        __M_writer(u'\r\n\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_js(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def head_js():
            return render_head_js(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 17
        __M_writer(u'\r\n\t        <!-- jquery js  -->\r\n\t\t\t\t<script src="')
        # SOURCE LINE 19
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/jquery-1.11.2.min.js" type="text/javascript"></script>\r\n\t<!-- \t        <script src="')
        # SOURCE LINE 20
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'jquery/jquery.json-2.3.min.js"></script> -->\r\n\t\t\t\t<!-- bootstrap js  -->\r\n<!-- \t\t\t\t<script src="')
        # SOURCE LINE 22
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'bootstrap-3.3.2/js/bootstrap.min.js" type="text/javascript"></script> -->\r\n \t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


