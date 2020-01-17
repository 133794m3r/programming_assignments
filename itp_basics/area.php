#!/bin/php
<?PHP
/*
* Area of a Rectangle calculator.
* This is the PHP Version.
*/
//In PHP there is no input function so I'm writing one.
function input($prefix=Null){
	//could have made this global but I decided not to.
	$content='';
	//to emulate the prefix option.
	if($prefix !== Null){
		//echo out the user's inptut.
		echo $prefix;
	}
	//First I open up stdin for reading as a file.
	$fh=fopen('php://stdin','r');
	//then I do the following.
	//first I read one line from that user's input. Then I strip all
	//whitespace from the beginning or end. Newlines etc.
	//Then I set this resulting string to the variable content.
	$content=trim(fgets($fh));
	//I close the pointer pointing to the resource I opened.
	fclose($fh);
	//Then I return that string.
	return $content;
}
//initializing some variables.
$base=0;
$height=0;
$area=0;
//we echo out the same string and also make sure that we use OS 
//indepdendent new lines.
echo "Area of a rectangle calculator.".PHP_EOL;
//Get the user's input with the prompt. Then we convert it to an integer.
//then we set it to the variable $base.
$base=intval(input("Enter the base: "));
//same as above but with height.
$height=intval(input("Enter the height: "));
//multiply values to get the area.
$area=$base*$height;
//finally echo the result. in PHP like BASH inside of "" anything following
//a $ symbol unless escaped will be treated like a variable.
echo "The area is $area square units.".PHP_EOL;
