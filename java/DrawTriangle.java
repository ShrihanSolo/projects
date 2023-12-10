public class DrawTriangle {
  public static void drawTriangle(int N) {
    int count = 1;
    while (count < N + 1) {
      int stars = count;
      while (stars > 0) {
        System.out.print("*");
        stars -= 1;
      }
      System.out.println("");
      count += 1;
    }
  }
  public static void main(String[] args) {
    drawTriangle(69);
  }
}
