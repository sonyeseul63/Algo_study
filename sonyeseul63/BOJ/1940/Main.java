import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        int i = 0;
        int j = n - 1;
        int sum, cnt = 0;

        while (i < j) {
            sum = arr[i] + arr[j];
            if (sum < m)
                i++;
            else if (sum == m) {
                cnt++;
                i++;
                j--;
            } else if (sum > m)
                j--;
        }

        System.out.print(cnt);
    }
}