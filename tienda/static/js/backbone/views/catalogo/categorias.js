Loviz.Views.Categorias = Backbone.View.extend({
    className: 'bloque categorias',
    events: {
    },
    template: swig.compile($("#filtro_template").html()),
    
    initialize: function () {
        var self = this;
        this.render();
        window.routers.base.on('route',function(e){
            if (e==='catalogo_categoria') {
                self.$el.hide();
            }else{
                self.$el.show();
            }
        });
    },
    render: function () {
        var json_filtro = {'titulo': 'Categorias'}
        var html = this.template(json_filtro);
        this.$el.html(html);
        this.buscar_categorias();
    },
    addCategoria:function (cate) {   
        var link = new Loviz.Views.Categoria_link({ model: cate });
        this.$('.filtros').append(link.render().el);
    },
    buscar_categorias:function () {
        var self = this;
        if (window.collections.categorias.length===0) {
            window.collections.categorias.fetch().done(function () {
                self.addCategorias();
            })
        }else{
            this.addCategorias();
        }
    },
    addCategorias:function () {
        var coleccion = window.collections.categorias.where({genero_slug:window.app.catalogo.genero});
        coleccion.forEach(this.addCategoria,this);
    },
});