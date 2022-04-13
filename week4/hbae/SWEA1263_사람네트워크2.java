package day0404;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class SWEA1263_사람네트워크2 {

	static final int INF = 9999999;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for (int tc = 0; tc < T; tc++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int[][] adjMatrix = new int[N][N];
			for (int i = 0; i < N; ++i) {
				for (int j = 0; j < N; ++j) {
					adjMatrix[i][j] = Integer.parseInt(st.nextToken());
					if (i != j && adjMatrix[i][j] == 0) {// 자기자신으로의 인접 정보가 아니고 인접해있지 않다면 INF로 채우기
						adjMatrix[i][j] = INF;
					}
				}
			}
			//System.out.println("===========입력==========");
			// 출발지-->경유지-->목적지로 3중 루프 돌리면 오답
			// 경유지-->출발지-->목적지로 3중 루프 돌려야 정답
			int res = Integer.MAX_VALUE;
			for (int k = 0; k < N; ++k) {
				for (int i = 0; i < N; ++i) {
					if (i == k)
						continue; // 출발지와 경유지가 같다면 다음 출발지
					for (int j = 0; j < N; ++j) {
						if (i == j || k == j)
							continue; // 경유지와 목적지가 같거나 출발지가 곧 목적지라면 패스
						if (adjMatrix[i][j] > adjMatrix[i][k] + adjMatrix[k][j]) {
							adjMatrix[i][j] = adjMatrix[i][k] + adjMatrix[k][j];
						}
					}
				}
			}
			for (int i = 0; i < adjMatrix.length; i++) {
				int temp = 0;
				for (int j = 0; j < adjMatrix[i].length; j++) {
					temp += adjMatrix[i][j];
				}
				if(res>temp)
					res = temp;
			}
			sb.append("#").append(tc+1).append(" ").append(res).append("\n");
		}
		sb.setLength(sb.length()-1);
		bw.write(sb.toString());
		bw.flush();
		bw.close();

	}

}
