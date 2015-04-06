# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1427442289.326
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
        __M_writer(u'images/640"></a>\r\n\t</dt>\r\n\t<dd class="brand_tit gray">\r\n\t\t{{store}}\r\n\t</dd>\r\n\t<dd class="pro_list_tit">\r\n\t\t<a href="/show/{{store_id}}/{{id}}/" target="_blank">{{name}}</a>\r\n\t</dd>\r\n\t<dd class="pro_list_data">\r\n\t\t<span class="deep_red"><em>\xa5{{min_price}}</em></span>\r\n\t</dd>\r\n</dl>\r\n</script>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


