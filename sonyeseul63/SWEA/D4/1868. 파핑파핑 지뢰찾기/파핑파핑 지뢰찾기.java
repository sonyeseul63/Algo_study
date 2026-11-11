
import java.io.*;
import java.util.*;

public class Solution {
	static int n;
	static boolean[][] bomb, visited;
	static ArrayDeque<int[]> dq;
	static int[] dr = {-1,-1, -1,0,1,1,1,0};
	static int[] dc = {-1,0,1,1,1,0,-1,-1};
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int testcase = 1; testcase<=T; testcase++) {
			n = Integer.parseInt(br.readLine());
			int total = 0;
			bomb = new boolean[n][n];
			for(int i = 0; i<n; i++) {
				String str =br.readLine();
				for(int j = 0; j<n; j++) {
					if(str.charAt(j) == '.') {
						bomb[i][j] = false;
						total++;
					}
					else bomb[i][j] = true;
				}
			}
			
			visited = new boolean[n][n];
			dq = new ArrayDeque<>();

			int answer = 0;
			// 미방문 not bomb면 bfs행
			for(int i = 0; i<n; i++) {
				for(int j = 0; j<n; j++) {
					if(!bomb[i][j] && !visited[i][j]) {
						
						// 주변에 다 0인거 먼저 처리
						if(isZero(i, j)) {
							// 현재 방문
							visited[i][j] = true;
							// 큐에 넣기
							dq.offer(new int[] {i, j});
							// bfs
							total -= bfs();
							answer++;
						}

					}
				}
			}
			
			System.out.println("#" + testcase + " " +(total+ answer));
		}
		
	}
	
	// 터뜨린 개수 
		private static int bfs() {
			int cnt = 1;
			while(!dq.isEmpty()){
				int[] now = dq.poll();
				int r= now[0];
				int c= now[1];

				
				for(int d = 0; d<8;d++) {
					int nr = r+dr[d];
					int nc = c+dc[d];
					if(nr<0 || nc<0 || nr>=n|| nc>=n) continue;
					if(visited[nr][nc]) continue;
						
					visited[nr][nc] = true;
					cnt++;
					
					// 주변에 다 0인지
					if(isZero(nr, nc))
						dq.offer(new int[] {nr, nc});
				}
				
			}
			return cnt;
		}
	
		private static boolean isZero(int r, int c) {
			for(int d = 0; d<8; d++) {
				int nr = r+dr[d];
				int nc = c+dc[d];
				if(nr<0 || nc<0 || nr>=n|| nc>=n || visited[nr][nc]) continue;
				if(bomb[nr][nc]) return false;
			}
			return true;
		}
	
	
}
