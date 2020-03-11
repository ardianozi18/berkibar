var trucks, text;
trucks = ["MAN", "Scania", "Volvo", "Kamaz", "Renault", "DAF", "Mercedes-Benz"]

text = "<ol>"
trucks.forEach(myFunction);
text += "</ol>";
document.getElementById("testloop").innerHTML = text;

function myFunction(value) {
    text += "<li>" + value + "</li>";
}