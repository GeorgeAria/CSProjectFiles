<html>
    <head>
        <?php
        $connect = mysqli_connect("localhost", "root", "123456");
        mysqli_select_db($connect, "company");
        ?>
    </head>

    <body>
        <?php
        $getDepartment = "select * from department where Dnumber = "
        . $_GET['id'] . ";"; 
        $result = mysqli_query($connect, $getDepartment);
        $row = mysqli_fetch_assoc($result);
        //print $row['Dname'];
        //header("Refresh:0; url=html_php.php");
        ?>

        <h1 align="center"> 
            Update The Department Information 
        </h1> 

        <form align="center" action="updateDepartment.php" method="post">
            <table align="center">
                <tr>
                    <td>
                        Department Name:
                    </td>
                    <td>
                        <input type="text" name="Dname" id="Dname" value= <?php print '"';
                        print $row['Dname'];
                        print '"';?>>
                        <span id="errorMsg" class="errorMsg"/>
                    </td>
                </tr>
                <tr>
                    <td>
                        Department Number:
                    </td>
                    <td>
                        <input type="text" name="Dnumber" value= <?php print '"';
                        print $row['Dnumber'];
                        print '"';?>>
                    </td>
                </tr>
                <tr>
                    <td>
                        Manager SSN:
                    </td>
                    <td>
                        <input type="text" name="Mgr_ssn" value= <?php print '"';
                        print $row['Mgr_ssn'];
                        print '"';?>>
                    </td>
                </tr>
                <tr>
                    <td class="fieldLabel">
                        Manager Start Date:
                    </td>
                    <td>
                        <input type="text" name="Mgr_start_date" value= <?php print '"';
                        print $row['Mgr_start_date'];
                        print '"';?>>
                    </td>
                </tr>
                <tr>
                    <td colspan="2" align="center">
                        <input type="submit" name="submit" value="update" id="submit">
                    </td>
                </tr>
            </table>
        </form>
    </body>
</html>