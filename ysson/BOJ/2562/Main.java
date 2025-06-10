import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] arg) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(system.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(system.in));

                int max = -1;
        int idx = 0;
        for (int i = 1; i <= 9; i++) {
            int n = Integer.parseInt(br.readLine());
            if (n > max) {
                max = n;
                idx = i;
            }
        }
        bw.write(max + "\n");
        bw.write(idx + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}