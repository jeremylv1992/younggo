# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1429004689.700265
_template_filename=u'/home/jeremy/Desktop/younggo/younggo/code/mysite/templates/chat/chat_window.part'
_template_uri=u'/chat/chat_window.part'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        WS4REDIS_HEARTBEAT = context.get('WS4REDIS_HEARTBEAT', UNDEFINED)
        WEBSOCKET_URI = context.get('WEBSOCKET_URI', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<link rel="stylesheet" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/chat/chat_window.css" type="text/css" media="screen" title="no title" charset="utf-8"/>\n<script src="')
        # SOURCE LINE 2
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/ws4redis.js" type="text/javascript"></script>\n\n<div class="webim_fold clearfix" style="bottom: 0px; right: 0px; visibility: visible;" node-type="chatMiniRoot" action-type="chatmini" action-data="from=chatmini">\n\t<div class="fold_bg"></div>\n\t<p class="fold_cont clearfix">\n\t\t<em class="fold_font W_fl W_f14" node-type="miniContent">\u5728\u7ebf\u804a\u5929</em>\n\t</p>\n</div>\n<div class="webim_chat_window clearfix f-hide" style="width: 560px; position: fixed; right: 0px; bottom: 0px; z-index: 950; \n\tborder:1px solid #CBCC4A; background-color: #CDCC4A" node-type="_root">\n\t<div class="WB_webim_page W_fl">\n\t\t<div node-type="_search" class="webim_serch">\n\t\t\t<span class="WB_search_s">\n\t\t\t\t<input type="text" maxlength="20" value="\u67e5\u627e\u8054\u7cfb\u4eba\u6216\u7fa4" suda-data="key=webim_group_restr&amp;value=webim_search_group" node-type="iptSearch" class="W_input">\n\t\t\t\t<span class="pos"></span></span>\n\t\t</div>\n\t\t<div node-type="_concact" class="webim_contacts_mod">\n\t\t\t<div node-type="contact_slider_root" class="webim_contacts_bd" style="position: relative; overflow: auto;">\n\t\t\t\t<div class="webim_tab_bd">\n\t\t\t\t\t<div class="webim_contacts_group">\n\t\t\t\t\t\t<ul node-type="contact_list" class="webim_contacts_list">\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n\t<div class="private_dialogue_box W_fl" node-type="_container">\n\t\t<div class="chat_head clearfix" node-type="_root">\n\t\t\t<h3 class="chat_title W_fl W_autocut W_f14" id="user" data-user=""></h3>\n\t\t\t<div class="chat_icon W_fr">\n\t\t\t\t<a href="javascript:hide_chat_window();" class="W_ficon ficon_close S_ficon" title="\u5173\u95ed" node-type="_closeBtn">X</a>\n\t\t\t</div>\n\t\t</div>\n\t\t<div class="private_dialogue_body" style="position: relative; height: 319px;">\n\t\t\t<div class="private_dialogue_cont" style="position: relative; top: 0px; overflow: hidden; display: block; visibility: visible; height: 319px;">\n\t\t\t</div>\n\t\t</div>\n\t\t<div class="private_send_box S_bg2" style="position:absolute; bottom:0;" node-type="root">\n\t\t\t<!-- \u89e6\u53d1textarea \u65f6\u52a0 sendbox_mod_focus -->\n\t\t\t<div class="sendbox_mod clearfix S_line1 " node-type="_frameContent">\n\t\t\t\t<!-- \u79c1\u4fe1\u6a21\u5757 -->\n\t\t\t\t<div class="sendbox_mod_l W_fl" node-type="_tipsNode">\n\t\t\t\t\t<div class="sendbox_area S_bg2" node-type="editorNode">\n\t\t\t\t\t\t<textarea id="text_message" class="W_input" style="overflow: hidden; height: 22px;" node-type="_editorNode" placeholder="\u6309\u56de\u8f66\u53d1\u9001\u79c1\u4fe1!"></textarea>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<!-- \u79c1\u4fe1\u6a21\u5757 -->\n\t\t\t</div>\n\t\t</div>\n\t</div>\n</div>\n\n<script type="text/javascript" charset="utf-8">\n\tjQuery(document).ready(function($) {\n\t\tvar ws4redis = WS4Redis({\n\t\t\turi: \'')
        # SOURCE LINE 58
        __M_writer(unicode(WEBSOCKET_URI))
        __M_writer(u"foobar?subscribe-user',\n\t\t\treceive_message: receiveMessage,\n\t\t\theartbeat_msg: ")
        # SOURCE LINE 60
        __M_writer(unicode(WS4REDIS_HEARTBEAT))
        __M_writer(u'\n\t\t});\n\n\t\t$("#text_message").keydown(function(event) {\n\t\t\tif (event.keyCode === 13) {\n\t\t\t\tevent.preventDefault();\n\t\t\t\tsendMessage();\n\t\t\t}\n\t\t});\n\n\t\t$(\'#send_message\').click(sendMessage);\n\n\t\t// send message to the server using Ajax\n\t\tfunction sendMessage() {\n\t\t\t$.post(\'/chat/send_message/\', {\n\t\t\t\tuser: $(\'#user\').attr("data-user"),\n\t\t\t\tmessage: $(\'#text_message\').val()\n\t\t\t}, function(res){\n\t\t\t\t$(\'#text_message\').val("");\n\t\t\t}, "json");\n\t\t}\n\n\t\t// receive a message though the Websocket from the server\n\t\tfunction receiveMessage(msg) {\n\t\t\tconsole.log(msg);\n\t\t\tvar tmp = $("#chat_window_msg_tmp").html();\n\t\t\tMustache.parse(tmp);\n\t\t\tvar html = Mustache.render(tmp, {msg:msg});\n\t\t\tconsole.log(html)\n\t\t\t$(".private_dialogue_cont").append(html);\n\t\t}\n\t\t\n\t\t$(".webim_fold").click(show_chat_window);\n\t\tinit_user_list();\n\t});\n\t\n\tfunction init_user_list(){\n\t\tvar url = "/passport/get_username_list/";\n\t\t$.get(url, {}, function(res){\n\t\t\tif (res.result) {\n\t\t\t\tfor (var i=0; i < res.data.length; i++) {\n\t\t\t\t  \tvar tmp = $("#chatwindow_contact_item_tmp").html();\n\t\t\t\t  \tMustache.parse(tmp);\n\t\t\t\t  \tvar html = Mustache.render(tmp, {username:res.data[i]});\n\t\t\t\t  \t$(".webim_contacts_list").append(html);\n\t\t\t\t};\n\t\t\t\t$(".contacts").click(select_user);\n\t\t\t}else{\n\t\t\t\tconsole.log(res.message);\n\t\t\t}\n\t\t}, "json");\n\t}\n\t\n\tfunction select_user(){\n\t\tvar username = $(this).find(".name").attr("data-user-name");\n\t\t$("#user").text(username);\n\t\t$("#user").attr("data-user", username);\n\t}\n\t\n\tfunction show_chat_window(){\n\t\t$(".webim_chat_window").removeClass("f-hide");\n\t}\n\t\n\tfunction hide_chat_window(){\n\t\t$(".webim_chat_window").addClass("f-hide");\n\t}\n\t\n</script>')
        return ''
    finally:
        context.caller_stack._pop_frame()


