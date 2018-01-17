/* as same as undirected graph */

public class DirectedDFS
{
  private boolean[] marked;                        //true if path from s

  public DirectedDFS(Digraph G, int s)            // constructor marks vertices reachable from s
  {
    marked = new boolean[G.V()];
    dfs(G, s);
  }

  private void dfs(Digraph G, int v)             // recursive DFS does the work
  {
    marked[v] = true;
    for (int w : G.adj(v))
      if(!marked[v])
        dfs(G, w);
  }

  public boolean visited(int v)                 // client can ask whether any vertex is reachable from s
  {
    return marked[v];
  }
}
