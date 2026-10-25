class Solution {
    public int solution(int[][] board, int[][] skill) {
        int answer = 0;
        int row = board.length;
        int col = board[0].length;
        int[][] diff = new int[row+1][col+1];
        
        // skill대로 경계값 넣기
        for(int[] s:skill){
            int type = s[0]; // s=1:-, s=2:+
            int r1 = s[1];
            int c1 = s[2];
            int r2 = s[3];
            int c2 = s[4];
            int degree = s[5];
            diff[r1][c1] += degree * ((type == 1)? -1 : 1);
            diff[r1][c2+1] += degree * ((type == 1)? 1 : -1); // 반대
            diff[r2+1][c1] += degree * ((type == 1)? 1 : -1); // 반대
            diff[r2+1][c2+1] += degree * ((type == 1)? -1 : 1);
        }
        
        // 누적합 갱신
        for(int r = 0; r < row; r++){
            for(int c = 1; c < col; c++){
                diff[r][c] += diff[r][c-1];
            }
        }
        
        for(int c = 0; c < col; c++){
            for(int r = 1; r < row; r++){
                diff[r][c] += diff[r-1][c];
            }
        }
        
        // board와 diff를 합침
        for(int r=0; r<row; r++){
            for(int c=0; c<col; c++){
                board[r][c] += diff[r][c];
                if(board[r][c] > 0) answer++;
            }
        }
        
        return answer;
    }
}