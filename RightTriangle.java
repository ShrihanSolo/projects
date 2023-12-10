public class RightTriangle {
  public static void main(String[] args) {
    int count = 0;
    while (count < 100) {
      int stars = count;
      while (stars > 0) {
        System.out.print("*");
        stars -= 1;
      }
      System.out.println("");
      count += 1;
    }
  }
}
