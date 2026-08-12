package ysson.SWEA.D2;
import java.util.*;

public class S25985 {
    public static void main(String[] args){
        // 입력 처리
        Scanner sc =new Scanner(System.in);
        int T = sc.nextInt();
        for(int testcase = 1; testcase <= T; testcase++){
            int N = sc.nextInt();
            int M = sc.nextInt();
            int[] A = new int[N];
            int[] B = new int[M];
            for(int i = 0; i<N; i++){
                A[i] = sc.nextInt();
            }
            for(int i = 0; i<M; i++){
                B[i] = sc.nextInt();
            }

            int max = Integer.MIN_VALUE;

            // shift : M의 index 0 을 기준으로 N의 index 0의 위치
            // j -> N 인덱스
            // shift + j : A[j] 일때 B[0+j]
            for(int shift = -(N-1); shift < M; shift++){ //A의 시작점이 올 수 있는 범위
                int sum = 0;

                for(int j = 0; j < N; j++){
                    if((shift+j >= 0) && (shift+j < M ))
                        sum += (A[j]) * (B[shift+j]);
                }

                
                if(max < sum) max = sum;
            }

            System.out.println("#" + testcase + " " + max);
        }
        sc.close();
    }
}


// 2        0
// 1 2      0 1
// 0 1 2    0 1 2
// 0 1 2    1 2 3
// 0 1 2    2 3 4
// 0 1      3 4
// 0        4

