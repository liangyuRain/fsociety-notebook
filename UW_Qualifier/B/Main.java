import java.util.*;

public class Main {

	public static void main(String[] args) {
		HashSet<Integer> sizes = new HashSet<Integer>();
		sizes.add(1);
		for (int i = 3; i <= 10000; i = i * 2 + 1) {
			sizes.add(i);
		}
		int[] unionSet = new int[8191];
		for (int i = 1; i < unionSet.length; i += 2) {
			unionSet[i] = i;
		}
		int end = 8191;
		while(end > 1) {
			int i = 1, j = end - 2;
			while(i < j) {
				merge(unionSet, i, j);
				i += 2;
				j -= 2;
			}
			end /= 2;
		}
		for (int i = 1; i < unionSet.length; i += 2) {
			find(unionSet, i);
		}
		Scanner console = new Scanner(System.in);
		for(;;) {
			int k = console.nextInt();
			if (k == 0) {
				return;
			}
			String str = console.nextLine();
			if (!sizes.contains(str.length())) {
				System.out.println(-1);
				continue;
			}
			if (solution(unionSet, str, k) == -1) {
				System.out.println(-1);
			} else {
				System.out.println();
			}
		}
	}
	
	public static int find(int[] arr, int x) {
		if (arr[x] == x) {
			return x;
		} else {
			arr[x] = find(arr, arr[x]);
			return arr[x];
		}
	}
	
	public static void merge(int[] arr, int x, int y) {
		arr[find(arr, y)] = find(arr, x);
	}
	
	public static int solution(int[] union, String str, int k) {
		char[] chararr = str.toCharArray();
		Map<Integer, Character> setChar = new HashMap<>();
		for (int i = 0; i < chararr.length; ++i) {
			char ch = setChar.computeIfAbsent(union[i], (key) -> '?');
			if (ch != chararr[i]) {
				if (ch == '?') {
					if (union[i] == 0 && chararr[i] == '0') {
						return -1;
					}
					setChar.put(union[i], chararr[i]);
				} else {
					if (chararr[i] != '?') {
						return -1;
					}
				}
			}
		}
		TreeSet<Integer> ques = new TreeSet<Integer>();
		Set<Integer> added = new HashSet<Integer>();
		for (int i = 0; i < chararr.length; ++i) {
			char ch = setChar.get(union[i]);
			if (ch == '?' && !added.contains(union[i])) {
				ques.add(i);
				added.add(union[i]);
			} else {
				chararr[i] = ch;
			}
		}
		Map<Integer, Set<Integer>> setCannot = new HashMap<>();
		for (int i = 0; i < chararr.length; ++i) {
			Set<Integer> cannot = setCannot.computeIfAbsent(union[i], (key) -> new HashSet<Integer>());
			if (i > 0) {
				cannot.add(chararr[i - 1] - '0');
			} else if (i < chararr.length - 1) {
				cannot.add(chararr[i + 1] - '0');
			}
			if (cannot.size() == 10) {
				return -1;
			}
		}
		if (setCannot.containsKey(0)) {
			setCannot.get(0).add(0);
		}
		Map<Integer, List<Integer>> setCan = new HashMap<>();
		for (Map.Entry<Integer, Set<Integer>> entry : setCannot.entrySet()) {
			int key = entry.getKey();
			Set<Integer> value = entry.getValue();
			List<Integer> l = new ArrayList<Integer>();
			for (int i = 0; i < 10; ++i) {
				if (!value.contains(i)) {
					l.add(i);
				}
			}
			setCan.put(key, l);
		}
		int[] indexToSet = new int[ques.size()];
		int i = 0;
		for (int num : ques) {
			indexToSet[i++] = union[num];
		}
		List<Integer>[] possibles = (List<Integer>[])new Object[ques.size()];
		for (i = 0; i < possibles.length; ++i) {
			possibles[i] = setCan.get(indexToSet[i]);
		}
		int[] arr = new int[ques.size()];
		if (indexToSet[0] == 0) {
			int ch = possibles[0].get(0);
			for (i = 1; i < arr.length; ++i) {
				if (possibles[i].get(0) == ch) {
					++arr[i];
					if (arr[i] >= possibles[i].size()) {
						return -1;
					}
				}
			}
		}
		for (i = 0; i < possibles.length; ++i) {
			System.out.println(possibles[i].toString());
		}
		return -1;
	}

}
