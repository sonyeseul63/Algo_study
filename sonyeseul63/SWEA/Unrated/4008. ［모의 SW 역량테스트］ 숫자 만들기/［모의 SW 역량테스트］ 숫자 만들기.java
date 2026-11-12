

import java.io.*;
import java.util.*;

public class Solution {
	static int[] oper, num;
	static int n;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T= Integer.parseInt(br.readLine());
		for(int testcase = 1; testcase <= T; testcase++) {
			n = Integer.parseInt(br.readLine());
			oper = new int[4]; // 1:'+', 2:'-', 3:'*', 4:'/'
			num = new int[n];
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int i = 0; i<4; i++) {
				oper[i] = Integer.parseInt(st.nextToken());
			} 
			st = new StringTokenizer(br.readLine());
			for(int i =0; i<n; i++) {
				num[i] = Integer.parseInt(st.nextToken());
			}
			
			min = Integer.MAX_VALUE;
			max = Integer.MIN_VALUE;
			
			bt(1, num[0]);
			System.out.println("#" + testcase + " " + Math.abs(min-max));
		}
	}
	
	static int min;
	static int max;
	
	// 연산자 조합 & 계산
	private static void bt(int dept, int sum) {
		// 종료 조건
		if(dept == n) {
			// 최대 최소
			min = Math.min(min, sum);
			max = Math.max(max, sum);
			return;
		}
		
		// 조합
		for(int i = 0; i<4; i++) {
			if(oper[i] > 0) {
				oper[i]--;
				int after_sum = calc(sum, num[dept], i);
				bt(dept+1, after_sum);
				
				oper[i]++;
			}
		}
	}
	
	private static int calc(int n1, int n2, int oper) {
		switch(oper) {
		case 0 : return n1 + n2;
		case 1 : return n1 - n2;
		case 2 : return n1 * n2;
		case 3 : return n1 / n2;
		}
		return 0;
	}
}
// 여기서 얻어갈 조합, 백트