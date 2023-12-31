<html>
    <head>
        <title>Input Form</title>
        <style>
            h2{
                color: blue;
            }
           table{
            border:100px;
            font-family:sans-serif;
          }
          th,td{
            border: 1px-solid black;
          }
        </style>
    </head>
    <body>
        <center>
          <h2><u><b><i>PRODUCT DETAILS</i></b></u></h2>
          <form method="post" action=" ">
            <table>
                <tr>
                    <td>Product Name</td>
                    <td><input type="text" name="t1"></td>
                    </tr>
                    <tr>
                        <td>Quantity</td>
                        <td><input type="number" name="t2"></td>
                        </tr>
                        <tr>
                            <td>Unit Price</td>
                            <td><input type="text" name="t3"></td>
                            </tr>
                            <tr>
                                <td>Manufacture Date</td>
                                <td><input type="date" name="t4"></td>
                                </tr>
                                <tr>
                                    <td>Expiry Date</td>
                                    <td><input type="date" name="t5"></td>
                                    </tr>
                                   
                                    <tr>
                                        <td align="center" colspan="2">
                                            <br>
                                        <input type="submit" name="btns" value="Submit">
                                        <input type="reset" name="btnc" value="Cancel"></td>
                                        </tr>
     </table>
    </form>
   </center>
  </body>
 </html>
<?php
$conn=new mysqli("localhost","root","","S1MCA");
if($conn->connect_error)
{
 die("connection error".$conn->connect_error);
}
if(isset($_POST["btns"]))
{
  if(!(empty($_POST['t1']) || empty($_POST['t2']) || empty($_POST['t3']) || empty($_POST['t4']) ||    empty($_POST['t5'])))
{
                        $t1 =$_POST['t1'];
			$t2=$_POST['t2'];
			$t3=$_POST['t3'];
			$t4=$_POST['t4'];
			$t5=$_POST['t5'];

$ins="INSERT INTO Product(product name,quantity,price,man_date,exp_date)VALUES('$t1','$t2','$t3','$t4','$t5')";
if($conn->query($ins)==TRUE)
 echo "Data Inserted";
else
 echo "Error".$conn_error;
}
else
 echo "Provide Data";
}
$conn->close();
?>


            
