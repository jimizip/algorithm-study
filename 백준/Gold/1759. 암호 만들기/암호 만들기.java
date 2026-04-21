import java.util.*;
import java.io.*;

public class Main {
    static int L, C;
    static char[] input;   
    static char[] password;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        input = new char[C];
        password = new char[L];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < C; i++) {
            input[i] = st.nextToken().charAt(0);
        }

        // 사전순으로 정렬
        Arrays.sort(input);

        generatePassword(0, 0);
    }

    static void generatePassword(int depth, int start) {
        if (depth == L) {
            // 조건 검사 (모음 1개, 자음 2개 이상)
            if (isValid()) {
                System.out.println(new String(password));
            }
            return;
        }

        for (int i = start; i < C; i++) {
            password[depth] = input[i];
            generatePassword(depth + 1, i + 1);
        }
    }

    static boolean isValid() {
        int vowelCount = 0; 
        int consonantCount = 0;

        for (char c : password) {
            if (isVowel(c)) vowelCount++;
            else consonantCount++;
        }

        return vowelCount >= 1 && consonantCount >= 2;
    }

    static boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}