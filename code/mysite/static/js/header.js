// 初始化 header中的事件
$(function(){
	$(".sel_area_change").mouseover(function(){
		$(this).addClass("selected");
	})
	$(".sel_area_change").mouseout(function(){
		$(this).removeClass("selected");
	})
	
	init_areas();
})

function init_areas(){
	var url = "/school/get_school_list/";
	$.get(url, {}, function(res){
		if (res.result) {
			for (var i=0; i < res.data.length; i++) {
				add_area(res.data[i]);
			};
		}else{
			console.log(res.message);
		}
	}, "json");
}

function add_area(obj){
	var tmp = $("#area_tmp").html();
	var dom = Mustache.render(tmp, obj);
	$(".sel_area_box").find("table.sab_table").find("tbody").append(dom);
}
