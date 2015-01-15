Loviz.Routers.Base = Backbone.Router.extend({
	routes : {
		"" : "root",
		'carro/':'carro',
		'comprar/':'comprar',
		'catalogo/':'catalogo',		
		'catalogo/:genero/':'catalogo',
		'catalogo/:genero/:categoria/':'catalogo_categoria',
		'producto/:slug/':'producto_single',
		'pagina/:slug/':'pagina',
		'carro':'carro',
		'*notFound': 'notFound',
	},
	initialize : function () {
		window.app.catalogo = {};		
  	},
	root : function () {
		var self = this;
		this.pagina('home')
		window.views.head.todoDefault();
	},
	carro : function () {
		window.app.page = 'carro';
		window.views.carro.render();
	},
	catalogo:function (genero) {
		window.app.page = 'catalogo'
		window.app.catalogo.genero = genero;

		window.collections.catalogo.reset();
		
		if (window.views.catalogo === undefined) {
			window.views.catalogo = new Loviz.Views.Catalogo({
				collection:window.collections.catalogo
			});
		};
		window.views.catalogo.render();
		window.collections.catalogo.buscar_productos()
	},
	catalogo_categoria:function () {
		window.app.page = 'catalogo'

	},
	producto_single:function (slug) {
		window.app.page = 'producto_single'

		var modelo = window.collections.producto_single.findWhere({slug:slug});
		if (modelo===undefined) {
			modelo = new Loviz.Models.Producto_single()
			modelo.buscar(slug)
		}else{
			if (window.models.producto_single.id!==modelo.id) {
				window.models.producto_single.set(modelo.toJSON());
			}else{
				window.views.producto_single.render();
			}
		}
	},
	pagina:function (slug) {
		console.log('es una pagina '+slug);
		var modelo = window.collections.paginas.findWhere({slug:slug});
		if (modelo === undefined) {
			modelo = new Loviz.Models.Pagina();
			modelo.buscar(slug);
		}else{
			window.models.pagina.set(modelo.toJSON());
		}
	},
	carro:function () {
		window.app.page = 'carro';
		window.views.carro.render();
	},
	notFound:function () {
		this.error_404 = new Loviz.Views.Pagina_404();
	},
});