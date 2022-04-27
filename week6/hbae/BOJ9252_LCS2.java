
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ9252_LCS2 {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		char[] arr = br.readLine().toCharArray();
		char[] arr2 = br.readLine().toCharArray();

		int N = arr.length;
		int M = arr2.length;
		int[][] dp = new int[N + 1][M + 1];
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= M; j++) {
				if (arr[i - 1] == arr2[j - 1]) {
					dp[i][j] = dp[i - 1][j - 1] + 1;
				} else {
					dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
				}
			}
		}
		int i = dp.length - 1;
		int j = dp[0].length - 1;
		while (i != 0 && j != 0) {
			if (dp[i][j] == dp[i - 1][j]) {
				i--;
			} else if (dp[i][j] == dp[i][j - 1]) {
				j--;
			} else {
				sb.append(arr[i - 1]);
				i--;
				j--;
			}
		}
		System.out.println(dp[N][M]);
		System.out.println(sb.reverse().toString());
	}

}
