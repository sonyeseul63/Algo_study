import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[][] board;
    static boolean[] isTeamA;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        board = new int[n+1][n+1];
        for(int i = 1; i<=n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 1; j<=n; j++){
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        isTeamA = new boolean[n+1];  // visited  
        isTeamA[1] = true; // 1번 무조건 A팀에 

        answer = Integer.MAX_VALUE;
        match(1, 1);
        System.out.println(answer);
    }

    static int answer;
    private static void match(int dept, int idx){
        if(dept > n/2){
            answer = Math.min(answer, sumTeam());
            return;
        }

        if(idx > n) return;

        // idx를 어떤 팀에 배치
        isTeamA[idx] = true;
        match(dept+1, idx+1);

        isTeamA[idx] = false;
        match(dept, idx+1);

    }

    // 배열로 할 수 있는 조합들
    private static int sumTeam(){
        int totalA = 0;
        int totalB = 0;
        for(int i = 0; i < n; i++){
            for(int j=i+1; j<=n; j++){

                if(isTeamA[i] && isTeamA[j])
                    totalA += board[i][j] + board[j][i];
                else if(!isTeamA[i] && !isTeamA[j])
                    totalB += board[i][j] + board[j][i];
            }
        }
        return Math.abs(totalA - totalB);
    }
}

// 1번이 누구와 팀인지만 알면 게산 가능
// 부분 집합으로 팀짜고 계산할 땐 조합
// 가지치기가 가능한 경우가 있나?

// 모든 두수의 조합을 보며 같은팀인지 어떤 팀인지 다른팀인지
