function fungsiKita() {
    var age, voteable;
    age = Number(document.getElementById("umur").value);
    if (isNaN(age)) {
        voteable = "Masukkan umur Anda dalam angka!";
    } else {
        voteable = (age < 18) ? "Anda belum bisa ikut pemilu" : "Anda boleh ikut pemilu";
    }
    document.getElementById("percobaan").innerHTML = voteable;
}