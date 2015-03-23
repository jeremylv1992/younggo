# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1427077995.064
_template_filename='C:\\Users\\Jeremy\\Desktop\\younggo\\code\\mysite\\templates/passport/success_register.html'
_template_uri='/passport/success_register.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n\t<head>\n\t\t<title>YoungGo \u6ce8\u518c\u6210\u529f</title>\n\t</head>\n\t<body></doby>\n</html>\n<script type="text/javascript" charset="utf-8">\n\tif(confirm("\u6ce8\u518c\u6210\u529f\uff0c\u7acb\u5373\u767b\u5f55\uff01")){\n\t\twindow.location.href = "/passport/login/";\t\n\t}\n</script>')
        return ''
    finally:
        context.caller_stack._pop_frame()


