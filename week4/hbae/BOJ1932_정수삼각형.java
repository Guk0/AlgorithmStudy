package day0407;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ1932_정수삼각형 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());
		int[][] arr = new int[N + 1][N + 1];
		int[][] dp = new int[N + 1][N + 1];
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= i; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		dp[1][1] = arr[1][1];
		for (int i = 1; i < N; i++) {
			for (int j = 1; j <= i; j++) {
				dp[i+1][j] = Math.max(dp[i+1][j], dp[i][j]);
				dp[i+1][j+1] = Math.max(dp[i+1][j+1], dp[i][j]);
			}
			for (int j = 1; j <= i+1; j++) {
				dp[i+1][j] += arr[i+1][j];
			}
		}
		int res = 0;
		for (int i = 1; i <= N; i++) {
			res = Math.max(res, dp[N][i]);
		}
		System.out.println(res);
	}

}
