//1. Define the interface of the algorithm
interface Strategy {
  void solve();
}

//2. Bury implementation
@SuppressWarnings("ALL")
abstract class StrategySolution implements Strategy {
  //3. Template Method
  public void solve() {
    start();
    while (nextTry() && !isSolution()) {}
    stop();
  }

  abstract void start();
  abstract boolean nextTry();
  abstract boolean isSolution();
  abstract void stop();
}

class FOO extends StrategySolution {
  private int state = 1;

  protected void start() {
    System.out.print("Start ");
  }

  protected void stop() {
    System.out.print("Stop");
  }

  protected boolean nextTry() {
    System.out.print("nextTry-" + state++ + " ");
  }

  protected boolean isSolution() {
    System.out.print("isSolution-" + (state == 3) + " ");
  }
}

// 2. Bury implementation
abstract class StrategySearch implements Strategy {
  //3. Template Method
  public void solve() {
    while (true) {
      preProcess();
      if (search()) {
        break;
      }
      postProcess();
    }
  }

  abstract void preProcess();
  abstract boolean search();
  abstract void postProcess();
}

@SuppressWarnings("ALL")
class BAR extends StrageSearch {
  private int state = 1;

  protected void preProcess() {
    System.out.print("PreProcess ");
  }

  protected void postProcess() {
    System.out.print("Post Process()");
  }

  protected boolean search() {
    System.out.print("Search-" + state++ + " ");
    return state == 3 ? true : false;
  }
}

//4. Clients couple strictly to the interface
public class StrageDemo {
    //client code here
    private static void execute(Strategy strategy) {
      strategy.solve();
    }

    public static void main(String[] args) {
      Strategy[] algorithms = { new FOO(), new BAR() };
      for (Strategy algorithm : algorithms) {
        execute(algorithm);
      }
    }
}

/*
Output

start  nextTry-1  isSolution-false  nextTry-2  isSolution-true  stop
preProcess  search-1  postProcess  preProcess  search-2

*/
