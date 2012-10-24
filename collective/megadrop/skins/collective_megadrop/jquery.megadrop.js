

$(document).ready(function()
{
  //hide the all of the element with class msg_body

  $("#portal-globalnav a").click(
        function(){
        var className = "." + $(this).attr('id');
        var tabName = "#" + $(this).parent().parent().attr('id');



  if ($(className).hasClass('megatrack')) {
  $('.megatrack').slideUp(600).addClass('megahide');
  $('.megatrack').removeClass('megatrack');
  } else {

  $('.megatrack').slideUp(5).addClass('megahide');
  $('.megatrack').removeClass('megatrack');

  $(className).slideDown(600).removeClass('megahide').addClass('megatrack');}
  
  //remove megaselect class when closing tabs and add to tab that is active
  if ($(tabName).hasClass('megaselect')) {
  $('.megaselect').removeClass('megaselect');
  } else {
  $('.megaselect').removeClass('megaselect');
  $(tabName).addClass('megaselect');}
  
  });
  //ajax necessary to reload tab content on the fly
  //$("body").delegate("#portal-globalnav li #managetab a", "click", function() {
  //      location.reload();
  //});
  
});


