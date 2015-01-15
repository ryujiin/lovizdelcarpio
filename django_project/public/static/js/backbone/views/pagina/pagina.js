Loviz.Views.Pagina = Backbone.View.extend({
	el:$('#contenido'),
	template : swig.compile($("#pagina_template").html()),
	events :{
	},
	initialize: function () {
		var self = this;
		this.listenTo(this.model, "change", this.render, this);
	},
	render:function () {
		var modelo = this.model.toJSON();
		var html = this.template(modelo);
	    this.$el.html(html);
	    this.rellenar_pag();
	    if (this.model.toJSON().css) {
	    	this.$el.addClass(this.model.toJSON().css)
	    };
	},
	rellenar_pag:function () {
		this.llenar_bloques();
		this.llenar_carruseles();
	},
	llenar_bloques:function () {
		var self = this;
		var id_pagina = this.model.id;
		if (id_pagina!==undefined) {
			var bloques = window.collections.bloques.where({pagina_mostrar:id_pagina})
			if (bloques.length === 0) {
				bloques = new Loviz.Collections.Bloques()
				bloques.fetch({
					data:$.param({pagina:id_pagina})
				}).done(function () {
					bloques.forEach(self.addbloque,self);
				});
			}else{
				bloques.forEach(this.addbloque,this);
			}
		};
	},
	addbloque:function (bloque) {
		var views_bloque = new Loviz.Views.Bloque({model:bloque});
		debugger;
	},
	llenar_carruseles:function () {
		var self = this;
		var id_pagina = this.model.id;
		var carruseles = window.collections.carruseles
	},
	addcarrusel:function (carrusel) {
		var modelo = new Loviz.Models.Carrusel();
		modelo.set(carrusel)
		var views_carrusel = new Loviz.Views.Carrusel({model:modelo})
		//this.lista_carrusel(views_carrusel);
	},
	lista_carrusel:function (view) {
		this.num_carrusel=0
		var modelo_view = view.model.toJSON();
		var modelo = modelo_view.modelo;
		this.carrusel_contenedor=view;
		if (modelo = 'Producto') {
			window.collections.productos.forEach(this.addproducto(),this);
		};
	},
	addproducto:function (producto) {
		if (this.num_carrusel<5) {
			console.log(producto)

			this.num_carrusel++
		};
	}
})
