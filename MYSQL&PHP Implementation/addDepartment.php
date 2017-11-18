<html>
<head>
    <?php 
    $connect = mysqli_connect("localhost", "root", "123456");
    mysqli_select_db($connect, "company");
    ?>
</head>
<body>
    <?php 
    $addDepartment = "insert into department values('"
        . $_POST['Dname'] . "'," 
        . $_POST['Dnumber'] . ",'"
        . $_POST['Mgr_ssn']  . "','"
        . $_POST['Mgr_start_date'] . "');";
    print $addDepartment;
    mysqli_query($connect, $addDepartment);
    header("Refresh:0; url=html.php");
    ?>
    
    <p>
        Well Done.
    </p>
    <a href = "html.php">Click to Return Home</a>
</body>
</html>