package day0408;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ2166_다각형의면적 {

	public static class pot {
		long x;
		long y;

		public pot(long x, long y) {
			super();
			this.x = x;
			this.y = y;
		}
	}

	static int N;
	static pot[] pots;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		pots = new pot[N + 1];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			long x = Long.parseLong(st.nextToken());
			long y = Long.parseLong(st.nextToken());
			pots[i] = new pot(x, y);
		}
		pots[N] = pots[0];
		long res = sinbal();
		String ans = String.format("%.1f", (double) res / 2.0);
		System.out.println(ans);
	}

	public static long sinbal() {
		long multi1 = 0;
		long multi2 = 0;
		for (int i = 0; i < N; i++) {
			multi1 += pots[i].x * pots[i+1].y;
			multi2 += pots[i].y * pots[i+1].x;
		}
		long res = Math.abs(multi2 - multi1);
		return res;
	}

}
