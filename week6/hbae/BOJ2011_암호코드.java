
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ2011_암호코드 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		for (int i = 0; i < str.length(); i++) {
			if (str.charAt(i) < '0' || str.charAt(i) > '9') {
				System.out.println("0");
				return;
			}
		}
		if (str.charAt(0) == '0') {
			System.out.println("0");
			return;
		}
		long[] dp = new long[str.length() + 1];
		dp[0] = 1;
		dp[1] = 1;

		for (int i = 2; i <= str.length(); i++) {
			char left = str.charAt(i - 2);
			char right = str.charAt(i - 1);
			if (right > '0') { // 한개 택
				dp[i] += dp[i - 1];
				dp[i] %= 1000000;
			}
			int temp = (left - '0') * 10 + (right - '0');
			if (temp >= 10 && temp <= 26) // 2개 택;
				dp[i] = (dp[i] + dp[i - 2]) % 1000000;
		}
		System.out.println(dp[str.length()]);
	}

}
