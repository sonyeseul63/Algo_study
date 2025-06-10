import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String line = br.readLine();
        line = line.trim();

        if(line == null || line.isEmpty()){
            bw.write("0\n");
        } else {
            String[] words = line.split("\\s+");
            bw.write(words.length + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}


// 예외적인 상황: 입력값이 공백일때 split()의 불확실한 동작
// 확실하게 공백일 때 단어 0개로 처리해줘야함
// isEmpty -> 아무것도 안쓰거나 공백일때 true, null일땐? 따로 처리해야함

// bw.write을 쓸 때 마지막에 줄바꿈 처리

