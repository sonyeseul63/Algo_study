import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt(); // 테스트 케이스 수
        sc.nextLine(); // 개행 문자 처리

        for (int i = 0; i < t; i++) {
            String s = sc.nextLine();
            int score = 0;
            int streak = 0;

            for (int j = 0; j < s.length(); j++) {
                if (s.charAt(j) == 'O') {
                    streak++;
                    score += streak;
                } else {
                    streak = 0;
                }
            }

            System.out.println(score);
        }
    }
}
