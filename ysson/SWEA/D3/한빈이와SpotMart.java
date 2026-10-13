package ysson.SWEA.D3;
import java.io.*;
import java.util.*;
public class 한빈이와SpotMart {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int testcase = 1; testcase <= T; testcase++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            int[] snacks = new int[N];
            for(int i = 0; i< N;i++){
                snacks[i] = Integer.parseInt(st.nextToken());
            }

            int l = 0; 
            int r = N-1;
            int answer = -1;
            Arrays.sort(snacks);
            while(l < r){
                if(snacks[l] + snacks[r] == M){
                    answer = M;
                    break;
                }
                else if(snacks[l] + snacks[r] > M){
                    r--;
                }
                else{ // snacks[l] + snacks[r] < M
                    if(answer < snacks[l] + snacks[r]){
                        answer = Math.max(snacks[l] + snacks[r], answer);
                    }
                    l++;
                }
            }
            System.out.println("#" + testcase + " " + answer );
        }   
    }
    
}
