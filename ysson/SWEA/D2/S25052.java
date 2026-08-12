package ysson.SWEA.D2;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;

public class S25052 {
    static int T;
    static int N;
    static int[][] arr;
    static int[][] visited;

    static int[] dr = {-1,1,0,0};
    static int[] dc = {0,0,-1,1};

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());
        for(int test_case = 1; test_case <= T; test_case++){
            input();

            int answer = 0;

            for(int i = 0; i < N; i++){
                for(int j= 0; j< N; j++){
                    answer = Math.max(answer, dfs(i, j));
                }
            }

            System.out.println("#" + test_case + " " + answer);
        }
    }
    
    // 입력처리 함수
    static void input() throws IOException{
        N = Integer.parseInt(br.readLine());
        arr = new int[N][N];
        visited= new int[N][N];
        for(int i = 0; i < N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j<N;j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }

    // 방문 안 한 시작점(r, c) -> 최장거리 
    static int dfs(int r, int c){
        // 방문 했으면 
        if(visited[r][c] != 0){
            return visited[r][c];
        }

        // 현재 처리
        visited[r][c] += 1;

        // 탐색 시작 - 작은 거 찾기
        int target = arr[r][c];
        int target_r = r;
        int target_c = c;
        for (int i = 0; i< 4; i++){
            int nr = r + dr[i];
            int nc = c + dc[i];
            if(nr < 0 || nc <0 || nr >=N || nc>= N){
                continue;
            }
            if(target > arr[nr][nc]){
                target = arr[nr][nc];
                target_r = nr;
                target_c = nc;
            }
        }
        
        // 재귀 탐색
        if(target != arr[r][c]) {
            return visited[r][c] += dfs(target_r, target_c);
        }

        return visited[r][c];
    }
}

// dfs.. -> method? stack?
// 어차피 한번 지난 거는 끝.. (길의 갈 수 있는 방향이 하나다) -> visited
// visited에 해당 시작점에서의 최장거리 저장
// 방문 노드가 visitied 더하기, 아니면 순회
// 탐색 -> 제일 작은거
