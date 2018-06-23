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
   if ($('#navigateUp').length) {
   	$('#navigateUp')[0].click();
   }
});

$(document).bind('keydown', 'Shift+p', function(){
   if ($('#playButton').length) {
   	   $('#playButton')[0].click();
   }
});

$(document).bind('keydown', 'Shift+f', function(){
   if ($('#nextButton').length) {
       $('#nextButton')[0].click();
   }
});

$(document).bind('keydown', 'Shift+b', function(){
   if ($('#previousButton').length) {
       $('#previousButton')[0].click();
   }
});

$(document).bind('keydown', 'right', function(){
   $(':focus').parent().next().children('a.dirThumb,a#navigateUp').focus();
   // Make sure the whole thumb is visible
   scrollThumbIntoView(element.parent());
});

$(document).bind('keydown', 'left', function(){
   $(':focus').parent().prev().children('a.dirThumb,a#navigateUp').focus();
});

$(document).bind('keydown', 'down', function(){
   columns = colCount();
   element = $(':focus')
   for (n=0; n<columns; n++) {
      element = element.parent().next().children('a.dirThumb,a#navigateUp');
   }
   element.focus();
   // Make sure the whole thumb is visible
   scrollThumbIntoView(element.parent());
});

$(document).bind('keydown', 'up', function(){
   columns = colCount();
   element = $(':focus')
   for (n=0; n<columns; n++) {
      element = element.parent().prev().children('a.dirThumb,a#navigateUp');
   }
   element.focus();
});

function scrollThumbIntoView(element) {
   var elementBottom = element.position().top + element.outerHeight(true);
   var viewportBottom = window.scrollY + window.innerHeight;

   console.log("Element bottom: " + elementBottom + " , Viewport bottom: " + viewportBottom);

   if (elementBottom > viewportBottom) {
     var amountToScroll = elementBottom - viewportBottom;
     var y = $(window).scrollTop();  // current y position on the page
     $(window).scrollTop(y+amountToScroll);
   }
}

function colCount() {
   size = Foundation.MediaQuery.current;
   columns = 6
   if (size == 'medium') {
      columns = 3
   } else if (size == 'small') {
      columns = 2
   }
   return columns;
}

function rowCount() {
   thumbs = $('a.dirThumb').length;
   cols = colCount();
   rows = Math.ceil(thumbs / cols);
   return rows;
}

function getRow() {
   // First find the index of the thumb we're on
   thumbs = $('a.dirThumb');
   idx = -1;
   $.each( thumbs, function( index, value ) {
      if ($(value).is(":focus")) {
         idx = index;
      }
   });
   // Now, see what row we're on
   cols = colCount();
   row = Math.floor(idx / cols) + 1;
   return row;
}
