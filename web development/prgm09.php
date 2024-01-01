<?php
	$con=new mysqli("localhost","root","","S1MCA");
	if($con->connect_error)
		die("\nconnection failed:".$con->connect_error);
$sel="SELECT  * FROM Product";
if($con->query($sel)==TRUE)
{
	$result=$con->query($sel);
	if($result->num_rows>0)
	{	
		?>
		<table border="1">
		<tr>
		<th>PRODUCT ID</th>
		<th>PRODUCT NAME</th>
		<th>QUANTITY</th>
		<th>UNIT PRICE</th>
		<th>MANUFACTURED DATE</th>
		<th>EXPIRY DATE</th>
		</tr>
		<?php
		while($row=$result->fetch_assoc())
		{
			
				echo "<tr><th>".$row['product_id']."</th><th>".$row['product_name']."</th><th>".$row['quantity']."</th><th>".$row['price']."</th><th>".$row['man_date']."</th><th>".$row['exp_date'].
				"</th></th></tr>";
		}
			
	}
	echo "</table>";
}
else
	echo "\nfailed to display details:",$con->error;
$con->close();
?>