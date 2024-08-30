namespace Assignment2;


public class Node<T>
{
	public T value;
	public List<Node<T>> children = new List<Node<T>>();
	public Node(T value)
	{
		this.value = value;
	}

	public void AddChild(Node<T> item)
	{
		children.Add(item);
	}
	
	public void AddChildren(List<Node<T>> items)
	{
		foreach (Node<T> item in items)
		{
			children.Add(item);
		}
	}

	public override string ToString()
	{
		return $"Node of value: {value}";
	}
	
	public static Node<int>? BFS(Node<int> start, int target)
	{
		Queue<Node<int>> BFS_Q = new Queue<Node<int>>();
		BFS_Q.Enqueue(start);
		int step = 1;
		while (BFS_Q.Count > 0)
		{
			Node<int> current = BFS_Q.Dequeue();
			Console.WriteLine($"Step {step}: Dequeued {current.value}");
			step++;
			if (current.value == target)
			{
				//exit if found
				return current;
			}

			foreach (Node<int> child in current.children)
			{
				BFS_Q.Enqueue(child);
			}
		}
		return null;
	}

	public static Node<int>? DFS(Node<int> start, int target)
	{
		Stack<Node<int>> DFS_Stack = new Stack<Node<int>>();
        List<Node<int>> visited = new List<Node<int>>();

        DFS_Stack.Push(start);

        int step = 1;

        while (DFS_Stack.Count > 0)
		{

            //Console.WriteLine("Current Stack:");
            //foreach (Node<int> node in DFS_Stack)
            //{
             //   Console.WriteLine("  Stack: " + node.value);
            //}

            Node<int> current = DFS_Stack.Pop();

            if (visited.Contains(current))
            {
				continue;
            }

			visited.Add(current);

            if (current.value == target)
            {
                return current;
            }

            for (int i = current.children.Count - 1; i >= 0; i--)
            {
                if (!visited.Contains(current.children[i]))
                {
                    DFS_Stack.Push(current.children[i]);
                }
            }

            Console.WriteLine($"Step {step}: Popped {current.value}");
			step++;
           

        }

		return null;
	}
}