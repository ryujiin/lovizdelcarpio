Loviz.Views.Body = Backbone.View.extend({
	events: {
		'click .link' : 'linknormal',
		'click .logo' : 'navega_home',
		'blur .requerido':'verificar_input_requerido',
		'blur input[type=password]':'verificar_pass',
		'click .login_face' : 'login_face',
		'click .link':'link_intero',
	},
	initialize : function ($el) {
		var self = this;
		this.$el = $el;
		this.cargar_menus();
		this.cargar_bloques();
		this.view_banner_header = new Loviz.Views.Header_banner();
		this.view_newslatter = new Loviz.Views.Newsletter({
			model:new Loviz.Models.Newsletter()
		});
	},
	link_intero:function (e) {
		e.preventDefault();
		var link = e.currentTarget.pathname;
		
		window.routers.base.navigate(link, {trigger:true});
	},
	obt_galleta : function(){
		var galleta = $.cookie('carrito');
		if (galleta==null) {
			console.log('veamos');
			var session = getRandomChar();
			$.cookie('carrito',session,{ expires: 1, path: '/'});
			galleta = session;
		};
		function getRandomChar() {
			numCara = 50
			chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
			pass ='';
			for (i=0;i<numCara;i++) {
				x = Math.floor(Math.random()*62);
				pass+=chars.charAt(x);
			};
			return pass
		};
		return galleta
	},
	modificar_cabezera:function (titulo,descripcion) {
		document.title=titulo + ' | LovizdelCarpio.com'
		$('meta[name="description"]').remove();
		$('head').append("<meta name='description' content='"+descripcion+"'>");
	},
	cargar_bloques:function () {
		var self = this;
		this.coleccion_bloques = new Loviz.Collections.Bloques();
		this.coleccion_bloques.fetch({
			data:$.param({cms:'slug'})
		}).done(function () {
			self.coleccion_bloques.forEach(self.crear_bloque,self)
		})
	},
	crear_bloque:function (bloque) {
		window.collections.bloques.add(bloque)
		var views_bloque = new Loviz.Views.Bloque({model:bloque});
	},
	cargar_menus:function () {
		var self = this;
		this.coleccion_menus = new Loviz.Collections.Menus();
		this.coleccion_menus.fetch({
			data:$.param({cms:'slug'})
		}).done(function () {
			self.coleccion_menus.forEach(self.crear_menu,self)
		});
	},
	crear_menu:function (menu) {
		window.collections.menus.add(menu);
		var views_menu = new Loviz.Views.Menu({model:menu});
	},
	validarEmail:function( email ) {
		expr = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
		if ( !expr.test(email) ){
		 	return false
		}else{
		 	return true
		}
	},
});
