import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(br.readLine());
        int sum = 0;
        int max = 0;

        for (int i = 0; i < N; i++) {
            int token = Integer.parseInt(st.nextToken());
            if (token > max)
                max = token;
            sum += token;
        }

        System.out.println(sum * 100.0 / max / N);
    }
}
