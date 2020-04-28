function fnameBlockFixer() {
  var fnameTags = $("p > strong > fname")
    .parent()
    .parent();

  //Loop through each block
  $.each(fnameTags, function(index, elem) {
    var nextElem = $(elem)
      .next()
      .get(0);
    if ($(nextElem).prop("tagName") == "PRE") {
      //verified
      $("<div class='belongs-together'></div>").insertBefore($(elem));
      // $(nextElem).before("<div class='belongs-together' ></div>");
      var newDiv = $(elem)
        .prev()
        .get(0);
      $(newDiv).append($(elem));
      $(newDiv).append($(nextElem));
    }
  });
}

fnameBlockFixer();

// function fnameBlockFixer() {
//   var fnameTags = $("p > strong > fname")
//     .parent()
//     .parent();

//   //Loop through each block
//   $.each(fnameTags, function(index, elem) {
//     var nextElem = $(elem)
//       .next()
//       .get(0);
//     if ($(nextElem).prop("tagName") == "PRE") {
//       //verified
//       $(elem).before("<div class='belongs-together' ></div>");
//       var newDiv = $(elem)
//         .prev()
//         .get(0);
//       $(newDiv).append($(elem));
//       $(newDiv).append($(nextElem));
//     }
//   });
// }

// fnameBlockFixer();
Prism.highlightAll();