//Loviz Tienda
$(document).ready(function(){
	console.log('main.js loaded');
    
    //Urls
    window.routers.base = new Loviz.Routers.Base();

    //Modelos
    window.models.usuario = new Loviz.Models.Usuario();
    window.models.carro = new Loviz.Models.Carro();
    window.models.producto_single = new Loviz.Models.Producto_single();
    window.models.pagina = new Loviz.Models.Pagina();
    window.models.header_banner = new Loviz.Models.Header_banner();

    //Collecciones
    window.collections.paginas = new Loviz.Collections.Paginas();
    window.collections.bloques = new Loviz.Collections.Bloques();
    window.collections.carruseles = new Loviz.Collections.Carruseles();
    window.collections.menus = new Loviz.Collections.Menus();
    window.collections.categorias = new Loviz.Collections.Categorias();
    window.collections.producto_single = new Loviz.Collections.Productos_Single();
    window.collections.catalogo = new Loviz.Collections.Productos();

    //Vista Tienda
    

    //buscar
    window.collections.bloques.fetch().done(function () {
        window.collections.carruseles.fetch().done(function () {
            window.collections.menus.fetch().done(function () {                
                window.collections.categorias.fetch().done(function () {
                    iniciar_vistas();
                    Backbone.history.start({
                        pushState:true,
                    });
                })                
            })
        })
    });

    function iniciar_vistas () {
        window.views.body = new Loviz.Views.Body( $('body') );
        window.views.head = new Loviz.Views.Header();
        window.views.bread = new Loviz.Views.Bread();
        window.views.pagina = new Loviz.Views.Pagina({
            model:window.models.pagina
        });
        window.views.carro = new Loviz.Views.Carro({
            model:window.models.carro
        });
        window.views.producto_single = new Loviz.Views.Producto_single({
            model: window.models.producto_single
        });
        window.views.mini_carro = new Loviz.Views.Mini_carro({
            model:window.models.carro
        });
        window.views.mini_usuario = new Loviz.Views.Mini_usuario({
            model:window.models.usuario
        });
        galleta = window.views.body.obt_galleta();
    }

    //Funcion para el CRF
    function getCookie(name){
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?  
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }    
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        } 
    });
});