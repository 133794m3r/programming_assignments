/*
* Java Area of a rectangle.
* By Macarthur Inbody
* Java is typed so you have to set the type for everything.
*/
//In java the Scanner class is how you handle user input.
import java.util.Scanner;
//we have to create a class that'll be utilized.
public class Area{
	//we have to have a main method that'll be called whenever this class is
	//called. We also have to pass it an array of strings as the arguments.
	//even if we're not going to use it.
	public static void main(String args[]){
		//initialize and set the value of base to zero. Also make it an int.
		int base=0;
		//same but for height.
		int height=0;
		//same again but for area.
		int area=0;
		/*
		* We have to create a new scanner Object. I'm telling it to scan
		* from stdin aka raw bytes of user input.
		* Here I'm using camelCase solely because that's the Java way.
		*/
		Scanner myScanner=new Scanner(System.in);
		//Print out the string to the console with a new line.
		System.out.println("Rectangle area calculator");
		//Prompt the user to enter the base value.
		System.out.print("Enter the base: ");
		/*
		*We use our scannerObject and get the nextInt method to get the
		*next value that the user gives us and then casts it to a signed
		*integer.
		*/
		base=myScanner.nextInt();
		//Do the same again but this time for the height.
		System.out.print("Enter the height: ");
		height=myScanner.nextInt();
		//Get the area value.
		area=base*height;
		/*
		*We print out the string below and put the area value into it
		*and make sure it's a signed Int. Also we include a newline at the
		*end of the string. It's OS indepedent. On *nix it is \n on Windows
		*it's \r\n
		*/
		System.out.format("The area was %d square units.%n",area);
	}
}

