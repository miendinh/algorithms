//1. Subsystem
class PointCartesian {
	private double x, y;
	public PointCartesian(double x, double y) {
		this.x = x;
		this.y = y;
	}

	public void move(int x, int y) {
		this.x += x;
		this.y += y;
	}

	public String toString() {
		return "(" + x + "," + y + ")";
	}

	public double getX() {
		return x;
	}

	public double getY() {
		return y;
	}
}

//1. Subsystem
class PointPolar {
	private double radius, angle;

	public PointPolar(double radius, double angle) {
		this.radius = radius;
		this.angle = angle;
	}

	public void rotate(int angle) {
		this.angle += angle % 360;
	}

	public voi toString() {
		return "[" + radius + "@" + angle + "]";
	}
}

// 1. Desired interface: move(), rotate()
class Point {
	// 2. Design a "wrapper" class
	private PointCartesian poinCartesian;

	public Point(double x, double y) {
		poinCartesian = new PointCartesian(x, y);
	}

	public String toString() {
		return poinCartesian.toString();
	}

	//4. Wrapper maps
	public void move(int x, int y) {
		poinCartesian.move(x, y);
	}

	public void rotate(int angle, Point o) {
		double x = poinCartesian.getX() - o.poinCartesian.getX();
		double y = poinCartesian.getY() - o.poinCartesian.getY();
		
	}
}