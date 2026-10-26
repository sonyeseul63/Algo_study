class Solution {
    static int answer;
    static boolean[][][] visited;
    
    public int solution(int[][] info, int n, int m) {
        answer = Integer.MAX_VALUE;
        int len = info.length;
        visited = new boolean[41][120][120];
        DFS(info, 0, 0, 0, len, n, m);
        if(answer == Integer.MAX_VALUE) answer = -1;
        return answer;
    }
    
    // 조합 생성
    public void DFS(int[][] info, int i, int a, int b, int len, int n, int m){
        // 누적값 초과인지 검증
        if(a >= n || b >=m) return;

        // 최솟값보다 많은지 검증
        if(a>=answer) return;
        
        // 끝까지 다 돌았는으면 최솟값 확인
        if(i == len){
            answer = Math.min(answer, a);
            return;
        }
        
        // 이미 이 다음 결과들을 저장해 놨는지 검증
        if(visited[i][a][b]) return;
        visited[i][a][b] = true;
        
        // 조합
        // a가 선택
        DFS(info, i+1, a+info[i][0], b, len, n, m);
        
        // b가 선택
        DFS(info, i+1, a, b+info[i][1], len, n, m);
    }
}