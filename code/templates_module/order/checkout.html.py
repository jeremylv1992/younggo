# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1428857484.688
_template_filename='C:\\Users\\Jeremy\\Desktop\\younggo\\code\\mysite\\templates/order/checkout.html'
_template_uri='/order/checkout.html'
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
        items = context.get('items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        

        # SOURCE LINE 8
        __M_writer(u'\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head_js'):
            context['self'].head_js(**pageargs)
        

        # SOURCE LINE 13
        __M_writer(u'\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        # SOURCE LINE 17
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
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 19
        __M_writer(u'\r\n')
        # SOURCE LINE 20

        groups = {}
        for _i in items:
                if _i.good.store.id not in groups.keys():
                        groups[_i.good.store.id] = [_i.good.store, []]
                groups[_i.good.store.id][1].append(_i)  
        
        
        # SOURCE LINE 26
        __M_writer(u'\r\n<div class="g-bd">\r\n\t<div class="g-row J_ue_position_container">\r\n\t\t<div class="m-ad page-top-ad f-hide" id="J_comm_ad">\r\n\t\t\t<p class="ad-text J_ad_text"></p>\r\n\t\t</div>\r\n\t\t<div class="m-flow-steps z-flow-steps-confirm J_flow_steps">\r\n\t\t\t<i class="flow-steps-bg"></i>\r\n\t\t\t<ul class="m-inline-block">\r\n\t\t\t\t<li class="inline-block-item flow-step flow-step-cart">\r\n\t\t\t\t\t<span class="flow-step-text">\u67e5\u770b\u8d2d\u7269\u888b</span>\r\n\t\t\t\t</li>\r\n\t\t\t\t<li class="inline-block-item flow-step flow-step-confirm">\r\n\t\t\t\t\t<span class="flow-step-text">\u786e\u8ba4\u8ba2\u5355\u4fe1\u606f</span>\r\n\t\t\t\t</li>\r\n\t\t\t\t<li class="inline-block-item flow-step flow-step-submit">\r\n\t\t\t\t\t<span class="flow-step-text">\u6210\u529f\u63d0\u4ea4\u8ba2\u5355</span>\r\n\t\t\t\t</li>\r\n\t\t\t</ul>\r\n\t\t</div>\r\n\t\t<div class="m-inline-block channel-tips">\r\n\t\t\t<h2 class="inline-block-item channel-tips-title">\u786e\u8ba4\u8ba2\u5355\u4fe1\u606f</h2>\r\n\t\t</div>\r\n\t\t<div class="m-box address-box z-address-box-initialize-success z-address-box-old-customers" id="J_address_module">\r\n\t\t\t<div class="box-hd">\r\n\t\t\t\t<h2 class="box-hd-title">\u6536\u8d27\u4fe1\u606f</h2>\r\n\t\t\t</div>\r\n\t\t\t<div class="box-bd">\r\n\t\t\t\t<div class="address-box-cnt address-box-cnt-initialize-success">\r\n\t\t\t\t\t<div class="address-list-wrapper J_address_list_wrapper z-address-lt-3">\r\n\t\t\t\t\t\t<div class="m-address">\r\n\t\t\t\t\t\t\t<ul class="m-inline-block address-list my_address_list">\r\n\t\t\t\t\t\t\t\t<li class="inline-block-item address-item address-item-add address_item_container " data-hover="address-item-add-hover" data-touch="z-touch">\r\n\t\t\t\t\t\t\t\t\t<div class="address-inner">\r\n\t\t\t\t\t\t\t\t\t\t<a class="add-address address_add_btn J_fake_a" href="###" mars_sead="address_new_radio"> <span class="u-icon icon-address-add"></span>\r\n\t\t\t\t\t\t\t\t\t\t<p>\r\n\t\t\t\t\t\t\t\t\t\t\t\u6dfb\u52a0\u5730\u5740\r\n\t\t\t\t\t\t\t\t\t\t</p> </a>\r\n\t\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t</ul>\r\n\t\t\t\t\t\t</div><!-- / .m-address -->\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t</div><!-- / .box-bd -->\r\n\t\t</div>\r\n\t\t<div class="m-box payment-box co_payment z-payment-box-initialize-success" id="paymentTabModule">\r\n\t\t\t<div class="box-hd">\r\n\t\t\t\t<h2 class="box-hd-title">\u652f\u4ed8\u65b9\u5f0f</h2>\r\n\t\t\t\t<p class="u-ad-text payment-box-hd-ad-text J_ad_AD14">\r\n\t\t\t\t\t*&nbsp;\u76ee\u524d\u4ec5\u652f\u6301\u8d27\u5230\u4ed8\u6b3e\r\n\t\t\t\t</p>\r\n\t\t\t</div>\r\n\t\t\t<div class="box-bd">\r\n\t\t\t\t<div class="payment-box-cnt payment-box-cnt-initialize-success">\r\n\t\t\t\t\t<div id="J_payment_module_new" class="payment-container">\r\n\t\t\t\t\t\t<div class="m-payment-type">\r\n\t\t\t\t\t\t\t<div class="payment-type-item J_cod_method_item">\r\n\t\t\t\t\t\t\t\t<div class="radio-item J_cod_method_radio_item" mars_sead="payment_cod_radio">\r\n\t\t\t\t\t\t\t\t\t<div class="m-radio z-radio-checked">\r\n\t\t\t\t\t\t\t\t\t\t<div class="u-radio">\r\n\t\t\t\t\t\t\t\t\t\t\t<input type="radio" id="J_cod_method_radio" name="pay_type_radio" simulate="done">\r\n\t\t\t\t\t\t\t\t\t\t\t<label class="simulate" for="J_cod_method_radio">\u8d27\u5230\u4ed8\u6b3e</label>\r\n\t\t\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t\t\t<label for="J_cod_method_radio" class="radio-text">\u8d27\u5230\u4ed8\u6b3e</label>\r\n\t\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t\t<p class="payment-desc">\r\n\t\t\t\t\t\t\t\t\t\t<span class="J_ad_AD015wm15">\u9001\u8d27\u4e0a\u95e8\u540e\u518d\u4ed8\u6b3e\u3002</span>\r\n\t\t\t\t\t\t\t\t\t</p>\r\n\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t</div><!-- / .payment-container -->\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t</div><!-- / .m-box -->\r\n\t\t<div class="m-box order-info-box z-order-info-box-initialize-success" id="J_order_info_module">\r\n\t\t\t<div class="box-hd">\r\n\t\t\t\t<h2 class="box-hd-title">\u8ba2\u5355\u5546\u54c1\u4fe1\u606f</h2>\r\n\t\t\t</div>\r\n\t\t\t<div class="box-bd">\r\n\t\t\t\t<div class="order-info-wrapper">\r\n\t\t\t\t\t')
        # SOURCE LINE 108

        total = 0
        trans_fare = 0
                                                
        
        # SOURCE LINE 111
        __M_writer(u'\r\n')
        # SOURCE LINE 112
        for group in groups.values():
            # SOURCE LINE 113
            __M_writer(u'\t\t\t\t\t<table class="u-table order-info-table vip-order-info-table" id="J_info_table">\r\n\t\t\t\t\t\t')
            # SOURCE LINE 114
        
            sub_total = 0 
            sub_trans_fare = 10
                                                            
            
            # SOURCE LINE 117
            __M_writer(u'\r\n\t\t\t\t\t\t<thead>\r\n\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t<th colspan="2" class="product-item">\r\n\t\t\t\t\t\t\t\t<div class="product-item-inner">\r\n\t\t\t\t\t\t\t\t\t<em>')
            # SOURCE LINE 122
            __M_writer(unicode(group[0].name))
            __M_writer(u'</em>\u53d1\u8d27\u8ba2\u5355\r\n\t\t\t\t\t\t\t\t</div></th>\r\n\t\t\t\t\t\t\t\t<th class="price-item">\u5355\u4ef7</th>\r\n\t\t\t\t\t\t\t\t<th class="quantity-item">\u6570\u91cf</th>\r\n\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t</thead>\r\n\t\t\t\t\t\t<tbody>\r\n')
            # SOURCE LINE 129
            for item in group[1]:
                # SOURCE LINE 130
                __M_writer(u'\t\t\t\t\t\t\t<tr class="product-row table-last-row">\r\n\t\t\t\t\t\t\t\t<td class="product-item">\r\n\t\t\t\t\t\t\t\t<p class="product-item-text" title="')
                # SOURCE LINE 132
                __M_writer(unicode(item.good.name))
                __M_writer(u'">\r\n\t\t\t\t\t\t\t\t\t')
                # SOURCE LINE 133
                __M_writer(unicode(item.good.name))
                __M_writer(u'\r\n\t\t\t\t\t\t\t\t</p><p class="product-item-notice"></p></td>\r\n\t\t\t\t\t\t\t\t<td class="size-item "> ')
                # SOURCE LINE 135
                __M_writer(unicode(item.options))
                __M_writer(u' </td>\r\n\t\t\t\t\t\t\t\t<td class="price-item"><span class="m-price"> <span class="u-yen">\xa5</span><span class="u-price">')
                # SOURCE LINE 136
                __M_writer(unicode(item.unit_price))
                __M_writer(u'</span> </span></td>\r\n\t\t\t\t\t\t\t\t<td class="quantity-item">')
                # SOURCE LINE 137
                __M_writer(unicode(item.amount))
                __M_writer(u'</td>\r\n\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t')
                # SOURCE LINE 139
                sub_total += item.unit_price*item.amount 
                
                __M_writer(u'\r\n')
                pass
            # SOURCE LINE 141
            __M_writer(u'\t\t\t\t\t\t</tbody>\r\n\t\t\t\t\t\t<tfoot>\r\n\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t<td colspan="4">\r\n\t\t\t\t\t\t\t\t<div class="inner">\r\n\t\t\t\t\t\t\t\t\t<div class=" shipping-costs J_sum_items" data-hover="shipping-costs-hover" data-touch="z-touch">\r\n\t\t\t\t\t\t\t\t\t\t<span class="tooltips-trigger-text"> \u8fd0\u8d39\uff1a \r\n\t\t\t\t\t\t\t\t\t\t\t<span class="">\r\n\t\t\t\t\t\t\t\t\t\t\t\t<span class="m-price"> \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t<span class="u-yen">\xa5</span>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t<span class="u-price">')
            # SOURCE LINE 151
            __M_writer(unicode(sub_trans_fare))
            __M_writer(u'</span> \r\n\t\t\t\t\t\t\t\t\t\t\t\t</span>\r\n\t\t\t\t\t\t\t\t\t\t\t</span> \r\n\t\t\t\t\t\t\t\t\t\t</span>\r\n\t\t\t\t\t\t\t\t\t</div><!-- / .shipping-costs -->\r\n\t\t\t\t\t\t\t\t\t')
            # SOURCE LINE 156
            sub_total += sub_trans_fare 
            
            __M_writer(u'\r\n\t\t\t\t\t\t\t\t\t<span class="subtotal J_sum_items"> \u672c\u8ba2\u5355\u91d1\u989d\uff1a <span class="m-price"> <span class="u-yen">\xa5</span><span class="u-price J_amount_0">')
            # SOURCE LINE 157
            __M_writer(unicode(sub_total))
            __M_writer(u'</span> </span> </span>\r\n\t\t\t\t\t\t\t\t</div></td>\r\n\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t</tfoot>\r\n\t\t\t\t\t</table>\r\n\t\t\t\t\t')
            # SOURCE LINE 162

            trans_fare += sub_trans_fare;
            total += sub_total;
                                                    
            
            # SOURCE LINE 165
            __M_writer(u'\r\n')
            pass
        # SOURCE LINE 167
        __M_writer(u'\t\t\t\t</div>\r\n\t\t\t\t<div class="m-checkout-review">\r\n\t\t\t\t\t<div class="m-inline-block checkout-review-inner">\r\n\t\t\t\t\t\t<div class="inline-block-item review-others-wrapper">\r\n\t\t\t\t\t\t\t<div class="review-others">\r\n\t\t\t\t\t\t\t\t<div class="m-inline-block review-item review-address-item" data-hover="review-item-hover" data-touch="z-touch">\r\n\t\t\t\t\t\t\t\t\t<h3 class="inline-block-item review-item-title">\u6536\u8d27\u4fe1\u606f\uff1a</h3>\r\n\t\t\t\t\t\t\t\t\t<div class="inline-block-item review-item-cnt transport_info">\r\n\t\t\t\t\t\t\t\t\t\t<div class="">\r\n\t\t\t\t\t\t\t\t\t\t\t<span></span>\r\n\t\t\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t<div class="m-inline-block review-item review-payment-item" data-hover="review-item-hover" data-touch="z-touch">\r\n\t\t\t\t\t\t\t\t\t<h3 class="inline-block-item review-item-title">\u652f\u4ed8\u65b9\u5f0f\uff1a</h3>\r\n\t\t\t\t\t\t\t\t\t<div class="inline-block-item review-item-cnt J_paymen_info">\r\n\t\t\t\t\t\t\t\t\t\t\u8d27\u5230\u4ed8\u6b3e\r\n\t\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t<!-- / .m-shopping-tips -->\r\n\t\t\t\t\t\t\t</div><!-- / .review-others -->\r\n\t\t\t\t\t\t</div><!-- / .inline-block-item -->\r\n\t\t\t\t\t\t<div class="inline-block-item review-price-wrapper">\r\n\t\t\t\t\t\t\t<div class="review-price">\r\n\t\t\t\t\t\t\t\t<ul class="review-price-list">\r\n\t\t\t\t\t\t\t\t\t<li class="review-price-item J_sum_items">\r\n\t\t\t\t\t\t\t\t\t\t<span class="m-price"> <span class="u-yen">\xa5</span><span class="u-price J_goods_amount">')
        # SOURCE LINE 193
        __M_writer(unicode(total-trans_fare))
        __M_writer(u'</span> </span>\r\n\t\t\t\t\t\t\t\t\t\t<h4 class="review-price-item-title">\u5546\u54c1\u91d1\u989d\uff1a</h4>\r\n\t\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t\t\t<li class="review-price-item J_sum_items">\r\n\t\t\t\t\t\t\t\t\t\t<span class="m-price"> <span class="u-yen">\xa5</span><span class="u-price J_shipping_amount">')
        # SOURCE LINE 197
        __M_writer(unicode(trans_fare))
        __M_writer(u'</span> </span>\r\n\t\t\t\t\t\t\t\t\t\t<h4 class="review-price-item-title">\u8fd0\u8d39\uff1a</h4>\r\n\t\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t\t</ul>\r\n\t\t\t\t\t\t\t\t<div class="review-total-price J_sum_items">\r\n\t\t\t\t\t\t\t\t\t<strong class="m-price"> <span class="u-yen">\xa5</span><span class="u-price J_pay_amount">')
        # SOURCE LINE 202
        __M_writer(unicode(total))
        __M_writer(u'</span> </strong>\r\n\t\t\t\t\t\t\t\t\t<h4 class="review-total-price-title">\u5f85\u652f\u4ed8\uff1a</h4>\r\n\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t<div class="review-price-actions J_can_not_order_tips" id="J_can_not_order_tips">\r\n\t\t\t\t\t\t\t\t\t<form id="order_frmSave" method="post" action="/order/generate/" role="form">\r\n\t\t\t\t\t\t\t\t\t\t<input type="hidden" name="address_id" value="">\r\n\t\t\t\t\t\t\t\t\t\t<input type="hidden" name="pay_way" value="1" id="pay_way"/>\r\n\t\t\t\t\t\t\t\t\t\t<button class="u-btn btn-primary btn-large J_order_submit_btn" type="submit">\r\n\t\t\t\t\t\t\t\t\t\t\t<span class="btn-text" mars_sead="checkout_submit_btn">\u63d0\u4ea4\u8ba2\u5355</span>\r\n\t\t\t\t\t\t\t\t\t\t</button>\r\n\t\t\t\t\t\t\t\t\t</form>\r\n\t\t\t\t\t\t\t\t</div><!-- / .review-price-actions -->\r\n\t\t\t\t\t\t\t</div><!-- / .review-price -->\r\n\t\t\t\t\t\t</div><!-- / .inline-block-item -->\r\n\t\t\t\t\t</div><!-- / .checkout-review-inner -->\r\n\t\t\t\t</div><!-- / .m-checkout-review -->\r\n\t\t\t</div><!-- / .box-bd -->\r\n\t\t</div><!-- / .m-box -->\r\n\t</div><!-- / .g-row -->\r\n</div>\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        # SOURCE LINE 15
        __M_writer(u'\r\n\t')
        # SOURCE LINE 16
        runtime._include_file(context, u'/cute_header.part', _template_uri)
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_js(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def head_js():
            return render_head_js(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 10
        __M_writer(u'\r\n\t')
        # SOURCE LINE 11
        __M_writer(unicode(parent.head_js()))
        __M_writer(u'\r\n\t<script src="')
        # SOURCE LINE 12
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/order/checkout.js" type="text/javascript" charset="utf-8"></script>\r\n')
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
        __M_writer(u'css/order/checkout.css" type="text/css" media="screen" title="no title" charset="utf-8"/>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


