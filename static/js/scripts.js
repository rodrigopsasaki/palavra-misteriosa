$(document).ready(function(){
  $(".letra").keyup(function() {
    $(this).val($(this).val().toUpperCase());
    var limit  = parseInt($(this).attr('maxlength'));
    var length = $(this).val().length;
    if(length == limit){
      var inputs = $(this).closest('form').find(':input');
      inputs.eq( inputs.index(this)+ 1 ).focus();
    }
  });
});
