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
