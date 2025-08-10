import java.io.*;

class permutation {
	public static void main(String args[]) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s1 = "";
		System.out.print("Enter a String: ");
		s1 = br.readLine();
		String s2 = "";
		System.out.println("permuted combinations are: ");
		comb(s1, s2);
	}

	static void comb(String s1, String s2) {
		if (s2.length() == s1.length()) {
			System.out.print(" " + s2);
			// System.out.println();
			return;
		}
		for (int i = 0; i < s1.length(); i++) {
			if (s2.indexOf(s1.charAt(i)) != -1) {
				continue;

			}
			comb(s1, s2 + s1.charAt(i));
		}
	}

}
