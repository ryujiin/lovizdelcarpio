Loviz.Views.Imagen_Carrusel = Backbone.View.extend({
    className: 'imagen_carrusel',
    template:swig.compile($("#imagen_carrusel_template").html()),
    events: {
    },    
    initialize: function () {
        this.render();
    },
    render:function () {
        var modelo = this.model;
        var html = this.template(modelo);
        this.$el.html(html);
    },
});