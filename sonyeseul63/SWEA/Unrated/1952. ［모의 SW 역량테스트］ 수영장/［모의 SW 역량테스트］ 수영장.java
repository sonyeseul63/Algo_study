import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static int d, m, t, y;
	static int[] plan, dp;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int testcase = 1; testcase <= T; testcase++) {
			StringTokenizer st= new StringTokenizer(br.readLine());
			d = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			t = Integer.parseInt(st.nextToken());
			y = Integer.parseInt(st.nextToken());
			
			st = new StringTokenizer(br.readLine());
			plan = new int[13];
			dp = new int[13];
			for(int i = 1 ; i<= 12; i++) {
				plan[i] = Integer.parseInt(st.nextToken());
			
				// d일때 
				int fee = plan[i] * d;
				
				// m 일때
				fee = Math.min(fee, m);
				
				dp[i] = dp[i-1] + fee;
				
				// 3m 일때 : 3개월까지의 누적값
				if(i >=3 ) {
					// 비교대상
					dp[i] = Math.min(t + dp[i-3], dp[i]);
				}
			}
			int answer = Math.min(y, dp[12]);
			System.out.println("#" + testcase + " " + answer);
		}
	}
}
