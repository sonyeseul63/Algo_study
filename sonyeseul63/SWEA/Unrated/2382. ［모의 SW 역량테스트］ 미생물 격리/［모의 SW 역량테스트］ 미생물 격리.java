

import java.io.*;
import java.util.*;

public class Solution {
	static int n, m, k;
	static int[] dr = {0, -1, 1,0,0};
	static int[] dc = {0,0,0,-1,1}; // 상하 좌우, 방향 전환-> idx 2의 배수면--, 아니면 ++
	static int[][] list;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int testcase = 1; testcase <= T; testcase++) {
			StringTokenizer st= new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			k = Integer.parseInt(st.nextToken());
			
			// 미생물 관리 -> 2차원 배열 리스트
			list = new int[k+1][5];
			for(int i = 1; i<=k; i++) {
				st = new StringTokenizer(br.readLine());
				list[i][0] = Integer.parseInt(st.nextToken());
				list[i][1] = Integer.parseInt(st.nextToken());
				list[i][2] = Integer.parseInt(st.nextToken());
				list[i][3] = Integer.parseInt(st.nextToken());
			}
			
			// 시점별로 이동 관리, 충돌 체크
			for(int time = 0; time <m; time++) {
				int[][] board = new int[n][n];
				
				// 미생물 하나씩 이동
				for(int i = 1; i<=k; i++) {
					if(list[i][2] <= 0) continue;
					
					int d= list[i][3];
					int nr = list[i][0] + dr[d];
					int nc = list[i][1] + dc[d];
					
					// 미생물 위치 갱신
					list[i][0] = nr;
					list[i][1] = nc;
					
					// 맨 끝에서는 충돌하지 않으네
					if(nr==0 || nc==0 || nr ==n-1 || nc ==n-1) {
						list[i][2] /= 2;
						list[i][3] = (d % 2== 0 ? d-1 : d+1);
					}
					
					if(board[nr][nc] == 0) {
						board[nr][nc] = i;
						list[i][4] = list[i][2];
						continue;
					}
					
					// 충돌 확인
					if(board[nr][nc] != 0) {
						int pre = board[nr][nc];
						int total = list[pre][4] + list[i][2];
							
						if(list[pre][2] < list[i][2]) {
							list[i][4] = total;
							board[nr][nc] = i;
							list[pre][4] = 0;
							list[pre][2] = 0;
						} else {
							list[pre][4] = total;
							list[i][4] = 0;
							list[i][2] = 0;
						}
					}
				}
				
				// 순회 끝난 후 충돌 정리
				for(int[] life: list) {
					if(life[4] > life[2]) {
						life[2] = life[4];
						life[4] = 0;
					}
				}
			}
			
			int answer = 0;
			for(int[] life:list) {
				answer += life[2];
			}
			
			System.out.println("#" + testcase + " " + answer);
		}
	}
}

// 모두 이동후 셀에 남아있는거 수집 or 죽은 거 표시? 목록 관리
// total은 가지고, 이전거랑 계속 비교해야함. idx =4 에 total 가지고, 살려두는건 순수 [2]가 큰 것. 죽은애는 -1
