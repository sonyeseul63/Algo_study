

import java.io.*;
import java.util.*;

public class Solution {
	static int n, m, c;
	static int[][] arr;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int testcase =1; testcase <=T; testcase++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());
			arr = new int[n][n];
			for(int i = 0; i< n; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j = 0; j<n; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			answer = 0;
			comb(0, 0, 0, 0);
			System.out.println("#" + testcase + " " + answer);
		}
	}
	
	static int answer;
	private static void comb(int cnt, int r, int c,int sum) {
		
		if(cnt == 2) {
			answer = Math.max(answer, sum);
			return;
		}
		
		

		for(int i = r; i<n; i++) { //가로
			for(int j = (r== i? c: 0); j<(n-m+1); j++) { //세로

				int[] candi = new int[m];
				
				for(int z = 0; z<m ;z++) {
					candi[z] = arr[i][j+z];
				}
				
				max_sum = 0;
				bt(candi, 0, 0, 0);
				
				int nr, nc;
				if(j+m >= (n-m+1)) {
					nr = i+1;
					nc = 0;
				}
				else {
					nr = i;
					nc = j+m;
				}
				
				comb(cnt+1, nr, nc, sum+max_sum); 
			}
		}
	}

	// 제곱해서 합 업데이트 -> 큰값, 일반합 -> c넘으면 안됨
	static int max_sum;
	private static void bt(int[] candi, int dept, int sum, int total) {
		if(sum> c) return;
		
		if(dept == m) {
			max_sum = Math.max(max_sum, total);
			return;
		}
		
		bt(candi, dept+1, sum+candi[dept], total+candi[dept]*candi[dept]);
		bt(candi, dept+1, sum, total);
	}
}
// M개씩 한쌍 -> 두쌍 고르기