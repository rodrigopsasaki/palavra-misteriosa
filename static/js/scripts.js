$(document).ready(function(){

  // go to next input when the current one is filled
  $(".letra").keyup(function() {
    $(this).val($(this).val().toUpperCase());
    var limit  = parseInt($(this).attr('maxlength'));
    var length = $(this).val().length;
    if(length == limit){
      moveToNextInput(this);
    }
  });

  // go back to the previous input if you hit backspace on an empty input
  $(".letra").keydown(function(e){
    if ((e.which == 8 || e.which == 46) && $(this).val() =='') {
      moveToPreviousInput(this);
    }
  });
});

function moveToPreviousInput(input){
  moveToInput(input, -1)
}

function moveToNextInput(input){
  moveToInput(input, 1)
}

function moveToInput(input, i){
  var inputs = $(input).closest('form').find(':input');
  inputs.eq( inputs.index(input) + i ).focus();
}
