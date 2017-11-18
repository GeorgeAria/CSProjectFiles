<html>
    <head>
        <?php
        $connect = mysqli_connect("localhost", "root", "123456");
        mysqli_select_db($connect, "company");
        ?>
    </head>
    <body>
        <?php
        $updateDepartment = "update department set Dname = '"
        . $_POST['Dname'] . "', Dnumber = "
        . $_POST['Dnumber'] . ", Mgr_ssn = '"
        . $_POST['Mgr_ssn'] . "', Mgr_Start_date = '"
        . $_POST['Mgr_start_date']
        . "' where Dnumber = " .  $_POST['Dnumber']; 
        print $updateDepartment;
        mysqli_query($connect, $updateDepartment);
        //header("Refresh:0; url=html_php.php");
        ?>
        <p> Well Done. Department Updated. </p> 
        <a href="html.php">Click to return Home </a>
    </body>
</html>