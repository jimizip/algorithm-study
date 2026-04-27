import java.io.*;
import java.util.*;

public class Main {

	static int N;
    static int[][] board;
    static int count = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        board = new int[N + 1][N + 1];

        for (int i = 1; i <= N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dfs(1, 2, 0);

        System.out.println(count);
    }


    static void dfs(int r, int c, int dir) {
        // 목표 지점 도달 시
        if (r == N && c == N) {
            count++;
            return;
        }

        // 가로로 이동 (현재 방향이 가로(0)거나 대각선(2)인 경우만)
        if (dir == 0 || dir == 2) {
            if (c + 1 <= N && board[r][c + 1] == 0) {
                dfs(r, c + 1, 0);
            }
        }

        // 세로로 이동 (현재 방향이 세로(1)거나 대각선(2)인 경우만)
        if (dir == 1 || dir == 2) {
            if (r + 1 <= N && board[r + 1][c] == 0) {
                dfs(r + 1, c, 1);
            }
        }

        // 대각선으로 이동 (현재 모든 방향에서 가능)
        if (r + 1 <= N && c + 1 <= N) {
            // 3칸 체크
            if (board[r + 1][c + 1] == 0 && board[r][c + 1] == 0 && board[r + 1][c] == 0) {
                dfs(r + 1, c + 1, 2);
            }
        }
    }

}