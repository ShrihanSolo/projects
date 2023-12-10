public class SumElements {
  public static int listSum(int[] lst) {
    int i = 0;
    int tot = 0;
    while (i < lst.length) {
      tot+= lst[i];
      i += 1;
    }
    return tot;
  }
  public static int forSum(int[] lst) {
    int sum = 0;
    for (int i = 0; i < lst.length; i += 1) {
      sum += lst[i];
    }
    return sum;
  }
  public static void main(String[] args) {
    int[] lol = new int[]{1, 3, 4, 5, 6, 7, 23, 4, 5};
    System.out.println(forSum(lol));
  }
}
