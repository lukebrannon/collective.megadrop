/*
$(document).ready(function() {

    $(".mdtab").hover(
        function(){
        var className = "." + $(this).attr('id');
        $(className).toggleClass("megahide");
        }
    );

    $(".mdtab").focus(
        function(){
        var className = "." + $(this).attr('id');
        $(className).toggleClass("megahide");
        }
    );

    $(".mdtab").blur(
        function(){
        var className = "." + $(this).attr('id');
        $(className).toggleClass("megahide");
        }
    );

});
*/

$(document).ready(function()
{
  //hide the all of the element with class msg_body
  
  $("#portal-globalnav a").click(
        function(){
        var className = "." + $(this).attr('id');
  $(className).slideToggle(600);
  });
});