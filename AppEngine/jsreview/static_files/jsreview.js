function fadeOutDone() {
  alert("Fade out is complete");
}

function readywork() {
  alert("Hello World");
  $("#greeting").click(function() {
    $("#greeting").fadeOut(3000, fadeOutDone);
  }

)
}


$(document).ready(readywork)
