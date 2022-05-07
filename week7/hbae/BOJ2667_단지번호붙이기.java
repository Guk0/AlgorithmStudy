package day0503;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;

public class BOJ2667_단지번호붙이기 {

	static int[] dx = { -1, 0, 1, 0 };
	static int[] dy = { 0, 1, 0, -1 };
	static int N, res, arr[][];
	static boolean[][] isVisited;
	static PriorityQueue<Integer> pq = new PriorityQueue<>();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		N = Integer.parseInt(br.readLine());
		arr = new int[N][N];
		isVisited = new boolean[N][N];
		for (int i = 0; i < arr.length; i++) {
			String str = br.readLine();
			for (int j = 0; j < str.length(); j++) {
				arr[i][j] = str.charAt(j) - '0';
			}
		}
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[i].length; j++) {
				if (arr[i][j] == 1 && isVisited[i][j] == false) {
					bfs(i, j);
					res++;
				}
			}
		}
		sb.append(res).append("\n");
		while (!pq.isEmpty()) {
			sb.append(pq.poll()).append("\n");
		}
		sb.setLength(sb.length() - 1);
		System.out.println(sb.toString());

	}

	public static void bfs(int row, int col) {
		Queue<int[]> queue = new LinkedList<int[]>();
		queue.add(new int[] { row, col });
		int count = 1;
		isVisited[row][col] = true;
		while (!queue.isEmpty()) {
			int[] temp = queue.poll();
			int x = temp[0];
			int y = temp[1];
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx < 0 || ny < 0 || nx >= N || ny >= N)
					continue;
				if (arr[nx][ny] == 1 && !isVisited[nx][ny]) {
					queue.add(new int[] { nx, ny });
					isVisited[nx][ny] = true;
					count++;
				}
			}
		}
		pq.add(count);
	}

}
