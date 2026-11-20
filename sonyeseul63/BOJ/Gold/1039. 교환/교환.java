import java.io.*;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String str = st.nextToken();
        int k = Integer.parseInt(st.nextToken());
        int len = str.length();

        // 큐
        Queue<String> q = new ArrayDeque<>();
        q.offer(str);

        // k 번 bfs를 돌린다?
        for(int i =0; i<k;i++){

            int size = q.size();
            // 상태 중복 방지
            boolean[] visited = new boolean[1_000_001];
            for(int j=0; j<size;j++){
                // q가 비었으면 탐색 빠르게 종료
                if(q.isEmpty()) break;
    

                // 현재 기준 가능한 모든 상태
                String cur = q.poll();
                int curInt = Integer.parseInt(cur);


                for(int r = 0; r<len-1; r++){
                    for(int z = r+1; z<len; z++){
                        char[] arr = cur.toCharArray();
                        char temp = arr[r];
                        arr[r] = arr[z];
                        arr[z] = temp;

                        String next = new String(arr);
                        int nextInt = Integer.parseInt(next);
                        
                        if(visited[nextInt] || arr[0] == '0') continue;

                        visited[nextInt] = true;
                        q.offer(next);
                    }
                }
            }
        }

        int answer = -1;
        while(!q.isEmpty()){
            answer = Integer.max(answer, Integer.parseInt(q.poll()));
        }

        System.out.println(answer);
    }
}
