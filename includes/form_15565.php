<?php	
	
	
	$input_769 = $_POST['input_769'];
	$input_79 = $_POST['input_79'];
	$input_1590 = $_POST['input_1590'];
	$input_113 = $_POST['input_113'];
	$input_1108 = $_POST['input_1108'];
	$input_41 = $_POST['input_41'];
	
	$to = 'receiver@yoursite.com'; // Email submissions are sent to this email

	// Create email	
	$email_subject = "Message from My Blocs Website.";
	$email_body = "You have received a new message. \n\n".
				  "Input_769: $input_769 \nInput_79: $input_79 \nInput_1590: $input_1590 \nInput_113: $input_113 \nInput_1108: $input_1108 \nInput_41: $input_41 \n";
	$headers = "MIME-Version: 1.0\r\nContent-type: text/plain; charset=UTF-8\r\n";	
	$headers .= "From: contact@yoursite.com\n";
	$headers .= "Reply-To: DoNotReply@yoursite.com";	
	
	mail($to,$email_subject,$email_body,$headers); // Post message
	return true;			
?>