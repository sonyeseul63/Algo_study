package sonyeseul63.SWEA.모의sw역량테스트;

import java.util.*;
import java.io.*;

public class 화물도크 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int testcase = 1; testcase <= T; testcase++) {
            int N = Integer.parseInt(br.readLine());
            int[][] docs = new int[N][2];
            for(int i = 0; i<N; i++){
                StringTokenizer st = new StringTokenizer(br.readLine());
                docs[i][0] = Integer.parseInt(st.nextToken());
                docs[i][1] = Integer.parseInt(st.nextToken());
            }

            Arrays.sort(docs, (a, b) -> Integer.compare(a[1], b[1]));
            int cnt = 0;
            int end = 0;
            for(int i = 0; i < docs.length; i++){
                if(docs[i][0]>=end){
                    cnt++;
                    end = docs[i][1];
                    System.out.println(cnt + " " + end);
                }
            }
            System.out.println("#" + testcase + " " + cnt);
        }
    }   
}
// 끝나는 시간이 기준으로 정렬해서, 작은거부터처리
// Arrays.sort(arr, (a, b) -> Integer.compare(a[1], b[1]))