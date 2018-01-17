public class DepthFirstSearchOrder {
	private boolean[] marked;
	private Stack<Integer> reversePost;

	public DepthFirstSearchOrder(Digraph G)
	{
		reversePost = new Stack<Integer>();
		marked = new boolean[G.V()];
		for (int v = 0; v < G.V(); v ++)
			if (!marked[v]) dfs(G, V);
	}

	private void dfs(Digraph G, int v)
	{
		marked[v] = true;
		for(int w : G.adj(v))
			if(!marked[w]) dfs(G, w);
		reversePost.push(v);
	}

	public Iterable<Integer> reversePost()
	{
		return reversePost;
	}
}