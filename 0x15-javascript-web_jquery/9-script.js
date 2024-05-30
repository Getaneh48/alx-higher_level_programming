window.onload = function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    success: function (resp) {
      $('#hello').text(resp.hello);
    },
    error: function (xhr, textStatus, errorThrown) {
      console.log(xhr);
    }
  });
};
