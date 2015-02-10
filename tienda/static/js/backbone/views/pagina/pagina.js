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
	    if (this.model.toJSON().css) {
	    	this.$el.addClass(this.model.toJSON().css)
	    };
	    if (modelo.slug!=='home') {
	    	var titulo = this.model.toJSON().titulo+' || LovizDelCarpio.com lo mejor en calzado para dama, caballeros y niños';
	    	window.views.head.modificar_titulo(titulo)	
	    };
	    
	},
})
