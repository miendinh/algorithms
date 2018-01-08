/*
API:

public class Paths
             Paths(Graph G, int S) // find paths in G from source S
  boolean    hasPathTo(int v)     // is there a path from s to v ?
  Interable<Integer> pathTo(int v) // path from s to v: null if no such path

Example:
Paths paths = new Paths(G, s);
for(int v = 0; v < G.V(); v ++) {
  if (paths.hastPathTo(v))
    StdOut.println(v); // print all vertices connected to s
}

public boolean hasPathTo(int v) {
  return marked[v];
}

public Iterable<Integer> pathTo(int v) {
  if (!hasPathTo(v)) return null;
  Stack<Integer> path = new Stack<Integer>();
  for (int x = v; x != s; x = edgeTo[x])
    path.push(x);
  path.push(s);
  return path;
}
*/
