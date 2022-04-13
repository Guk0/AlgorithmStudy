package day0411;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class SWEA3238_이항계수구하기 {

	static long N, R, P;
	static long[] factorial;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for (int tc = 0; tc < T; tc++) {
			st = new StringTokenizer(br.readLine());
			N = Long.parseLong(st.nextToken());
			R = Long.parseLong(st.nextToken());
			P = Integer.parseInt(st.nextToken());
			factorial = new long[(int) P];
			factorial[0] = 1;
			for (int i = 1; i < factorial.length; i++) {
				factorial[i] = (factorial[i - 1] * i) % P;
			}

			long res = 1;
			while (N != 0 || R != 0) {
				long x = N % P;
				long y = R % P;
				if (x < y)
					res = 0;
				if (res == 0)
					break;
				res = (res * factorial[(int) x]) % P;
				res = (res * solve((factorial[(int) y] * factorial[(int) (x - y)]) % P, P - 2, P)) % P;
				N /= P;
				R /= P;
			}
			sb.append("#").append(tc + 1).append(" ").append(res).append("\n");
		}
		bw.write(sb.toString());
		bw.flush();
		bw.close();
	}

	public static long solve(long x, long y, long P) {
		if (y == 0) // 지수가 0이면 1이니까
			return 1;
		if (y == 1) // 지수가 1이면 그 숫자 그대로
			return x;
		if (y % 2 == 0) { // 지수가 짝수면 x^10 = (X^5)^2 니까
			long temp = solve(x, y / 2, P);
			return temp * temp % P;
		} else { // 지수가 홀수면 x^9 = x*x^8 = x*(x^4)^2
			long temp = solve(x, y - 1, P) % P;
			return temp * x % P;
		}
	}

}
