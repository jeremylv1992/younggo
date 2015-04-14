// 初始化检验订单页面的效果
$(function(){
	$(".address_add_btn").click(show_addr_tmp);
	init_address();
})

function init_address(){
	var url = "/order/addr/get_all/";
	$.get(url, {}, function(res){
		if (res.result) {
			$(".my_address_list").find(".address-item:not(.address-item-add)").remove();
			for (var i=0; i < res.data.length; i++) {
			  	var tmp = $("#address_item_show").html();
			  	Mustache.parse(tmp);
			  	var html = Mustache.render(tmp, res.data[i]);
				$(".my_address_list").find(".address-item-add").before(html);			  	
			};
			$(".my_address_list").find(".address-item:not(.address-item-add)").click(select_addr);
		}else{
			console.log(res.message);
		}
	}, "json");
}

function select_addr(){
	var $addr_container = $(this);
	var cur_address_id = $addr_container.attr("data-address-id")
	var cur_class = $addr_container.attr("data-current");
	var cur_addr = $addr_container.attr("data-intro");
	
	$(".my_address_list").find(".address-item").removeClass(cur_class);
	$addr_container.addClass(cur_class);
	
	$(".transport_info").find("span").text(cur_addr);
	$("#order_frmSave").find("input[name='address_id']").val(cur_address_id);
}

function show_addr_tmp(){
	var $container = $(this).closest(".address_item_container");
	var tmp = $("#address_item_tmp").html();
	Mustache.parse(tmp);
	var html = Mustache.render(tmp, {});
	$container.addClass("z-address-item-modify");
	$container.append(html);
}

function close_addr_tmp(){
	var $modal = $(".modify-address-modal");
	var $container = $modal.closest("li.address-item");

	$modal.remove();
	$container.removeClass("z-address-item-modify");
}

function submit_addr(){
	var $modal = $(".modify-address-modal");
	
	var params = {
		id: $modal.find("input[name='id']").val(),
		name: $modal.find("input[name='consignee']").val(),
		tel: $modal.find("input[name='mobile']").val(),
		second_tel: $modal.find("input[name='phone']").val(),
		addr: $modal.find("textarea[name='address']").val(),
	}
	
	var url = "/order/addr/update/";
	$.post(url, params, function(res){
		if (res.result){
			close_addr_tmp();
			init_address();
		}else{
			alert(res.message);			
		}
	}, "json")
}
