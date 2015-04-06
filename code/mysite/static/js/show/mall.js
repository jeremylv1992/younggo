// 初始化商城页面
$(function(){
	pull_stores(0, 8);
})

function pull_stores(begin, num){
	var url = '/store/get_store_list/';
	$.get(url, {begin:begin, num:num}, function(res){
		if (res.result) {
			for (var i=0; i < res.data.length; i++) {
			  	add_store(res.data[i]);
			};
		}else{
			console.log(res.message);
		}
	}, "json");
}

function add_store(obj){
	var tmp = $("#store_item").html();
	Mustache.parse(tmp);
	var html = Mustache.render(tmp, obj);
	$(".hys_list").find("ul").append(html);
}
