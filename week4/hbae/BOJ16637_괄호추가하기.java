package day0406;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class BOJ16637_괄호추가하기 {

	static int ans, N;
	static ArrayList<Integer> num = new ArrayList<Integer>();
	static ArrayList<Character> sign = new ArrayList<Character>();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		char[] arr = br.readLine().toCharArray();
		num = new ArrayList<Integer>();
		sign = new ArrayList<Character>();
		for (int i = 0; i < arr.length; i++) {
			if ((i + 1) % 2 == 0) { // 숫자면
				sign.add(arr[i]);
			} else
				num.add((int) arr[i] - 48);
		}
//		System.out.println(sign.toString());
//		System.out.println(num.toString());
		ans = Integer.MIN_VALUE;
		dfs(0, num.get(0));
		System.out.println(ans);
	}

	public static void dfs(int depth, int res) {
		if (depth >= sign.size()) {
			ans = Math.max(res, ans);
			//System.out.println(ans);
			return;
		}
		// 괄호 없이 갈때
		int newres = solve(res, sign.get(depth), num.get(depth + 1));
		dfs(depth + 1, newres);
		// 괄호 있이 갈때
		if (depth < sign.size() - 1) {
			// 현재까지의 결과값보다 오른쪽에 있는 것들에 대한 연산
			int temp = solve(num.get(depth + 1), sign.get(depth + 1), num.get(depth + 2));
			// 현재까지의 결과값과 방금 구해진 값에 대한 연산
			dfs(depth + 2, solve(res, sign.get(depth), temp));
		}
	}

	public static int solve(int left, char sign, int right) {
		if (sign == '+') {
			return left + right;
		} else if (sign == '-') {
			return left - right;
		} else if (sign == '*')
			return left * right;
		return 0;
	}

}
