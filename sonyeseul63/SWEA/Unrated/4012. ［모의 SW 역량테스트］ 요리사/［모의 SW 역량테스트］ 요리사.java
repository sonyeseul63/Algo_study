

import java.io.*;
import java.util.*;

public class Solution {
	static int[][] map;
	static int n;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int testcase = 1; testcase<=T; testcase++) {
			n = Integer.parseInt(br.readLine());
			map = new int[n+1][n+1];
			for(int i = 1; i <= n;i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for(int j =1; j<= n;j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			// 부분집합 맹들기
			comb = new int[n+1];
            answer = Integer.MAX_VALUE;
			bt(2, 0); // comb[1] = 0 고정 
			System.out.println("#"+ testcase + " " + answer);
		}
	}
	
	static int[] comb;
    static int answer;
	private static void bt(int dept, int cnt) {
        if(cnt > n/2) return;

        if(dept > n) {
            if(cnt == n/2){
			// 조합으로 차이 구하기
            answer = Math.min(answer, p());
            }
            return;
        }
		
		comb[dept] = 0;
		bt(dept+1, cnt);
		comb[dept] = 1;
        bt(dept+1, cnt+1);
	}

    private static int p(){
        // 조합 for로 만들면서 합 구하기
        int c0 = 0;
        int c1 = 0;
        for(int i = 1; i<n ;i++){
            for(int j = i+1; j<=n; j++){
                if(comb[i] == 0 && comb[j] == 0){
                    c0 += (map[i][j]+map[j][i]);
                }
                if(comb[i] == 1 && comb[j] == 1){
                    c1 += (map[i][j]+map[j][i]);
                }
            }
        }

        return Math.abs(c0-c1);
    }
}



// n개 중에 2개의 군집으로 나눔 -> 
// 군집내의 원소 중 두개씩 순열 -> 해당 map value
// 최적화 기법 -> ab/cd == cd/ab
