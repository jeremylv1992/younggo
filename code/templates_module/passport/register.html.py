# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1427096629.575
_template_filename='C:\\Users\\Jeremy\\Desktop\\younggo\\code\\mysite\\templates/passport/register.html'
_template_uri='/passport/register.html'
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
        

        # SOURCE LINE 106
        __M_writer(u'\r\n\r\n<script type="text/javascript" charset="utf-8">\n\t$(function(){\r\n\t\t$("#btnRegister").click(function(){\r\n\t\t\t$("#user_reg_form").submit();\r\n\t\t})\r\n\t\t\r\n\t\t$("#y_name").change(check_blank);\r\n\t\t$("#y_email").change(check_blank);\r\n\t\t$("#y_password").change(check_blank);\r\n\t\t$("#y_con_password").change(check_blank);\r\n\r\n\t\tinit_inputs();\r\n\t})\n</script>')
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
        __M_writer(u'\r\n\t<div class="content login_ad clear" style="background-image: url(https://img.vipstatic.com/upload/cmc/2015/03/18/183/05527ee4f0c54ae7b81291c02a213c77.jpg);">\r\n\t\t<div class="regForm">\n')
        # SOURCE LINE 16
        if '__all__' in form.errors.viewkeys():
            # SOURCE LINE 17
            for msg in form.errors['__all__']:
                # SOURCE LINE 18
                __M_writer(u'\t\t\t\t\t<p class="err_msg">')
                __M_writer(unicode(msg))
                __M_writer(u'</p>\r\n')
                pass
            pass
        # SOURCE LINE 21
        __M_writer(u'\t\t\t<div class="regHeaderTip">\r\n\t\t\t\t<span class="f-right f12">\u5df2\u6ce8\u518c\uff1f<a href="/passport/login/" class="red hvLine">\u767b\u5f55</a></span>\r\n\t\t\t</div>\r\n\t\t\t<form id="user_reg_form" action="/passport/register/" method="post" autocomplete="off">\r\n\t\t\t<p class="inputs">\r\n\t\t\t\t')
        # SOURCE LINE 26

        err_class = 'error' if 'username' in form.errors.viewkeys() else ''
        cache_val = request.POST.get('username','') if request.method == 'POST' else ''
                                        
        
        # SOURCE LINE 29
        __M_writer(u'\r\n\t\t\t\t<input id="y_name" type="text" class="ipt ')
        # SOURCE LINE 30
        __M_writer(unicode(err_class))
        __M_writer(u'" name="username" value="')
        __M_writer(unicode(cache_val))
        __M_writer(u'"> \r\n\t\t\t\t<label for="">\u7528\u6237\u540d</label>\r\n\t\t\t</p>\r\n\t\t\t<p class="labels">\r\n')
        # SOURCE LINE 34
        if 'username' in form.errors.viewkeys():
            # SOURCE LINE 35
            for msg in form.errors['username']:
                # SOURCE LINE 36
                __M_writer(u'\t\t\t\t\t<span class="err_msg">')
                __M_writer(unicode(msg))
                __M_writer(u'</span>\r\n')
                pass
            # SOURCE LINE 38
        else:
            # SOURCE LINE 39
            __M_writer(u'\t\t\t\t<span class="err_msg"></span>\r\n')
            pass
        # SOURCE LINE 41
        __M_writer(u'\t\t\t</p>\r\n\t\t\t<div class="auth-tips auth-tips-single z-hide" for="">\r\n\t\t\t\t<div class="tips-arrow"></div>\r\n\t\t\t\t\u8be5\u503c\u53ea\u80fd\u5305\u542b\u5b57\u6bcd\u3001\u6570\u5b57\u548c\u5b57\u7b26@/./+/-/_\r\n\t\t\t</div>\r\n\t\t\t<p class="inputs">\r\n\t\t\t\t')
        # SOURCE LINE 47

        err_class = 'error' if 'email' in form.errors.viewkeys() else ''
        cache_val = request.POST.get('email','') if request.method == 'POST' else ''
                                        
        
        # SOURCE LINE 50
        __M_writer(u'\r\n\t\t\t\t<input id="y_email" type="text" class="ipt ')
        # SOURCE LINE 51
        __M_writer(unicode(err_class))
        __M_writer(u'" name="email" value="')
        __M_writer(unicode(cache_val))
        __M_writer(u'">\r\n\t\t\t\t<label for="">\u90ae\u7bb1</label>\r\n\t\t\t</p>\r\n\t\t\t<p class="labels">\r\n')
        # SOURCE LINE 55
        if 'email' in form.errors.viewkeys():
            # SOURCE LINE 56
            for msg in form.errors['email']:
                # SOURCE LINE 57
                __M_writer(u'\t\t\t\t\t<span class="err_msg">')
                __M_writer(unicode(msg))
                __M_writer(u'</span>\r\n')
                pass
            # SOURCE LINE 59
        else:
            # SOURCE LINE 60
            __M_writer(u'\t\t\t\t<span class="err_msg"></span>\r\n')
            pass
        # SOURCE LINE 62
        __M_writer(u'\t\t\t</p>\r\n\t\t\t<div class="auth-tips auth-tips-single z-hide" for="">\r\n\t\t\t\t<div class="tips-arrow"></div>\r\n\t\t\t\t\u8bf7\u6b63\u786e\u90ae\u7bb1\u5730\u5740\uff0c\u683c\u5f0f\u5982\uff1ajeremylv@gmail.com\r\n\t\t\t</div>\r\n\t\t\t<p class="inputs">\r\n\t\t\t\t')
        # SOURCE LINE 68

        err_class = 'error' if 'password1' in form.errors.viewkeys() else ''
        cache_val = request.POST.get('password1','') if request.method == 'POST' else ''
                                        
        
        # SOURCE LINE 71
        __M_writer(u'\r\n\t\t\t\t<input id="y_password" type="password" class="ipt ')
        # SOURCE LINE 72
        __M_writer(unicode(err_class))
        __M_writer(u'" name="password1" \r\n\t\t\t\t\tvalue="')
        # SOURCE LINE 73
        __M_writer(unicode(cache_val))
        __M_writer(u'" maxlength="20">\r\n\t\t\t\t<label for="">\u5bc6\u7801</label>\r\n\t\t\t</p>\r\n\t\t\t<p class="labels">\r\n')
        # SOURCE LINE 77
        if 'password1' in form.errors.viewkeys():
            # SOURCE LINE 78
            for msg in form.errors['password1']:
                # SOURCE LINE 79
                __M_writer(u'\t\t\t\t\t<span class="err_msg">')
                __M_writer(unicode(msg))
                __M_writer(u'</span>\r\n')
                pass
            # SOURCE LINE 81
        else:
            # SOURCE LINE 82
            __M_writer(u'\t\t\t\t<span class="err_msg"></span>\r\n')
            pass
        # SOURCE LINE 84
        __M_writer(u'\t\t\t</p>\r\n\t\t\t<p class="inputs">\r\n\t\t\t\t')
        # SOURCE LINE 86

        err_class = 'error' if 'password2' in form.errors.viewkeys() else ''
        cache_val = request.POST.get('password2','') if request.method == 'POST' else ''
                                        
        
        # SOURCE LINE 89
        __M_writer(u'\r\n\t\t\t\t<input id="y_con_password" type="password" class="ipt ')
        # SOURCE LINE 90
        __M_writer(unicode(err_class))
        __M_writer(u'" name="password2" \r\n\t\t\t\t\tvalue="')
        # SOURCE LINE 91
        __M_writer(unicode(cache_val))
        __M_writer(u'" maxlength="20">\r\n\t\t\t\t<label for="">\u786e\u8ba4\u5bc6\u7801</label>\r\n\t\t\t</p>\r\n\t\t\t<p class="labels"></p>\r\n\t\t\t<p class="mb30">\r\n\t\t\t\t<a id="btnRegister" href="javascript:void(0);" class="btn btnReg">\u6ce8\u518c</a>\r\n\t\t\t</p>\r\n\t\t\t<p class="inputs">\r\n\t\t\t\t<span class="checkbox" data-for="agree"><i class="checked"></i> \u6211\u5df2\u9605\u8bfb\u5e76\u63a5\u53d7YoungGo\u670d\u52a1\u6761\u6b3e</a>\u3002</span>\r\n\t\t\t\t<input id="J_R_agree" name="agree" type="hidden" value="1" data-type="checkbox">\r\n\t\t\t</p>\r\n\t\t\t<p class="labels"><span class="err_msg"></span></p>\r\n\t\t</form>\r\n\t\t</div>\r\n\t</div>\r\n')
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


