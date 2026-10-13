package ysson.SWEA.D5;

import java.io.*;
import java.util.*;

public class 수제버거장인 {
    static int N, M;
    static boolean[][] blackList;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int testcase = 1; testcase <= T; testcase++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
            blackList = new boolean[N+1][N+1];
            for(int i = 0; i<M; i++){
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                blackList[a][b] = true;
                blackList[b][a] = true;
            }

            total = 0;
            used = new boolean[N+1];
            makeBurg(1);
            System.out.println("#" + testcase + " " + total);
        }
    }

    static int total;
    static boolean[] used;
    public static void makeBurg(int idx){

        if(idx == N+1) {
            total++;
            return;
        }

        makeBurg(idx+1);

        // 이제 추가하려는 idx에 대하여 기존의 재료와 안되는 조합인지 확인
        boolean isPossible = true;
        for(int i = 0; i<= idx; i++){
            if(used[i] && blackList[i][idx]){
                isPossible = false;
                break;
            }
        }

        if(isPossible){
            used[idx] = true;
            makeBurg(idx+1);
            used[idx] = false;
        }
        
    }
}
