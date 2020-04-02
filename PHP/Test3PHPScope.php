<!DOCTYPE html>
<html>
<body>

<?php
$x = 10; // global scope
 
function myTest() {
    $x = 5;// using x inside this function will generate an error
    echo "<p>Variable x inside function is: $x</p>";
} 
myTest();

echo "<p>Variable x outside function is: $x</p>";
?>

</body>
</html>
