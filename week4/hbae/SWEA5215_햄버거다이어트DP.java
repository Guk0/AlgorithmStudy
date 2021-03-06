package day0404;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
/*
1
5 1000
100 200
300 500
250 300
500 1000
400 400
*/
public class SWEA5215_햄버거다이어트DP {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int L = Integer.parseInt(st.nextToken());
			int[] P = new int[N+1];
			int[] W = new int[N+1];

			
			for (int i = 1; i <=N; i++) {
				st = new StringTokenizer(br.readLine());
				P[i] = Integer.parseInt(st.nextToken());
				W[i] = Integer.parseInt(st.nextToken());
			}
			int[] memo = new int[L+1];
			long[][] dp = new long[N+1][L+1];
			for (int i = 1; i <= N; i++) {
				for (int w = L; w >= W[i]; w--) {
					memo[w] = Math.max(memo[w], P[i]+memo[w-W[i]]);
				}
			}
			sb.append("#").append(tc).append(" ").append(memo[L]).append("\n");
		}
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		
	}

}
