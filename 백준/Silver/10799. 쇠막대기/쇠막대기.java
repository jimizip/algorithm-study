import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	    String line = in.readLine();
        Stack<Character> stack = new Stack<>();
        
        int total = 0;
        
        for (int i = 0; i < line.length(); i++) {
            if (line.charAt(i) == '(') {
                // 막대기 시작(or 레이저 시작) 찾아서 스택에 추가
                stack.push('(');
            } else {
                // ')'를 만난 경우 pop
                stack.pop(); 
                
                if (line.charAt(i - 1) == '(') {
                    // 바로 앞이 '('였다면 레이저
                    // 현재 스택에 쌓여있는 막대기 수만큼 조각 추가
                    total += stack.size();
                } else {
                    // 바로 앞도 ')'였다면 막대기의 끝
                    total += 1;
                }
            }
        }
        
        System.out.println(total);

	}

}