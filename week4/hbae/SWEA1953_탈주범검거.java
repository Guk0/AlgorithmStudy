package day0407;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

/*
1
5 6 2 1 3
0 0 5 3 6 0
0 0 2 0 2 0
3 3 1 3 7 0
0 0 0 0 0 0
0 0 0 0 0 0
*/

public class SWEA1953_탈주범검거 {

	static int[][] arr;
	static int N, M, R, C, L, res;
	static boolean[][] isVisited;
	static int[] dx = { 0, -1, 0, 1 }; // 좌, 상, 우, 하 (왼쪽부터 시계방향)
	static int[] dy = { -1, 0, 1, 0 };
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for (int tc = 0; tc < T; tc++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			R = Integer.parseInt(st.nextToken());
			C = Integer.parseInt(st.nextToken());
			L = Integer.parseInt(st.nextToken());
			arr = new int[N][M];
			isVisited = new boolean[N][M];
			for (int i = 0; i < arr.length; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < arr[i].length; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			res = 0;
			solve();
			sb.append("#").append(tc + 1).append(" ").append(res).append("\n");
		}
		sb.setLength(sb.length() - 1);
		bw.write(sb.toString());
		bw.flush();
		bw.close();
	}

	public static void solve() {
		Queue<int[]> queue = new LinkedList<>();
		queue.add(new int[] { R, C, 1 });
		isVisited[R][C]= true;
		while (!queue.isEmpty()) {
			int[] temp = queue.poll();
			int x = temp[0];
			int y = temp[1];
			int depth = temp[2];
			if (depth>=L)
				continue;
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx < 0 || ny < 0 || nx >= N || ny >= M) // 범위 넘어가는 것
					continue;
				if (isValid(x, y, nx, ny) && isVisited[nx][ny]==false) {
					isVisited[nx][ny] = true;
					queue.add(new int[] { nx, ny,depth+1 });
				} else
					continue;
			}
		}

		for (int i = 0; i < isVisited.length; i++) {
			for (int j = 0; j < isVisited[i].length; j++) {
				if (isVisited[i][j] == true)
					res++;
			}
		}
	}

	public static boolean isValid(int x, int y, int nx, int ny) {
		if (arr[nx][ny] == 0) // 파이프가 없는곳
			return false;
		int command = arr[x][y];
		int forward = arr[nx][ny];
		switch (command) {
		case 1: // 1번타입
			if (nx==x-1 && ny==y) { //1번 타입 위 연결
				if(forward==1 || forward==2 || forward==5 || forward==6)
					return true;
			}
			if(nx==x+1 && ny==y) { //1번 타입 아래 연결
				if(forward==1 || forward==2 || forward==4 || forward==7)
					return true;
			}
			if(nx==x && ny==y-1) { // 1번타입 왼쪽에 연결
				if(forward==1 ||forward==3 || forward== 4 || forward==5)
					return true;
			}
			if(nx==x && ny==y+1) { //1번 타입 오른쪽에 연결
				if(forward==1 || forward== 3 || forward== 6 || forward==7)
					return true;
			}
			return false;
		case 2: // 2번타입
			if (nx == x - 1 && ny == y) { // 2번타입 위에 연결
				if (forward==2 || forward == 1 || forward == 5 || forward == 6)
					return true;
			}
			if (nx == x + 1 && ny == y) { // 2번 타입 아래에 연결
				if (forward==2||forward == 1 || forward == 4 || forward == 7)
					return true;
			}
			return false;
		case 3: // 3번타입
			if (nx == x && ny == y - 1) { // 3번타입 좌 연결
				if (forward==3 || forward == 1 || forward == 4 || forward == 5)
					return true;
			}
			if (nx == x && ny == y + 1) { // 3번타입 우 연결
				if (forward==3 || forward == 1 || forward == 6 || forward == 7)
					return true;
			}
			return false;
		case 4: // 4번타입
			if (nx == x - 1 && ny == y) { // 4번타입 위에 연결
				if (forward == 1 || forward == 2 || forward == 5 || forward == 6)
					return true;
			}
			if (nx == x && ny == y + 1) { // 4번타입 우 연결
				if (forward == 1 || forward == 3 || forward == 6 || forward == 7)
					return true;
			}
			return false;
		case 5: // 5번타입
			if (nx == x + 1 && ny == y) { // 5번타입 아래 연결
				if (forward == 1 || forward == 2 || forward == 4 || forward == 7)
					return true;
			}
			if (nx == x && ny == y + 1) { // 5번타입 우 연결
				if (forward == 1 || forward == 6 || forward == 7 || forward == 3)
					return true;
			}
			return false;
		case 6: // 6번 타입
			if (nx == x && ny == y - 1) { // 6번 타입 왼쪽 연결
				if (forward == 1 || forward == 5 || forward == 4 || forward == 3)
					return true;
			}
			if (nx == x + 1 && ny == y) { // 6번 타입 아래 연결
				if (forward == 1 || forward == 2 || forward == 4 || forward == 7)
					return true;
			}
			return false;
		case 7: // 7번타입
			if (nx == x - 1 && ny == y) { // 7번 타입 위 연결
				if (forward == 1 || forward == 2 || forward == 5 || forward == 6)
					return true;
			}
			if (nx == x && ny == y - 1) { // 7번타입 왼쪽연결
				if (forward == 1 || forward == 3 || forward == 4 || forward == 5)
					return true;
			}
			return false;
		default:
			break;
		}
		return false;
	}
}
