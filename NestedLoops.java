// staircase problem from hackerRank.

public class NestedLoops {
  public static void main(String[] args) {
    quadPattern(4);
    System.out.println("");
    stairCase(4);


  }

  public static void quadPattern(int n){
    // quadratic patterns
    for(int i = 0; i < n; i++){
      for(int j = 0; j < n; j++){
        System.out.print("*");
      }
      System.out.println("");
    }
  }

  public static void stairCase(int n){
    // staircase with #
    for(int i = 0; i < n; i++){
      for(int j = 0; j <= n; j++){
        System.out.print(i<n-j?" ":"#");
      }
      System.out.println("");
    }
  }
}
