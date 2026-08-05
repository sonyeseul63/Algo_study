import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.List;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());
        for(int T = 1; T<=testCase; T++){
            String result = "None";
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            char[] arr = (br.readLine()).toCharArray();
            List<String> list = new ArrayList<String>(); 
            for(int i = 0; i<=N-M; i++){
                int left = i;
                int right = left + (M-1);
                if(arr[left] == arr[right]){
                    boolean isCircle = true;
                    while(left<=right){
                        if(arr[left] != arr[right]){
                            isCircle = false;
                            break;
                        }
                        left++;
                        right--;
                    }
                    // if(isCircle){
                    //     list.add(new String(arr, i, M));
                    // }
                    if(isCircle) {
                        result = new String(arr, i, M);
                        break;
                    }
                }
            }
             System.out.println("#" + T + " " + result);
        }
    }
}

// 양 끝 비교를 포인터 통해서 하고 통과하면 그때부터 하나씩 줄어가며 비교
// 또는 문자열을 아에 슬라이싱? 쪼개서 거꾸로랑 비교하는 게 괜찮을지
// 자바 문법 -> 배열을 string 만들기 
// new String(arr, 시작인덱스, 개수)