# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1427360613.795
_template_filename='C:\\Users\\Jeremy\\Desktop\\younggo\\code\\mysite\\templates/show/home.html'
_template_uri='/show/home.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = [u'content', u'header', u'head_css']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 10
    ns = runtime.TemplateNamespace('__anon_0x2513cd0', context._clean_inheritance_tokens(), templateuri=u'/header.part', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x2513cd0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2513cd0')._populate(_import_ns, [u'*'])
        dynamic_head = _import_ns.get('dynamic_head', context.get('dynamic_head', UNDEFINED))
        def head_css():
            return render_head_css(context.locals_(__M_locals))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        STATIC_URL = _import_ns.get('STATIC_URL', context.get('STATIC_URL', UNDEFINED))
        def content():
            return render_content(context.locals_(__M_locals))
        def header():
            return render_header(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head_css'):
            context['self'].head_css(**pageargs)
        

        # SOURCE LINE 7
        __M_writer(u'\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        # SOURCE LINE 12
        __M_writer(u'\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 66
        __M_writer(u'\r\n<script type="text/javascript" charset="utf-8">\n</script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2513cd0')._populate(_import_ns, [u'*'])
        def content():
            return render_content(context)
        STATIC_URL = _import_ns.get('STATIC_URL', context.get('STATIC_URL', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 14
        __M_writer(u'\r\n\t<div class="s_bg">\r\n\t\t')
        # SOURCE LINE 16
        runtime._include_file(context, u'/show/home_slide.part', _template_uri)
        __M_writer(u'\r\n\t\t<div class="content_inner">\n\t\t\t<div class="f-clearfix">\r\n\t\t\t\t<div class="h_title">\r\n\t\t\t\t\t<h2>\u6bcf\u65e5\u7279\u60e0</h2>\r\n\t\t\t\t</div>\r\n\t\t\t\t<ul class="goodshot_list f-clearfix">\r\n\t\t\t\t\t<li class="goodshot_item">\r\n\t\t\t\t\t\t<a target="_blank" href="###"><img src="')
        # SOURCE LINE 24
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'images/test.jpg" class="goodshot_img"></a>\r\n\t\t\t\t\t\t<div class="goodshot_bg trans200"></div>\r\n\t\t\t\t\t\t<p class="goodshot_looking trans200">\r\n\t\t\t\t\t\t\t<span class="good_title">\u4e2d\u5927\u72ee</span><br/>\r\n\t\t\t\t\t\t\t<span class="good_intro">\u5409\u7965\u72ee\u8d3a\u65b0\u5e74</span><br/>\r\n\t\t\t\t\t\t\t<span class="good_discount">\u4e70200\u9001100</span>\r\n\t\t\t\t\t\t</p>\r\n\t\t\t\t\t</li>\r\n\t\t\t\t\t<li class="goodshot_item">\r\n\t\t\t\t\t\t<a target="_blank" href="###"><img src="')
        # SOURCE LINE 33
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'images/test.jpg" class="goodshot_img"></a>\r\n\t\t\t\t\t\t<div class="goodshot_bg trans200"></div>\r\n\t\t\t\t\t\t<p class="goodshot_looking trans200">\r\n\t\t\t\t\t\t\t<span class="good_title">\u4e2d\u5927\u72ee</span><br/>\r\n\t\t\t\t\t\t\t<span class="good_intro">\u5409\u7965\u72ee\u8d3a\u65b0\u5e74</span><br/>\r\n\t\t\t\t\t\t\t<span class="good_discount">\u4e70200\u9001100</span>\r\n\t\t\t\t\t\t</p>\r\n\t\t\t\t\t</li>\r\n\t\t\t\t\t<li class="goodshot_item">\r\n\t\t\t\t\t\t<a target="_blank" href="###"><img src="')
        # SOURCE LINE 42
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'images/test.jpg" class="goodshot_img"></a>\r\n\t\t\t\t\t\t<div class="goodshot_bg trans200"></div>\r\n\t\t\t\t\t\t<p class="goodshot_looking trans200">\r\n\t\t\t\t\t\t\t<span class="good_title">\u4e2d\u5927\u72ee</span><br/>\r\n\t\t\t\t\t\t\t<span class="good_intro">\u5409\u7965\u72ee\u8d3a\u65b0\u5e74</span><br/>\r\n\t\t\t\t\t\t\t<span class="good_discount">\u4e70200\u9001100</span>\r\n\t\t\t\t\t\t</p>\r\n\t\t\t\t\t</li>\r\n\t\t\t\t\t<li class="goodshot_item">\r\n\t\t\t\t\t\t<a target="_blank" href="###"><img src="')
        # SOURCE LINE 51
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'images/test.jpg" class="goodshot_img"></a>\r\n\t\t\t\t\t\t<div class="goodshot_bg trans200"></div>\r\n\t\t\t\t\t\t<p class="goodshot_looking trans200">\r\n\t\t\t\t\t\t\t<span class="good_title">\u4e2d\u5927\u72ee</span><br/>\r\n\t\t\t\t\t\t\t<span class="good_intro">\u5409\u7965\u72ee\u8d3a\u65b0\u5e74</span><br/>\r\n\t\t\t\t\t\t\t<span class="good_discount">\u4e70200\u9001100</span>\r\n\t\t\t\t\t\t</p>\r\n\t\t\t\t\t</li>\r\n\t\t\t\t</ul>\r\n\t\t\t\t<div class="goodshot_more">\r\n\t\t\t\t\t<a href="###" target="_blank"><img src="')
        # SOURCE LINE 61
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'images/more.png" alt="\u66f4\u591a\u4f18\u60e0"></a>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\n\t\t</div>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2513cd0')._populate(_import_ns, [u'*'])
        dynamic_head = _import_ns.get('dynamic_head', context.get('dynamic_head', UNDEFINED))
        def header():
            return render_header(context)
        __M_writer = context.writer()
        # SOURCE LINE 9
        __M_writer(u'\r\n\t')
        # SOURCE LINE 10
        __M_writer(u'\r\n\t')
        # SOURCE LINE 11
        __M_writer(unicode(dynamic_head('home')))
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_css(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2513cd0')._populate(_import_ns, [u'*'])
        STATIC_URL = _import_ns.get('STATIC_URL', context.get('STATIC_URL', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def head_css():
            return render_head_css(context)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\r\n\t')
        # SOURCE LINE 4
        __M_writer(unicode(parent.head_css()))
        __M_writer(u'\r\n\t<link rel="stylesheet" href="')
        # SOURCE LINE 5
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/show/slide.css"/>\r\n\t<link rel="stylesheet" href="')
        # SOURCE LINE 6
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/show/index.css" type="text/css" charset="utf-8"/>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


