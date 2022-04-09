package day0404;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ1106_호텔 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int C = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		int[] dp = new int[C + 101];
		int INF = 987654321;
		Arrays.fill(dp, INF);
		dp[0] = 0;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int price = Integer.parseInt(st.nextToken());
			int customer = Integer.parseInt(st.nextToken());
			for (int j = customer; j < C + 101; j++) {
				dp[j] = Math.min(dp[j], dp[j - customer] + price);
			}
		}
		int res = INF;
		for (int i = C; i < C + 101; i++) {
			res = Math.min(res, dp[i]);
		}
		System.out.println(res);
	}

}
