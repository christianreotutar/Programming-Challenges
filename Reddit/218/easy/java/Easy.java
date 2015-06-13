import java.util.Scanner;

public class Easy {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        while (scan.hasNextLine()) {
            //System.out.println(scan.nextLine());
            String line = scan.nextLine().trim();

            int num = 0;
            try {
                num = Integer.parseInt(line);
            } catch (NumberFormatException e) {
                System.err.println("Incorrect input.");
                return;
            }

            System.out.println(isPalindrome(num));
        }
    }

    public static boolean isPalindrome(int num) {
        String strnum = num + "";
        int numLength = strnum.length();
        for (int i = 0; i < numLength/2; i++) {
            if (strnum.charAt(i) != strnum.charAt(numLength-1-i)) {
                return false;
            }
        }
        return true;
    }
}
