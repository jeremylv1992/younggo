# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1427360636.239
_template_filename=u'C:\\Users\\Jeremy\\Desktop\\younggo\\code\\mysite\\templates/header.part'
_template_uri=u'/header.part'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = ['dynamic_head']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_dynamic_head(context,tag):
    context.caller_stack._push_frame()
    try:
        school = context.get('school', UNDEFINED)
        user = context.get('user', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2

        home = 'current' if tag == 'home' else ''
        mall = 'current' if tag == 'mall' else ''       
        
        
        # SOURCE LINE 5
        __M_writer(u'\n<header class="header">\n\t<nav class="top_nav">\n\t\t<div id="" class="head_inner">\n\t\t\t<ul class="top_nav_tool">\n')
        # SOURCE LINE 10
        if user.is_authenticated():
            # SOURCE LINE 11
            __M_writer(u'\t\t\t\t<li>\n\t\t\t\t\t<a href="###" target="_self">\u6b22\u8fce\uff0c')
            # SOURCE LINE 12
            __M_writer(unicode(user.username))
            __M_writer(u' |</a>\n\t\t\t\t</li>\t\t\n\t\t\t\t<li>\n\t\t\t\t\t<a href="/passport/logout/" target="_self">\u6ce8\u9500 |</a>\n\t\t\t\t</li>\t\t\n')
            # SOURCE LINE 17
        else:
            # SOURCE LINE 18
            __M_writer(u'\t\t\t\t<li>\n\t\t\t\t\t<a href="/passport/login/" target="_self">\u767b\u5f55 |</a>\n\t\t\t\t</li>\n\t\t\t\t<li>\n\t\t\t\t\t<a href="/passport/register/" target="_self">\u6ce8\u518c |</a>\n\t\t\t\t</li>\t\t\t\t\n')
            pass
        # SOURCE LINE 25
        __M_writer(u'\t\t\t\t<li>\n\t\t\t\t\t<a href="###" target="_blank">\u6211\u7684\u5927\u5b66</a>\n\t\t\t\t</li>\n\t\t\t\t<li>\n\t\t\t\t\t<a href="###" target="_blank">\u6211\u7684\u8ba2\u5355</a>\n\t\t\t\t</li>\n\t\t\t\t<li>\n\t\t\t\t\t<a href="###" target="_blank">\u8d2d\u7269\u8f66</a>\n\t\t\t\t</li>\n\t\t\t\t<li>\n\t\t\t\t\t<a href="###" target="_blank">\u6536\u85cf</a>\n\t\t\t\t</li>\n\t\t\t\t<li>\n\t\t\t\t\t<a href="###" target="_blank">\u5728\u7ebf\u5ba2\u670d</a>\n\t\t\t\t</li>\n\t\t\t</ul>\n\t\t\t<div class="header_logo_dop">\n\t\t\t\t<a target="_self" href="/"> \n\t\t\t\t\t<img src="')
        # SOURCE LINE 43
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'images/younggo_logo.jpg" alt="\u4e00\u5bb6\u4e70\u5356\u60c5\u6000\u7684\u7f51\u7ad9"> </a>\n\t\t\t</div>\n\t\t\t<div class="sel_area">\n                <div class="sel_area_change" id="">\n                    <div class="sel_area_btn">\n                    \t<i class="sel_area_arrow"></i><span>')
        # SOURCE LINE 48
        __M_writer(unicode(school.name))
        __M_writer(u'</span>\n                    </div>\n\t\t\t\t\t<div class="sel_area_box" id="J_area_content" style="">\n\t\t\t\t\t\t<i class="ico_arw"></i>\n\t\t\t\t\t\t<p class="sab_tit">\n\t\t\t\t\t\t\t\u8bf7\u9009\u62e9\u611f\u5174\u8da3\u7684\u5b66\u6821\n\t\t\t\t\t\t</p>\n\t\t\t\t\t\t<table class="sab_table" mars_sead="home_top_zone_link">\n\t\t\t\t\t\t\t<tbody>\n\t\t\t\t\t\t\t</tbody>\n\t\t\t\t\t\t</table>\n\t\t\t\t\t</div>\n                </div>\n            </div>\n            <div class="header_search">\n            \t<ul class="hide" style="display: none;"></ul>\n\t\t\t\t<div class="form">\n\t\t\t\t\t<input type="text" class="text" value="\u4e2d\u5927\u6587\u5316\u6749\u5e74\u7ec8\u7279\u5356">\n\t\t\t\t\t<input type="button" value="\u641c\u7d22" class="button">\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t</nav>\n\t<nav class="main_nav">\n\t\t<div class="head_inner">\n\t\t\t<ul class="main_nav_link">\n\t\t\t\t<li>\n\t\t\t\t\t<a href="/" class="')
        # SOURCE LINE 75
        __M_writer(unicode(home))
        __M_writer(u'" >\u9996\u9875</a>\n\t\t\t\t</li>\n\t\t\t\t<li>\n\t\t\t\t\t<a href="/show/" class="')
        # SOURCE LINE 78
        __M_writer(unicode(mall))
        __M_writer(u'">\u8fdb\u5165\u5546\u57ce</a>\n\t\t\t\t</li>\n\t\t\t\t<li>\n\t\t\t\t\t<a href="###">\u6bcf\u65e5\u4f18\u60e0</a>\n\t\t\t\t</li>\n\t\t\t\t<li>\n\t\t\t\t\t<a href="###">\u521b\u610f\u5b75\u5316</a>\n\t\t\t\t</li>\n\t\t\t\t<li>\n\t\t\t\t\t<a href="###">\u8d5b\u533a</a>\n\t\t\t\t</li>\n\t\t\t\t<li>\n\t\t\t\t\t<a href="###">\u751f\u4ea7\u5546</a>\n\t\t\t\t</li>\n\t\t\t\t<li>\n\t\t\t\t\t<a href="###" class="special">\u6211\u8981\u5f00\u5e97</a>\n\t\t\t\t</li>\n\t\t\t</ul>\n\t\t</div>\n\t</nav>\n</header>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


