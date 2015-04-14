$(function(){
// 初始化购物车页面的效果
	$("button.cart_del_btn").click(remove_item_from_cart);
	$("a.amount-trigger-minus").bind("click",{val:-1},server_update_amount);
	$("a.amount-trigger-plus").bind("click",{val:1},server_update_amount);
	update_order_total()
})

function remove_item_from_cart(){
	var confirm_res = confirm("确认从购物车中移除选中的商品");
	if (!confirm_res) {
		return false;
	};
	var $cart_item = $(this).closest(".cart_item");
	var $cart_order = $cart_item.closest(".cart_order")
	var item_id = $cart_item.attr("data-item-id");
	var url = "/cart/remove_record/";
	$.post(url, {item_id:item_id}, function(res){
		if (res.result) {
			$cart_item.remove();
			if ($cart_order.find(".cart_item").length==0) {
				$cart_order.remove();
			};
			update_order_total()
		}else{
			alert(res.message);
		}
	}, "json");
	
}

function server_update_amount(e){
	var val = e.data.val;
	var $cart_item = $(this).closest(".cart_item");
	var $amount = $cart_item.find("input[name='amount']");
	
	var item_id = parseInt($cart_item.attr("data-item-id"));
	var amount = parseInt($amount.val())+val;
	
	var url = "/cart/update_amount/";
	$.post(url, {item_id:item_id, amount:amount}, function(res){
		if (res.result) {
			change_amount($cart_item, amount);
			update_order_total();
		}else{
			alert(res.message);
		}
	}, "json")
	
}

function change_amount($cart_item, val){
	var $amount_minus = $cart_item.find(".quantity-item").find(".amount-trigger-minus");
	var $subtotal = $cart_item.find(".subtotal-item").find("strong.u-price");
	
	var $amount = $cart_item.find("input[name='amount']");
	var $unit_price = $cart_item.find("input[name='unit_price']");
	
	var amount = val;
	if (amount <= 1) {
		amount = 1;
		$amount_minus.addClass("z-amount-trigger-disabled");
	}else{
		$amount_minus.removeClass("z-amount-trigger-disabled");
	}
	$amount.val(amount);
	$subtotal.text($unit_price.val()*amount);
}

function update_order_total(){
	var num_total = 0;
	var goods_total = 0;
	var total = 0;
	$("#cart_list").find(".cart_order").each(function(){
		$(this).find(".cart_item").each(function(){
			var u_pirce = $(this).find("input[name='unit_price']").val();
			var amount = $(this).find("input[name='amount']").val();
			num_total += amount;
			var item_total = u_pirce*amount;
			goods_total += item_total;
			total += item_total;
		})
		var ext_fare = parseInt($(this).find(".trans_fare_total").attr("date-trans-fare"));
		total += ext_fare;
	})
	$total_mod = $("#amount_mod");
	$total_mod.find(".info_numTotal").text(total);
	$total_mod.find(".info_goodsTotal").text(goods_total);
	$total_mod.find(".info_total").text(total);
}
