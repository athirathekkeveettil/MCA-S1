<?php
$conn=new mysqli("localhost","root","","S1MCA");
if($conn->connect_error)
{
 die("connection failed".$conn->connect_error);
}

$alt="ALTER TABLE Product ADD COLUMN man_name varchar(10)";

if($conn->query($alt)==TRUE)
{
 echo "column created";
}
else
{
 echo "Error".$conn_error;
}
$conn->close();
?>