import java.io.*;
import java.util.*;

public class Solution {
	static int D, W, K;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int testcase = 1; testcase<=T; testcase++) {
			StringTokenizer st  =new StringTokenizer(br.readLine());
			D = Integer.parseInt(st.nextToken()); // 두께
			W = Integer.parseInt(st.nextToken()); // 가로
			K = Integer.parseInt(st.nextToken()); // 기준 
			
			int[][] film = new int[D][W];
			for(int i = 0; i< D; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j = 0; j<W; j++) {
					film[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			answer = Integer.MAX_VALUE;
			
			bt(0,0,film);
			
			System.out.println("#" + testcase + " " + answer);
		}
	
	}
	
	// 단순히 백트래킹이라면 
	// 머부터 바꿔야하지...
	// 바꾼게 의미있단건 어케알지
	// 한줄에서 a, b, x
	static int answer;
	public static void bt(int dept, int cnt, int[][] film) {
		// 연속되어있는지
		if(isSeq(film)) {
			if(dept==0) {
				answer = 0;
			} else {
				answer = Math.min(answer, cnt);
			}
			return;
		}

		if(dept == D) return;
		
		if(cnt >= answer) return;
		
		// 안바꿔
		bt(dept+1, cnt, film);
		
		
		// 바꿔
		int[] origin = film[dept];
		// a -> 0
		int[] next = new int[W];
		
		film[dept] = next;
		bt(dept+1, cnt+1, film);
		
		// b -> 1
		Arrays.fill(next, 1);
		film[dept] = next;
		bt(dept+1, cnt+1, film);
		
		
		film[dept] = origin;

	}
	
	// 연속되어있는지
	public static boolean isSeq(int[][] film) {
		for(int i = 0; i< W; i++) {
			// 한 줄씩
			int cnt = 1;
			int max_cnt = 0;
			for(int j = 1; j < D; j++) {
				if(film[j][i] == film[j-1][i]) cnt++;
				
				max_cnt = Math.max(max_cnt, cnt);
				
				if(film[j][i] != film[j-1][i]) cnt = 1;
			}
			if(max_cnt < K) return false;
		}
		
		return true;
	}

}