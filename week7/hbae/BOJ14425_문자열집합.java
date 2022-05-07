package day0503;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class BOJ14425_문자열집합 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		HashMap<String, String> hash = new HashMap<>();
		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			hash.put(str, "value");
		}
		int count = 0;
		for (int i = 0; i < M; i++) {
			String str = br.readLine();
			if (hash.get(str) != null && hash.get(str).equals("value"))
				count++;
		}
		System.out.println(count);
	}

}
