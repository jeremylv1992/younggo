# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1427439946.853
_template_filename='C:\\Users\\Jeremy\\Desktop\\younggo\\code\\mysite\\templates/show/store.html'
_template_uri='/show/store.html'
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
    ns = runtime.TemplateNamespace('__anon_0x26410b0', context._clean_inheritance_tokens(), templateuri=u'/header.part', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x26410b0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x26410b0')._populate(_import_ns, [u'*'])
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
        total = _import_ns.get('total', context.get('total', UNDEFINED))
        store = _import_ns.get('store', context.get('store', UNDEFINED))
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
        _mako_get_namespace(context, '__anon_0x26410b0')._populate(_import_ns, [u'*'])
        def content():
            return render_content(context)
        total = _import_ns.get('total', context.get('total', UNDEFINED))
        store = _import_ns.get('store', context.get('store', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 18
        __M_writer(u'\r\n<div id="list_define">\r\n\t<div class="wrap" id="J_display_wrap">\r\n\t\t<!-- \u54c1\u724c\u5370\u8c61 -->\r\n\t\t<div class="pro-impress clearfix">\r\n\t\t\t<div class="pro-list-fav" id="J_pro_list_fav">\r\n\t\t\t\t<div class="pro-fav-name">\r\n\t\t\t\t\t<p id="store_info" data-val="')
        # SOURCE LINE 25
        __M_writer(unicode(store.id))
        __M_writer(u'">\r\n\t\t\t\t\t\t')
        # SOURCE LINE 26
        __M_writer(unicode(store.name))
        __M_writer(u'\r\n\t\t\t\t\t</p>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t\t<!-- \u591a\u529f\u80fd\u533a @todo-->\r\n\t\t<div class="pro_choose" id="J_fileter_outFrame">\r\n\t\t\t<div id="J_fileter_frame">\r\n\t\t\t\t<!-- \u5206\u7c7b\u533a -->\r\n\t\t\t\t<div class="pro_search">\r\n\t\t\t\t\t<!-- \u66f4\u591aadd .pro-sortbar-show -->\r\n\t\t\t\t\t<dl class="pro-sortbar-all pro-sortbar-category clearfix J-class" style="height: 46px;">\r\n\t\t\t\t\t\t<dt class="pro-sortbar-name">\r\n\t\t\t\t\t\t\t\u5206\u7c7b\uff1a\r\n\t\t\t\t\t\t</dt>\r\n\t\t\t\t\t\t<dd class="pro-sortbar-cnt">\r\n\t\t\t\t\t\t\t<ul class="pro-sortbar-choice J-ctHeight">\r\n\t\t\t\t\t\t\t\t<li>\r\n\t\t\t\t\t\t\t\t\t<a href="/show-382299.html?q=0|0|0|0|0|1" id="J_firstsize_0" mars_sead="te_list_main_sort0" class="pro_selected active">\u5168\u90e8(381) </a>\r\n\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t\t<li>\r\n\t\t\t\t\t\t\t\t\t<a href="/show-382299.html?q=0|280|0|0|0|1" id="J_firstsize_280" mars_sead="te_list_main_sort" class=" J_firstsize">\u767e\u8936\u88d9(268) </a>\r\n\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t</ul>\r\n\t\t\t\t\t\t</dd>\r\n\t\t\t\t\t</dl>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t\t<!-- \u7b5b\u9009\u533a -->\r\n\t\t<div class="pro-list-oper">\r\n\t\t\t<div class="pro-oper">\r\n\t\t\t\t<div class="oper-hd-price">\r\n\t\t\t\t\t<div class="oper-price-tp f-oper-default-secluded">\r\n\t\t\t\t\t\t<a class="J_filter_param" target="_self" href="/show-382299.html?q=0|0|0|0|0|1">\u9ed8\u8ba4</a>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t\t<div class="oper-price-tc ">\r\n\t\t\t\t\t\t<p class="oper-price-txt">\r\n\t\t\t\t\t\t\t\u4ef7\u683c<i class="pop_arrow"></i>\r\n\t\t\t\t\t\t</p>\r\n\t\t\t\t\t\t<div class="oper-price-pop">\r\n\t\t\t\t\t\t\t<p>\r\n\t\t\t\t\t\t\t\t<a class="J_filter_param" target="_self" href="/show-382299.html?q=0|0|0|0|4|1">\u4ef7\u683c\u7531\u9ad8\u5230\u4f4e</a>\r\n\t\t\t\t\t\t\t</p>\r\n\t\t\t\t\t\t\t<p>\r\n\t\t\t\t\t\t\t\t<a class="J_filter_param" target="_self" href="/show-382299.html?q=0|0|0|0|3|1">\u4ef7\u683c\u7531\u4f4e\u5230\u9ad8</a>\r\n\t\t\t\t\t\t\t</p>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t\t<!-- \u7ffb\u9875\u5bfc\u822a\u5de5\u5177\u680f author:eason.chen@vipshop.com -->\r\n\t\t\t<div id="J_page_special" class="page pro-paging">\r\n\t\t\t\t<span class="page-total"><em class="page-nub">')
        # SOURCE LINE 79
        __M_writer(unicode(total))
        __M_writer(u'</em>\u4ef6\u5546\u54c1</span>\r\n\t\t\t\t<span><em class="page-nub">1</em>/1</span>\r\n\t\t\t\t<span class="page-pre">&lt;</span>\r\n\t\t\t\t<a class="page-next-txt" target="_self" mars_sead="te_list_main_head_p1" href="/show-382299.html?q=0|0|0|0|0|2">\u4e0b\u4e00\u9875&gt;</a>\r\n\t\t\t</div>\r\n\t\t</div><!-- \u7b5b\u9009\u533a end -->\r\n\t\t<!-- \u6240\u6709\u5546\u54c1\u533a -->\r\n\t\t<div class="pro_list clearfix">\r\n\t\t</div>\r\n\t\t\r\n\t</div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x26410b0')._populate(_import_ns, [u'*'])
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
        _mako_get_namespace(context, '__anon_0x26410b0')._populate(_import_ns, [u'*'])
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
        __M_writer(u'js/show/store.js" type="text/javascript" charset="utf-8"></script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_css(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x26410b0')._populate(_import_ns, [u'*'])
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
        __M_writer(u'css/show/store.css" type="text/css" media="screen" title="no title" charset="utf-8"/>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


