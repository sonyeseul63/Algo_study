import java.util.Arrays;
class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        // people 오름차순 정렬
        Arrays.sort(people);
        
        // pointer a, b
        int a = 0; // 작은 값
        int b = people.length - 1; // 큰 값
        while(a <= b){
            if(people[a] + people[b] <= limit){
                a++;
            }
            b--;
            answer++;
        }

        return answer;
    }
}
\;
