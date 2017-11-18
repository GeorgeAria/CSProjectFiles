<html>
<head>
    <?php 
    $connect = mysqli_connect("localhost", "root", "123456");
    mysqli_select_db($connect, "company");
    ?>
    <style>
        .errorMsg
        {
            background-color: #0C3;
        }
    </style>
</head>
<body>
    <h1 align = "center"> 
        Department Information 
    </h1>
    <table align = "center" border = "2">
        <tr>
            <th>
                Department Name
            </th>
            <th>
                Department Number
            </th>
            <th>
                Manager SSN
            </th>
            <th>
                Manager Start Date
            </th>
            <th>
                Actions
            </th>
            <th>
                Actions
            </th>
        </tr>

        <?php 
        $departmentInfo = mysqli_query($connect, "select * from department");
        while($row = mysqli_fetch_assoc($departmentInfo))
        {
            print "<tr>";
            print "<td>";
            print $row['Dname'];
            print "</td>";

            print "<td>";
            print $row['Dnumber'];
            print "</td>";

            print "<td>";
            print $row['Mgr_ssn'];
            print "</td>";

            print "<td>";
            print $row['Mgr_start_date'];
            print "</td>";

            print "<td>";
            $editLink = "<a href='editDepartment.php?id=" . $row['Dnumber'] . "'> [EDIT] </a>";
            print $editLink;
            print "</td>";

            print "<td>";
            $deleteLink = "<a href='deleteDepartment.php?id=" . $row['Dnumber'] . "'> [DELETE] </a>";
            print $deleteLink;
            print "</td>";


            #print "<td>";
            #$editRow = "<a href = 'edit.php?id="
           #             . $row['Dnumber']
            #            . $row['Dname'];
            #print $editRow;
            #print "</td>";
            print "</tr>";

        }
        ?>
    </table>
<br />
<form align = "center" action = "addDepartment.php" method = "POST">
        <table align = "center">
            <tr>
                <td>
                    Department Name: 
                </td>
                <td>
                    <input type = "text" name = "Dname" id = "Dname">
                    <span id = "errorMsg" class = "errorMsg"/>
                </td>
            </tr>
            <tr>
                <td>
                    Department Number: 
                </td>
                <td>
                    <input type = "text" name = "Dnumber">
                </td>
            </tr>
            <tr>
                <td>
                    Manager SSN: 
                </td>
                <td>  
                    <select name="Mgr_ssn">
                        <?php
                        $employeeInformation = "select Ssn from employee";
                        $result = mysqli_query($connect, $employeeInformation);
                        while ($row = mysqli_fetch_assoc($result))
                        {
                            print "<option value='" . $row['Ssn'] . " '>" . $row['Ssn'] . "</option> ". "\r\n";
                        }
                        ?>
                   </select>
                </td>
            </tr>
            <tr>
                <td>
                    Manager Start Date: 
                </td>
                <td>
                    <input type = "text" name = "Mgr_start_date">
                </td>
            </tr>
            <tr>
                <td colspan = 2 align = "center">
                    <input type = "submit" name = "submit"  value = "Submit" id = "submit">
                </td>
            </tr>
        </table>
</form>
<script>
var $ = function(id)
{
    return document.getElementById(id);
}
var errorReport = function()
{
    if ($("Dname").value == "")
    {
        $("errorMsg").innerHTML = "Can't be empty";
        return false;
    }
}
$("submit").onclick = errorReport;
</script>
</body>
</html>