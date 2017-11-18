<html>
    <head>
        <style>
            .errorMsg
            {
                color:#F00;
            }
            div{text-align:center;}
            img {vertical-align:middle}
            body{background-color: #0000cc;}
        </style>
        <!-- Function to calculate distance in PHP -->
        <?php
            function distance($lat1, $lon1, $lat2, $lon2) 
            {

                $pi80 = M_PI / 180;
                $lat1 *= $pi80;
                $lon1 *= $pi80;
                $lat2 *= $pi80;
                $lon2 *= $pi80;

                $r = 6372.797; // mean radius of Earth in km
                $dlat = $lat2 - $lat1;
                $dlon = $lon2 - $lon1;
                $a = sin($dlat / 2) * sin($dlat / 2) + cos($lat1) * cos($lat2) * sin($dlon / 2) * sin($dlon / 2);
                $c = 2 * atan2(sqrt($a), sqrt(1 - $a));
                $km = $r * $c;

                //echo '<br/>'.$km;
                return $km;
            }
        ?>
    </head>

    <body>
        <h1 align = "center"> Price Calculator </h1>
        <h2 align = "center"> Please fill out all fields to calculate how much it costs to ship your item </h2>
        <div><img src = "https://i.ytimg.com/vi/e6q41nVwJoo/maxresdefault.jpg" width = "320" height = "180"/></div>
        <form align="center" action="finalPrice.php" method="post">
            <table align="center">
                <tr>
                    <td> Weight (in lbs) </td>
                    <td> <input type = "number" name="Weight" id="Weight"><span id="errorMsg" class="errorMsg"/> </td>                 
                </tr>
                <tr>
                    <td> Package Type </td>
                    <td> 
                        <select name = "Package">
                            <option value = "Postcard"> Postcard </option>
                            <option value = "Envelope"> Envelope </option>
                            <option value = "Box"> Box </option>
                        </select>
                    </td>
                </tr>
                <tr>
                    <td> Zip Code </td>
                    <td> <input type = "number" name="zipCode" id="zipCode"> <span id="errorMsg2" class="errorMsg"/> </td>
                </tr>
                <tr>
                    <td colspan="2" align="center">
                        <input type="submit" name="submit" value="submit" id="submit">
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
                if($("Weight").value == "")
                {
                    $("errorMsg").innerHTML = "  Please enter a weight.";
                    return false;
                }
                if($("zipCode").value > 99999)
                {
                    $("errorMsg2").innerHTML = "  Please enter a Zip Code with less than 6 digits.";
                    return false;
                }
                if($("zipCode").value < 10000)
                {
                    $("errorMsg2").innerHTML = "  Please enter a Zip Code with more than 4 digits.";
                    return false;
                }
            }
            $("submit").onclick=errorReport;
        </script>                        
    </body>
</html>       