<!DOCTYPE html>
<html>
<body>

<h1> Student Information </h1>
<tr>
<th>
Student CIN
</th>
<th>
Student Name
</th>
</tr>
<tr>
<td>
<?php
      print("123456");
?>
</body>
</html>
<?php 
$connect = mysqli_connect("localhost", "root", "123456");
      mysqli_select_db($connect, "company");
     $insertEmployee = "insert into dependent values 
     (123456781, 'Elizabeth', 'F', '1967-05-05', 'Spouse');";
     $result = mysqli_query($connect, $insertEmployee);

print "New work_on was inserted!"
?>
