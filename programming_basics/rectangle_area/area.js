/*
* Area of a Rectangle JavaScript Version.
* By Macarthur Inbody
* The following is a basic version of the same script but in JavaScript.
*/
//declare base to zero.
var base=0;
//same again.
var height=0;
//and a third time.
var area=0;
//going to have to alert unless they want to install node.
alert("Area of a Rectangle calculator.")
//Here we prompt the user to enter a string. Then we take that value turn it into an Integer.
//Then we set the value to be base.
base=parseInt(prompt("Enter the base: "))
//same as height.
height=parseInt(prompt("Enter the height: "))
//simply multiply them together.
area=base*height
//alert the value to them.
//JavaScript is fine with adding strings and "Ints"* together in a string. It doesn't care.
alert("The area is "+area+" square units.")


//* Actually all numeric values in javascript are stored as signed "integers". In reality they are really
//doubles but are shown as either floating point or are floored to be shown to you.
