package day0405;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class SWEA5656_벽돌깨기DFS {

	public static class Point {
		int r, c, cnt;

		public Point(int r, int c, int cnt) {
			super();
			this.r = r;
			this.c = c;
			this.cnt = cnt;
		}
	}

	static int[] dx = { -1, 0, 1, 0 };
	static int[] dy = { 0, 1, 0, -1 };
	static int N, W, H, min;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int tc = 0; tc < T; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());
			H = Integer.parseInt(st.nextToken());
			int[][] map = new int[H][W];
			for (int i = 0; i < H; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < W; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			min = Integer.MAX_VALUE;
			go(0, map);
			sb.append("#").append(tc + 1).append(" ").append(min).append("\n");
		}
		sb.setLength(sb.length() - 1);
		bw.write(sb.toString());
		bw.flush();
		bw.close();
	}

	// count는 구술을 던진 횟수
	// 벽돌이 다 부서졌다면 true, 아니면 false 리턴
	public static boolean go(int count, int[][] map) { // 중복순열 이용하여 구슬 던지기

		int res = getRemain(map);
		if (res == 0) { // 모든 벽돌이 부서졌다면
			min = 0;
			return true;
		}

		if (count == N) { // 모든 구슬을 다 던졌다면
			min = Math.min(min, res);
			return false;
		}

		int[][] newmap = new int[H][W];

		// 0열부터 W-1열까지 구슬 던져보기
		for (int c = 0; c < W; c++) {
			// 구슬에 맞는 벽돌 찾기
			int r = 0;
			while (r < H && map[r][c] == 0)// 빈공간이면 계속해서 아래로
				r++;
			// 해당열은 벽돌이 없음
			if (r == H)
				continue;
			// 배열의 상태를 백업
			copy(map, newmap);
			boom(newmap, r, c); // 현재 벽돌기준으로 주변의 가능한 모든 벽돌 함께 연쇄처리
			down(newmap); // 부서진 벽돌 정리
			if (go(count + 1, newmap)) // 다음 구슬 던지러 go
				return true;
		}
		return false;
	}

	public static void boom(int[][] map, int r, int c) { // r,c위치에서 주변의 가능한 모든 벽돌 제거처리
		Queue<Point> queue = new LinkedList<Point>();
		if (map[r][c] > 1) { // 벽돌 크기가 2이상이면
			queue.offer(new Point(r, c, map[r][c]));
		}
		map[r][c] = 0; // 자신은 제거처리(빈공간으로) : visit처리 역할
		while (!queue.isEmpty()) {
			Point p = queue.poll();
			for (int i = 0; i < 4; i++) {
				int nr = p.r;
				int nc = p.c;
				for (int k = 1; k < p.cnt; k++) { // 벽돌의 크기-1만큼 반복
					nr += dx[i];
					nc += dy[i];
					if (nr>=0 && nr<H && nc>=0 && nc<W && map[nr][nc]>0) {
						if (map[nr][nc] > 1) { // 주변 벽돌에 영향을 주는 벽돌이면
							queue.offer(new Point(nr, nc, map[nr][nc]));
						}
						map[nr][nc] = 0; // 제거처리
					}
				}
			}
		}
	}
	static ArrayList<Integer> list = new ArrayList<>();
	public static void down(int[][] map) { // 부서진 벽돌 정리, 남은 벽돌 정리(공중에 떠있는 벽돌 아래로 땡기기)
		for (int c = 0; c < W; c++) {
			int r = H - 1; // 아래행 시작
			while (r >= 0) {
				if (map[r][c] > 0) { // 벽돌 찾기
					list.add(map[r][c]);
					map[r][c] = 0;
				}
				r--;
			} // 부서지지 않고 남아있는 벽돌 리스트에 다 담기, 벽돌이 있떤 자리는 빈공간으로 처리
			r = H-1;
			for(int a: list) { // 벽돌리스트
				map[r--][c] = a; 
			}
			list.clear();
		}
		
	}

	public static int getRemain(int[][] map) { // 남은 벽돌 수 리턴
		int count = 0;
		for (int r = 0; r < H; r++) {
			for (int c = 0; c < W; c++) {
				if (map[r][c] > 0)
					count++;
			}
		}
		return count;
	}

	public static void copy(int[][] map, int[][] newmap) {
		for (int r = 0; r < H; r++) {
			for (int c = 0; c < W; c++) {
				newmap[r][c] = map[r][c];
			}
		}
	}
}
