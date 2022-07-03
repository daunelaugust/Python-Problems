import java.util.Scanner;

/**
 * In this assignment, you will implement a simple game.  This game has 2 options for the user playing.  Based on user input, the 
 * user can choose to either convert time, from seconds to hours, minutes, and seconds, or calculate the sum of all digits in an integer.  
 * 
 * At the beginning of the game, the user will be prompted to input either 1 or 2, to indicate which option of the game they want 
 * to play.  1 will indicate converting time, and 2 will indicate calculating the sum of digits in an integer.
 * 
 * For converting time, the user will be prompted to input a number of seconds (as an int) and the program will call a method that 
 * will convert the seconds to time, in the format hours:minutes:seconds, and print the result.  For example, if the user enters 6734, 
 * the program will print the time, 1:52:14. As another example, if the user enters 10,000, the program should print 2:46:39.
 * 
 * For calculating the sum of digits in an integer, the user will be prompted to input a number (as a non-negative int) and the program will 
 * call a method to calculate the sum of the digits in that number, and print the result.  For example, if the user enters 321, 
 * the program will print the sum, 6, because the individual digits in the number add up to 6.  3 + 2 + 1 = 6.
 * 
 * Each method has been defined for you, but without the code. See the javadoc for each method for instructions on what the method 
 * is supposed to do and how to write the code. It should be clear enough.  In some cases, we have provided hints to help you get started.
 * 
*/
public class SimpleGame {

	/**
	 * Write a method to convert the given seconds to hours:minutes:seconds.
	 * @param seconds to convert
	 * @return string for the converted seconds in the format: 23:59:59
	 * 
	 * Example(s): 
	 * - If input seconds is 1432, print and return output in the format: 0:23:52
	 * - If input seconds is 0, print and return output in the format: 0:0:0
	 * - If input seconds is not valid (negative), print and return: -1:-1:-1.  
	 *   So if input seconds is -2, print and return: -1:-1:-1 
	 *   If input seconds is -3214, likewise print and return: -1:-1:-1
	 */
	public String convertTime(int seconds){
       String negativetime = "-1:-1:-1";
       String zerotime = "0:0:0";
       String time;
       if (seconds < 0){
 
           return negativetime;
       }
       else if (seconds == 0){
    	   
           return zerotime;
       }
       else if (seconds > 0){
    	   double newseconds = (double)seconds;
           double hours = newseconds/3600;
           //hours with no decimal
           int hoursd = (int)hours;
           //put 0 in front of it
           	
           double minutes = (hours-hoursd)*60;
           //mins with no decimal
          int minsd = (int)minutes;
		  while (seconds>=60){
		  seconds -=60;
		  }
          //double newerseconds = (minutes-minsd)*60;
          //int secs = (int)newerseconds+;
         
          time = String.format("%01d", hoursd) + ":"+ String.format("%01d", minsd) + ":" + String.format("%01d", seconds);
           
           return time;
       }
       else {
    	   return zerotime;
       }
   }
	/**
	 * Write a method that adds all the digits in the given non-negative integer.
	 * @param integer to add digits
	 * @return integer in which all the digits in the given non-negative integer are added.
	 * 
	 * Example(s): 
	 * - If input is 565, print and return 16.
	 * - If input is 7, print and return 7.
	 * - If input is 0, print and return 0.
	 */
	public int digitsSum(int input){
		// TODO: Your code goes here
		
		String firstsum = String.valueOf(input);
    	int sum =0;
		//arrayOfChars contains input as list of chars
		char[] arrayOfChars = firstsum.toCharArray(); 

		for(int i=0; i<arrayOfChars.length; i++){

         sum = sum + Character.getNumericValue(arrayOfChars[i]);

      }
	  return sum;
	}

	


	
	public static void main(String[] args) {
		// Create an instance of the SimpleGame class.
		// TODO: Your code goes here
		SimpleGame SimpleGame = new SimpleGame();

		int Game;
		
		Scanner sc = new Scanner(System.in);

		System.out.println("What game would you like to play");

		System.out.println("");

		System.out.println("Enter 1 for ConvertTime or Enter 2 for digitsSum");

		Game = sc.nextInt();

		System.out.println("");
		

		if (Game == 1){
			System.out.println("Enter a number of seconds");
			System.out.println("");
			int seconds = sc.nextInt();
			SimpleGame.convertTime(seconds);
			System.out.println("");
			System.out.println(SimpleGame.convertTime(seconds));
		}

		if (Game == 2){
    	   System.out.println("Enter an integer");
			System.out.println("");
			int numbers = sc.nextInt();
			SimpleGame.digitsSum(numbers);
            System.out.println("");
			System.out.println(SimpleGame.digitsSum(numbers));
		}
		

	



		
		// Ask the user which game to play.
		// Then ask the user for input and pass the value to the corresponding method.
		
		// If the user enters 1, ask for an integer to convert and call the convertTime method.
		// If the user enters 2, ask for an integer and call the digitsSum method.
		
		// TODO: Your code goes here
		
		sc.close();
	}	
}