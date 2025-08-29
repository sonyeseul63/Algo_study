## 입출력, 자료구조, 알고리즘 템플릿화
| 전략 요소           | 이유                                              |
| --------------- | ----------------------------------------------- |
| 입출력 템플릿 미리 외워두기 | `BufferedReader`, `split`, `parseInt` 등 반복 구조   |
| 자료구조/알고리즘 템플릿화  | `PriorityQueue`, `HashMap`, `DFS/BFS` 템플릿 미리 저장 |
| 코드 압축 연습        | 한 줄에 for/if 구성하는 법, `var` 축약 사용                 |
| 실수 줄이기 → 정답률 확보 | 컴파일 오류나 NPE 줄이기 위해 테스트 케이스 검증 철저히               |


### 코드 템플릿
- 자바 메인 클래스 템플릿:
  ```java
  import java.util.*;
  public class Main {
      public static void main(String[] args) throws IOException {
          // 여기에 코드 작성
      }
  }
  ```


- `BufferedReader + StringTokenizer` 템플릿:  
  ```java
  BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  StringTokenizer st = new StringTokenizer(br.readLine());
  int a = Integer.parseInt(st.nextToken());
  ```

- `BufferedWriter` 출력 템플릿:
  ```java 
  BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
  bw.write("결과\n");
  bw.flush();
  bw.close();
  ```


### solved 계획
```
  Class 1~2 빠르게 정리 (문법 리뷰 & 손 풀기)
  Class 3~4 
  Class 5~6, 유형 공부
  Class 7 이상 + 기출 문제 
```
