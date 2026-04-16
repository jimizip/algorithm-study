import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque; 
import java.util.Deque;    
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        // ArrayDeque 사용
        Deque<Integer> deque = new ArrayDeque<>();

        for (int i = 1; i <= N; i++) {
            deque.addLast(i); // 뒤에 추가 (add와 동일)
        }

        StringBuilder sb = new StringBuilder();
        sb.append("<");

        while (!deque.isEmpty()) {
            // K-1번만큼 앞에서 빼서 뒤로 넣기
            for (int i = 0; i < K - 1; i++) {
                deque.addLast(deque.pollFirst());
            }
            
            sb.append(deque.pollFirst());

            if (!deque.isEmpty()) {
                sb.append(", ");
            }
        }

        sb.append(">");
        System.out.println(sb.toString());
    }
}