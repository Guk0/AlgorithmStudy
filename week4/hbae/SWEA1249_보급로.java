package day0407;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class SWEA1249_보급로 {

	static int[][] arr, dp;
	static boolean[][] isVisited;
	static int res, N;
	static int[] dx = { -1, 0, 1, 0 };
	static int[] dy = { 0, 1, 0, -1 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int tc = 0; tc < T; tc++) {
			N = Integer.parseInt(br.readLine());
			arr = new int[N][N];
			dp = new int[N][N];
			isVisited = new boolean[N][N];
			for (int i = 0; i < N; i++) {
				String[] str = br.readLine().split("");
				Arrays.fill(dp[i], Integer.MAX_VALUE);
				for (int j = 0; j < N; j++) {
					arr[i][j] = Integer.parseInt(str[j]);
				}
			}
			isVisited[0][0] = true;
			dp[0][0] = 0;
			res = Integer.MAX_VALUE;
			solve();
			sb.append("#").append(tc + 1).append(" ").append(res).append("\n");
		}
		sb.setLength(sb.length() - 1);
		bw.write(sb.toString());
		bw.flush();
		bw.close();

	}

	public static void solve() {
		Queue<int[]> queue = new LinkedList<int[]>();
		queue.add(new int[] { 0, 0 });
		while (!queue.isEmpty()) {
			int[] temp = queue.poll();
			int x = temp[0];
			int y = temp[1];
			if (x == N - 1 && y == N - 1) {
				res = Math.min(res, dp[x][y]);
				continue;
			}
			if (res <= dp[x][y])
				continue;
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx < 0 || ny < 0 || nx >= N || ny >= N)
					continue;
				if (isVisited[nx][ny]==false || dp[nx][ny] > dp[x][y] + arr[nx][ny]) {
					isVisited[nx][ny] = true;
					dp[nx][ny] = dp[x][y] + arr[nx][ny];
					queue.add(new int[] { nx, ny });
				}
			}
		}
	}
	
}
