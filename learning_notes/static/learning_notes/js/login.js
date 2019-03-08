// This function runs NOT when the page is ready, but when the page is FULLY LOADED.
// It's basically asynchronous. Given that the form takes time to be rendered, 
// changes made to the form's elements must be called AFTER the form has already been loaded.
$(window).on('load', function() {
  $('#id_username').attr({class:'form-control', placeholder:'Username'});
  $('#id_password').attr({class:'form-control', placeholder:'Password'});
});