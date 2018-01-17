/* API

public class Digraph
             Digraph(int V)        // Create an empty digraph with V vẻtices
             Digraph(In in)        // Cretae a digraph from input stream
      void   addEdge(int v, int w) // add a directed edge v -> w
  Iterable<Integer> adj(int v)     // vertices pointing from v
            int V()                // number of vertices
            int E()                // number of edges
      Digraph Reverse()            // reverse of this digraph
      String toString()            // string representation


      In in = new In(args[0]);
      Digraph G = new Digraph(in);            //read digraph from input stream

      for (int v = 0; v < G.V(); v ++){      //print out each edge(once)
        for(int w : G.adj(v))
          Stdout.println(v + '->' + w);
      }

*/

public class Digraph
{
    private final int V;
    private final Bag<Integer>[] adj;                 // adjacency lists

    public Digraph(int V)
    {
      this.V = V;                                    // create empty digraph with V vertices
      adj = (Bag<Integer>[]) new Bag[V];
      for (int v = 0; v < V; v ++)
        adj[v] = new Bag<Integer>();
    }

    public void addEdge(int v, int w)                 // add edge v -> w
    {
      adj[v].add(w);
    }

    public Iterable<Integer> adj(int v)
    {
      return adj[v];
    }

}
