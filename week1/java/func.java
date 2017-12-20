// since EVERYTHING in Java is OO, functions are methods on objects    

public class Test {
    public static void main(String args[]) {
        int c = findMinOfTwoNums(5, 10);
        System.out.println("Avg val: " + c);
        ///
    }
    public static int findAvgOfTwoNums(int a, int b) {
        int returnVal = ((a + b) / 2);
        return returnVal;
    }
    // overloading is like a concept called function arity
    // (where the language will choose which function body to call based on the number of args)
    // in java you can use the same # of params but diff types
    // OR same function name but diff # of params
    public static int findSumOfTwoInts(int a, int b) {
        int sumVal = (a + b);
        return sumVal;
    }
    public static double findSumOfTwoDoubles(double a, double b) {
        double sumVal = (a + b);
        return sumVal;
    }
}

// Looks like Java does provide an interface to use functions in a first class fashion
