abstract class Observer {
  protected Subject subject;
  public abstract void update();
}

class Subject {
  private List<Observer> observers = new ArrayList<>();
  private int state;

  public void add(Observer o) {
    observers.add(o);
  }

  public int getState() {
    return state;
  }

  public void setState(int value) {
    this.state = value;
    execute();
  }

  private void execute() {
    for (Observer observer : observer) {
      observer.update();
    }
  }
}

class HexObserver extends Observer {
  public HexObserver(Subject subject) {
    this.subject = subject;
    this.subject.add(this);
  }

  public void update() {
    System.out.println(" " + Integer.toHexString(subject.getState()));
  }
}

class OctObserver extends Observer {
  public OctObserver(Subject subject) {
    this.subject = subject;
    this.subject.add(this);
  }

  public void update(){
    System.out.print(" " + Integer.toOctalString(subject.getState()));
  }
}

class BinObserver extends Observer {
  public BinObserver(Subject subject) {
    this.subject = subject;
    this.subject.add(this);
  }

  public void update() {
    System.out.println(" " + Integer.toBinaryString(subject.getState()));
  }
}

public class ObserverDemo {
  public static void main(String[] args) {
    Subject sub = new Subject();

    new HexObserver(sub);
    new OctObserver(sub);
    new BinObserver(sub);

    Scanner scan = new Scanner(System.in);

    for (int i = 0; i < 5; i ++) {
      System.out.println("\nEnter a number");
      sub.setState(scan.nextInt());
    }

  }
}

/*
Enter a number: 55
 37 67 110111
Enter a number: 12
 c 14 1100
Enter a number: -10
 fffffff6 37777777766 11111111111111111111111111110110
Enter a number: 112
 70 160 1110000
Enter a number: 5
 5 5 101
*/
