$(document).ready(function()
{
  //hide the all of the element with class msg_body

  $("#portal-globalnav a").click(
        function(){
        var className = "." + $(this).attr('id');



  if ($(className).hasClass('megatrack')) {
  $('.megatrack').slideUp(600).addClass('megahide');
  $('.megatrack').removeClass('megatrack');
  } else {

  $('.megatrack').slideUp(5).addClass('megahide');
  $('.megatrack').removeClass('megatrack');

  $(className).slideDown(600).removeClass('megahide').addClass('megatrack');}
  });
});