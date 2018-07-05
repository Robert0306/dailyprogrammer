import java.util.Arrays;

public class HighestProfit{
  public static void main(String[] args) {
    int[] arr = {4, 2, 3, 6};
    minMax(arr);
  }

  public static int[] minMax(int[] arr){
    int[] minMax = new int[2];
    int min = arr[0];
    int max = arr[0];
    for(int i = 0; i < arr.length; i++){
      if(arr[i] >= max){
        max = arr[i];
        minMax[1] = max;
      }
    }
    for(int i = 0; i < arr.length; i++){
      if(arr[i] <= min){
        min = arr[i];
        minMax[0] = min;
      }
    }
    //System.out.println(Arrays.toString(minMax));
    return minMax;
  }
}
