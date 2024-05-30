$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  success: function (resp) {
    resp.results.forEach((elm) => {
      $('#list_movies').append(`<li>${elm.title}</li>`);
    });
  },
  error: function (xhr, textStatus, errorThrown) {
    console.log(textStatus);
  }
});
