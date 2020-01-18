#!/bin/bash
#Area of a Rectangle Calculator
#By Macarthur Inbody
#make base always be an int.
declare -i base;
#ditto
declare -i height;
#ditto
declare -i area;
#echo it out.
echo "Area of a Rectangle calculator.";
#printf doesn't print a newline
printf "Enter the base: ";
#read in the base variable
read base;
#same thing again
printf "Enter the height: ";
read height;
#calculate area
area=$(( $base*$height));
#echo out results
echo "The area is $area square units.";
