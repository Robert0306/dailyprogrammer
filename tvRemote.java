// count clicks on a remote.

public class tvRemote{


  public static void main(String[] args) {
    tvRemote("b");

  }

  public static int tvRemote(String word) {
    // making the keyboard with 2d arrays.
    String[][] keyboard = {
      {"a", "b", "c", "d", "e", "1", "2", "3"},
      {"f", "g", "h", "i", "j", "4", "5", "6"},
      {"k", "l", "m", "n", "o", "7", "8", "9"},
      {"p", "q", "r", "s", "t", ".", "@", "0"},
      {"u", "v", "w", "x", "y", "z", "_", "/"},
    };

    int count = 0;
    for(int row = 0; row < keyboard.length; row++){
      count++;
      if(word.charAt())
      for(int col = 0; col < keyboard[row].length; col++){

        //System.out.println(keyboard[row][col]);
      }
    }
    return 1;
  }

} // end class
