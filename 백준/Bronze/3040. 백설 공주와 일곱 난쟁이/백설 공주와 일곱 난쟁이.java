import java.util.Scanner;
import java.util.Arrays;

public class Main {

	static int n = 9;          
    static int r = 7;           
    static int[] input = new int[n];   
    static int[] numbers = new int[r];
    static boolean found = false;      

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        for (int i = 0; i < n; i++) {
            input[i] = sc.nextInt();
        }

        Arrays.sort(input);

        combi(0, 0, 0);
    }

    public static void combi(int depth, int start, int currentSum) {

        if (found) return;

        if (depth == r) {
            if (currentSum == 100) {
                for (int val : numbers) {
                    System.out.println(val);
                }
                found = true;
            }
            return;
        }

        for (int i = start; i < n; i++) {
            numbers[depth] = input[i]; // 현재 자리에 난쟁이 배치

            combi(depth + 1, i + 1, currentSum + input[i]);
        }
    }
}