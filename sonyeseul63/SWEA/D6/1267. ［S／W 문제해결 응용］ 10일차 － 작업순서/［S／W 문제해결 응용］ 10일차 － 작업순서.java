
import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for(int testcase = 1; testcase <=10; testcase++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken()); // 정점이 1  ~ v까지 있음
            int e = Integer.parseInt(st.nextToken()); // for로 e번 (2개씩 추출)

            int[] degrees = new int[v+1];
            List<Integer>[] list = new ArrayList[v+1];
            for(int i = 1; i<=v; i++){
                list[i] = new ArrayList<>();
            }

            st = new StringTokenizer(br.readLine());
            for(int i =0; i <e; i++){
                int f = Integer.parseInt(st.nextToken());
                int s = Integer.parseInt(st.nextToken());
                list[f].add(s);
                degrees[s] +=1;
            }

            Queue<Integer> q = new ArrayDeque<>();
            for(int i =1 ;i<= v; i++){
                
                if(degrees[i] == 0) q.offer(i);
            }

            System.out.print("#" + testcase + " ");
            while(!q.isEmpty()){
                int cur = q.poll();
                int len = list[cur].size();


                System.out.print(cur +" ");

                
                for(int i =0 ;i<len;i++){
                    int next = list[cur].get(i);
                    degrees[next]--;
                    if(degrees[next] == 0) q.offer(next);
                }
            }
            System.out.println("");
        }
    }
}
// 고민한 부분 : 큐에는 정점 번호만 담아도 되는지? -> 각 차수는 배열로 관리하니까 
// 다음 노드 탐색을 위해 연결성을 담은 자료구조가 필요 -> 연결리스트