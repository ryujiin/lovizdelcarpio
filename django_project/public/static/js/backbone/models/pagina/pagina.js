Loviz.Models.Pagina = Backbone.Model.extend({
	urlRoot : '/api/tienda/pagina/',
	buscar :function (slug) {
		var self=this;
		this.fetch({
			data:$.param({slug:slug})
		}).done(function (data) {
			window.models.pagina.set(data);
			window.collections.paginas.add(self)
		})
	}
});