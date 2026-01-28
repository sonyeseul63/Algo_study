import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        int cnt = 0;
        int i, j, c, target, sum;

        for (c = 1; c < n; c++) {
            i = 0;
            j = n - 1;
            while (i < j) {
                if (i == c) {
                    i++;
                    continue;
                }
                if (j == c) {
                    j--;
                    continue;
                }

                sum = arr[i] + arr[j];
                target = arr[c];

                if (sum == target) {
                    cnt++;
                    break;
                } else if (sum > target) {
                    j--;
                } else {
                    i++;
                }
            }
        }

        System.out.print(cnt);
    }
}
