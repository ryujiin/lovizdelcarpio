Loviz.Views.Newsletter = Backbone.View.extend({
    el:$('#newsletter'),
    template : swig.compile($("#newsletter_template").html()),
    events: {
    	'keydown':'enviar_enter',
    },    
    initialize: function () {
        this.render();
        this.listenTo(this.model, "change", this.render, this);
    },    
    render: function () {
        var modelo = this.model.toJSON();
        var html = this.template(modelo);
        this.$el.html(html);
    },
    enviar_enter:function (e) {
    	var keycode = e.keyCode;
    	if (keycode === 13) {
            var email = this.$('.input_newsletter').val();
    		var verificado = window.views.body.validarEmail(email);
            this.enviar_suscritos(email,verificado);
    	}
    },
    enviar_suscritos:function (email,verificado) {
        if (verificado===true) {
            this.correcto();
        }else{
            this.fallo();
        }
    },
    fallo:function () {
        this.$('.input_newsletter').val('');
        this.$('.input_newsletter').addClass('error_sombra');
        this.model.set('error',true);
    },
    correcto: function () {
        var email = this.$('.input_newsletter').val();
        this.model.set({'email':email,'user':window.models.usuario.id});
        this.model.save();
    }
});