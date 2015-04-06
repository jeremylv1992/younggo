// 初始化商店页面
$(function(){
	pull_goods(0, 8);
})

function pull_goods(begin, num){
	var store_id = $("#store_info").attr("data-val");
	var params = {
		store_id: store_id,
		begin: begin,
		num: num
	}
	var url = '/good/get_good_list/';
	$.get(url, params, function(res){
		if (res.result) {
			for (var i=0; i < res.data.length; i++) {
				res.data[i]['store_id'] = store_id;
			  	add_good(res.data[i]);
			};
		}else{
			console.log(res.message)
		}
	}, "json")
}

function add_good(obj){
	var tmp = $("#good_item").html();
	Mustache.parse(tmp);
	var html = Mustache.render(tmp, obj);
	$(".pro_list").append(html);
}
