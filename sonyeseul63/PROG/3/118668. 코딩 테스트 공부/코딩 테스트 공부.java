import java.util.*;
class Solution {
    
    public int solution(int alp, int cop, int[][] problems) {
        int answer = 0;
        int n = problems.length;
        t_alp = 0;
        t_cop = 0;
        for(int i = 0; i<n;i++){
            t_alp = Math.max(t_alp, problems[i][0]);
            t_cop = Math.max(t_cop, problems[i][1]);
        }
        
        alp = Math.min(alp, t_alp);
        cop = Math.min(cop, t_cop);
        memo = new int[t_alp+1][t_cop+1];
        for(int[] row : memo){
            Arrays.fill(row, -1);
        }
        
        return dfs(alp, cop, problems);
    }
    
    static int[][] memo; // 현재 ~ 목표까지의 최소 거리
    static int t_alp;
    static int t_cop;
    // 현재 ~ 목표까지의 비용 구해, 최소 거리,, 갖고 다니면서
    public int dfs(int alp, int cop, int[][] problems){
        // 리턴 조건-> 마지막
        if(alp == t_alp && cop == t_cop) return 0;
        
        // 현재상태에 이미 메모값있으면 그거써
        if(memo[alp][cop] != -1)
            return memo[alp][cop];
        
        // 현재 상태부터 끝까지의 최소를 구해
        int min = Integer.MAX_VALUE;
        
        // 1.
        if(alp != t_alp)
             min = Math.min(min, dfs(alp+1, cop, problems)+1);
        
        // 2.
        if(cop != t_cop)
            min = Math.min(min, dfs(alp, cop+1, problems)+1);
        
        // 3.
        for(int[] p: problems){
            // 풀 수 있는 것만
            if(p[0] > alp || p[1]>cop) continue;
            
            int nextA = Math.min(t_alp, alp+p[2]);
            int nextC = Math.min(t_cop, cop+p[3]);
            
            if(nextA == alp && nextC == cop) continue;
            min = Math.min(min, dfs(nextA, nextC, problems) + p[4]);
        }
        
        memo[alp][cop] = min;
        return memo[alp][cop];
    }
}