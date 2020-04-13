<!DOCTYPE html>
<html>
<body>

<?php
$myfile = fopen("src/Technology.txt", "r") or die("Unable to open file!");
echo fread($myfile,filesize("src/Technology.txt"));
fclose($myfile);
?>

</body>
</html>