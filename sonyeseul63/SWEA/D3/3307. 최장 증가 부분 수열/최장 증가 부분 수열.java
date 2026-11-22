
import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int testcase = 1; testcase<=T; testcase++){
            int n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] dp = new int[n];
            int[] arr = new int[n];
            for(int i = 0; i<n ;i++){
                arr[i] = Integer.parseInt(st.nextToken());
            }

            for(int now = 0; now< n; now++){
                for(int prev = 0; prev<now; prev++){
                    if(arr[prev] < arr[now])
                        dp[now] = Math.max(dp[now], dp[prev]+1);
                }
            }

            int answer = 0;
            for(int num: dp){
                answer = Math.max(num, answer);
            }
            answer++;
            System.out.println("#" + testcase + " " + answer);
        }
    }
}
