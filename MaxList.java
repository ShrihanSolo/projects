public class MaxList {
    /** Returns the maximum value from m. */
    public static int max(int[] m) {
      int maxno = 0;
      int i = 0;
      while (i < m.length) {
        if (maxno < m[i]) {
          maxno = m[i];
        }
        i += 1;
      }
      return maxno;
    }
    public static int forMax(int[] lst) {
      int maxno = 0;
      for (int i = 0; i < lst.length; i += 1) {
        if (maxno < lst[i]) {
          maxno = lst[i];
        }
      }
      return maxno;
    }
    public static void main(String[] args) {
       int[] numbers = new int[]{9, 2, 15, 2, 22, 10, 6};
       System.out.println(forMax(numbers));
    }
}
