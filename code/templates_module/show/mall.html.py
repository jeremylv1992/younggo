# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1427374200.994
_template_filename='C:\\Users\\Jeremy\\Desktop\\younggo\\code\\mysite\\templates/show/mall.html'
_template_uri='/show/mall.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = [u'content', u'header', u'head_js', u'head_css']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 14
    ns = runtime.TemplateNamespace('__anon_0x26bff70', context._clean_inheritance_tokens(), templateuri=u'/header.part', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x26bff70')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x26bff70')._populate(_import_ns, [u'*'])
        dynamic_head = _import_ns.get('dynamic_head', context.get('dynamic_head', UNDEFINED))
        def head_css():
            return render_head_css(context.locals_(__M_locals))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        STATIC_URL = _import_ns.get('STATIC_URL', context.get('STATIC_URL', UNDEFINED))
        def content():
            return render_content(context.locals_(__M_locals))
        def header():
            return render_header(context.locals_(__M_locals))
        def head_js():
            return render_head_js(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head_css'):
            context['self'].head_css(**pageargs)
        

        # SOURCE LINE 6
        __M_writer(u'\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head_js'):
            context['self'].head_js(**pageargs)
        

        # SOURCE LINE 11
        __M_writer(u'\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        # SOURCE LINE 16
        __M_writer(u'\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x26bff70')._populate(_import_ns, [u'*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 18
        __M_writer(u'\r\n<div class="hys_wrapper">\r\n\t<div class="hys_box">\r\n\t\t<div class="act-brand-list hys_list">\r\n\t\t\t<ul class="">\r\n\t\t\t</ul>\r\n\t\t</div>\r\n\t</div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x26bff70')._populate(_import_ns, [u'*'])
        dynamic_head = _import_ns.get('dynamic_head', context.get('dynamic_head', UNDEFINED))
        def header():
            return render_header(context)
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer(u'\r\n\t')
        # SOURCE LINE 14
        __M_writer(u'\r\n\t')
        # SOURCE LINE 15
        __M_writer(unicode(dynamic_head('mall')))
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_js(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x26bff70')._populate(_import_ns, [u'*'])
        def head_js():
            return render_head_js(context)
        STATIC_URL = _import_ns.get('STATIC_URL', context.get('STATIC_URL', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 8
        __M_writer(u'\r\n\t')
        # SOURCE LINE 9
        __M_writer(unicode(parent.head_js()))
        __M_writer(u'\r\n\t<script src="')
        # SOURCE LINE 10
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/show/mall.js" type="text/javascript" charset="utf-8"></script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_css(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x26bff70')._populate(_import_ns, [u'*'])
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
        __M_writer(u'css/show/mall.css" type="text/css" media="screen" title="no title" charset="utf-8"/>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


