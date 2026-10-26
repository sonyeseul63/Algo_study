import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        int i = 1;
        int j = 1;
        int sum = 0; // i ~ j까지의 구간
        int cnt = 0;

        while (i <= n) {
            if (sum < n) {
                sum += j;
                j++;
            } else if (sum == n) { // 시작점을 옮긴다
                cnt++;
                sum -= i++;
            } else if (sum > n) {
                sum -= i;
                i++;
            }
        }

        System.out.print(cnt);
    }
}
