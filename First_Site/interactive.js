/*function disappear() {
  $("#profile").toggleClass("hidden");
} */
function reveal(){
  $("#profile").fadeIn();
}
function fastremove(){
  $("#profile").fadeOut(200);

}
function alarm(){
  alert("Welcome To My Page");
}
function moveText() {
  var input_text = $('input').val(); //Create variable that stores value from input tags
  $('#result').text(input_text); //Set Input text into entities with id result
}
$(document).ready(function() {
    $("#profile").fadeOut();
    $("#picbutton").click(reveal);
    $("img").hover(fastremove);
    $("#submit").click(moveText);
  }
)
