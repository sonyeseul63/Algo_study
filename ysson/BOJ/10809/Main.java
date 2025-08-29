import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int[] Alpha = new int['z' - 'a' + 1];
        Arrays.fill(Alpha, -1);
        String s = br.readLine();
        for (int i = 0; i < s.length(); i++) {
            char j = s.charAt(i);
            if (Alpha[j - 'a'] == -1)
                Alpha[j - 'a'] = i;
        }
        for (int i = 0; i < Alpha.length; i++) {
            sb.append(Alpha[i]);
            if (i < 'z' - 'a')
                sb.append(' ');
        }
        System.out.println(sb);
    }
}

/*
 * 아스키 코드 이용해서 개수, 인덱스 값 구할때 수 달라짐 주의
 * 출력할때 strinbuilder 사용 습관화
 * legnth, length() 구분
 * 마지막 공백 제거 차이가 출력 스트림 처리와 메모리 연산 최적화에 좋다!
 */