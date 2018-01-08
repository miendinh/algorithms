'''
Depth-first Search. Put unvisited vertices on a Stack
Bread-first search. Put unvisited vertices on a queue.
'''

public class DepthFirstPaths
{
  private boolean[] marked; //marked[v] = true if v connected to s
  private int[] edgeTo;  //edgeTo[v] -> previous vertex on path from s to v
  private int s;

  public DepthFirstPaths(Graph G, int s)
  {
    ...
    dfs(G, s);
  }

  private void dfs(Graph G, int v){
    marked[v] = true;
    for (int w : G.adj(v)) {
      if (!marked[w]){
        dfs(G, w);
        edgeTo[w] = v;
      }
    }
  }
}
