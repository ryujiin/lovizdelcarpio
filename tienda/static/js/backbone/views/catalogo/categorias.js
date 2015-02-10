Loviz.Views.Categorias = Backbone.View.extend({
    className: 'bloque categorias',
    events: {
    },
    template: swig.compile($("#filtro_template").html()),
    
    initialize: function () {
        var self = this;
    },
    render: function () {
        var json_filtro = this.crear_json();
        var html = this.template(json_filtro);
        this.$el.html(html);
        $('#categoria_producto').append(this.$el);
        this.addCategorias();
    },
    addCategoria:function (cate) {   
        var link = new Loviz.Views.Categoria_link({ model: cate });
        this.$('.filtros').append(link.render().el);
    },
    addCategorias:function () {
        var coleccion = this.collection.where({padre:window.app.slug});
        coleccion.forEach(this.addCategoria,this);
    },
    crear_json:function () {
        var json = {'titulo': 'Categorias'}
        return json
    }
});