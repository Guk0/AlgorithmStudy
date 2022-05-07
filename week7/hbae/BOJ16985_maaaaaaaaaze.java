package day0507;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ16985_maaaaaaaaze {

	static int[][][] arr, cube;
	static int[] dx = { 0, -1, 0, 1, 0, 0 };
	static int[] dy = { 1, 0, -1, 0, 0, 0 };
	static int[] dz = { 0, 0, 0, 0, 1, -1 };
	static int[] numbers, input;
	static boolean[] isSelected;
	static int res;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		arr = new int[5][5][5];
		cube = new int[5][5][5];
		input = new int[5];
		numbers = new int[5];
		isSelected = new boolean[5];
		for (int i = 0; i < input.length; i++) {
			input[i] = i;
		}
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++) {
				st = new StringTokenizer(br.readLine());
				for (int k = 0; k < 5; k++) {
					arr[i][j][k] = Integer.parseInt(st.nextToken());
				}
			}
		}
		res = Integer.MAX_VALUE;
		permutation(0);
		if (res != Integer.MAX_VALUE)
			System.out.println(res);
		else
			System.out.println(-1);

	}

	public static void permutation(int cnt) {
		if (cnt == 5) {
			for (int i = 0; i < 5; i++) {
				int index = numbers[i];
				for (int j = 0; j < 5; j++) {
					for (int k = 0; k < 5; k++) {
						cube[i][j][k] = arr[index][j][k];
					}
				}
			}

			solve();
			return;
		}
		for (int i = 0; i < 5; i++) {
			if (!isSelected[i]) {
				isSelected[i] = true;
				numbers[cnt] = input[i];
				permutation(cnt + 1);
				isSelected[i] = false;
			}
		}
	}

	public static void solve() {
		for (int i = 0; i <= 3; i++) {
			rotate90(0);
			for (int j = 0; j <= 3; j++) {
				rotate90(1);
				for (int k = 0; k <= 3; k++) {
					rotate90(2);
					for (int m = 0; m <= 3; m++) {
						rotate90(3);
						for (int n = 0; n <= 3; n++) {
							rotate90(4);
							if (cube[0][0][0] == 1 && cube[4][4][4] == 1)
								bfs();
						}
					}
				}
			}
		}
	}

	public static void rotate90(int layer) {
		int[][] temp = new int[5][5];
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++) {
				temp[i][j] = cube[layer][4 - j][i];
			}
		}
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++) {
				cube[layer][i][j] = temp[i][j];
			}
		}

	}

	public static void bfs() {
		Queue<int[]> queue = new LinkedList<int[]>();
		boolean[][][] isVisited = new boolean[5][5][5];
		queue.add(new int[] { 0, 0, 0, 0 });
		isVisited[0][0][0] = true;
		while (!queue.isEmpty()) {
			int[] temp = queue.poll();
			int x = temp[0];
			int y = temp[1];
			int z = temp[2];
			int depth = temp[3];
			if (x == 4 && y == 4 && z == 4) {
				res = Math.min(res, depth);
				if (res == 12)
					return;
				continue;
			}
			for (int i = 0; i < 6; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				int nz = z + dz[i];
				if (nx < 0 || ny < 0 || nz < 0 || nx >= 5 || ny >= 5 || nz >= 5)
					continue;
				if (isVisited[nx][ny][nz] || cube[nx][ny][nz] == 0)
					continue;
				queue.add(new int[] { nx, ny, nz, depth + 1 });
				isVisited[nx][ny][nz] = true;
			}
		}
	}

}
