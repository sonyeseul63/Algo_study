package ysson.SWEA.D3;

import java.io.*;
import java.util.*;

public class 규영이와인영이의카드게임 {
    static int[] iy; // 인영이 카드 후보
    static int[] ky; //순서를 인덱스로
    static boolean[] used;
    static int total;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int testcase = 1; testcase <=T; testcase++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
            iy = new int[9];
            ky = new int[9];
            used = new boolean[9];
            boolean[] isky = new boolean[19];
            for(int i = 0; i<9; i++){
                ky[i] = Integer.parseInt(st.nextToken());
                isky[ky[i]] = true;
            }
            total = 0;
            int idx = 0;
            for(int i = 1; i<= 18; i++){
                total += i;
                if(!isky[i]) iy[idx++] = i; 
            }

            kyWin = 0;
            kyLose = 0;
            perm(0, 0, 0, 0);
            System.out.println("#" + testcase + " " + kyWin + " " + kyLose);
        }
    }

    static int kyWin;
    static int kyLose;
    public static void perm(int depth, int kySum , int iySum, int usedSum){
        if(depth == 9){
            if(kySum < iySum) kyLose++;
            else if(kySum > iySum) kyWin++;
            return;
        }

        if(kySum > iySum + (total - usedSum)){
            kyWin += factorial(9 - depth);
            return;
        }

        if(iySum > kySum + (total - usedSum)){
            kyLose += factorial(9 - depth);
            return;
        }

        for(int i = 0; i<9; i++){
            if(used[i]) continue;

            used[i] = true;
            if(iy[i] < ky[depth]){
                perm(depth + 1, kySum + ky[depth] + iy[i], iySum, usedSum + ky[depth] + iy[i]);
            }
            else if(iy[i] > ky[depth]){
                perm(depth + 1, kySum, iySum + ky[depth] + iy[i], usedSum + ky[depth] + iy[i]);
            }
            else{
                perm(depth + 1, kySum, iySum, usedSum + ky[depth] + iy[i]);
            }
            used[i] = false;
        }

        return;
    }
    
    // 남은 뒷자리 순열 개수
    public static int factorial(int n){
        int result = 1;
        for(int i = n; i > 0 ; i--){
            result *= i;
        }
        return result;
    }
}
// 1 - 18
// 규영이 카드 9개 제시됨
// 인영이 카드 순열에 따른 각 매칭의 값 -> 규영이가 이기는 경우, 지는 경우(비기는 경우도 있으니까.)