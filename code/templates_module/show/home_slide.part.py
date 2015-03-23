# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1426682374.859
_template_filename=u'C:\\Users\\Jeremy\\Desktop\\younggo\\code\\mysite\\templates/show/home_slide.part'
_template_uri=u'/show/home_slide.part'
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
        __M_writer(u'<!-- \u8f6e\u64ad\u6a2a\u5e45\u5e7f\u544a -->\r\n<div class="focus_banner" >\r\n\t<div class="focus_banner_con">\r\n\t\t<ul class="fbc_list" style="">\r\n\t\t\t<li class="fbc_list_item">\r\n\t\t\t\t<a href="###" target="_self"><img src="')
        # SOURCE LINE 6
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'images/sysu_index.jpg" class="fbc_list_img" alt="\u4e2d\u5c71\u5927\u5b66\u9884\u89c8\u56fe1"></a>\r\n\t\t\t</li>\r\n\t\t</ul>\r\n\t\t<span class="fbc_btn fbc_btn_left"></span>\r\n\t\t<span class="fbc_btn fbc_btn_right"></span>\r\n\t\t<div class="fbc_trigger">\r\n\t\t\t<span class="fbc_trigger_con"><i class="selected">\u2022</i><i class="">\u2022</i><i class="">\u2022</i><i class="">\u2022</i><i class="">\u2022</i></span>\r\n\t\t</div>\r\n\t</div>\r\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


