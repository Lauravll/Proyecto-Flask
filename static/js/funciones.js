/*Con respuestas con Callback y utiliza un parámetro */
$(document).ready(function(){
    $('input.autocomplete').autocomplete({
      data: {
        "Apple": null,
        "Html": null,
        "Microsoft": null,
        "Google": 'https://placehold.it/250x250'
      },
      onAutocomplete: function(texto){
          console.log(`diste clic ${texto}`);
          respuesta.innerHTML = `<h3>Soy un elemento dinámico: ${texto}</h3> `
      }
    });
  });

  const respuesta = document.getElementById('respuesta');

$(document).ready(function(){
  $('.scrollspy').scrollSpy({
    scrollOffset: 30
  }
  );
});

$(document).ready(function(){
    $('select').formSelect();
  });

/*Para el preloader*/
window.addEventListener('load', () => {
  /*Si lo quiero reetrazar, si fuera de un sitio externo no seria necesario */
  //setTimeout(carga, 2000);
  carga();
  function carga(){
    /*Detectamos el contenido y con className reemplazamos las clases que estan en el hide*/
    document.getElementById('contenido').className = 'animated fadeInDown';
    /*Escondemos el preloader*/
    document.getElementById('circulo').className = 'hide';

}
}
)

var boton = document.getElementById("prueba");
boton.onclick = function(){
   // aca tu codigo
   if (document.getElementById('slide-out').className == 'sidenav sidenav-fixed hide-on-large-only'){
    document.getElementById('slide-out').className = 'sidenav sidenav-fixed show-on-large-only';
    $('header').removeClass("sticky");
    $('main').removeClass("sticky");
    $('footer').removeClass("sticky");
   }
   else{
    document.getElementById('slide-out').className = 'sidenav sidenav-fixed hide-on-large-only';
   
    $('header').addClass("sticky");
    $('main').addClass("sticky");
    $('footer').addClass("sticky");
   }
   
}