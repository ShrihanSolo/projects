public class ContinueDemo {
    public static void main(String[] args) {
        String[] a = {"cat", "dog", "laser horse", "ketchup", "horse", "horbse"};

        for (int i = 0; i < a.length; i += 1) {
            if (a[i].contains("horse")) {
                continue;
            }
            for (int j = 0; j < 3; j += 1) {
                System.out.println(a[i]);
            }
        }
        String[] b = {"cat", "dog", "laser horse", "ketchup", "horse", "horbse"};

        for (int i = 0; i < b.length; i += 1) {
            for (int j = 0; j < 3; j += 1) {
                System.out.println(b[i]);
                if (b[i].contains("horse")) {
                    break;
                }
            }
        }
    }
}
