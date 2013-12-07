$(function(){
    $("form input[type!='submit']").live("focus.labelFx", function(){
		$(this).prev().hide();
	})
	.live("blur.labelFx", function(){
		$(this).prev()[!this.value ? "show" : "hide"]();
	})
	.trigger("blur.labelFx");
});
