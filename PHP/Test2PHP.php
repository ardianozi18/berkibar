<!DOCTYPE html>
<html>
<body>

<h1>Percobaan PHP</h1>

<?php
$testkalimat = "Halo Dunia!";
$testangka = 12;
$testlain = "Bella Praviyanti";
$testLain = 999;

echo $testkalimat;
echo "<br>";
echo $testangka;
echo "<br>";
echo "I love $testlain forever";
echo "<br>";
echo "I love the number of " . $testLain . " and 99";
print "<br>";
var_dump($testangka);
print "<br>";
print str_replace("Dunia", "Ciledug", $testkalimat);

?> 

</body>
</html>