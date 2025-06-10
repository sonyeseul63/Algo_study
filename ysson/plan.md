# 여기에 계획같은거를 적어보죠 문제풀이과정이나 로직 설명도 좋겠네요!
## Markdown Preview Enhanced 확장 설치 후
## Ctrl + Shift + V 누르면 미리보기

# 입출력, 자료구조, 알고리즘 템플릿화
| 전략 요소           | 이유                                              |
| --------------- | ----------------------------------------------- |
| 입출력 템플릿 미리 외워두기 | `BufferedReader`, `split`, `parseInt` 등 반복 구조   |
| 자료구조/알고리즘 템플릿화  | `PriorityQueue`, `HashMap`, `DFS/BFS` 템플릿 미리 저장 |
| 코드 압축 연습        | 한 줄에 for/if 구성하는 법, `var` 축약 사용                 |
| 실수 줄이기 → 정답률 확보 | 컴파일 오류나 NPE 줄이기 위해 테스트 케이스 검증 철저히               |


# ✅ 백준 코딩테스트 1차 계획 (7일간 30문제)
**목표:** 문자열 함수 & 입출력 최적화 + 구현 사고력  
**입출력 연습:** BufferedReader, BufferedWriter 사용 습관화  
**문자열 함수:** charAt, substring, split, indexOf, toCharArray 등 익히기  
**기간:** 2025-06-09 ~ 2025-06-15

---

## 📆 Day 1 - 문자열 & 입출력 기초 (2025-06-09)
- [11654] 아스키 코드 (`char` ↔ `int`)
- [11720] 숫자의 합 (`charAt`, `Character.getNumericValue`)
- [10809] 알파벳 찾기 (`indexOf`, 배열 초기화)
- [2675] 문자열 반복 (`repeat`, `StringBuilder`)
- [2743] 단어 길이 재기 (`length()`)

📝 목표: `BufferedReader`, `readLine()`, `charAt()` 완전 숙지

---

## 📆 Day 2 - 문자열 함수 & 조건 분기 (2025-06-10)
- [2908] 상수 (`StringBuilder.reverse()`)
- [1157] 단어 공부 (`대소문자`, 배열 index 활용)
- [27866] 문자와 문자열 (`charAt()`)
- [1316] 그룹 단어 체커 (`boolean 배열`, `이전 문자 기록`)
- [2941] 크로아티아 알파벳 (`replace()`, 패턴 인식)

📝 목표: 다양한 `String` 처리 연습 (replace, toCharArray 등)

---

## 📆 Day 3 - 브루트포스 입문 (2025-06-11)
- [2798] 블랙잭 (3중 반복문)
- [2231] 분해합 (자릿수 분해)
- [1018] 체스판 다시 칠하기 (부분 탐색)
- [19532] 수학은 비대면강의입니다 (완전탐색)
- [1436] 영화감독 숌 (`while`과 `String.contains()`)

📝 목표: 브루트포스 사고방식에 익숙해지기

---

## 📆 Day 4 - 구현 + 정렬 기초 (2025-06-12)
- [2750] 수 정렬하기 (기본 `Arrays.sort`)
- [1427] 소트인사이드 (`char 배열 정렬`)
- [1181] 단어 정렬 (`Comparator` 익히기)
- [11650] 좌표 정렬하기 (2차원 정렬)
- [14681] 사분면 고르기 (조건 분기)

📝 목표: `Comparator`, 2차원 배열 정렬 체험

---

## 📆 Day 5 - 시뮬레이션 + 예외 처리 (2025-06-13)
- [2739] 구구단 (기본 반복문)
- [2501] 약수 구하기
- [10951] A+B - 4 (`while ((line = br.readLine()) != null)`)
- [10952] A+B - 5 (`while`, 종료 조건)
- [7567] 그릇 (연속적 조건 처리)

📝 목표: 종료 조건, 예외 흐름 처리 연습

---

## 📆 Day 6 - 오답 복습 + 입출력/문자열 함수 총정리 (2025-06-14)
**오답 복습:** Day 1~5 중 틀렸거나 오래 걸렸던 문제 2~3문제  
**추가 연습 문제:**
- [StringTokenizer] 사용 → [10953] A+B - 6
- [BufferedWriter] 출력 연습 → [2439] 별 찍기 - 2
- [StringBuilder] 반복 출력 → [8393] 합
- [replaceAll vs replace] → [27866] 문자와 문자열

📝 목표: Java 입출력 템플릿 및 문자열 도구 정리

---

## 📆 Day 7 - 실버 진입 실력 테스트 (2025-06-15)
- [1978] 소수 판별 (`isPrime`)
- [1920] 수 찾기 (이진 탐색 기초)
- [10816] 숫자 카드 2 (카운트 배열 or `Map`)
- [11653] 소인수분해
- [9020] 골드바흐의 추측 (소수 + 조합)

📝 목표: 실버 중위권 이상 문제 패턴 파악

---

- `BufferedReader + StringTokenizer` 템플릿:  
  ```java
  BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  StringTokenizer st = new StringTokenizer(br.readLine());
  int a = Integer.parseInt(st.nextToken());

- `BufferedWriter` 출력 템플릿:
```java 
BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
bw.write("결과\n");
bw.flush();
bw.close();
