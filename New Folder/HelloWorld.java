import java.util.Scanner;  // Importing Scanner class for taking user input

// Main class
class HelloWorld {

    // Method to add two numbers and return the result
    public static int AddTwoNum(int a, int b) {
        return a + b;  // Returns the sum of a and b
    }

    // Main method - execution starts here
    public static void main(String[] args) {
        
        // Create a Scanner object to take input from the keyboard
        Scanner sc = new Scanner(System.in);

        // Prompt the user to enter the first number
        System.out.print("Enter a = ");
        int a = sc.nextInt();  // Read integer input for 'a'

        // Prompt the user to enter the second number
        System.out.print("Enter b = ");
        int b = sc.nextInt();  // Read integer input for 'b'

        // Display the sum of the two numbers using the AddTwoNum method
        System.out.print(a + " + " + b + " = " + AddTwoNum(a, b));
    }
}

