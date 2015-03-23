# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1426868397.17
_template_filename=u'C:\\Users\\Jeremy\\Desktop\\younggo\\code\\mysite\\templates/passport/logo_header.part'
_template_uri=u'/passport/logo_header.part'
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
        __M_writer(u'<header class="header">\r\n\t<nav class="top_nav">\r\n\t\t<div id="" class="head_inner">\r\n\t\t\t<div class="header_logo_dop">\r\n\t\t\t\t<a target="_self" href="/"> \r\n\t\t\t\t\t<img src="')
        # SOURCE LINE 6
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'images/younggo_logo.jpg" alt="\u4e00\u5bb6\u4e70\u5356\u60c5\u6000\u7684\u7f51\u7ad9"> </a>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t</nav>\r\n</header>\r\n\r\n<style type="text/css" media="screen">\n\t.header {\r\n\t\toverflow: hidden;\r\n  \t\tzoom: 1;\r\n  \t\tmargin: 20px auto;\r\n\t}\n</style>')
        return ''
    finally:
        context.caller_stack._pop_frame()


