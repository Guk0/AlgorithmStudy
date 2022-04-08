package day0408;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ14502_연구소 {

	static int N, M, arr[][], res;
	static List<int[]> list = new ArrayList<int[]>();
	static List<int[]> numbers = new ArrayList<int[]>();
	static List<int[]> virus = new ArrayList<int[]>();
	static int[] dx = { -1, 0, 1, 0 };
	static int[] dy = { 0, 1, 0, -1 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		arr = new int[N][M];
		for (int i = 0; i < arr.length; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < arr[i].length; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				if (arr[i][j] == 0)
					list.add(new int[] { i, j });
				if (arr[i][j] == 2)
					virus.add(new int[] { i, j });
			}
		}
		res = Integer.MIN_VALUE;
		combination(0, 0);
		System.out.println(res);
	}

	public static void combination(int cnt, int start) {
		if (cnt == 3) {
			int[][] temp = new int[N][M];
			for (int i = 0; i < temp.length; i++) {
				temp[i] = arr[i].clone();
			}
			for (int i = 0; i < numbers.size(); i++) {
				int[] pos = numbers.get(i);
				int x = pos[0];
				int y = pos[1];
				temp[x][y] = 1;
			}
			res = Math.max(res, solve(temp));
//			System.out.println(numbers.toString());
			return;
		}
		for (int i = start; i < list.size(); i++) {
			numbers.add(cnt, list.get(i));
			combination(cnt + 1, i + 1);
			numbers.remove(cnt);
		}
	}

	public static int solve(int[][] virusmap) {
		Queue<int[]> queue = new LinkedList<int[]>();
		int count = 0;
		for (int i = 0; i < virus.size(); i++) {
			queue.add(virus.get(i));
		}
		while (!queue.isEmpty()) {
			int[] temp = queue.poll();
			int x = temp[0];
			int y = temp[1];
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx < 0 || ny < 0 || nx >= N || ny >= M)
					continue;
				if(virusmap[nx][ny]==1 || virusmap[nx][ny]==2)
					continue;
				if (virusmap[nx][ny] == 0) {
					virusmap[nx][ny] = 2;
					queue.add(new int[] { nx, ny });
				}
			}
		}
		for (int i = 0; i < virusmap.length; i++) {
			for (int j = 0; j < virusmap[i].length; j++) {
				if (virusmap[i][j] == 0)
					count++;
			}
		}
		return count;
	}
}
