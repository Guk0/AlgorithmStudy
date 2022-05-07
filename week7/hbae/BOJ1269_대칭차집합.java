package day0503;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ1269_대칭차집합 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int A_count = Integer.parseInt(st.nextToken());
		int B_count = Integer.parseInt(st.nextToken());
		List<Integer> A = new ArrayList<>();
		List<Integer> B = new ArrayList<>();
		HashMap<Integer, String> A_map = new HashMap<>();
		HashMap<Integer, String> B_map = new HashMap<>();
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < A_count; i++) {
			int temp = Integer.parseInt(st.nextToken());
			A.add(temp);
			A_map.put(temp, "value");
		}
		int count = 0;
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < B_count; i++) {
			int temp = Integer.parseInt(st.nextToken());
			B.add(temp);
			B_map.put(temp, "value");
		}
		for (int i = 0; i < A.size(); i++) {
			int temp = A.get(i);
			if(B_map.get(temp)==null)
				count++;
		}
		for (int i = 0; i < B.size(); i++) {
			int temp = B.get(i);
			if(A_map.get(temp)==null)
				count++;
		}
		System.out.println(count);
	}

}
