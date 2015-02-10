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
		this.view_newslatter = new Loviz.Views.Newsletter({
			model:new Loviz.Models.Newsletter()
		});
		window.collections.menus.forEach(this.vista_menu,this);
		window.collections.bloques.forEach(this.vista_bloques,this);
		window.collections.carruseles.forEach(this.vista_carrusel,this);
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
	validarEmail:function( email ) {
		expr = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
		if ( !expr.test(email) ){
		 	return false
		}else{
		 	return true
		}
	},
	vista_menu:function (modelo) {
		var menu = new Loviz.Views.Menu({
			model:modelo
		});
	},vista_bloques:function (modelo) {
		var bloque = new Loviz.Views.Bloque({
			model:modelo
		})
	},
	vista_carrusel:function (modelo) {
		var carrusel = new Loviz.Views.Carrusel({
			model:modelo
		})
	},
});
