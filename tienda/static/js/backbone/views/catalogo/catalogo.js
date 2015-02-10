Loviz.Views.Catalogo = Backbone.View.extend({
	className: 'cotenedor',
	el:$('#contenido'),
	
    template: swig.compile($("#catalogo_template").html()),

	events: {
		'click .bloque_filtro input':'mostrar_clear_filtro',
		'click .clear_filtros':'borrar_filtros',
	},
	initialize : function () {
		var self = this;
		this.listenTo(window.collections.catalogo, "add", this.addOne, this);
		this.banner_top = new Loviz.Views.Header_categoria({model: new Loviz.Models.Categoria()});
		this.view_categoria = new Loviz.Views.Categorias({collection: window.collections.categorias});
	},
	render:function () {
		var html = this.template();
        this.$el.html(html);
        this.view_categoria.render();
	},
	addOne: function (produ) {
		var producto = new Loviz.Views.Producto({ model: produ });
		this.$('.productos').append(producto.render().el);
		producto.$el.addClass('col-md-4');
	},
	no_productos:function () {
		console.log('no hay productos');
	},
});