<?php 

$cookie = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=";
$jsondata = json_encode(array("showpassword"=>"no", "bgcolor"=>"#ffffff"));
function xor_encrypt($in,$key){
	$text = $in;
	$outText = '';

	for($i=0;$i<strlen($text);$i++){
		$outText .= $text[$i] ^ $key[$i % strlen($key)];
	}
	return $outText;
}
$clave = xor_encrypt(base64_decode($cookie),$jsondata);
// New cookie 
$newdata= array("showpassword"=>"yes", "bgcolor"=>"#ffffff");
echo base64_encode(xor_encrypt(json_encode($newdata),$clave));

?>
