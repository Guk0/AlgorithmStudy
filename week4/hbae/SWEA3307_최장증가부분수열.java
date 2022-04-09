package day0404;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class SWEA3307_최장증가부분수열 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			int N = Integer.parseInt(br.readLine());
			int[] arr = new int[N];
			int[] dp = new int[N];
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < arr.length; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}
			Arrays.fill(dp, 1);
			int res = 0;
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < i; j++) {
					if(arr[i]>arr[j]) {
						dp[i] = Math.max(dp[i], dp[j] + 1);
					}
				}
				res = Math.max(res, dp[i]);
			}
			sb.append("#").append(tc).append(" ").append(res).append("\n");
		}
		bw.write(sb.toString());
		bw.flush();
		bw.close();

	}

}
