public class Test {    
    public static void main(String args[]) {
        // + - * / %
        int a = 3;
        int b = 6;
        int c = a + b;
        int d = b - a;
        int e = a * c;
        int f = e / a;
        int g = 12 % d; // modulus = remainder
        
        // if/elseif/else < > <= >= == != === !==
        if (a < b)
            System.out.println("a < b");
        if (a > b)
            System.out.println("should never happen");
        int h = 3;
        if (a === h)
            System.out.println("these are exactly equal");
        int i = 4;
        if (a > b) {
            System.out.println("a was reassigned");
        } else if (a < b) {
            System.out.println("a might have its original val");
        } else {
            System.out.println("something else happened to a");
        }
        
        // || && !
        if ((a < b) && (e > c))
            System.out.println("math is working, yay!");
        if ((a > b) || (b > a))
            System.out.println("well the second one is true");
        // ! is negation
        if (!a) System.out.println("will this log?");
        j = false;
        if (!j)
            System.out.println("what about this?");
        if (!!j)
            System.out.println("this?')}
        
        // loops
        for (int i = 0; i < 5; i++) {
            // doing some iterative processing here
        }
        int z = 0;
        while (z <= 10) {
            System.out.println("val of z: " + z);
            z++;
        }
    }
}
