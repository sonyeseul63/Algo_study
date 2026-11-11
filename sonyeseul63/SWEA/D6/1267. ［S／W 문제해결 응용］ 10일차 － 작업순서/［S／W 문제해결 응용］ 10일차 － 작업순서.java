
import java.io.*;
import java.util.*;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for(int testcase = 1; testcase <= 10; testcase++) {
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int v = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());

			// 인접리스트
			List<Integer>[] graph = new ArrayList[v+1];
			for(int i=1; i<=v;i++) {
				graph[i] = new ArrayList<>();
			}
			int[] indegrees = new int[v+1];
			
			st = new StringTokenizer(br.readLine());
			for(int i = 0; i< e; i++) {
				int from = Integer.parseInt(st.nextToken());
				int to = Integer.parseInt(st.nextToken());
				
				graph[from].add(to);
				indegrees[to]++;
			}
			
			Queue<Integer> q = new ArrayDeque<>();
			
			// 초기 : 진입차수 0인 것 넣기
			for(int i = 1; i <=v; i++) {
				if(indegrees[i] == 0) q.offer(i);
			}
			
			List<Integer> answer = new ArrayList<>();
			
			// 차수 0이여서 들어온 q 처리(다음 방문할 것을 고른다)
			while(!q.isEmpty()) {
				int now = q.poll();
				
				answer.add(now);
				
				// 현재 정점에서 다음 정점들 
				for(int next: graph[now]) {
					indegrees[next]--;
					
					if(indegrees[next]==0)
						q.offer(next);
				}
			}
			
			System.out.print("#" + testcase + " ");
			for(int ans:answer) {
				System.out.print(ans + " ");
			}
			System.out.println();
		}
	}
}
