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
        if (e==='root') {
            this.$el.hide();
        }else{
            this.$el.show();
            this.ver_links();
        }
    },
    ver_links:function () {
        if (window.app.page==='catalogo') {
            json = {link:'/',nombre:'Home'};
            
        };
    }
});