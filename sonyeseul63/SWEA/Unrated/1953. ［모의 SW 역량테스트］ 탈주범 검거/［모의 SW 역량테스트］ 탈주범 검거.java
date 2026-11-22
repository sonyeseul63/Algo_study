
import java.util.*;
import java.io.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T=Integer.parseInt(br.readLine());
        for(int testcase = 1; testcase<=T; testcase++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());

            int[][] board = new int[n][m];
            for(int i = 0; i< n; i++){
                st = new StringTokenizer(br.readLine());
                for(int j = 0; j<m ; j++){
                    board[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            // 상 우 하 좌
            boolean[][] pipe = {
                {false, false, false, false}, // 0: 터널 없음
                {true,  true,  true,  true }, // 1
                {true,  true,  false, false}, // 2: 상하
                {false, false, true,  true }, // 3: 좌우
                {true,  false, false, true }, // 4: 상우
                {false, true,  false, true }, // 5: 하우
                {false, true,  true,  false}, // 6: 하좌
                {true,  false, true,  false}  // 7: 상좌
            };

            int[] dr = {-1,1,0,0};
            int[] dc= {0,0,-1,1};
            int[] opposite = {1,0,3,2};
            boolean[][] visited = new boolean[n][m];
            Queue<int[]> q = new ArrayDeque<>();
            q.offer(new int[]{r, c, 1});
            visited[r][c] = true;
            int cnt = 1;
            while(!q.isEmpty()){
                int[] cur = q.poll();
                int cr = cur[0];
                int cc = cur[1];
                int time = cur[2];
                int tun = board[cr][cc];
                
                if(time == t) break;

                // dir
                for(int i = 0; i<4; i++){
                    // 현제에서 가는 범위
                    if(!pipe[board[cr][cc]][i]) continue;

                    int nr = cr + dr[i];
                    int nc = cc + dc[i];
                    
                    // 다음 것 유효한지
                    if(nr<0 || nc <0 || nr >= n || nc >= m) continue;
                    if(visited[nr][nc]) continue;
                    if(!pipe[board[nr][nc]][opposite[i]]) continue;

                    // 유효하면 다음 작업 
                    visited[nr][nc] = true;
                    q.offer(new int[]{nr, nc, time+1});
                    cnt++;
                }
            }

            System.out.println("#" + testcase +" " + cnt);
        }
    }
}
// 세로n, 가로m, 맨홀뚜껑위치r, 맨홀뚜껑위치c, 탈출 후 소요시간
// 상하좌우 
// 1 -> 0,1,2,3
// 2 -> 0,1
// 3 -> 2, 3
// 4 -> 0, 3
// 5 -> 1, 3
// 6 -> 0, 2
// 7 -> 1, 2

// 한칸씩 갈 수 있는 곳 방문 하고, 방문한 갯수 -> bfs

// 각 칸의 정보를 저장하려면?
