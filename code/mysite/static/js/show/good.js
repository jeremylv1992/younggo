// 初始化页面的效果
$(function(){
	$(".option-list-item").click(select_option);
	$(".num-reduce").bind("click",{val:-1},update_amount);
	$(".num-add").bind("click",{val:1},update_amount);
})

function update_amount(e){
	var val = e.data.val;
	var amount_dom = $("#amount");
	var amount = parseInt(amount_dom.text());
	amount+=val;
	if (amount <= 1) {
		amount = 1;
		$(".num-reduce").addClass("num-reduce-disabled");
	}else{
		$(".num-reduce").removeClass("num-reduce-disabled");
	}
	amount_dom.text(amount);
	update_price();
}

function select_option(){
	var items = $(this).closest(".option-list").find(".option-list-item");
	items.removeClass("option-selected");
	$(this).addClass("option-selected");
	update_price();
}

function get_chose_options(){
	var pairs = [];
	for (var i=0; i < options.length; i++) {
	  	var opt = $("#"+options[i][0]).find(".option-selected");
		if (opt.length == 0) {
			pairs.push([options[i][0], null]);	
		}else{
			pairs.push([options[i][0], opt.attr("data-item")]);
		}
	};	
	return pairs;
}

function get_price(pairs){
	var opt_group = [];
	for (var i=0; i < pairs.length; i++) {
	  	if (pairs[i][1] != null) {
	  		opt_group.push(pairs[i][1]);
	  	}else{
	  		return undefined;
	  	}
	};
	return prices[opt_group.join("+")];
}

function update_price(){
	var pairs = get_chose_options();
	var unit_price = get_price(pairs);
	var amount = parseInt($("#amount").text());
	if (unit_price != undefined) {
		$("#cur_price").text(unit_price*amount);
	};
}

function add_to_cart(){
	var pairs = get_chose_options();
	var unit_price = parseInt(get_price(pairs));
	var amount = parseInt($("#amount").text());
	var good_id = parseInt($("#good_id").attr("data-good-id"));
	if (unit_price == undefined) {
		alert("请选择您需要的商品类别！");
		return false;
	};		
	var params = $.toJSON({
		options:pairs,
		unit_price:unit_price,
		amount:amount,
		good_id:good_id
	})	
	var url = "/cart/add_record/";
	$.post(url, {params:params}, function(res){
		if (res.result) {
			alert("成功添加至购物车，请到购物车提交订单！");
		}else{
			alert(res.message);
		}
	}, "json")
}
