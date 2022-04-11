package day0411;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class SWEA8485_원점으로집합 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		OUT: for (int tc = 0; tc < T; tc++) {
			int N = Integer.parseInt(br.readLine());
			boolean flag = true;
			st = new StringTokenizer(br.readLine());
			int d = Math.abs(Integer.parseInt(st.nextToken())) + Math.abs(Integer.parseInt(st.nextToken()));
			int mod = d % 2;
			for (int i = 1; i < N; i++) { // 각각의 좌표들의 거리 저장
				st = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				int temp = Math.abs(x) + Math.abs(y);
				if (temp % 2 != mod) {
					flag = false;
				}
				d = Math.max(d, temp);
			}
			if(flag==false) {
				sb.append("#").append(tc + 1).append(" ").append("-1").append("\n");
				continue OUT;
			}
			int sum = 0;
			for (int i = 0; i <= d; i++) {
				sum += i;
				if (d - sum <= 0 && Math.abs(d - sum) % 2 == 0) {
					sb.append("#").append(tc + 1).append(" ").append(i).append("\n");
					break;
				}
			}
		}
		bw.write(sb.toString());
		bw.flush();
		bw.close();

	}
}
