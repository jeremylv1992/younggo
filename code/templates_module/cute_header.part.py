# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1428595403.625
_template_filename=u'C:\\Users\\Jeremy\\Desktop\\younggo\\code\\mysite\\templates/cute_header.part'
_template_uri=u'/cute_header.part'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user = context.get('user', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<header class="header">\r\n\t<nav class="top_nav">\r\n\t\t<div id="" class="head_inner">\r\n\t\t\t<ul class="top_nav_tool">\r\n')
        # SOURCE LINE 5
        if user.is_authenticated():
            # SOURCE LINE 6
            __M_writer(u'\t\t\t\t<li>\r\n\t\t\t\t\t<a href="###" target="_self">\u6b22\u8fce\uff0c')
            # SOURCE LINE 7
            __M_writer(unicode(user.username))
            __M_writer(u' |</a>\r\n\t\t\t\t</li>\t\t\r\n\t\t\t\t<li>\r\n\t\t\t\t\t<a href="/passport/logout/" target="_self">\u6ce8\u9500 |</a>\r\n\t\t\t\t</li>\t\t\r\n')
            # SOURCE LINE 12
        else:
            # SOURCE LINE 13
            __M_writer(u'\t\t\t\t<li>\r\n\t\t\t\t\t<a href="/passport/login/" target="_self">\u767b\u5f55 |</a>\r\n\t\t\t\t</li>\r\n\t\t\t\t<li>\r\n\t\t\t\t\t<a href="/passport/register/" target="_self">\u6ce8\u518c |</a>\r\n\t\t\t\t</li>\t\t\t\t\r\n')
            pass
        # SOURCE LINE 20
        __M_writer(u'\t\t\t\t<li>\r\n\t\t\t\t\t<a href="###" target="_blank">\u6211\u7684\u5927\u5b66</a>\r\n\t\t\t\t</li>\r\n\t\t\t\t<li>\r\n\t\t\t\t\t<a href="###" target="_blank">\u6211\u7684\u8ba2\u5355</a>\r\n\t\t\t\t</li>\r\n\t\t\t\t<li>\r\n\t\t\t\t\t<a href="/cart/" target="_blank">\u8d2d\u7269\u8f66</a>\r\n\t\t\t\t</li>\r\n\t\t\t</ul>\r\n\t\t\t<div class="header_logo_dop">\r\n\t\t\t\t<a target="_self" href="/"> \r\n\t\t\t\t\t<img src="')
        # SOURCE LINE 32
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'images/younggo_logo.jpg" alt="\u4e00\u5bb6\u4e70\u5356\u60c5\u6000\u7684\u7f51\u7ad9"> </a>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t</nav>\r\n</header>\r\n\r\n<style type="text/css" media="screen">\r\n\t.header {\r\n\t\toverflow: hidden;\r\n  \t\tzoom: 1;\r\n  \t\tmargin-bottom: 25px;\r\n  \t\theight: 96px;\r\n  \t\tborder-bottom: 2px solid #f3168a;\r\n\t}\r\n</style>')
        return ''
    finally:
        context.caller_stack._pop_frame()


