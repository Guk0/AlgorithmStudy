package day0411;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class SWEA5607_조합 {

	private static final int mod = 1234567891;
	static int N, R;
	static long[] factorial;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		factorial = new long[1000001];
		factorial[0] = 1;
		for (int i = 1; i < factorial.length; i++) {
			factorial[i] = factorial[i - 1] * i % mod;
		}
		int T = Integer.parseInt(br.readLine());
		for (int tc = 0; tc < T; tc++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			R = Integer.parseInt(st.nextToken());
			long res = 0;
			long x = factorial[N];
			long y = (factorial[N - R] * factorial[R]) % mod;
			y = solve(y, mod - 2);
			res = x * y % mod;
			sb.append("#").append(tc + 1).append(" ").append(res).append("\n");
		}
		bw.write(sb.toString());
		bw.flush();
		bw.close();
	}

	public static long solve(long x, long y) {
		if (y == 0) // 지수가 0이면 1이니까
			return 1;
		if (y == 1) // 지수가 1이면 그 숫자 그대로
			return x;
		if (y % 2 == 0) { // 지수가 짝수면 x^10 = (X^5)^2 니까
			long temp = solve(x, y / 2);
			return temp * temp % mod;
		} else { // 지수가 홀수면 x^9 = x*x^8 = x*(x^4)^2
			long temp = solve(x, y - 1) % mod;
			return temp * x % mod;
		}
	}

}
