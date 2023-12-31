<?php
$conn=new mysqli("localhost","root","");
if($conn->connect_error)
{
  die("connection failed".$conn->connect_error);
 }

$sql="CREATE DATABASE S1MCA";
if($conn->query($sql)==TRUE)
{
echo "Database Created";
}
else{
   echo "Error".$conn_error;
}

$conn=new mysqli("localhost","root","","S1MCA");
if($conn->connect_error)
{
 die("connection error".$conn->connect_error);
}

$tbl="CREATE TABLE Product(product_id ini primary key,product name varchar(20),quantity int,price varchar(10),man_date date,exp_date date)";

if($conn->query($tbl)==TRUE)
{
 echo "Table Created";
}
else
{
 echo "Error".$conn_error;
}
$conn->close();
?>

