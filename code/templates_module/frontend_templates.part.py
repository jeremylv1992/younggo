# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1428992104.535
_template_filename=u'C:\\Users\\Jeremy\\Desktop\\younggo\\code\\mysite\\templates/frontend_templates.part'
_template_uri=u'/frontend_templates.part'
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
        __M_writer(u'<script type="text/x-mustache" id="area_tmp">\r\n\t<tr>\r\n\t<td><a class = "J_select_item" href="/school/locate/?school_id={{id}}"> {{name}} </a></td>\r\n\t</tr>\r\n</script>\r\n\r\n<script type="text/x-mustache" charset="utf-8" id="store_item">\n<li class="brand_new">\r\n\t<div class="act-item-wrap" data-bid="382299">\r\n\t\t<div class="b_f_con_img_box">\r\n\t\t\t<a class="b_f_item_c" target="_blank" href="/show/{{id}}/"> \r\n\t\t\t<img width="226" height="288" class="" alt="" src="')
        # SOURCE LINE 12
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'images/store.jpg"> </a>\r\n\t\t</div>\r\n\t\t<div class="b_f_info">\r\n\t\t\t<p class="b_f_brand">\r\n\t\t\t\t<a href="###" target="_blank" href="/show/{{id}}/">{{name}}</a>\r\n\t\t\t</p>\r\n\t\t\t<p class="b_f_intro fwr">\r\n\t\t\t\t{{summary}}\r\n\t\t\t</p>\r\n\t\t</div>\r\n\t</div>\r\n</li>\r\n</script>\r\n\r\n<script type="text/x-mustache" charset="utf-8" id="good_item">\n<dl class="J_pro_items" id="J_pro_50490864" data-hover="dl_hover">\r\n\t<dt class="pro_list_pic">\r\n\t\t<a href="/show/{{store_id}}/{{id}}/" title="{{name}}" target="_blank"> <img class="J_first_pic" width="235" height="297" alt="{{name}}" src="')
        # SOURCE LINE 29
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'images/640"></a>\r\n\t</dt>\r\n\t<dd class="brand_tit gray">\r\n\t\t{{store}}\r\n\t</dd>\r\n\t<dd class="pro_list_tit">\r\n\t\t<a href="/show/{{store_id}}/{{id}}/" target="_blank">{{name}}</a>\r\n\t</dd>\r\n\t<dd class="pro_list_data">\r\n\t\t<span class="deep_red"><em>\xa5{{min_price}}</em></span>\r\n\t</dd>\r\n</dl>\r\n</script>\r\n\r\n<script type="text/x-mustache" charset="utf-8" id="address_item_tmp">\n<div class="m-modal modify-address-modal">\r\n\t<div class="modal-inner">\r\n\t\t<div class="modal-cnt">\r\n\t\t\t<h2 class="modify-address-title">\u6536\u8d27\u4fe1\u606f</h2>\r\n\t\t\t<form class="m-form address-form" role="form" action="./address.php">\r\n\t\t\t\t<input type="hidden" name="id" value="">\r\n\t\t\t\t<div class="form-item form-title-item J_form_item">\r\n\t\t\t\t\t<input type="text" class="u-ipt" placeholder="\u6536\u8d27\u4eba\u59d3\u540d" name="consignee" value="" autofocus="true" mars_sead="address_name_input">\r\n\t\t\t\t\t<div class="m-tooltips tooltips-left-arrows tooltips-error">\r\n\t\t\t\t\t\t<div class="tooltips-arrows-wrapper">\r\n\t\t\t\t\t\t\t<div class="tooltips-arrows">\r\n\t\t\t\t\t\t\t\t<span class="tooltips-arrow-border">\u25c6</span>\r\n\t\t\t\t\t\t\t\t<span class="tooltips-arrow-bg">\u25c6</span>\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t<div class="tooltips-cnt">\r\n\t\t\t\t\t\t\t<div class="m-tips tips-small">\r\n\t\t\t\t\t\t\t\t<i class="u-icon tips-icon icon-error-small"></i>\r\n\t\t\t\t\t\t\t\t<div class="tips-cnt">\r\n\t\t\t\t\t\t\t\t\t<p class="tips-text J_tips_txt"></p>\r\n\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t\t<div class="form-item form-mobile-item J_form_item">\r\n\t\t\t\t\t<input type="text" class="u-ipt" placeholder="\u624b\u673a\u53f7\u7801" name="mobile" value="" mars_sead="address_phone_input" data-or-verification="phone">\r\n\t\t\t\t\t<div class="m-tooltips tooltips-left-arrows tooltips-error">\r\n\t\t\t\t\t\t<div class="tooltips-arrows-wrapper">\r\n\t\t\t\t\t\t\t<div class="tooltips-arrows">\r\n\t\t\t\t\t\t\t\t<span class="tooltips-arrow-border">\u25c6</span>\r\n\t\t\t\t\t\t\t\t<span class="tooltips-arrow-bg">\u25c6</span>\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t<div class="tooltips-cnt">\r\n\t\t\t\t\t\t\t<div class="m-tips tips-small">\r\n\t\t\t\t\t\t\t\t<i class="u-icon tips-icon icon-error-small"></i>\r\n\t\t\t\t\t\t\t\t<div class="tips-cnt">\r\n\t\t\t\t\t\t\t\t\t<p class="tips-text J_tips_txt"></p>\r\n\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t\t<div class="form-item form-tel-item J_form_item" data-input-error="z-form-item-error z-form-item-error-tooltips">\r\n\t\t\t\t\t<input type="text" class="u-ipt" placeholder="\u5907\u7528\u8054\u7cfb\u7535\u8bdd\uff08\u56fa\u8bdd/\u624b\u673a\uff09" name="phone" value="" mars_sead="address_telephone_input" data-or-verification="mobile">\r\n\t\t\t\t\t<div class="m-tooltips tooltips-left-arrows tooltips-error">\r\n\t\t\t\t\t\t<div class="tooltips-arrows-wrapper">\r\n\t\t\t\t\t\t\t<div class="tooltips-arrows">\r\n\t\t\t\t\t\t\t\t<span class="tooltips-arrow-border">\u25c6</span>\r\n\t\t\t\t\t\t\t\t<span class="tooltips-arrow-bg">\u25c6</span>\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t<div class="tooltips-cnt">\r\n\t\t\t\t\t\t\t<div class="m-tips tips-small">\r\n\t\t\t\t\t\t\t\t<i class="u-icon tips-icon icon-error-small"></i>\r\n\t\t\t\t\t\t\t\t<div class="tips-cnt">\r\n\t\t\t\t\t\t\t\t\t<p class="tips-text J_tips_txt">\r\n\t\t\t\t\t\t\t\t\t\t\u7535\u8bdd\u683c\u5f0f\u4e0d\u6b63\u786e\uff08\u8bf7\u8f93\u5165\u624b\u673a\u53f7 \u6216 \u533a\u53f7-\u56fa\u8bdd\uff09\r\n\t\t\t\t\t\t\t\t\t</p>\r\n\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t</div><!-- / .tooltips-left-arrows -->\r\n\t\t\t\t</div>\r\n\t\t\t\t<div class="form-item form-address-detail-item J_form_item">\r\n\t\t\t\t\t<textarea class="u-textarea address-textarea J_special_tips_textarea" placeholder="\u8be6\u7ec6\u5730\u5740" name="address" mars_sead="address_detail_input"></textarea>\r\n\t\t\t\t\t<div class="m-tooltips tooltips-left-arrows tooltips-info address-guide-tooltips">\r\n\t\t\t\t\t\t<div class="tooltips-arrows-wrapper">\r\n\t\t\t\t\t\t\t<div class="tooltips-arrows">\r\n\t\t\t\t\t\t\t\t<span class="tooltips-arrow-border">\u25c6</span>\r\n\t\t\t\t\t\t\t\t<span class="tooltips-arrow-bg">\u25c6</span>\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t<div class="tooltips-cnt">\r\n\t\t\t\t\t\t\t<p>\r\n\t\t\t\t\t\t\t\t\u586b\u5199\u8def\u540d\u3001\u95e8\u724c\u53f7\uff0c\u8bf7\u52ff\u518d\u6b21\u586b\u5199\u7701\u5e02\u533a\r\n\t\t\t\t\t\t\t</p>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t\t<div class="form-item-actions">\r\n\t\t\t\t\t<a href="javascript:submit_addr();" role="button" class="u-btn btn-primary J_address_save J_fake_a"> <span class="btn-text">\u4fdd\u5b58</span> <span class="btn-loading-text bg-loading-gray-small">\u52a0\u8f7d\u4e2d...</span> </a>\r\n\t\t\t\t\t<a href="javascript:close_addr_tmp();" role="button" class="u-btn btn-link J_address_cancel J_fake_a" >\u53d6\u6d88</a>\r\n\t\t\t\t</div>\r\n\t\t\t</form>\r\n\t\t</div>\r\n\t</div>\r\n\t<a href="javascript:close_addr_tmp();" class="btn-modal-close J_address_cancel J_fake_a" title="\u5173\u95ed" role="button" mars_sead="address_notsave_btn">\xd7</a>\r\n\t<!-- / .address-system-info-modal -->\r\n</div>\n</script>\r\n\r\n<script type="text/x-mustache" charset="utf-8" id="address_item_show">\n<li class="inline-block-item address-item J_address_item_container" data-current="z-address-item-current" \r\n\tdata-intro="{{name}}.{{tel}}.{{addr}}" data-address-id="{{id}}">\r\n\t<div class="m-member-info address-inner J_address_item" data-hover="address-inner-hover" >\r\n\t\t<div class="member-info-item member-info-title">\r\n\t\t\t<span class="u-icon icon-address-member"></span>\r\n\t\t\t<p class="member-text">\r\n\t\t\t\t<span class="member-name" title="{{name}}">{{name}}</span>\r\n\t\t\t</p>\r\n\t\t</div>\r\n\t\t<div class="member-info-item member-info-phone">\r\n\t\t\t<span class="u-icon icon-address-phone"></span>\r\n\t\t\t<p class="member-text">\r\n\t\t\t\t<span class="member-mobile">{{tel}}</span>\r\n\t\t\t</p>\r\n\t\t</div>\r\n\t\t<div class="member-info-item member-info-local" title="{{addr}}">\r\n\t\t\t<span class="u-icon icon-address-local"></span>\r\n\t\t\t<address class="member-text">\r\n\t\t\t\t{{addr}}\r\n\t\t\t</address>\r\n\t\t</div>\r\n\t\t<span class="u-icon icon-corner-tick"></span>\r\n\t</div><!-- / .m-member-info -->\t\t\r\n</li>\r\n</script>\r\n \r\n<script type="text/x-mustache" charset="utf-8" id="chatwindow_contact_item_tmp">\n<li node-type="contact_item_1980923321" class="contacts SW_fun_bg clearfix">\r\n\t<p node-type="nick" class="name W_autocut W_fl S_txt1" data-user-name="{{username}}">{{username}}</p>\r\n</li>\t\r\n</script>\r\n\r\n<script type="text/x-mustache" charset="utf-8" id="chat_window_msg_tmp">\r\n<div class="msg_bubble_list bubble_l " style="display: block">\r\n\t<div class="bubble_mod clearfix">\r\n\t\t<div class="bubble_box SW_fun ">\r\n\t\t\t<div class="bubble_cont ">\r\n\t\t\t\t<div class="bubble_main clearfix" node-type="conRoot">\r\n\t\t\t\t\t<div class="cont">\r\n\t\t\t\t\t\t<p class="page">\r\n\t\t\t\t\t\t\t{{msg}}\r\n\t\t\t\t\t\t</p>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t</div>\r\n</div>\t\n</script>')
        return ''
    finally:
        context.caller_stack._pop_frame()


