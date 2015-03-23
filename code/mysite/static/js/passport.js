
function init_inputs(){
	$(".inputs").find("input").focus(function(){
		$(this).next().addClass("z-hide");
		var $tips = $($(this).closest(".inputs").nextAll().filter(".auth-tips")[0]);
		var x_pos = $(this).offset().left+parseFloat($(this).css("width"))+20 ;
		var y_pos = $(this).offset().top -parseFloat($(this).css("height"))/2;
		console.log(x_pos, y_pos)
		$tips.css({top:y_pos, left:x_pos});
		$tips.removeClass("z-hide")
	})
	$(".inputs").find("input").blur(function(){
		if ($(this).val() == "") {
			$(this).next().removeClass("z-hide");
		};	
		$($(this).closest(".inputs").nextAll().filter(".auth-tips")[0]).addClass("z-hide")
	})
	$(".inputs").click(function(){
		$(this).find("input").focus();
	})
}


function check_blank(e){
	$input = $(this);
	var val = $input.val();
	if (val == "") {
		$input.addClass("error");
		$input.closest(".inputs").next().find(".err_msg").text("该值不可为空");
		return true;
	}
	$input.removeClass("error");
	$input.closest(".inputs").next().find(".err_msg").text("");
	return false;
}