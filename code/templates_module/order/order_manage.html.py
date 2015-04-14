# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1428939340.761
_template_filename='C:\\Users\\Jeremy\\Desktop\\younggo\\code\\mysite\\templates/order/order_manage.html'
_template_uri='/order/order_manage.html'
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
        def head_css():
            return render_head_css(context.locals_(__M_locals))
        parent = context.get('parent', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context.locals_(__M_locals))
        def header():
            return render_header(context.locals_(__M_locals))
        orders = context.get('orders', UNDEFINED)
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
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        orders = context.get('orders', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer(u'\r\n<div class="g-wrap clearfix">\r\n\t<div class="g-content">\r\n\t\t<div class="g-container">\r\n\t\t\t<div id="J_order_list">\r\n\t\t\t\t<table class="m-table">\r\n\t\t\t\t\t<colgroup>\r\n\t\t\t\t\t\t<col class="c1">\r\n\t\t\t\t\t\t<col class="c2">\r\n\t\t\t\t\t\t<col class="c3">\r\n\t\t\t\t\t\t<col class="c4">\r\n\t\t\t\t\t\t<col class="c5">\r\n\t\t\t\t\t</colgroup>\r\n\t\t\t\t\t<thead>\r\n\t\t\t\t\t\t<tr class="col-name">\r\n\t\t\t\t\t\t\t<th>\u5546\u54c1</th>\r\n\t\t\t\t\t\t\t<th>\u8ba2\u5355\u603b\u989d</th>\r\n\t\t\t\t\t\t\t<th></th>\r\n\t\t\t\t\t\t\t<th>\u64cd\u4f5c</th>\r\n\t\t\t\t\t\t\t<th>\u5176\u4ed6\u64cd\u4f5c</th>\r\n\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t</thead>\r\n')
        # SOURCE LINE 35
        for order in orders:
            # SOURCE LINE 36
            __M_writer(u'\t\t\t\t\t<tbody data-receiver="\u5415\u6cfd\u7acb">\r\n\t\t\t\t\t\t<tr class="order-hd">\r\n\t\t\t\t\t\t\t<td colspan="5"><i class="">&nbsp;</i><span class="num">\u8ba2\u5355\u53f7\uff1a')
            # SOURCE LINE 38
            __M_writer(unicode(order.id))
            __M_writer(u'<em class="type">&nbsp;&nbsp;</em></span><span class="recipients">\u6536\u8d27\u4eba\uff1a')
            __M_writer(unicode(order.customer))
            __M_writer(u'</span><span class="num">\u4e0b\u5355\u65f6\u95f4\uff1a')
            __M_writer(unicode(order.time))
            __M_writer(u'</span><!-- \u83b7\u5f97\u7684\u552f\u54c1\u5e01\u5927\u4e8e\u96f6\uff0c\u5c55\u793a\u552f\u54c1\u5e01\u6570\u76ee --></td>\r\n\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t')
            # SOURCE LINE 40
 
            first_item = True 
            count = order.order_items.all().count()
                                                            
            
            # SOURCE LINE 43
            __M_writer(u'\r\n')
            # SOURCE LINE 44
            for item in order.order_items.all():
                # SOURCE LINE 45
                __M_writer(u'\t\t\t\t\t\t<tr class="order-bd">\r\n\t\t\t\t\t\t\t<!--\u7b2c\u4e00\u4e2a\u8d27\u54c1\u4fe1\u606f\u5f00\u59cb\u8bfb  \u552f\u95ea\u4e0d\u80fd\u6253\u5f00\u94fe\u63a5-->\r\n\t\t\t\t\t\t\t<td class="goods"><a href="/')
                # SOURCE LINE 47
                __M_writer(unicode(item.good.store.id))
                __M_writer(u'/')
                __M_writer(unicode(item.good.id))
                __M_writer(u'/" target="_blank" class="pic"><img src="')
                __M_writer(unicode(STATIC_URL))
                __M_writer(u'images/640" width="50" height="63" alt=""></a>\r\n\t\t\t\t\t\t\t<div class="goods-info">\r\n\t\t\t\t\t\t\t\t<a href="/')
                # SOURCE LINE 49
                __M_writer(unicode(item.good.store.id))
                __M_writer(u'/')
                __M_writer(unicode(item.good.id))
                __M_writer(u'/" target="_blank" class="name">')
                __M_writer(unicode(item.good.name))
                __M_writer(u'</a>\r\n\t\t\t\t\t\t\t\t<span class="size">')
                # SOURCE LINE 50
                __M_writer(unicode(item.options))
                __M_writer(u'</span>\r\n\t\t\t\t\t\t\t</div></td>\r\n\t\t\t\t\t\t\t<!--\u7b2c\u4e00\u4e2a\u8d27\u54c1\u4fe1\u606f\u5f00\u59cb\u8bfb  \u7ed3\u675f-->\r\n')
                # SOURCE LINE 53
                if first_item:
                    # SOURCE LINE 54
                    __M_writer(u'\t\t\t\t\t\t\t<td class="price" rowspan="')
                    __M_writer(unicode(count))
                    __M_writer(u'">\r\n\t\t\t\t\t\t\t<p>\r\n\t\t\t\t\t\t\t\t<strong>\xa5')
                    # SOURCE LINE 56
                    __M_writer(unicode(order.total_fare))
                    __M_writer(u'</strong>\r\n\t\t\t\t\t\t\t</p></td>\r\n\t\t\t\t\t\t\t<td class="state" rowspan="')
                    # SOURCE LINE 58
                    __M_writer(unicode(count))
                    __M_writer(u'">\r\n\t\t\t\t\t\t\t<p class="purple">\r\n\t\t\t\t\t\t\t\t<span style="color:red">\u672a\u7b7e\u6536</span>\r\n\t\t\t\t\t\t\t</p><!-- \u5224\u65ad\u662f\u5426\u5c55\u793a\u8ba2\u5355\u7269\u6d41\u4fe1\u606f --><!-- \u5224\u65ad\u662f\u5426\u5c55\u793a\u8ba2\u5355\u7269\u6d41\u4fe1\u606f \u7ed3\u675f--><a href="###" target="_blank" mars_sead="account_order_detail_btn">\u8ba2\u5355\u8be6\u60c5</a></td>\r\n\t\t\t\t\t\t\t<!-- \u83dc\u5355\u8ba2\u5355\u4fe1\u606f -->\r\n\t\t\t\t\t\t\t<td class="control" rowspan="')
                    # SOURCE LINE 63
                    __M_writer(unicode(count))
                    __M_writer(u'">\r\n\t\t\t\t\t\t\t<p>\r\n\t\t\t\t\t\t\t\t<a href="javascript:;" role="button" mars_sead="account_order_secondpay_btn" class="ui-btn-mini ui-btn1 J_pay">\u7b7e\u6536</a>\r\n\t\t\t\t\t\t\t</p></td>\r\n\t\t\t\t\t\t\t<td class="other" rowspan="')
                    # SOURCE LINE 67
                    __M_writer(unicode(count))
                    __M_writer(u'">\r\n\t\t\t\t\t\t\t<p>\r\n\t\t\t\t\t\t\t\t<a class="J_cancel" role="button" mars_sead="account_order_cancel_btn" href="javascript:;">\u53d6\u6d88\u8ba2\u5355</a>\r\n\t\t\t\t\t\t\t</p></td>\r\n\t\t\t\t\t\t\t<!-- \u83dc\u5355\u8ba2\u5355\u4fe1\u606f  \u7ed3\u675f-->\r\n')
                    pass
                # SOURCE LINE 73
                __M_writer(u'\t\t\t\t\t\t\t')
                first_item = False 
                
                __M_writer(u'\r\n\t\t\t\t\t\t</tr>\r\n')
                pass
            # SOURCE LINE 76
            __M_writer(u'\t\t\t\t\t</tbody>\r\n')
            pass
        # SOURCE LINE 78
        __M_writer(u'\t\t\t\t</table>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t</div>\r\n\t\t\r\n</div>\r\n')
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
        __M_writer(u'css/order/common2.css" type="text/css" media="screen" title="no title" charset="utf-8"/>\r\n\t<link rel="stylesheet" href="')
        # SOURCE LINE 6
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/order/order_list.css" type="text/css" media="screen" title="no title" charset="utf-8"/>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


