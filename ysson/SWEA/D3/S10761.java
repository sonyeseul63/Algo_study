package ysson.SWEA.D3;
import java.io.*;
import java.util.*;

class S10761 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int testcase = 1; testcase <= T; testcase++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int sum = 0;
            int[] t  = {0, 0};
            int[] pos = {1, 1};
            for(int i = 0; i < n; i++){
                char robot_c = st.nextToken().charAt(0);
                int robot = (robot_c == 'B') ? 0 : 1;
                int target = Integer.parseInt(st.nextToken());

                // target 까지 거리
                int distance = Math.abs(pos[robot] - target);
                

                // 거리만큼 시간 추가
                // 여분 시간(다른 로봇이 움직인 시간) 있으면 반영
                if(t[robot] < sum ){
                    // 여분시간 초과면 추가
                    if(distance > sum-t[robot])
                        sum += Math.abs((sum - t[robot]) - distance);
                }
                if(t[robot] == sum ){
                    sum += distance;
                }

                // 버튼 누른 시간 더하기
                sum++;
                
                // 최종 시각과 위치 반영
                t[robot] = sum;
                pos[robot] = target;

            }
            System.out.println("#" + testcase + " " + sum);
        }
    }
}

// A가 쓴 시간 -> t
// 전체 테스트 누적 시간 -> sum
// a, b의 현재위치 -> int[] pos (char->int 매핑때문에 변수로 안두고 배열로 관리)
// a, b의 타겟 위치까지 이동-> pos 업데이트
// 한 테스트의 위치 도달까지 거리와 t 비교,, -> t 업데이트 -> 스위치 누른 1초까지 더해서 sum에 누적
