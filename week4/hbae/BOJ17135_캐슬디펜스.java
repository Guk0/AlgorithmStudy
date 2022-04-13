package day0408;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ17135_캐슬디펜스 {

	static int N, M, D, res, enemy, arr[][];
	static List<int[]> list = new ArrayList<>();
	static List<int[]> numbers = new ArrayList<>();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		D = Integer.parseInt(st.nextToken());
		arr = new int[N][M];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				if (arr[i][j] == 1)
					enemy++;
			}
		}
		if (enemy == 0) {
			System.out.println(0);
			return;
		}
		for (int j = 0; j < M; j++) {
			list.add(new int[] { N, j });
		}
		res = Integer.MIN_VALUE;
		combination(0, 0);
		System.out.println(res);
	}

	public static void combination(int cnt, int start) {
		if (cnt == 3) {
			res = Math.max(res, solve(numbers));
			return;
		}
		for (int i = start; i < list.size(); i++) {
			numbers.add(cnt, list.get(i));
			combination(cnt + 1, i + 1);
			numbers.remove(cnt);
		}
	}

	public static int solve(List<int[]> list) {
		List<int[]> killlist = new LinkedList<>();
		int depth = 0;
		int death = 0;
		int[][] map = new int[N][M];
		for (int i = 0; i < arr.length; i++) {
			map[i] = arr[i].clone();
		}
		while (depth < N) {
			for (int tc = 0; tc < list.size(); tc++) {
				int x = list.get(tc)[0] - depth;
				int y = list.get(tc)[1];
				int target_d = 999999999;
				int target_x = -1;
				int target_y = -1;
				for (int i = N - depth - 1; i >= 0; i--) {
					for (int j = 0; j < M; j++) {
						if (map[i][j] == 1) {
							int distance = Math.abs(i - x) + Math.abs(j - y);
							if (distance > D)
								continue;
							if (distance < target_d) { // 최소거리에 있는 타겟 갱신
								target_d = distance;
								target_x = i;
								target_y = j;
							} else if (distance == target_d) { // 거리가 같다면 왼쪽에 있는 타겟으로
								if (j < target_y) {
									target_x = i;
									target_y = j;
								}
							}
						}
					}
				}
				if (target_x == -1 || target_y == -1)
					continue;
				// 최소 거리이자, 가장 왼쪽에 있는 타겟을 찾았으니까 큐에 넣어줌.
				// 즉 궁수가 3명이니까 타겟이 3개 들어가는 셈(타겟은 중복가능)
				killlist.add(new int[] { target_x, target_y });
			}
			for (int i = 0; i < killlist.size(); i++) {
				int[] temp = killlist.get(i);
				int x = temp[0];
				int y = temp[1];
				if (map[x][y] == 1) {
					map[x][y] = 0;
					death++;
				}
			}
			killlist.clear();
			depth++;
		}
		return death;
	}

}
