# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1427089584.51
_template_filename='C:\\Users\\Jeremy\\Desktop\\younggo\\code\\mysite\\templates/passport/login.html'
_template_uri='/passport/login.html'
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
        parent = context.get('parent', UNDEFINED)
        form = context.get('form', UNDEFINED)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context.locals_(__M_locals))
        def header():
            return render_header(context.locals_(__M_locals))
        def head_css():
            return render_head_css(context.locals_(__M_locals))
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
        

        # SOURCE LINE 96
        __M_writer(u'\r\n\r\n<script type="text/javascript" charset="utf-8">\n\t$(function(){\r\n\t\t$("#btnLogin").click(function(){\r\n\t\t\t$("#user_login_form").submit();\t\t\r\n\t\t})\r\n\t\t$("#J_L_name").change(check_blank);\r\n\t\t$("#J_L_psw").change(check_blank);\r\n\t\t\r\n\t\tinit_inputs();\r\n\t})\t\t\r\n\t\r\n</script>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        request = context.get('request', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer(u'\r\n\t<div class="content login_ad clear" style="background-image: url(https://img.vipstatic.com/upload/cmc/2015/03/18/183/05527ee4f0c54ae7b81291c02a213c77.jpg);">\r\n\t\t<div class="regForm">\r\n\t\t\t<form id="user_login_form" action="/passport/login/" method="post">\r\n')
        # SOURCE LINE 17
        if '__all__' in form.errors.viewkeys():
            # SOURCE LINE 18
            for msg in form.errors['__all__']:
                # SOURCE LINE 19
                __M_writer(u'\t\t\t\t\t\t<p class="err_msg">')
                __M_writer(unicode(msg))
                __M_writer(u'</p>\r\n')
                pass
            pass
        # SOURCE LINE 22
        __M_writer(u'\t\t\t\t<div class="regHeaderTip">\r\n\t\t\t\t\t\u6b22\u8fce\u56de\u6765\uff01\u8bf7\u767b\u5f55\r\n\t\t\t\t</div>\r\n\t\t\t\t<p class="inputs">\r\n')
        # SOURCE LINE 26
        if 'username' in form.errors.viewkeys():
            # SOURCE LINE 27
            if request.method == 'POST':
                # SOURCE LINE 28
                __M_writer(u'\t\t\t\t\t\t<input id="J_L_name" type="text" class="ipt error" name="username" \r\n\t\t\t\t\t\t\tvalue="')
                # SOURCE LINE 29
                __M_writer(unicode(request.POST.get('username','')))
                __M_writer(u'">\r\n')
                # SOURCE LINE 30
            else:
                # SOURCE LINE 31
                __M_writer(u'\t\t\t\t\t\t<input id="J_L_name" type="text" class="ipt error" name="username">\r\n')
                pass
            # SOURCE LINE 33
        else:
            # SOURCE LINE 34
            if request.method == 'POST':
                # SOURCE LINE 35
                __M_writer(u'\t\t\t\t\t\t<input id="J_L_name" type="text" class="ipt" name="username" \r\n\t\t\t\t\t\t\tvalue="')
                # SOURCE LINE 36
                __M_writer(unicode(request.POST.get('username','')))
                __M_writer(u'">\r\n')
                # SOURCE LINE 37
            else:
                # SOURCE LINE 38
                __M_writer(u'\t\t\t\t\t\t<input id="J_L_name" type="text" class="ipt" name="username">\r\n')
                pass
            pass
        # SOURCE LINE 41
        __M_writer(u'\t\t\t\t\t<label for="J_L_name" class="">\u767b\u5f55\u540d</label>\r\n\t\t\t\t</p>\r\n\t\t\t\t<p class="labels">\r\n')
        # SOURCE LINE 44
        if 'username' in form.errors.viewkeys():
            # SOURCE LINE 45
            for msg in form.errors['username']:
                # SOURCE LINE 46
                __M_writer(u'\t\t\t\t\t\t<span class="err_msg">')
                __M_writer(unicode(msg))
                __M_writer(u'</span>\r\n')
                pass
            # SOURCE LINE 48
        else:
            # SOURCE LINE 49
            __M_writer(u'\t\t\t\t\t<span class="err_msg"></span>\r\n')
            pass
        # SOURCE LINE 51
        __M_writer(u'\t\t\t\t</p>\r\n\t\t\t\t<p class="inputs">\r\n')
        # SOURCE LINE 53
        if 'password' in form.errors.viewkeys():
            # SOURCE LINE 54
            if request.method == 'POST':
                # SOURCE LINE 55
                __M_writer(u'\t\t\t\t\t\t<input id="J_L_psw" type="password" class="ipt error" name="password" \r\n\t\t\t\t\t\t\tvalue="')
                # SOURCE LINE 56
                __M_writer(unicode(request.POST.get('password','')))
                __M_writer(u'">\r\n')
                # SOURCE LINE 57
            else:
                # SOURCE LINE 58
                __M_writer(u'\t\t\t\t\t\t<input id="J_L_psw" type="password" class="ipt" name="password">\r\n')
                pass
            # SOURCE LINE 60
        else:
            # SOURCE LINE 61
            if request.method == 'POST':
                # SOURCE LINE 62
                __M_writer(u'\t\t\t\t\t\t<input id="J_L_psw" type="password" class="ipt" name="password" \r\n\t\t\t\t\t\t\tvalue="')
                # SOURCE LINE 63
                __M_writer(unicode(request.POST.get('password','')))
                __M_writer(u'">\r\n')
                # SOURCE LINE 64
            else:
                # SOURCE LINE 65
                __M_writer(u'\t\t\t\t\t\t<input id="J_L_psw" type="password" class="ipt" name="password">\r\n')
                pass
            pass
        # SOURCE LINE 68
        __M_writer(u'\t\t\t\t\t<label for="J_L_psw" class="">\u5bc6\u7801</label>\r\n\t\t\t\t</p>\r\n\t\t\t\t<p class="labels">\r\n')
        # SOURCE LINE 71
        if 'password' in form.errors.viewkeys():
            # SOURCE LINE 72
            for msg in form.errors['password']:
                # SOURCE LINE 73
                __M_writer(u'\t\t\t\t\t\t<span class="err_msg">')
                __M_writer(unicode(msg))
                __M_writer(u'</span>\r\n')
                pass
            # SOURCE LINE 75
        else:
            # SOURCE LINE 76
            __M_writer(u'\t\t\t\t\t<span class="err_msg"></span>\r\n')
            pass
        # SOURCE LINE 78
        __M_writer(u'\t\t\t\t</p>\r\n\t\t\t\t\r\n\t\t\t\t<p class="mb15">\r\n\t\t\t\t\t<a id="btnLogin" href="javascript:void(0);" class="btn btnLoginDeep">\u767b\u5f55</a>\r\n\t\t\t\t</p>\r\n\t\t\t\t<p class="mb50 clear mr70 lh14">\r\n\t\t\t\t\t<span class="f-left"><span class="checkbox" data-for="remUser"> <i class="checked"></i> \u8bb0\u4f4f\u7528\u6237\u540d</span></span>\r\n\t\t\t\t\t<span class="f-right"> <a href="###" class="f12 coffee" target="_self">\u5fd8\u8bb0\u5bc6\u7801?</a> <span class="lgray f12">|</span> <a href="/passport/register/" class="regLink">\u514d\u8d39\u6ce8\u518c</a></span>\r\n\t\t\t\t\t<input name="remUser" type="hidden" value="1" data-type="checkbox">\r\n\t\t\t\t</p>\r\n\t\t\t</form>\r\n\t\t\t<div class="linkBox">\r\n\t\t\t\t<p class="f12 mb20 clear linkBoxTitle">\r\n\t\t\t\t\t<span class="mr5 mb5 clear block">\u76ee\u524d\u4e0d\u652f\u6301\u5176\u4ed6\u7f51\u7ad9\u8d26\u53f7\u767b\u5f55\uff01</span>\r\n\t\t\t\t</p>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t</div>\r\n')
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
        runtime._include_file(context, u'logo_header.part', _template_uri)
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
        __M_writer(u'css/passport.css" type="text/css" charset="utf-8"/>\r\n\t<script src="')
        # SOURCE LINE 6
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/passport.js" type="text/javascript" charset="utf-8"></script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


