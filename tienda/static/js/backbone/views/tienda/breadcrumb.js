Loviz.Views.Bread = Backbone.View.extend({
    el:$('#breadcrumb'),
    events: {
    },    
    initialize: function () {
        var self = this;
        window.routers.base.on('route',function(e){
            self.aparecer(e);
        });
    },
    aparecer:function (e) {
        if (e==='catalogo' || e === 'producto_single') {
            this.$el.show();
            this.generar_links();
        }else{
            this.$el.hide();
        }
    },
    generar_links:function () {
        this.$('.breadcrumb').empty();
        this.ver_links();
        this.linkhome();
    },
    ver_links:function () {
        var cate = window.collections.categorias.findWhere({slug:window.app.slug});
        this.nuevolink(cate);
        this.verificar_padre(cate);
    },
    nuevolink:function (cate) {
        var link = new Loviz.Views.Bread_link({model:cate});
        this.$('.breadcrumb').prepend(link.render().el);
    },
    linkhome:function () {
        var modelo_home = new Loviz.Models.Categoria();
        modelo_home.set({slug:'/',nombre:'Home',home:true});
        var link_home = new Loviz.Views.Bread_link({model:modelo_home});
        this.$('.breadcrumb').prepend(link_home.render().el);
    },
    verificar_padre:function (cate) {
        if (cate.toJSON().padre!==null) {
            cate = window.collections.categorias.findWhere({slug:cate.toJSON().padre});
            this.nuevolink(cate);
        };
    },
});