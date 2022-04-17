package day0417;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
import java.util.StringTokenizer;

public class BOJ2812_크게만들기2 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		Stack<Integer> stack = new Stack<Integer>();
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		String str = br.readLine();
		for (int i = 0; i < str.length(); i++) {
			int temp = (int) (str.charAt(i) - '0');
			while (K > 0 && !stack.isEmpty() && stack.peek() < temp) {
				stack.pop();
				K--;
			}
			stack.add(temp);
		}
		if (K > 0) {
			while (true) {
				if (K == 0)
					break;
				stack.pop();
				K--;
			}
		}
		for (int i = 0; i < stack.size(); i++) {
			sb.append(stack.get(i));
		}
		bw.write(sb.toString());
		bw.flush();
		bw.close();
	}

}
