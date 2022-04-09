package day0408;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ9465_스티커 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for (int tc = 0; tc < T; tc++) {
			int n = Integer.parseInt(br.readLine());
			int[][] arr = new int[2][n + 1];
			int[][] dp = new int[2][n + 1];
			for (int i = 0; i < arr.length; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 1; j < arr[i].length; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			dp[0][1] = arr[0][1];
			dp[1][1] = arr[1][1];
			for (int j = 2; j <= n; j++) {
				dp[0][j] = Math.max(dp[1][j - 1], dp[1][j - 2]) + arr[0][j];
				dp[1][j] = Math.max(dp[0][j - 1], dp[0][j - 2]) + arr[1][j];
			}
			int res = Math.max(dp[0][n], dp[1][n]);
			System.out.println(res);
		}
	}

}
