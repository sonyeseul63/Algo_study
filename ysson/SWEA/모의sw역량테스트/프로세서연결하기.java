package ysson.SWEA.모의sw역량테스트;

import java.util.*;
import java.io.*;

public class 프로세서연결하기 {
    static int[][] cores;
    static int coreSize;
    static int[][] board;
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int testcase = 1; testcase<=T; testcase++){
            N = Integer.parseInt(br.readLine());
            board = new int[N][N];
            cores = new int[13][2];
            coreSize = 0;
            int idx = 0;
            for(int i = 0; i<N; i++){
                StringTokenizer st = new StringTokenizer(br.readLine());
                for(int j = 0; j<N; j++){
                    board[i][j] = Integer.parseInt(st.nextToken());

                    if(board[i][j] == 1){
                        if(i==0 || i==N-1 || j== 0|| j==N-1)
                            coreSize++;
                        else{
                            cores[idx++] = new int[]{i, j};
                            coreSize++;
                        }
                    }
                }
            }

            coreLen = new int[13];
            maxCore = 0;
            conn(0, 0, 0);
            System.out.println("#" + testcase + " " + coreLen[maxCore]);
        }
    }
    

    // 같은 코어수마다 길이 다름(최소 길이 저장하는 용도)
    static int[] coreLen;
    static int maxCore;
    // 방향 : 상, 하, 좌, 우
    static int[] dr ={-1,1,0,0};
    static int[] dc = {0,0,-1,1}; 
    // 한 재귀 수 만큼 재귀
    public static void conn(int idx, int totalLen, int totalCore){
        if(coreSize - idx + totalCore < maxCore) return;

        if(idx == coreSize) {
            if(coreLen[totalCore] != 0){
                coreLen[totalCore] = Math.min(totalLen, coreLen[totalCore]);
            }
            else{
                coreLen[totalCore] = totalLen;
            }
            maxCore = Math.max(maxCore, totalCore);
            return;
        }
        
        
        // 해당 코어 연결 안 함
        conn(idx+1, totalLen, totalCore);
        
        // 해당 방향으로 갈 수 있는지 확인 후 넘기기
        for(int i = 0; i<4; i++){
            if(isPossible(cores[idx][0], cores[idx][1], i)){
                int cnt = checking(cores[idx][0], cores[idx][1], i, 1);
                conn(idx+1, totalLen+cnt, totalCore+1);
                checking(cores[idx][0], cores[idx][1], i, -1);
            }
        }
        
    }
    
    public static boolean isPossible(int r, int c, int i){
        int nr = r, nc = c;
        while(true){
            nr += dr[i];
            nc += dc[i];
            if(nr<0 || nc < 0 || nr > (N-1) || nc >(N-1)) break;
            if(board[nr][nc] == 1) return false;
        }
        return true;
    }

    // 방문 체크
    // 뱡향별로, code는 -1, 1
    public static int checking(int r, int c, int i, int code){
        int cnt = 0;
        int nr = r, nc = c;
        while(true){
            nr += dr[i];
            nc += dc[i];
            if(nr<0 || nc < 0 || nr > (N-1) || nc > (N-1)) break;
            board[nr][nc] += code;
            cnt++;
        }
        return cnt;
    }
}




// 교차 된 것을 어떻게 아나 -> cell의 사용여부
// core는 하나씩 탐색
// 백트래킹에서 전선 연결부분 used 처리하고, 중간에 전선만ㄴ나면 return히면서 used 지움
// 다른 방향탐색
// 그래도 안되면 ㄴㄴ
// 전선 안만나면 끝까지 useud 처리하고, 연결수++, 전선수 ++ 아에 종료
// 종료되면 다른 core 실행

// 한 코어당 4방향 탐색해야함
// 안되는 경우, 되는 경우 구분해야함
// 방향 다르게 했을때 아에 route 자체가 바뀔 수 있음
// 종료는 네 방향 다 탐색

// 되는 전선일지는 그냥 재귀 보다는 현재 코어 위치 ~ 끝 까지 for 로 visited 있는 지
// 재귀는 코어 수 만큼? 