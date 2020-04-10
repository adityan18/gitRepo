function changeTabs(buttonId, c) {
  var f1 = buttonId;
  var f2 = f1.toLowerCase();
  var loc;

  if (f1 == "Home") {
    loc = "../index.html";
  } else if (c == "h") {
    loc = f1 + "/" + f2 + ".html";
  } else if (c == "g") {
    loc = "../" + f1 + "/" + f2 + ".html";
  } else if (c == "r") {
    loc = f1.toLowerCase() + ".html";
  } else if (c == "ga") {
    loc = "../" + f1 + "/" + f2 + ".html";
  }

  location.replace(loc);
}

function changeGen(buttonId) {
  var f1 = buttonId;
  var f2 = f1.toLowerCase();
  var loc = "../" + f1 + "/" + f2 + ".html";

  if (f1 == "Home") {
    loc = "../index.html";
  }
  location.replace(loc);
}

function myFunction() {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("Input");
  filter = input.value.toUpperCase();
  table = document.getElementById("pokeTable");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0]; //td[0] pokemon name
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
