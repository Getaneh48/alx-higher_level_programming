$('header').click(function () {
  if ($(this).attr('class') === 'greeen') {
    $(this).removeClass('green');
    $(this).toggleClass('red');
  } else {
    $(this).removeClass('red');
    $(this).toggleClass('green');
  }
});
