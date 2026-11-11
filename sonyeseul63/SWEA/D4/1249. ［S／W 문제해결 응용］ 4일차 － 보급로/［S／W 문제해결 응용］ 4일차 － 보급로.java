

import java.io.*;
import java.util.*;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int testcase = 1; testcase <= T; testcase++) {
			int n = Integer.parseInt(br.readLine());
			
			int[][] map = new int[n][n];
			for(int i = 0; i < n; i++) {
				String str = br.readLine();
				for(int j = 0; j< n; j++) {
					map[i][j] = str.charAt(j) - '0';
				}
			}
			
			// pq 설정
			PriorityQueue<int[]> pq = new PriorityQueue<>(
					(a, b) -> Integer.compare(a[2], b[2])
					);
			
			pq.offer(new int[] {0,0,0});
			
			
			// 최소 누적 확정 배열
			int[][] dist = new int[n][n];
			for(int[] row : dist) {
				Arrays.fill(row, Integer.MAX_VALUE);
			}
			dist[0][0] = 0;
			
			
			// queue 처리
			while(!pq.isEmpty()) {
				
				// 현재 pq에서 빼기
				int[] cur = pq.poll();
				int r= cur[0];
				int c= cur[1];
				int v= cur[2];
				
				// 목표지점 도착
				if(r==n-1 && c==n-1) break;
				
				// 오래된 값인지
				if(dist[r][c] < v) continue;
				
				int[] dr = {-1,1,0,0};
				int[] dc = {0,0,-1,1};
				
				// 다음 노드 방문하며 누적합 계산 -> pq, dist 갱신
				for(int d = 0; d< 4; d++) {
					int nr = r+dr[d];
					int nc = c+dc[d];
					
					if(nr<0 || nc<0 || nr>=n || nc>=n) continue;
					
					
					// 계산
					int next = v + map[nr][nc];
					
					// 이미 있는 dist값보다 작은 경우만 유효하도록
					if(dist[nr][nc] > next) {
						pq.offer(new int[] {nr, nc, next});
						dist[nr][nc] = next;
					}
				}
				
			}
			
			System.out.println("#" + testcase + " " + dist[n-1][n-1]);
		}
	}
}
