import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        Map<String, String> phoneBook = new HashMap<String, String>(); 
        for(int i = 0; i < n; i++){
            String name = in.next();
            int phone = in.nextInt();
            phoneBook.put(name, String.valueOf(phone));
        }
        while(in.hasNext()){
            String s = scan.next();
            Integer phoneNumber = phoneBook.get(s);
            System.out.println(
                (phoneNumber != null) 
                ? s + "=" + phoneNumber 
                : "Not found"
            );
        }
        in.close();
    }
}