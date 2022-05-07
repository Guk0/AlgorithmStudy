package day0505;

import java.util.Arrays;
import java.util.Scanner;

public class BOJ10844_쉬운계단수 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long[][] dp = new long[N + 1][10];
		Arrays.fill(dp[1], 1);
		dp[1][0] = 0;
		for (int i = 2; i <= N; i++) {
			for (int j = 0; j < dp[i].length; j++) {
				if (j == 0)
					dp[i][j] = dp[i - 1][j + 1];
				else if (j == 9)
					dp[i][j] = dp[i - 1][j - 1];
				else
					dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1];
				dp[i][j] %= 1000000000;
			}
		}
		long res = 0;
		for (int j = 0; j < 10; j++) {
			res += dp[N][j];
			res %= 1000000000;
		}
		System.out.println(res);
		sc.close();
	}

}
