import java.util.*;

public class Solution {
    public static int mostConsecutiveOnes(int n) {
        // convert number->binary string->char array
        char[] binary = Integer.toBinaryString(n).toCharArray();
        
        // count of current sequence of consecutive ones
        int tmpCount = 0; 
        
        // running maximum count of consecutive ones for any section to left of tmpCount
        int maxCount = 0; 
        for(int i = 0; i < binary.length; i++){
            
            // reset to 0 if we hit a '0' char
            if(binary[i] == '0') {
                
                // set new max if needed
                if(tmpCount > maxCount){
                    maxCount = tmpCount;
                }
                    
                tmpCount = 0;
            }
            else { // current location is a section of consecutive 1's
                // increment tmpCount
                tmpCount =  tmpCount + 1; 
            }
        }
        // conditional is necessary here in case the string does not end with a 0
        return (tmpCount > maxCount) ? tmpCount : maxCount;
    }

    public static int mostConsecutiveOnes2(int n) {
        // convert number->binary string->char array
        char[] binary = Integer.toBinaryString(n).toCharArray();
        int tmpCount = 0; // count consecutive ones
        int maxCount = 0; // running maximum of consecutive ones
        for(int i = 0; i < binary.length; i++){
            // reset to 0 if we hit a '0' char
            tmpCount = (binary[i] == '0') ? 0 : tmpCount + 1; 
            
            // set max
            if(tmpCount > maxCount){
                maxCount = tmpCount;
            }
        }
        return maxCount;
    }

    public static int mostConsecutiveOnes3(int n) {
        // convert to binary and split into strings of consecutive ones
        String[] groupings = Integer.toBinaryString(n).split("0");
        int max = 0;
        for(String s : groupings){
            if(max < s.length()){
                max = s.length();
            }
        }
        return max;
    }

    public static int mostConsecutiveOnes4(int n) {
        // convert to binary and split into strings of consecutive ones
        String[] groupings = Integer.toBinaryString(n).split("0");
        // sorting strings only composed of a single character ("1") orders them by length
        Arrays.sort(groupings);
        return groupings[groupings.length - 1].length();
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();

        System.out.println(mostConsecutiveOnes(n));
        System.out.println(mostConsecutiveOnes2(n));
        System.out.println(mostConsecutiveOnes3(n));
        System.out.println(mostConsecutiveOnes4(n));
    }
}