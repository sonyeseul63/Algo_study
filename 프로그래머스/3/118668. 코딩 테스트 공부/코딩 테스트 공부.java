// 현재 능력치에서 최소 cost만 남긴다
import java.util.*;
class Solution {
    
    public int solution(int alp, int cop, int[][] problems) {
        int answer = 0;
        int n = problems.length;
        
        // 목표치 구하기
        int t_alp = 0;
        int t_cop = 0;
        
        for(int i = 0; i<n; i++){
            t_alp = Math.max(t_alp, problems[i][0]);
            t_cop = Math.max(t_cop, problems[i][1]);
         }
        
        // dp[][] : 해당 상태에서 최솟값 저장
        // bottom up으로 하는 이유: 방향이 증가만 함 
        int[][] dp = new int[t_alp+1][t_cop+1]; 
        for(int[] row: dp){
            Arrays.fill(row, Integer.MAX_VALUE);
        }
        alp = Math.min(alp, t_alp);
        cop = Math.min(cop, t_cop);
        dp[alp][cop] = 0;
        
        for(int i = alp; i<=t_alp; i++){
            for(int j = cop; j<=t_cop; j++){
                // 현재 상태 비용
                int cost = dp[i][j];
            
                // 다음 상태를 현재 상태를 기반으로 반영
                //1. 첫번째 경로
                if(i != t_alp)
                    dp[i+1][j] = Math.min(dp[i+1][j], cost + 1);
                
                //2. 두번째 경로
                if(j != t_cop)
                    dp[i][j+1] = Math.min(dp[i][j+1], cost + 1);
                
                //3. 풀 수 있는 문제
                for(int[] p: problems){
                    if(p[0]>i || p[1]>j) continue;
                    int nextA = Math.min(t_alp, i + p[2]);
                    int nextC = Math.min(t_cop, j + p[3]);
                    dp[nextA][nextC] = Math.min(dp[nextA][nextC], cost + p[4]);
                }
            }
        }
        
        
        return dp[t_alp][t_cop];
    }
}