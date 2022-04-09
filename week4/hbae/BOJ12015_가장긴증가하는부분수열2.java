package day0404;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ12015_가장긴증가하는부분수열2 {

// 시간복잡도가 N^2인 풀이 -> 시간초과 나온다.
//	public static void main(String[] args) throws IOException{
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		int N = Integer.parseInt(br.readLine());
//		int[] arr = new int[N];
//		int[] dp = new int[N];
//		StringTokenizer st = new StringTokenizer(br.readLine());
//		for (int i = 0; i < arr.length; i++) {
//			arr[i] = Integer.parseInt(st.nextToken());
//		}
//		for (int i = 1; i < arr.length; i++) {
//			dp[i] = 1;
//			for (int j = 0; j < i; j++) {
//				if (arr[i]>arr[j] && dp[i]<dp[j]+1)
//					dp[i] = dp[j]+1;
//			}
//			res = Math.max(res, dp[i]);
//		}
//		System.out.println(res);
//
//	}
	//시간복잡도가 NlogN 풀이
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		int[] dp = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < arr.length; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
	}
}
