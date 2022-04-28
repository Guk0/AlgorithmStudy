package day0428;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ3584_가장가까운공통조상 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for (int tc = 0; tc < T; tc++) {
			int N = Integer.parseInt(br.readLine());
			int[] parents = new int[N + 1];
			Arrays.fill(parents, -1);
			for (int i = 1; i <= N - 1; i++) {
				st = new StringTokenizer(br.readLine());
				int papa = Integer.parseInt(st.nextToken());
				int son = Integer.parseInt(st.nextToken());
				parents[son] = papa;
			}
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			System.out.println(solve(x, y, parents));
		}

	}

	public static int solve(int x, int y, int[] parents) {
		List<Integer> xlist = new ArrayList<>();
		while (x != -1) {
			xlist.add(x); // 자기 자신이 다른 노드의 부모가 될 수도 있으니까
			x = parents[x];
		}
		while (y != -1) {
			if (xlist.contains(y)) {
				return y;
			}
			y = parents[y];

		}

		return 0;
	}

}
