<!DOCTYPE html>
<html>
<body>

<?php
class Trucks {
    function Trucks() {
        $this->model = "Scania";
    }
}

class HeavyEq {
    function HeavyEq() {
        $this->model = "Komatsu";
    }
}


// create an object
$herbie = new Trucks();
$notherbie = new HeavyEq();

// show object properties
echo $herbie->model;
print "<br>";
print $notherbie->model;
?>

</body>
</html>
