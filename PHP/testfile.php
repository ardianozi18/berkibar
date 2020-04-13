<?php
$myfile = fopen("testfile.txt", "w") or die("Unable to open file!");
$txt = "Ardian Fauzi\n";
fwrite($myfile, $txt);
$txt = "Bella Praviyanti\n";
fwrite($myfile, $txt);
fclose($myfile);
?>