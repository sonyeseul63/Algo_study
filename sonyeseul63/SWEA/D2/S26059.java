package sonyeseul63.SWEA.D2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;
import java.util.Arrays;

public class S26059 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int testcase = 1; testcase <= T; testcase++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int lo = Integer.parseInt(st.nextToken());
            int hi = Integer.parseInt(st.nextToken());
            int[] arr = new int[N];
            for(int i = 0; i < N; i++){
                arr[i] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(arr);

            // 입력 값 검증
            if((N/3 < lo) || (3 * lo > N) || (3 * hi > N)){
                System.out.println("#" + testcase + " -1");
                break;
            }

            // 삼지창
            
        }
    }
}

// 경계에 있는 값 le, ri
// le, ri-le, (N-1)-ri
// 초기값과 방향을.. 3등분해서 그 값에서 조정..?
// 고려해야할 값 -> 
// - 한 구간의 최대/최소 -> 3/N > 최소, 3 * 최소 < N < 3 * 최대
// - 경계에 같은 값 -> 후보군 생성? 
// N이 1000 이하니까, 중첩 반복 가능하긴함