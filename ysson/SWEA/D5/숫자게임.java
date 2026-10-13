package ysson.SWEA.D5;
import java.util.*;
import java.io.*;

public class 숫자게임 {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T= Integer.parseInt(br.readLine());
        for(int testcase = 1; testcase <= T; testcase++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String str = st.nextToken();
            max = 0;
            divi(str, 0);

            System.out.println("#" + testcase + " " + max);
        }
    }

    static int max;
    public static void divi(String str, int turn){

        너
    }
}
// 시작수 1 ~ 99999
// 규칙 : 한 숫자 사이 -> 2개 이상으로 쪼개짐 (?)
//         -> 쪼개진 수들을 곱
// 이후의 조건 : 곱한수 >= 10 -> 쪼개질 수 없을 때까지 위의 행동 계속 반복함
// 이때, turn : 쪼갠 횟수
// answer : 최대 turn


// 쪼갠다 -> split
// 한자리수 -> null, 그 숫자 그대로 -> 분기해서 멈추는 조건

// String을 다루는 것 ->  한 자리수 뽑기, SubString(start, end) {start ~ end-1}