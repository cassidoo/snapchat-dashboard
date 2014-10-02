$(function() {

  setInterval(function() {
    $.getJSON( "get_images", function( data ) {
      $("#img0").attr("src", data.result[data.result.length - 1].substring(2));
      $("#img1").attr("src", data.result[data.result.length - 2].substring(2));
      $("#img2").attr("src", data.result[data.result.length - 3].substring(2));
    //  console.log(data.result);
    });
  }, 500);
});
