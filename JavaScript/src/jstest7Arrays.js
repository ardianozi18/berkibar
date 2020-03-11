var trucks, text, fLen, i;
trucks = ["MAN", "Scania", "Volvo", "Kamaz", "Renault", "DAF", "Mercedes-Benz"]
tLen = trucks.length;

text = "<ol>"
    for (i = 0; i < tLen; i++) {
        text += "<li>" + trucks[i] + "</li>";
    }
text += "</ol>";

document.getElementById("testloop").innerHTML = text;