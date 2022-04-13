package day0410;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ13460_구슬탈출2 {

	public static class ball {
		int rx;
		int ry;
		int bx;
		int by;
		int depth;

		public ball(int rx, int ry, int bx, int by, int depth) {
			super();
			this.rx = rx;
			this.ry = ry;
			this.bx = bx;
			this.by = by;
			this.depth = depth;
		}
	}

	static int N, M;
	static char[][] arr;
	static boolean[][][][] isVisited;
	static int[] dx = { -1, 0, 1, 0 };
	static int[] dy = { 0, 1, 0, -1 };
	static Queue<ball> queue;
	static int goal_x, goal_y;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		arr = new char[N][M];
		isVisited = new boolean[N][M][N][M];
		queue = new LinkedList<>();
		int bx = 0, by = 0, rx = 0, ry = 0;
		for (int i = 0; i < arr.length; i++) {
			arr[i] = br.readLine().toCharArray();
			for (int j = 0; j < arr[i].length; j++) {
				if (arr[i][j] == 'O') {
					goal_x = i;
					goal_y = j;
				} else if (arr[i][j] == 'R') {
					rx = i;
					ry = j;
				} else if (arr[i][j] == 'B') {
					bx = i;
					by = j;
				}
			}
		}
//		System.out.print(goal_x +" " + goal_y +" " +rx + " " + ry + " " + bx +" " + by + " ");
//		System.out.println();
		queue.add(new ball(rx, ry, bx, by, 0));
		isVisited[rx][ry][bx][by] = true;
		System.out.println(solve());
	}

	public static int solve() {
		while (!queue.isEmpty()) {
			ball temp = queue.poll();
			if (temp.depth > 10) { // 카운트가 10 넘어가면
				continue;
			}
			if (temp.bx == goal_x && temp.by == goal_y) // 파란공 빠지면 안됨
				continue;
			if (temp.rx == goal_x && temp.ry == goal_y) { // 파란공 안빠지고 빨간공빠짐.
				return temp.depth;
			}
			for (int i = 0; i < 4; i++) {
				int rnx = temp.rx;
				int rny = temp.ry;
				int bnx = temp.bx;
				int bny = temp.by;
				while (true) {
					rnx += dx[i];
					rny += dy[i];
					if (arr[rnx][rny] == 'O' || arr[rnx][rny] == '#')
						break;
				}
				if (arr[rnx][rny] == '#') {
					rnx -= dx[i];
					rny -= dy[i];
				}
				while (true) {
					bnx += dx[i];
					bny += dy[i];
					if (arr[bnx][bny] == 'O' || arr[bnx][bny] == '#')
						break;
				}
				if (arr[bnx][bny] == '#') {
					bnx -= dx[i];
					bny -= dy[i];
				}
				if (rnx == bnx && rny == bny && arr[rnx][rny] != 'O') {
					int r_d = Math.abs(rnx - temp.rx) + Math.abs(rny - temp.ry);
					int b_d = Math.abs(bnx - temp.bx) + Math.abs(bny - temp.by);
					if (r_d > b_d) {
						rnx -= dx[i];
						rny -= dy[i];
					} else {
						bnx -= dx[i];
						bny -= dy[i];
					}
				}
				if(isVisited[rnx][rny][bnx][bny]==false) {
					isVisited[rnx][rny][bnx][bny] =true;
					queue.add(new ball(rnx,rny,bnx,bny,temp.depth+1));
				}
			}
		}
		return -1;
	}
}
