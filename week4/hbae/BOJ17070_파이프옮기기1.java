package day0410;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ17070_파이프옮기기1 {
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());
		int[][] arr = new int[N+1][N+1];
		int[][][] dp = new int[N+1][N+1][3];
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= N; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		dp[1][2][0]=1;
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if(arr[i][j]==1)
					continue;
				// 이전칸이 가로거나 대각선일때, 가로로 파이프 놓을 수 있음
				dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2];
				// 이전칸이 세로거나 대각선일때, 세로로 파이프 놓을 수 있음
				dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2];
				// 대각선은 이전이 가로세로 상관없는데 그 주변이 다 0이어야 함.
				if(arr[i-1][j]!=1 && arr[i][j-1] !=1)
					dp[i][j][2] += dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2];
			}
		}
		int res = dp[N][N][0] + dp[N][N][1] + dp[N][N][2];
		System.out.println(res);
	}

}
