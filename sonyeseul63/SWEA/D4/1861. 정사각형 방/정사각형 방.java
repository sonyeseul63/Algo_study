

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	static int[][] dist, arr;
	static int n;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int testcase = 1; testcase <= T; testcase++) {
			n = Integer.parseInt(br.readLine());
			arr = new int[n][n];
			dist = new int[n][n]; 
			for(int i = 0; i<n; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for(int j =0; j<n; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			// dfs 호출
			for(int i = 0; i<n; i++) {
				for(int j = 0; j<n; j++) {
					if(dist[i][j] != 0) continue;
					
					// dist 채우기 
					 dfs(i, j);
				}
			}
			
			// 최대 구하기 -> 우선순위 1. 길이 긴 것 2. 길이 같으면 최소 시작점
			int max = 0;
			int min =n+1;
			for(int i = 0; i<n; i++) {
				for(int j = 0; j<n; j++) {
					if(max < dist[i][j]) {
						max = dist[i][j];
						min = arr[i][j];
					}
					else if(max == dist[i][j]) {
						min = Math.min(arr[i][j], min);
					}
				}
			}
			
			System.out.println("#" + testcase + " " + min + " " + max);
		}
	}
	
	static int[] dr= {-1,1,0,0};
	static int[] dc = {0,0,-1,1};
	private static int dfs(int r, int c) {
		
		if(dist[r][c] != 0) return dist[r][c];
		
		dist[r][c] = 1;
		
		for(int i = 0; i<4; i++) {
			int nr = r+ dr[i];
			int nc = c+ dc[i];
			
			if(nr<0 || nc<0 || nr>=n || nc>=n) continue;
			
			if(arr[nr][nc] == arr[r][c]+1) {
				
				dist[r][c] += dfs(nr, nc);
			}
		}
		
		
		return dist[r][c]; 
	}
}

// 9칸 다 하면서 visited 표시-> 여기서부터 앞으로 몇 칸 인지
// bfs가 아니라 dfs 인 이유, 갈 수 있는 방향이 하나임. 