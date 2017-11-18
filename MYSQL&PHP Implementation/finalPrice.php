<html>
    <head>
       <!-- Add php code here -->
       <style>
            div{text-align:center;}
            td{text-align: center}
            body{background-color: #0000cc;}
       </style>
    </head>
    <body>
        <h1 align = "center"> Final Price Quote </h1>
        <h2 align = "center"> Here is your receipt and quote for today. </h2>
        <table align="center" border="10">
            <tr>
                <th>Fields</th>
                <th>Values</th>
            </tr>
            <tr>
                <th>Weight</th>
                <td> <?php echo $_POST['Weight']; ?> </td>
            </tr>
            <tr>
                <th> Package Type </th>
                <td> <?php echo $_POST['Package']; ?> </td>
            </tr>
            <tr>
                <th> Zip Code </th>
                <td> <?php echo $_POST['zipCode']; ?> </td>
            </tr>
        </table>
        <h1 align = "center"> Final quote = $1,000,000 </h1>
        <div> <img src = "https://upload.wikimedia.org/wikipedia/en/1/16/Drevil_million_dollars.jpg"/></div>
        <h2 align = "center"> <a href="priceCalculator.php"> Click to return to Price Calculator </a> </h2>
    </body>
</html>
