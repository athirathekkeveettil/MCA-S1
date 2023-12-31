<html>
<body>
<center>
<?php
if(isset($_POST["sub"]))
{
	$n=$_POST["name"];
	$r=$_POST["roll"];
	$arr1=array("sub1"=>"ENGLISH","sub2"=>"MALAYALAM","sub3"=>"SCIENCE");
	$arr2=array("m1"=>"95","m2"=>"90","m3"=>"93");
	$arr3=array("r1"=>"PASS","r2"=>"PASS","r3"=>"PASS");	
?>
<h1>MACE</h1>
<h2>FIRST SESSIONAL EXAMINATION RESULTS</h2>
<h3>NAME:<?php echo $n;?></h3>
<h3>ROLL NO:<?php echo $r;?></h3>
<table border="1">
	
	<tr>
				<th>SI.NO</th>
				<th>SUBJECTS</th>
				<th>MARK</th>
				<th>REMARK</th>
	</tr>
	<tr>
				<th>1</th>
				<td><?php echo $arr1["sub1"];?></td>
				<td><?php echo $arr2["m1"];?></td>
				<td><?php echo $arr3["r1"];?></td>
	</tr>
	<tr>
				<th>2</th>
				<td><?php echo $arr1["sub2"];?></td>
				<td><?php echo $arr2["m2"];?></td>
				<td><?php echo $arr3["r2"];?></td>
	</tr>
	<tr>
				<th>3</th>
				<td><?php echo $arr1["sub3"];?></td>
				<td><?php echo $arr2["m3"];?></td>
				<td><?php echo $arr3["r3"];?></td>
	</tr>
	<tr>
				<th  colspan="3"><center>TOTAL:<?php echo  $arr2["m1"]+$arr2["m2"]+$arr2["m3"]."/300"."</center>";?></th>
				<th colspan="1">PASS</th>
	</tr>
</table>
<?php
}
?>
</center>
</body>
</html>