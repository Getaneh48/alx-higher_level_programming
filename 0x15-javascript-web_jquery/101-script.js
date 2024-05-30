window.onload = function () {
  $('#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });

  $('#remove_item').click(function () {
    $('.my_list>:last-child').remove();
  });
};
