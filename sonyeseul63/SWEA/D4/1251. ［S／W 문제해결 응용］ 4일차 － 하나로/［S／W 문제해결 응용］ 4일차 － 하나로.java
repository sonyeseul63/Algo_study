
import java.io.*;
import java.util.*;

public class Solution {
    static int[] r, c, parent;
    static ArrayList<Edge> list;
    private static class Edge{
        int from;
        int to;
        long dist;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int testcase = 1; testcase <=T; testcase++){
            int n = Integer.parseInt(br.readLine());
            r= new int[n+1];
            c = new int[n+1];
            
            StringTokenizer st1 = new StringTokenizer(br.readLine());
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            for(int i = 1; i<=n; i++){
                r[i] = Integer.parseInt(st1.nextToken());
                c[i] = Integer.parseInt(st2.nextToken());
            }

            double e = Double.parseDouble(br.readLine());

            // 간선 구하기
            list= new ArrayList<>();
            for(int i = 1; i< n; i++){
                for(int j = i+1;j<=n; j++){
                    Edge edge= new Edge();
                    edge.from = i;
                    edge.to = j;
                    edge.dist = (long)(r[i] - r[j]) * (r[i] - r[j]) + (long)(c[i] - c[j]) * (c[i] - c[j]);

                    list.add(edge);
                }
            }

            // 간선 정렬
            list.sort(
                (a,b) -> Long.compare(a.dist, b.dist)
            );

            // 정점 자기 가르키도록
            parent = new int[n+1];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }

            // 간선 작은것부터 선택해서 연결 + 유니온 파인드하기
            int cnt = 0;
            double total = 0;
            for(Edge edge: list){
                if(cnt == n-1) break;

                int rootA = find(edge.from);
                int rootB = find(edge.to);

                if(rootA != rootB) {
                    parent[rootB] = rootA; // b가 a에 속하도록
                    cnt++;
                    total += (edge.dist * e);
                }

            }

            System.out.println("#" + testcase + " " + Math.round(total));
        }
    }

    private static int find(int x){
        if(parent[x] == x) return parent[x];
        return parent[x] = find(parent[x]);
    }
}
// 거리 비교 -> L 가지고 가능
// 연결할때 환경부담금 계산