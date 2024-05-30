$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  type: 'GET',
  success: function (resp) {
    $('#character').text(resp.name);
  },
  error: function (xhr, textStatus, errorThrown) {
    console.log(xhr);
  }
});