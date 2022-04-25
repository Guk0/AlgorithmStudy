package day0425;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class BOJ11559_PuyoPuyo {

	static class area {
		int row;
		int col;

		public area(int row, int col) {
			super();
			this.row = row;
			this.col = col;
		}

	}

	static int[] dx = { -1, 0, 1, 0 };
	static int[] dy = { 0, 1, 0, -1 };
	static char[][] arr;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		List<int[]> list = new LinkedList<>();
		arr = new char[12][6];
		for (int i = 0; i < arr.length; i++) {
			arr[i] = br.readLine().toCharArray();
			for (int j = 0; j < arr[i].length; j++) {
				if (arr[i][j] != '.')
					list.add(new int[] { i, j });
			}
		}
		int res = 0;
		while (true) {
			boolean flag = false;
			for (int i = 0; i < 12; i++) {
				for (int j = 0; j < 6; j++) {
					if (arr[i][j] != '.' && bfs(i, j)) {
						pop(i, j);
						flag = true;
					}
				}
			}
			if (!flag)
				break;
			down();
			res++;
		}
		System.out.println(res);

	}

	public static boolean bfs(int row, int col) {
		Queue<area> queue = new LinkedList<>();
		boolean[][] isVisited = new boolean[12][6];
		isVisited[row][col] = true;
		queue.add(new area(row, col));
		char color = arr[row][col];
		while (!queue.isEmpty()) {
			area temp = queue.poll();
			int x = temp.row;
			int y = temp.col;
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx < 0 || ny < 0 || nx >= 12 || ny >= 6)
					continue;
				if (isVisited[nx][ny] == true)
					continue;
				if (arr[nx][ny] != color)
					continue;
				isVisited[nx][ny] = true;
				queue.add(new area(nx, ny));
			}
		}
		int count = 0;
		for (int i = 0; i < isVisited.length; i++) {
			for (int j = 0; j < isVisited[i].length; j++) {
				if (isVisited[i][j] == true)
					count++;
			}
		}
		if (count >= 4)
			return true;
		return false;
	}

	public static void pop(int row, int col) {
		Queue<int[]> queue = new LinkedList<>();
		boolean[][] isVisited = new boolean[12][6];
		char color = arr[row][col];
		arr[row][col] = '.';
		isVisited[row][col] = true;
		queue.add(new int[] { row, col });
		while (!queue.isEmpty()) {
			int[] temp = queue.poll();
			int x = temp[0];
			int y = temp[1];
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx < 0 || ny < 0 || nx >= 12 || ny >= 6)
					continue;
				if (isVisited[nx][ny])
					continue;
				if (arr[nx][ny] == color) {
					arr[nx][ny] = '.';
					isVisited[nx][ny] = true;
					queue.add(new int[] { nx, ny });
				}
			}
		}
	}

	public static void down() {
		for (int i = 11; i >= 0; i--) {
			for (int j = 0; j < 6; j++) {
				if (arr[i][j] == '.') {
					int remove = i;
					int count = i - 1;
					while (count >= 0) {
						if (arr[count][j] != '.') {
							arr[remove][j] = arr[count][j];
							arr[count][j] = '.';
							break;
						}
						count -= 1;
					}
				}
			}
		}
	}

}
