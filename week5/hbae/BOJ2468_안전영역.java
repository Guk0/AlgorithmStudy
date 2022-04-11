package day0411;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ2468_안전영역 {

	static int N, arr[][];
	static boolean[][] isVisited;
	static List<Integer> list;
	static int[] dx = { -1, 0, 1, 0 };
	static int[] dy = { 0, 1, 0, -1 };
	static Queue<int[]> queue;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		arr = new int[N][N];
		list = new ArrayList<>();
		for (int i = 0; i < arr.length; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < arr[i].length; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				if (!list.contains(arr[i][j]))
					list.add(arr[i][j]);
			}
		}
		list.add(0);
		int res = 0;
		for (int tc = 0; tc < list.size(); tc++) {
			int count = 0;
			isVisited = new boolean[N][N];
			queue = new LinkedList<>();
			int height = list.get(tc);
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (arr[i][j] <= height)
						isVisited[i][j] = true;
				}
			}
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (arr[i][j] > height && isVisited[i][j] == false) {
						queue.add(new int[] { i, j });
						isVisited[i][j] = true;
						solve();
						count++;
					}
				}
			}
			res = Math.max(res, count);
		}
		System.out.println(res);
	}

	public static void solve() {
		while (!queue.isEmpty()) {
			int[] temp = queue.poll();
			int x = temp[0];
			int y = temp[1];
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx < 0 || ny < 0 || nx >= N || ny >= N)
					continue;
				if (isVisited[nx][ny] == false) {
					isVisited[nx][ny] = true;
					queue.add(new int[] { nx, ny });
				}
			}
		}
	}
}
