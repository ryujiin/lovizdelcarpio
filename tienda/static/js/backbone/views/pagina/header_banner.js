Loviz.Views.Header_banner = Backbone.View.extend({
	el:$('#banner_header'),
	
    template: swig.compile($("#bloque_header_template").html()),

	events: {
	},
	initialize : function () {
		var self = this;
		this.render();
		window.routers.base.on('route',function(e){
			self.aparecer(e);
		});
	},
	render:function (datos) {
		if (datos) {
			var html = this.template(datos);
		}else{
			var html = this.template();
		}
        this.$el.html(html);
	},
	aparecer:function (e) {
		if (e==='carro'|| e==='producto_single' || e==='comprar' || e==='ingresar') {
			this.$el.hide();
		}else{
			this.$el.show();
			if (e!=='root') {
				this.$el.addClass('banner')
			}else{
				this.$el.removeClass('banner')
			}
		}
	},
	cambiar_genero:function (genero) {
		var modelo = window.collections.generos.findWhere({slug:genero});
		datos = modelo.toJSON();
		datos.titulo = modelo.toJSON().nombre
		this.render(datos);
	},
	cambiar_categoria:function () {
		var cate = window.app.catalogo.categoria;
		var modelo = window.collections.categorias.findWhere({slug:cate});
		var datos = modelo.toJSON()
		datos.foto = modelo.toJSON().imagen
		datos.titulo = modelo.toJSON().nombre
		this.render(datos);
	}
});