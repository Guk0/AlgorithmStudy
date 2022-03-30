import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ11067_모노톤길 {

	static class Cafe implements Comparable<Cafe> {
		int x;
		int y;

		public Cafe(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}
		// x좌표 를 기준으로 정렬
		@Override
		public int compareTo(Cafe o) {
			if (this.x != o.x) 
				return this.x - o.x;
			else return this.y - o.y;
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();

		int T = Integer.parseInt(br.readLine());

		for (int tc = 0; tc < T; tc++) {
			int N = Integer.parseInt(br.readLine()); // 카페의 수
			Cafe[] cafes = new Cafe[N]; // 카페 좌표 저장
			Cafe[] res = new Cafe[N]; // 카페 좌표 정렬 후 저장
			int[] count = new int[100001]; // 같은 x좌표에 카페가 몇 개 있는지 저장

			for (int n = 0; n < N; n++) {
				st = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());

				cafes[n] = new Cafe(x, y);
				count[x]++;
			}

			Arrays.sort(cafes);

			int init = 0; // 입구 좌표의 y값은 0
			int i = 0;
			while (i < N) {
				// 같은 x좌표일 때 범위 지정
				int start = i;
				int end = i + count[cafes[i].x] - 1;

				if (cafes[i].y == init) { // 오름차순 정렬된 y좌표가 이전 y좌표랑 동일한 경우
					for (int j = start; j <= end; j++) { // 정렬된 순서대로 새로운 배열에 넣어줌
						res[i++] = cafes[j];
					}
					init = cafes[end].y;
				} else { // 오름차순 정렬된 y좌표가 이전 y좌표랑 다른 경우
					for (int j = end; j >= start; j--) { // 뒤에서부터 새로운 배열에 넣어줌
						res[i++] = cafes[j];
					}
					init = cafes[start].y;
				}
			}

			st = new StringTokenizer(br.readLine());
			int M = Integer.parseInt(st.nextToken()); // 카페 번호를 M개 줌
			for (int m = 0; m < M; m++) {
				int idx = Integer.parseInt(st.nextToken());
				sb.append(res[idx - 1].x).append(" ").append(res[idx - 1].y).append("\n");
			}
		}

		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();

	}

}
