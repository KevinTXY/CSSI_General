function speak() {
  $("#speech").show();
}

var pet_counter = 0;

function pet() {
  if (pet_counter < 3) {
    alert("You pet the dog, he responds positively.");
  }
  else {
    alert("The dog gets annoyed and bites you.")
  }
  pet_counter++;
}

$(document).ready(function() {
  $("#speech").hide();
  $(".button").click(speak);
  $("#cosmo").click(pet);
}
)
