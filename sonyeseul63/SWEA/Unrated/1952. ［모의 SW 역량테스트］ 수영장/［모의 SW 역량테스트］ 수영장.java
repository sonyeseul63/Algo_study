
import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int testcase = 1; testcase <=T; testcase++){
            int[] fees = new int[4];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int i = 0; i<4; i++){
                fees[i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            // 누적 최소 값
            int dp[] = new int[13];

            for(int i = 1; i<=12; i++){
                int day = Integer.parseInt(st.nextToken());

                dp[i] = Math.min(day*fees[0], fees[1]) + dp[i-1];

                if(i < 3) continue;

                dp[i] = Math.min(dp[i], dp[i-3]+fees[2]);

                if(i<12) continue;

                dp[i] = Math.min(dp[i], fees[3]);
            }
            System.out.println("#" + testcase + " " + dp[12]);
        }
    }
}
