
import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int testcase = 1; testcase<=T; testcase++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String str = st.nextToken();
            int n = Integer.parseInt(st.nextToken());
            int len = str.length();
            int n_size = 1;
            for(int i =0; i<len; i++){
                n_size *= 10;
            }

            Queue<String> q = new ArrayDeque<>();
            q.offer(str);
            // 턴 수 관리
            for(int i =0; i<n;i++){
                int count = q.size();
                boolean[] visited = new boolean[n_size];

                for(int j= 0; j<count; j++){
                    String cur = q.poll();

                    // 다음 가능한 수 모집 
                    for(int r = 0; r<len-1;r++){
                        for(int z =r+1; z<len; z++){
                            char[] cur_char = cur.toCharArray();
                            char temp = cur_char[r];
                            cur_char[r] = cur_char[z];
                            cur_char[z] = temp;

                            String next = new String(cur_char);
                            int next_int = Integer.parseInt(next);
                            if(!visited[next_int]) q.offer(next);
                            visited[next_int] = true;
                        }
                    }
                }
            }

            // 담긴 큐에서 최대값
            int count = q.size();
            int answer =0;
            for(int i = 0; i<count; i++){
                int num = Integer.parseInt(q.poll());
                answer = Math.max(answer, num);
            }

            System.out.println("#"+ testcase+ " " + answer);

        }

    }
}

// 각 턴에서 바꿀 수 있는 숫자 -> 중복 제거 가능
// string -> char[] -> string, string -> int
// 몇 단계 턴인지 알려면?