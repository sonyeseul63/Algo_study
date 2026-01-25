import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int sum = 0;
        long result = 0;
        long[] sumArr = new long[m + 1];
        sumArr[0] = 1;

        for (int i = 1; i <= n; i++) {
            int num = Integer.parseInt(st.nextToken());
            sum = (sum + num) % m;
            result += sumArr[sum];
            sumArr[sum]++;
        }

        System.out.print(result);
    }
}
