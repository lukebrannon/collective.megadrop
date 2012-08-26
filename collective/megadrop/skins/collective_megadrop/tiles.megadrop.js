jQuery(function($) {
  $('div[data-tile]').each(function() {
      $(this).addClass('tile-editable');
      var href = $(this).attr('data-tile');
      var edithref = href.replace(/@@/, '@@edit-tile/');
      $('<a class="tile-edit-link" href="' + edithref + '"><img height="16" src="pencil_icon.png" width="16" />')
        .appendTo($(this))
        .prepOverlay({
            subtype: 'iframe',
            config: {
                onClose: function() { location.reload(); }
            }
        });
  });
  
  // Check if tiledata is available and valid
  if (typeof(tiledata) !== 'undefined') {

      // Check action
      if (tiledata.action === 'cancel' || tiledata.action === 'save') {
          // Close dialog
          window.parent.jQuery('.link-overlay').each(function() {
              try {
                  window.parent.jQuery(this).overlay({api: true}).close();
              } catch(e) { }
          });
      }
  }
  
});