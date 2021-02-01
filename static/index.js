const cloneRow = () => {
  var rowAmmount = 2;
  var getTotalRows = $('table > tbody').children().length;
  console.log(getTotalRows)
  for (var i = -1; i < rowAmmount-1; i++) {
    var row = document.getElementById("row"); // find row to copy
    var table = document.getElementById("table"); // find table to append to
    var clone = row.cloneNode(true); // copy children too
    clone.id = "newRow" + (getTotalRows + i); // change id or other attributes/contents
    clone.classList.remove('hidden');
    table.appendChild(clone); // add new row to end of table
    $('#newRow' + (getTotalRows + i)).children().each(function() {
      $(this).children().attr('id', $(this).children().attr('id') + (getTotalRows + i));
    });
}}

$('input').bind('paste', function (e) {
  var $start = $(this);
  var source

  //check for access to clipboard from window or event
  if (window.clipboardData !== undefined) {
      source = window.clipboardData
  } else {
      source = e.originalEvent.clipboardData;
  }
  var data = source.getData("Text");
  if (data.length > 0) {
    if (data.indexOf("\t") > -1) {
      var columns = data.split("\n");
      $.each(columns, function () {
        var values = this.split("\t");
        $.each(values, function () {
          $start.val(this);
          if ($start.closest('td').next('td').find('input')[0] != undefined) {
          $start = $start.closest('td').next('td').find('input');
          }
          else
          { 
            return false;  
          }
        });
        $start = $start.closest('td').parent().next('tr').children('td:first').find('input');
      });
      e.preventDefault();
    }
  }
});