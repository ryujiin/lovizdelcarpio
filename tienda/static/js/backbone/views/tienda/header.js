Loviz.Views.Header = Backbone.View.extend({
    el:$('head'),
    events: {
    },    
    initialize: function () {
    },    
    modificar_titulo:function (titulo) {
        this.$('title').html(titulo);
    },
    modificar_descripcion : function (desc) {
        this.$('meta[name=description]').attr('content',desc)
    },
    todoDefault:function () {
        var titulo = 'Loviz DelCarpio :: lovizdelcarpio.com donde encontras los mejores pantuflas, botas, sandalias y calzado'
        var description = 'Loviz DelCarpio® , Encontraras lo mejor en pantuflas, sandalias, botas, flats y demas. Envio Gratis para todo el peru por compras mayores a S/.60.00'
        this.$('title').html(titulo);
        this.$('meta[name=description]').attr('content',description)
    }
});