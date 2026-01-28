import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());

        String dna = br.readLine();

        st = new StringTokenizer(br.readLine());
        int[] arr = new int[4];
        for (int i = 0; i < 4; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int i = 0;
        int j = 0;
        int cnt = 0;
        int[] part = new int[4];
        for (j = 0; j < p; j++) {
            char c = dna.charAt(j);
            if (c == 'A')
                part[0]++;
            if (c == 'C')
                part[1]++;
            if (c == 'G')
                part[2]++;
            if (c == 'T')
                part[3]++;
        }

        if (part[0] >= arr[0] && part[1] >= arr[1] && part[2] >= arr[2] && part[3] >= arr[3]) {
            cnt++;
        }

        while (j < s) {
            char c1 = dna.charAt(i);
            char c2 = dna.charAt(j);

            if (c1 == 'A')
                part[0]--;
            if (c1 == 'C')
                part[1]--;
            if (c1 == 'G')
                part[2]--;
            if (c1 == 'T')
                part[3]--;

            if (c2 == 'A')
                part[0]++;
            if (c2 == 'C')
                part[1]++;
            if (c2 == 'G')
                part[2]++;
            if (c2 == 'T')
                part[3]++;

            if (part[0] >= arr[0] && part[1] >= arr[1] && part[2] >= arr[2] && part[3] >= arr[3]) {
                cnt++;
            }

            i++;
            j++;
        }
        System.out.print(cnt);
    }
}
