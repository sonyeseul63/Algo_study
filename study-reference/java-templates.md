
### 입력 템플릿 (BufferedReader + StringTokenizer)

```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
StringTokenizer st = new StringTokenizer(br.readLine());
int a = Integer.parseInt(st.nextToken());
int b = Integer.parseInt(st.nextToken());

// 다음 토큰이 남아 있는지 확인
while (st.hasMoreTokens()) {
    string token = st.nextToken();
    System.out.println("토큰: ", token);
}
```

### 출력 템플릿 (BufferedWriter)
```java
BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
bw.write("결과\n");
bw.flush();
bw.close();
```

### N줄 반복 입력 받기
```java
int N = Integer.parseInt(br.readLine());
for (int i = 0; i < N; i++){

}
```

### 문자열 숫자로 변환
```java
int num = Integer.parseInt("123");
```

### 문자열 한 글자씩 접근
```java
String s = "hello";
char c = s.charAt(0);
```

### 배열 선언/정렬
```java
int[] arr = new int[5];  숫자타입 5개 들어가는 배열
Arrays.sort(arr);
```

### 한 줄 공백 기준 숫자 입력(배열로)
```java
int[] arr = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt) //각 요소를 int로 바꾸고
                .toArray(); //int[]로 전환
```

### 문자열을 문자 하나하나로 쪼갬
```java
char[] chars = br.readLine().toCharArray();
```

### 아스키 코드 관련
```java
char c = 'A';
int code = (int) c; // 65
char fromCoe = (char) 97; //'a'
```

### 어떤 것의 알파벳 개수 세기
```java
String s = "apple";
int[] alpha = new int[26];

for(int i = 0; i < s.length(); i++){
    char c= s.charAt(i); //문자열 한 글자씩 접근
    alpha[c- 'a']++; //a->0 ~ Z->25 알바펫 별로 하나의 상자에 부여해서 담기!
}
```