
import java.util.*;
import java.io.*;
public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for(int testcase = 1; testcase<=T; testcase++){
            int n= Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());

            int[] trees = new int[n];
            int max_h = 0;
            for(int i = 0; i<n; i++){
                trees[i] = Integer.parseInt(st.nextToken());
                max_h = Math.max(max_h, trees[i]);
            }

            int aCnt = 0;
            int bCnt = 0;
            for(int i = 0; i< n; i++){
                int diff = max_h - trees[i];

                bCnt += diff/2;
                aCnt += diff%2;

            }

            // 고르게 분배
            while(bCnt > aCnt +1){
                bCnt--;
                aCnt+=2;
            }
            
            // a가 훨씬 많을 때
            // b가 a보다 1 더 많을때
            // a와 b의 개수에 따라 최종 걸린 날짜 구하기
            int end = (bCnt >= aCnt) ? 2*bCnt : 2*aCnt-1;;

            System.out.println("#"+ testcase + " " + end);
        }
    }
}

// 그리디인 이유
// 남는 짝수 날(+2)을 홀수 날(+1) 두 번으로 바꾸어, 쉬는 날을 줄일 수 있다면 바꾼다.
// -> 2와 1 개수의 균형을 맞추는 상황 (빈 날이 없도록)
// n2 > n1+1