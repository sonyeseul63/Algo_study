package ysson.SWEA.모의sw역량테스트;

import java.util.*;
import java.io.*;

public class 동전자판기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int total = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] wallet = new int[6];
        for(int i = 0; i < 6; i++){
            wallet[i] = Integer.parseInt(st.nextToken());
        }
        int[] coin = {500, 100, 50, 10, 5, 1};
        int sideTotal = 0;
        for(int i = 0 ; i < 6;i++){
            sideTotal += (coin[i] * wallet[i]);
        }

        sideTotal -= total;

        // 동전 최소로 지불하고 싶으면 큰 값부터 소비해라
        for(int i = 0; i<6; i++){
            int cnt = Math.min(wallet[i], sideTotal / coin[i]);
        
            wallet[i] -= cnt;
            sideTotal -= (cnt * coin[i]);

            System.out.print(wallet[i] + " ");
        }


    }
}
