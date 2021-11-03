$(document).ready( function() {
  $('a[href^="/account/logout"]').on("click", function() {
    $.ajax( $(this).attr('href') )
      .done(function() {
       // Choose direction here
       window.location.href = "/pages/contacts";
      });
    return false;
  });
});
