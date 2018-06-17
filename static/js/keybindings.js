/* Initialise soundmanager */
soundManager.setup({
  url: '/static/soundmanager2.swf',
  flashVersion: 8, // optional: shiny features (default = 8)
  // optional: ignore Flash where possible, use 100% HTML5 mode
  // preferFlash: false,
  onready: function() {
    // Ready to use; soundManager.createSound() etc. can now be called.
  }
});

/* Disable normal arrow key behaviours */
window.addEventListener("keydown", function(e) {
    // disable arrow keys
    if([37, 38, 39, 40].indexOf(e.keyCode) > -1) {
        e.preventDefault();
    }
}, false);

$(document).bind('keydown', 'esc', function(){
   //$('#navigateUp')[0].click();
   window.location.href = $('#navigateUp')[0].href;
   //alert('Esc pressed');
});

$(document).bind('keydown', 'p', function(){
   if ($('#playButton').length) {
   	   $('#playButton')[0].click();
   }
});

$(document).bind('keydown', '.', function(){
   if ($('#nextButton').length) {
       $('#nextButton')[0].click();
   }
});

$(document).bind('keydown', ',', function(){
   if ($('#previousButton').length) {
       $('#previousButton')[0].click();
   }
});

$(document).bind('keydown', 'right', function(){
   $(':focus').next('.dirEntry').focus();
   /*
   for (y=1; y<10; y++) {
   	   console.log(x);
   	   x = x.next();
   }*/
});