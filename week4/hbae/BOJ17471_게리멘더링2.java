package day0406;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ17471_게리멘더링2 {
	static int N, res;
	static int[] arr, area;
	static int[][] adjmatrix;
	static boolean[] isSelected;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		arr = new int[N + 1];
		for (int i = 1; i <= N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		adjmatrix = new int[N + 1][N + 1];
		area = new int[N + 1];
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			int tc = Integer.parseInt(st.nextToken());
			for (int j = 1; j <= tc; j++) {
				int next = Integer.parseInt(st.nextToken());
				adjmatrix[i][next] = 1;
				adjmatrix[next][i] = 1;
			}
		}
		res = Integer.MAX_VALUE;
		dfs(1);
		if (res == Integer.MAX_VALUE)
			System.out.println("-1");
		else
			System.out.println(res);

	}

	public static void dfs(int depth) {
		if (depth == N + 1) {
			int area1 = 0;
			int area2 = 0;
			for (int i = 1; i <= N; i++) {
				if (area[i] == 1)
					area1 += arr[i];
				else
					area2 += arr[i];
			}
			isSelected = new boolean[N + 1];
			int areacount = 0;
			for (int i = 1; i <= N; i++) {
				if (!isSelected[i]) {
					checkArea(i, area[i]);
					areacount++;
				}
			}
			// 선거구가 2개가 아닐때를 잘 못 체크해줌(더 많아지면 분리되는거니까..
			if (areacount == 2) {
				res = Math.min(res, Math.abs(area1 - area2));
			}
			return;
		}
		area[depth] = 1;
		dfs(depth + 1);
		area[depth] = 2;
		dfs(depth + 1);
	}

	public static void checkArea(int index, int num) {
		isSelected[index] = true;
		for (int i = 1; i <= N; i++) {
			if (adjmatrix[index][i] == 1 && !isSelected[i] && area[i] == num)
				checkArea(i, num);
		}
	}
}