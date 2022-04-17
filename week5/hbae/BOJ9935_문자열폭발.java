package day0417;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Iterator;
import java.util.Stack;

public class BOJ9935_문자열폭발 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		char[] arr = br.readLine().toCharArray();
		char[] check = br.readLine().toCharArray();
		Stack<Character> stack = new Stack<Character>();
		OUT: for (int i = 0; i < arr.length; i++) {
			stack.add(arr[i]);
			if (stack.size() >= check.length) {
				for (int j = 0; j < check.length; j++) {
					int idx = stack.size() - check.length + j;
					if (stack.get(idx) != check[j]) //check길이만큼 스택에서 확인해주 다르면 계
						continue OUT;
				}
				for (int j = 0; j < check.length; j++) { //check가 있다면 그만큼 스택에서 꺼내줌
					stack.pop();
				}
			}
		}
		for (int i = 0; i < stack.size(); i++) {
			sb.append(stack.get(i));
		}
		if (sb.length()==0)
			sb.append("FRULA");
		bw.write(sb.toString());
		bw.flush();
		bw.close();
	}

}
