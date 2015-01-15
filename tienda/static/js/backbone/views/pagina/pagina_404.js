Loviz.Views.Pagina_404 = Backbone.View.extend({
	el:$('#contenido'),
	template : swig.compile($("#pagina_404_template").html()),
	events :{
	},
	initialize: function () {
		this.render();
	},
	render:function () {
		var html = this.template();
	    this.$el.html(html);
	},
});