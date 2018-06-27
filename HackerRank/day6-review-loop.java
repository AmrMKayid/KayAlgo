import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        
        int t = sc.nextInt();
        while(t-- > 0) {
            String s_even = "", s_odd = "";
            
            String s = sc.next();
            int n = s.length();
            
            for(int i = 0; i < n; i++) {
                if(i % 2 == 0)
                    s_even += s.charAt(i);
                else
                    s_odd += s.charAt(i);
            }
            
            System.out.println(s_even + " " + s_odd);
            
            
        }
    }
}