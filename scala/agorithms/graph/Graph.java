public class Graph {

  private final int V;
  private Bag<Integer>[] adj; //adjacency list ( using Bag data type )

  public Graph(int V) //create an empty graph with V vertices
  {
    this.V = V;
    adj = (Bag<Integer>[]) new Bag[V]; // create empty graph with V vertices
    for (int v = 0; v < V; v++)
      adj[v] = new Bag[Integer]();
  }
  public Graph(In in); //create a graph from input stream
  public void addEdge(int v, int w) //add an edge v-w
  {
    adj[v].add(w);
    adj[w].add(v);
  }
  public Interable<Integer> adj(int v)  //vertices adjacent to v
  {
    return adj[v];
  }
  int V(); //number of vertices
  int E(); //number of edges
}

/*
In in = new In(args[0])
Graph G = new Graph(in);

for(int v = 0; v < G.V(); v++){
  for (int w : G.adj(v))
    stdOut.println(v + "-" + w);
}
*/
