<a data-target = "#main_Container_Id">cancel Quote</a>
<div id = "main_Container_Id">
	enter your code here. when we click on cancel Quote this piece of code will execute
</div>
------------------------------
<button data-bind = "{clcik : function_Name($data)}"> refresh </button>
<script>
	function function_Name(data){
		console.log('Write your code here')
	}
</script>
------------------------------------
ko.contextFor($0)
ko.dataFor($0)
---------------------------------------
function logColumnDataLineByLine(columnIndex) {
  // Select the table
  var table = document.querySelector('#ctl00_cph1_dataTable_gvData');
  // Get all rows from the table
  var rows = table.querySelectorAll('tr');
  
  // Loop through each row
  rows.forEach(function(row) {
    // Get all cells in the current row
    var cells = row.querySelectorAll('td');
    
    // Check if the row has enough cells
    if (cells.length > columnIndex) {
      // Get the text content of the specified column
      var cellData = cells[columnIndex]
      var altText = cellData.getAttribute('alt')
      // Log the data to the console line by line
      console.log(altText);
        console.log(1234)
    }
  });
}

// Example usage: Log data from the second column (index 1) line by line
logColumnDataLineByLine(8);
