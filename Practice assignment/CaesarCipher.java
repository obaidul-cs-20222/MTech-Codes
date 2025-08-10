import java.util.Scanner;

public class CaesarCipher {
    private String original_text;
    private int key;

    public CaesarCipher(String original_text, int key) {
        this.original_text = original_text;
        this.key = key % 26; // Normalize key
    }

    public String encrypt() {
        String s2 = "";
        for (int i = 0; i < original_text.length(); i++) {
            char character = original_text.charAt(i);
            if (Character.isLetter(character)) {
                char base = Character.isUpperCase(character) ? 'A' : 'a';
                int index = (character - base + key) % 26;
                s2 = s2 + (char) (base + index);
            } else {
                s2 = s2 + character;
            }
        }
        return s2;
    }

    public String decrypt(String dec) {
        String s3 = "";
        for (int i = 0; i < dec.length(); i++) {
            char character = dec.charAt(i);
            if (Character.isLetter(character)) {
                char base = Character.isUpperCase(character) ? 'A' : 'a';
                int index = (character - base - key + 26) % 26;
                s3 = s3 + (char) (base + index);
            } else {
                s3 = s3 + character;
            }
        }
        return s3;
    }

    public void bruteForceDecrypt(String s) {
        for (int i = 0; i < 26; i++) {
            CaesarCipher temp = new CaesarCipher("", i);
            String decryptedText = temp.decrypt(s);
            System.out.println("Key " + i + ": " + decryptedText);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a Text to encrypt: ");
        String original_text = sc.nextLine();
        System.out.print("Enter a key (0-25): ");
        int key = sc.nextInt();
        sc.close();

        CaesarCipher cipher = new CaesarCipher(original_text, key);
        String encrypted = cipher.encrypt();
        String decrypted = cipher.decrypt(encrypted);

        System.out.println("Original Text: " + original_text);
        System.out.println("Encrypted Text: " + encrypted);
        System.out.println("Decrypted Text: " + decrypted);
        System.out.println("Brute Force Decryption... All possible string combinations are:");
        cipher.bruteForceDecrypt(encrypted);

    }
}

// public class CaesarCipher {

// private String alphabet;
// private String shiftedAlphabet;
// private int key;

// public CaesarCipher(int key) {
// this.key = key;
// alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
// shiftedAlphabet = alphabet.substring(key) + alphabet.substring(0, key);
// }

// public String encrypt(String input) {
// StringBuilder encrypted = new StringBuilder();
// for (char c : input.toCharArray()) {
// if (Character.isLetter(c)) {
// char base = Character.isUpperCase(c) ? 'A' : 'a';
// int index = (c - base + key) % 26;
// encrypted.append((char) (base + index));
// } else {
// encrypted.append(c);
// }
// }
// return encrypted.toString();
// }

// public String decrypt(String input) {
// CaesarCipher reverseCipher = new CaesarCipher(26 - key);
// return reverseCipher.encrypt(input);
// }

// public static void main(String[] args) {
// CaesarCipher cipher = new CaesarCipher(3);
// String original = "Hello, World!";
// String encrypted = cipher.encrypt(original);
// String decrypted = cipher.decrypt(encrypted);

// System.out.println("Original: " + original);
// System.out.println("Encrypted: " + encrypted);
// System.out.println("Decrypted: " + decrypted);
// }
// }

// own
// import java.util.Scanner;

// public class CaesarCipher {

// static String encrypt(String s1, int key) {
// String s2 = "";
// for (int i = 0; i < s1.length(); i++) {
// char character = s1.charAt(i);
// if (Character.isLetter(character)) {
// char base = Character.isUpperCase(character) ? 'A' : 'a';
// int index = (character - base + key) % 26;
// s2 = s2 + (char) (base + index);
// } else {
// s2 = s2 + character;
// }

// }

// return s2;
// }

// static String decrypt(String dec, int key) {
// String s3 = "";
// for (int i = 0; i < dec.length(); i++) {
// char character = dec.charAt(i);
// if (Character.isLetter(character)) {
// char base = Character.isUpperCase(character) ? 'A' : 'a';
// int index = (character - base - key + 26) % 26;
// s3 = s3 + (char) (base + index);
// } else {
// s3 = s3 + character;
// }

// }

// return s3;
// }

// static void bruteForceDecrypt(String s) {

// for (int i = 0; i < 26; i++) {
// String decryptedText = decrypt(s, i);
// System.out.println("Key " + i + ": " + decryptedText);
// }

// }

// public static void main(String[] args) {
// Scanner sc = new Scanner(System.in);
// System.out.print("Enter a Text to encrypt: "); // Prompt the user
// String original_text = sc.nextLine();
// System.out.print("Enter a key (0-25): "); // Prompt the user for key
// int key = sc.nextInt();
// sc.close();
// System.out.println("Original Text: " + original_text); // Display the
// original text
// String en_text = encrypt(original_text, key);
// System.out.println("Encrypted Text: " + en_text); // Display the encrypted
// text
// String dec_text = decrypt(en_text, key);
// System.out.println("Decrypted Text: " + dec_text);
// System.out.println("Brute Force Decryption... All possible string
// combinations are: ");
// bruteForceDecrypt(en_text);

// }
// }