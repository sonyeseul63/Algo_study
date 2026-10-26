package sonyeseul63.SWEA.D2;

import java.io.*;
import java.util.StringTokenizer;
public class S26045 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int testcase = 1; testcase <= T; testcase++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int[] A = new int[a];
            st = new StringTokenizer(br.readLine());
            for(int i = 0; i < a; i++){
                A[i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            int j = 0;
            for(int i = 0; i < b; i++){
                int target = Integer.parseInt(st.nextToken());
                for(;j<a;j++){
                    if(target == A[j]){
                        break;
                    }
                }
            }
            String answer = "NO";
            if(j < a) answer = "YES";
            System.out.println("#"+ testcase + " " + answer);
        }
    }
}
