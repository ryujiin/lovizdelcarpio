Loviz.Views.Header_categoria = Backbone.View.extend({
	el:$('#banner_header_catalogo'),
	template : swig.compile($("#header_categoria_template").html()),
	className:'bloque',
	events :{
	},
	initialize: function () {
		var self = this;
		window.routers.base.on('route',function(e){
			self.aparecer(e);
		});
	    this.listenTo(this.model, "change", this.render, this);
	},
	render:function () {
		var modelo = this.model.toJSON();		
		var html = this.template(modelo);
	    this.$el.html(html);
	},
	aparecer:function (e) {
		if (window.app.page!=='catalogo') {
			console.log
			this.$el.hide();
		}else{
			this.$el.show();
		}
	},
	modificar_modelo:function (modelo) {
		this.model.set(modelo.toJSON());
	}
})