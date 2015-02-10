Loviz.Collections.Productos = Backbone.Collection.extend({
	model : Loviz.Models.Producto,
	url : '/api/catalogo/',
	
	initialize:function () {
	},
	buscar_productos:function () {
		var self = this;
		if (window.app.slug) {
			this.fetch({
				data:$.param({categoria:window.app.slug})
			}).done(function () {
				if (self.length===0) {
					window.views.catalogo.no_productos();
				};
			})
		};
	}
});