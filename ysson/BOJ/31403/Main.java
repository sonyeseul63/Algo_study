import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt(); // 첫 번째 정수 입력
        int b = sc.nextInt(); // 두 번째 정수 입력
        String s = sc.next(); // 문자열로 입력

        System.out.println(a + b); // 정수 덧셈
        System.out.println(s + b); // 문자열 + 정수 (문자열 연결)
        System.out.println(a + s); // 정수 + 문자열 (문자열 연결)
    }
}
