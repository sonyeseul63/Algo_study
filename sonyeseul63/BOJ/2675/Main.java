import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            String s = st.nextToken();

            for (int j = 0; j < s.length(); j++) {
                for (int z = 0; z < r; z++) {
                    sb.append(s.charAt(j));
                }
            }
            sb.append('\n');
        }
        System.out.println(sb);
    }
}

// 전체 반복 횟수(n), String을 순회(string의 길이만큼)하면서 각각의 문자를 r만큼 반복