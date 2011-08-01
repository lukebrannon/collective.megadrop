/*
Sagarika Gogikari <gsagarika2012@gmail.com>
*/

$(document).ready(function()
{
  //hide the all of the element with class msg_body
  
  $("#portal-globalnav a").click(
        function(){
    $("#portal-globalnav a").parent('h2').next('div').hide();
    $(this).parent().next('div').slideDown(600);
  });
});