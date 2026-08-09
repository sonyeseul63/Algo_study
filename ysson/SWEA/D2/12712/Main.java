import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int test_case = 1; test_case <= T; test_case++){
            // 케이스별 입력 처리
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int[][] arr = new int[N][N];
            for(int i = 0; i<N; i++){
                st = new StringTokenizer(br.readLine());
                for(int j = 0; j<N; j++){
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int answer = 0;

            // 방향 백터
            int[] cross_dr = {-1, 1, -1, 1};
            int[] cross_dc = {-1, -1, 1, 1};
            int[] plus_dr = {-1, 1, 0, 0};
            int[] plus_dc ={ 0, 0, -1, 1};
            // 중심점 돌면서 분사 했을 때 구하기
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < N; c++) {
                    int crossSum = arr[r][c];
                    int plusSum = arr[r][c];

                    //한 방향씩
                    for (int i = 0; i < 4; i++) {
                        int cross_nr = r;
                        int cross_nc = c;
                        int plus_nr = r;
                        int plus_nc =c;
                        for (int j = 1; j < M; j++) {

                            cross_nr += cross_dr[i];
                            cross_nc += cross_dc[i];

                            if (cross_nr < 0 || cross_nr >= N || cross_nc < 0 || cross_nc >= N) {
                                break;
                            }

                            crossSum += arr[cross_nr][cross_nc];
                        }

                        
                        for (int j = 1; j < M; j++) {
                            plus_nr += plus_dr[i];
                            plus_nc += plus_dc[i];

                            if (plus_nr < 0 || plus_nr >= N || plus_nc < 0 || plus_nc >= N) {
                                break;
                            }

                            plusSum += arr[plus_nr][plus_nc];
                        }
                    }
                    answer = Math.max(answer,Math.max(crossSum, plusSum));
                }   

            }
    }

}
}