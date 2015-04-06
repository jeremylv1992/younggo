# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1427452789.659
_template_filename='C:\\Users\\Jeremy\\Desktop\\younggo\\code\\mysite\\templates/show/good.html'
_template_uri='/show/good.html'
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
    ns = runtime.TemplateNamespace('__anon_0x275d470', context._clean_inheritance_tokens(), templateuri=u'/header.part', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x275d470')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x275d470')._populate(_import_ns, [u'*'])
        dynamic_head = _import_ns.get('dynamic_head', context.get('dynamic_head', UNDEFINED))
        good = _import_ns.get('good', context.get('good', UNDEFINED))
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
        _mako_get_namespace(context, '__anon_0x275d470')._populate(_import_ns, [u'*'])
        def content():
            return render_content(context)
        good = _import_ns.get('good', context.get('good', UNDEFINED))
        STATIC_URL = _import_ns.get('STATIC_URL', context.get('STATIC_URL', UNDEFINED))
        store = _import_ns.get('store', context.get('store', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 18
        __M_writer(u'\r\n<div class="FW-wrap fwr">\n\t<div class="FW-product clearfix">\r\n\t\t<!-- \u4ea7\u54c1\u4f4d\u7f6e\u6a21\u5757 -->\r\n\t\t<div class="M-class">\r\n\t\t\t<a href="/show/">\u5546\u57ce&nbsp;&gt;&nbsp;</a><a href="/show/')
        # SOURCE LINE 23
        __M_writer(unicode(store.id))
        __M_writer(u'/">')
        __M_writer(unicode(store.name))
        __M_writer(u'</a>&nbsp;&gt;&nbsp;')
        __M_writer(unicode(good.name))
        __M_writer(u'\r\n\t\t</div>\r\n\t\t<!-- \u4ea7\u54c1\u56fe\u7247\u6a21\u5757 -->\r\n\t\t<div class="M-pic" id="J-mer-ImgReview">\r\n\t\t\t<div class="pic-sliderwrap">\r\n\t\t\t\t<div class="show-midpic hidden" style="display: block;">\r\n\t\t\t\t\t<a href="')
        # SOURCE LINE 29
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'images/640" class="J-mer-bigImgZoom" rel="undefined" title="" style="outline-style: none; text-decoration: none;">\r\n\t\t\t\t\t<div class="zoomPad">\r\n\t\t\t\t\t\t<img src="')
        # SOURCE LINE 31
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'images/640" width="383" height="483" alt="" title="" style="opacity: 1;">\r\n\t\t\t\t\t\t<div class="zoomWindow" style="position: absolute; z-index: 5001; cursor: default; left: 0px; top: 0px; display: none;">\r\n\t\t\t\t\t\t\t<div class="zoomWrapper" style="border-width: 1px; width: 383px; cursor: crosshair;">\r\n\t\t\t\t\t\t\t\t<div class="zoomWrapperTitle" style="width: 100%; position: absolute; display: none;"></div>\r\n\t\t\t\t\t\t\t\t<div class="zoomWrapperImage" style="width: 100%; height: 483px;">\r\n\t\t\t\t\t\t\t\t\t<img src="')
        # SOURCE LINE 36
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'images/640" style="position: absolute; border: 0px; display: block; left: 0px; top: -168.354037267081px;">\r\n\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t</div> </a>\r\n\t\t\t\t\t<em class="icon-a"></em>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t\t<div class="pic-slider" id="J-sImgSlide-wrap">\r\n\t\t\t\t<span class="pic-slider-up switchable-first" id="J-slider-lef" mars_sead="m_te_goods_buy_next"> <em class="arrow-out"><em class="arrow-in"></em></em> </span>\r\n\t\t\t\t<div class="pic-slider-list">\r\n\t\t\t\t\t<div id="J-sImg-wrap" style="width: 390px; margin-left: 0px;">\r\n\t\t\t\t\t\t<div class="pic-slider-items J-picSlider-items" mars_sead="m_te_goods_buy_pic6_img">\r\n\t\t\t\t\t\t\t<img src="')
        # SOURCE LINE 49
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'images/640" width="57" height="73" alt="" class="J-mer-smallImg">\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t\t<span class="pic-slider-down" id="J-slider-rig" mars_sead="m_te_goods_buy_next"> <em class="arrow-out"><em class="arrow-in"></em></em> </span>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t\t<!-- \u4ea7\u54c1\u56fe\u7247\u6a21\u5757 end -->\r\n\t\t<!-- \u4ea7\u54c1\u4fe1\u606f\u6a21\u5757 -->\r\n\t\t<div class="M-productInfo">\r\n\t\t\t<div class="pi-title-box clearfix">\r\n\t\t\t\t<div class="pib-title">\r\n\t\t\t\t\t<p class="pib-title-class">\r\n\t\t\t\t\t\t<a href="/show/')
        # SOURCE LINE 62
        __M_writer(unicode(store.id))
        __M_writer(u'/" target="_blank">')
        __M_writer(unicode(store.name))
        __M_writer(u' </a>\r\n\t\t\t\t\t</p>\r\n\t\t\t\t\t<p class="pib-title-detail">\r\n\t\t\t\t\t\t')
        # SOURCE LINE 65
        __M_writer(unicode(good.name))
        __M_writer(u'\r\n\t\t\t\t\t</p>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t\t<div class="pi-price-box">\r\n\t\t\t\t<span class="pbox-price"><i class="pbox-yen">\xa5</i><em>')
        # SOURCE LINE 70
        __M_writer(unicode(good.min_price))
        __M_writer(u'</em></span>\r\n\t\t\t</div>\r\n\t\t\t<div class="pi-attr-box" id="J-proData-box">\r\n\t\t\t\t<form id="J-cartAdd-frm" class="cartAdd-form" method="post" action="http://cart.vip.com/te2/add.php">\r\n\t\t\t\t\t<dl class="color">\r\n\t\t\t\t\t\t<dt class="color-name">\r\n\t\t\t\t\t\t\t\u989c\u8272\uff1a\r\n\t\t\t\t\t\t</dt>\r\n\t\t\t\t\t\t<dd class="color-list">\r\n\t\t\t\t\t\t\t<ul>\r\n\t\t\t\t\t\t\t\t<li class="color-list-item">\r\n\t\t\t\t\t\t\t\t\t<a id="J-colorItem-50551455" href="/detail-385812-50551455.html" title="\u9ed1\u8272\u7ffb\u9886\u4f11\u95f2\u77ed\u8896T\u6064" class=""> <img class="fl" src="http://a.vpimg3.com/upload/merchandise/385812/H-7132217030099-1_2.jpg" data-original="http://a.vpimg3.com/upload/merchandise/385812/H-7132217030099-1_2.jpg" width="34" height="43" alt="\u9ed1\u8272\u7ffb\u9886\u4f11\u95f2\u77ed\u8896T\u6064" mars_sead="m_te_goods_buy_color_check" style="display: block;"> <span class="i-select"></span></a>\r\n\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t</ul>\r\n\t\t\t\t\t\t</dd>\r\n\t\t\t\t\t</dl>\r\n\t\t\t\t\t<dl class="i-size clearfix J-sizeArea-wrap " id="J-sizeArea-wrap">\r\n\t\t\t\t\t\t<dt class="size-name">\r\n\t\t\t\t\t\t\t\u5c3a\u7801\uff1a\r\n\t\t\t\t\t\t</dt>\r\n\t\t\t\t\t\t<dd class="size-list">\r\n\t\t\t\t\t\t\t<ul>\r\n\t\t\t\t\t\t\t\t<li class="size-list-item J-sizeID" id="J-cartAdd-sizeID-130616012" data-size-name="56" data-hover="size-list-item-hover" data-id="130616012" mars_sead="m_te_goods_buy_size_check" style="z-index: 1;">\r\n\t\t\t\t\t\t\t\t\t<span class="size-list-item-name">56</span>\r\n\t\t\t\t\t\t\t\t\t<span class="i-select"></span>\r\n\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t</ul>\r\n\t\t\t\t\t\t</dd>\r\n\t\t\t\t\t</dl>\r\n\t\t\t\t\t<dl class="i-num clearfix" id="J-num-select">\r\n\t\t\t\t\t\t<dt class="num-name">\r\n\t\t\t\t\t\t\t\u6570\u91cf\uff1a\r\n\t\t\t\t\t\t</dt>\r\n\t\t\t\t\t\t<dd class="i-notice-msg J-num-tips"></dd>\r\n\t\t\t\t\t\t<dd class="num-box">\r\n\t\t\t\t\t\t\t<span class="num-reduce num-reduce-disabled J-num-act-reduce"></span>\r\n\t\t\t\t\t\t\t<em class="num-input J-pro-num-txt">1</em>\r\n\t\t\t\t\t\t\t<span class="num-add J-num-act-add"></span>\r\n\t\t\t\t\t\t</dd>\r\n\t\t\t\t\t\t<dd class="num-msg hidden" id="J-proStock-type"></dd>\r\n\t\t\t\t\t</dl>\r\n\t\t\t\t\t<div class="i-button clearfix">\r\n\t\t\t\t\t\t<div id="J-button-box" class="button-box">\r\n\t\t\t\t\t\t\t<!-- loading\u72b6\u6001\u52a0 .z-ui-btn-loading -->\r\n\t\t\t\t\t\t\t<a href="javascript:;" class="ui-btn-large ui-btn-primary ui-btn-loading" id="J-cartAdd-submit"> \r\n\t\t\t\t\t\t\t\t<span class="ui-btn-loading-before">\u52a0\u5165\u8d2d\u7269\u888b </span> \r\n\t\t\t\t\t\t\t\t<span class="ui-btn-loading-after"><span class="ui-btn-txt"></span> </span> \r\n\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</form>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t\t<div class="f-clearfix"></div>\r\n\t</div>\r\n\t\r\n\t<!-- \u5546\u54c1\u8be6\u60c5 -->\r\n\t<div id="J-FW-detail" class="FW-detail J-data-module">\r\n\t\t<div class="M-detail">\r\n\t\t\t<!-- \u7ec8\u7aef\u9875\u6a21\u5757\u5bfc\u822a -->\r\n\t\t\t<div class="M-detailTop" id="J-topbar">\r\n\t\t\t\t<ul class="dt-list">\r\n\t\t\t\t\t<li>\r\n\t\t\t\t\t\t<a href="javascript:void(0);" class="dt-list-item J-topbar-tabs" >\u5546\u54c1\u8be6\u60c5</a>\r\n\t\t\t\t\t</li>\r\n\t\t\t\t</ul>\r\n\t\t\t</div>\r\n\t\t\t<div class="M-detailCon">\r\n\t\t\t\t<!-- \u5546\u54c1\u5c3a\u7801(\u65b0) -->\r\n\t\t\t\t\u5546\u5bb6\u81ea\u5df1\u7f16\u8f91\u3002\u3002\u3002\u3002\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t</div>\r\n</div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x275d470')._populate(_import_ns, [u'*'])
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
        _mako_get_namespace(context, '__anon_0x275d470')._populate(_import_ns, [u'*'])
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
        __M_writer(u'js/show/good.js" type="text/javascript" charset="utf-8"></script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_css(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x275d470')._populate(_import_ns, [u'*'])
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
        __M_writer(u'css/show/good.css" type="text/css" media="screen" title="no title" charset="utf-8"/>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


