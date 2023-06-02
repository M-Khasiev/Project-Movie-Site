var modal = document.getElementsByClassName("myModal")[0];
var btn = document.getElementsByClassName("myBtn")[0];
var span = document.getElementsByClassName("close")[0];
btn.onclick = function() {
  modal.style.display = "block";
}
span.onclick = function() {
  modal.style.display = "none";
}

var modal1 = document.getElementsByClassName("myModal")[1];
var btn1 = document.getElementsByClassName("myBtn")[1];
var span1 = document.getElementsByClassName("close")[1];
btn1.onclick = function() {
  modal1.style.display = "block";
}
span1.onclick = function() {
  modal1.style.display = "none";
}

var modal2 = document.getElementsByClassName("myModal")[2];
var btn2 = document.getElementsByClassName("myBtn")[2];
var span2 = document.getElementsByClassName("close")[2];
btn2.onclick = function() {
  modal2.style.display = "block";
}
span2.onclick = function() {
  modal2.style.display = "none";
}
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
  else if (event.target == modal1) {
    modal1.style.display = "none";
  }
  else if (event.target == modal2) {
    modal2.style.display = "none";
  }
}