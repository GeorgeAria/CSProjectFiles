<html>
    <head>
        <?php
        $connect = mysqli_connect("localhost", "root", "123456");
        mysqli_select_db($connect, "company");
        ?>
    </head>
    <body>
        <?php
        $deleteDepartment = "delete from department where Dnumber = "
        . $_GET['id'] . ";"; 
        print $deleteDepartment;
        mysqli_query($connect, $deleteDepartment);
        header("Refresh:0; url=html.php");
        ?>
    </body>
</html>