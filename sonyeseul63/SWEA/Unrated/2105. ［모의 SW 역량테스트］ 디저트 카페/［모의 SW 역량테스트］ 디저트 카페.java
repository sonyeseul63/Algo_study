
import java.util.*;
import java.io.*;
 
public class Solution {
	static int n;
	static int[][] map;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T= Integer.parseInt(br.readLine());
		for(int testcase = 1; testcase <= T ; testcase++) {
			n = Integer.parseInt(br.readLine().trim());
			map = new int[n][n];
			StringTokenizer st;
			for(int i = 0; i<n; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j =0; j<n; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			visited = new boolean[101]; // 디저트 종류
			answer = -1;

			// dfs에 시작점 넣어 보내기
			for(int i = 0; i<n-2; i++) {
				for(int j = 1; j<n-1; j++) {
					start = new int[]{i, j};
					dfs(i, j, 0, 0, 0, 0);
				}
			}
			
			System.out.println("#" + testcase + " " + answer);
		}
	}
	// 간 방향이 마름모 처럼 되려면, 온 방향 생각해서  대칭이용
	// 한 변 그리는 순서, 직진횟수가지고 이동 방향을 제한함. 무조건 도착지에 오도록(안되는 경우는 백트래킹)
	static int[] dr = {1,1,-1,-1};
	static int[] dc = {1,-1,-1,1};
	static boolean[] visited;
	static int[] start;
	static int answer;
	private static void dfs(int r, int c, int dIdx, int f, int s, int cnt) {
		// 종료조건
		if(dIdx == 3&&start[0] == r && start[1] == c) {
			if (f == 0 && s == 0) 
				 answer = Math.max(cnt,  answer);
			return;
		}
		
		// 직진
	    if (!(dIdx == 2 && f == 0) && !(dIdx == 3 && s == 0)) {

	        int nr = r + dr[dIdx];
	        int nc = c + dc[dIdx];

	        if (nr >= 0 && nc >= 0 && nr < n && nc < n) {


	            if (!visited[map[nr][nc]]) {

	                visited[map[nr][nc]] = true;

	                if (dIdx == 0) {
	                    dfs(nr, nc, dIdx, f + 1, s, cnt + 1);
	                }
	                else if (dIdx == 1) {
	                    dfs(nr, nc, dIdx, f, s + 1, cnt + 1);
	                }
	                else if (dIdx == 2) {
	                    dfs(nr, nc, dIdx, f - 1, s, cnt + 1);
	                }
	                else if (dIdx == 3) {
	                    dfs(nr, nc, dIdx, f, s - 1, cnt + 1);
	                }

	                visited[map[nr][nc]] = false;
	            }
	        }
	    }
		
		// 방향 전환
		if (dIdx == 0 && f > 0) {
		    dfs(r, c, dIdx + 1, f, s, cnt);
		}
		else if (dIdx == 1 && s > 0) {
		    dfs(r, c, dIdx + 1, f, s, cnt);
		}
		else if (dIdx == 2 && f == 0) {
		    dfs(r, c, dIdx + 1, f, s, cnt);
		}

		
	}
}
// 한칸 이상은 가는 경우 직진하는 경우,
// dIdx == 2,3 얘네는 이미 방향이 정해짐