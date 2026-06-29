import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int idx = 0;
        int[] temp = new int[progresses.length];
        
        Deque<Integer> q = new ArrayDeque<>();
        
        for (int i = 0; i < progresses.length; i++) {
            // progressses의 각 작업이 완료까지의 걸리는 기간
            int day = calcDays(progresses[i], speeds[i]);
            // 큐에 넣기
            q.offer(day);
        }
        
        while (!q.isEmpty()){
            int num = 1;
            int curfirst = q.poll();
            while (!q.isEmpty() && curfirst >= q.peek()){
                q.poll();
                num++;
            }
            temp[idx++] = num;
        }
        
        int[] answer = new int[idx];
        for(int i = 0; i<idx; i++){
            answer[i] = temp[i];
        }
        
        return answer;
    }
    
    // 입력: 작업의 progress, speeds
    // 출력: 완료까지 걸리는 날짜
    private int calcDays(int p, int speed){
        int day = (100 - p) / speed;
        if( (100-p) % speed > 0) day++;
        return day;
    }
    
}