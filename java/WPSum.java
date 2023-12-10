public class WPSum {
  public static void windowPosSum(int[] lst, int n) {
    for (int i = 0; i < lst.length; i += 1) {
      int rep_elem = 0;
      if (lst[i] >= 0) {
        for (int j = 0; j <= n; j += 1) {
          if (!(i + j < lst.length)) {
            break;
          }
          rep_elem += lst[i + j];
        }
      }
      else {
        continue;
      }
      lst[i] = rep_elem;
    }
  }

  public static void main(String[] args) {
    int[] a = {1, 2, -3, 4, 5, 4};
    int n = 3;
    windowPosSum(a, n);

    // Should print 4, 8, -3, 13, 9, 4
    System.out.println(java.util.Arrays.toString(a));
  }
}
