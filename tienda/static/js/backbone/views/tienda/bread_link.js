Loviz.Views.Bread_link = Backbone.View.extend({
    tagName: 'li',
    events: {
    },
    template: swig.compile($("#bread_link_template").html()),
    initialize: function () {
    },    
    render: function () {
        var album = this.model.toJSON()
        var html = this.template(album);
        this.$el.html(html);
        return this;
    },
});