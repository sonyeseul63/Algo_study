package sonyeseul63.SWEA.D4;

import java.io.*;
import java.util.*;

public class 장훈이의높은선반 {
    static int[] heights;
    static int N,target;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int testcase = 1; testcase <= T; testcase++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            target = Integer.parseInt(st.nextToken());
            heights = new int[N];
            st = new StringTokenizer(br.readLine());
            for(int i = 0; i < N;i++){
                heights[i] = Integer.parseInt(st.nextToken());
            }

            minDiff = heights[0];
            makeTeam(0, 0);
            System.out.println("#" + testcase + " " + minDiff);
        }
    }


    static int minDiff;
    public static void makeTeam(int depth, int sum){
        if(target <= sum){
            minDiff = Math.min(minDiff, sum-target);
            return;
        }

        if(depth == N){
            return;
        }

        makeTeam(depth+1, sum+heights[depth]);

        makeTeam(depth+1, sum);
    }
}
