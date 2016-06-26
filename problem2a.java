// 2.a) Just do it.
public class problem2a{
    
    public static void main(String []args){
        System.out.println("1->0: " + fibonat(1));
        System.out.println("2->1: " + fibonat(2));
        System.out.println("3->1: " + fibonat(3));
        System.out.println("4->2: " + fibonat(4));
        System.out.println("5->3: " + fibonat(5));
        System.out.println("6->5: " + fibonat(6));
        System.out.println("7->8: " + fibonat(7));
    }
    
    public static int fibonat(int n) {
        int prev = 0;
        int curr = 1;
        int currHold = curr;
        n -= 1;
        for (int stepsLeft = n; stepsLeft > 0; stepsLeft--) {
            currHold = curr;
            curr += prev;
            prev = currHold;
        }
        return prev;
    }
}
