Loviz.Routers.Base = Backbone.Router.extend({
	routes : {
		"" : "root",
		'carro/':'carro',
		'comprar/':'comprar',
		'catalogo/:categoria/':'catalogo',
		'producto/:slug/':'producto_single',
		'pagina/:slug/':'pagina',
		'carro':'carro',
		'*notFound': 'notFound',
	},
	initialize : function () {
  	},
	root : function () {
		window.app.page = 'home'
		var self = this;
		this.pagina('home');
		window.app.slug='home';
		window.views.head.todoDefault();
	},
	carro : function () {
		window.app.page = 'carro';
		window.views.carro.render();
	},
	catalogo:function (categoria) {
		var self = this;
		window.app.page = 'catalogo';
		window.app.slug = categoria;

		window.collections.catalogo.reset();
		var modelo = window.collections.categorias.findWhere({slug:window.app.slug});

		if (window.views.catalogo === undefined) {
			window.views.catalogo = new Loviz.Views.Catalogo({
				collection:window.collections.catalogo,
			});
		};
		window.views.catalogo.render();
		window.collections.catalogo.buscar_productos();
		window.views.catalogo.banner_top.modificar_modelo(modelo);
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
			if (modelo.id===window.models.pagina.id) {
				window.views.pagina.render();
			}else{
				window.models.pagina.set(modelo.toJSON());
			}
		}
	},
	carro:function () {
		window.app.page = 'carro';
		window.app.slug='carro';
		window.views.carro.render();
	},
	notFound:function () {
		this.error_404 = new Loviz.Views.Pagina_404();
	},

});