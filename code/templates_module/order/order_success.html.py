# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1428936774.071
_template_filename='C:\\Users\\Jeremy\\Desktop\\younggo\\code\\mysite\\templates/order/order_success.html'
_template_uri='/order/order_success.html'
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
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context.locals_(__M_locals))
        def header():
            return render_header(context.locals_(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        def head_css():
            return render_head_css(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head_css'):
            context['self'].head_css(**pageargs)
        

        # SOURCE LINE 7
        __M_writer(u'\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        # SOURCE LINE 11
        __M_writer(u'\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 33
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer(u'\r\n<div class="g-bd">\r\n\t<div data-isdaifu="" class="g-row J_ue_position_container\r\n\t" id="J_counter">\r\n\t\t<div class="m-orders-status J_order_info  " data-expire_time="1428937626">\r\n\t\t\t<div class="m-tips">\r\n\t\t\t\t<span class="u-icon tips-icon icon-success"></span>\r\n\t\t\t\t<div class="tips-cnt">\r\n\t\t\t\t\t<p class="tips-text J_ad_AD016wm08">\r\n\t\t\t\t\t\t\u8ba2\u5355\u63d0\u4ea4\u6210\u529f\uff0c\u8bf7\u7b49\u5f85\u5feb\u9012\u9001\u8d27\u4e0a\u95e8\uff01\r\n\t\t\t\t\t</p>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t\t<p class="orders-status-desc">\r\n\t\t\t\t\u53ef\u5728<a href="/order/"><span class="u-highlight J_countdown_container">\u6211\u7684\u8ba2\u5355</span></a>\u67e5\u770b\u8ba2\u5355\u8be6\u60c5\u3002\r\n\t\t\t</p>\r\n\t\t</div>\r\n\t</div>\r\n\t<!-- / .g-row -->\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        # SOURCE LINE 9
        __M_writer(u'\r\n\t')
        # SOURCE LINE 10
        runtime._include_file(context, u'/cute_header.part', _template_uri)
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_css(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
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
        __M_writer(u'css/order/common.css" type="text/css" media="screen" title="no title" charset="utf-8"/>\r\n\t<link rel="stylesheet" href="')
        # SOURCE LINE 6
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/order/success.css" type="text/css" media="screen" title="no title" charset="utf-8"/>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


