package ysson.SWEA.D3;
import java.io.*;
import java.util.*;
public class 퍼펙트셔플 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T= Integer.parseInt(br.readLine());
        for(int testcase = 1; testcase <= T; testcase++){
            int N = Integer.parseInt(br.readLine());
            StringTokenizer st= new StringTokenizer(br.readLine());
            String[] arr = new String[N];
            for(int i = 0; i<N; i++)
                arr[i] = st.nextToken();
            
            int half = (N+1) / 2;
            System.out.print("#" + testcase + " ");
            for(int i = 0; i< half ;i++){
                System.out.print(arr[i] + " ");
                
                if(half + i < N){
                    System.out.print(arr[half+i] + " ");
                }
            }
            System.out.println("");
        }
    }
}
//