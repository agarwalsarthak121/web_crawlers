//Assuming all the values to be greater than or equal to 1

import java.util.ArrayList;
import java.util.List;

public class ArrayToIndex {
	
	public static void main (String[] args) {
		int[] arr = new int[]{3,2,1};
		List<Node> rootNodes = new ArrayList<>();
		List<Node> currParents = new ArrayList<>();
		
		for(int i=0;i<arr.length;i++)
		{
			List<Node> forThisLoop = new ArrayList<>();
		    	for(int j=0;j<arr[i];j++)
		    	{
				if(currParents.size()==0)
				{
					    Node iter = new Node(j);
					    rootNodes.add(iter);
					    forThisLoop.add(iter);
				}
				else
				{
				    for(int k=0;k<currParents.size();k++)
				    {
					Node parent = currParents.get(k);
					Node iter = new Node(j);
					parent.children.add(iter);
					forThisLoop.add(iter);
				    }
				}
		    	}
		    	currParents.clear();
		    	currParents.addAll(forThisLoop);
		}
		
		List<String> indexes = new ArrayList<>();
		String str = "";
		printIndexes(rootNodes,str,indexes);
		
		for(int i=0;i<indexes.size();i++)
		{
			System.out.println(indexes.get(i));
		}
	}
	
	public static void printIndexes(List<Node> nodes,String str,List<String> indexes)
	{
		for(int i=0;i<nodes.size();i++)
		{
			Node obj = nodes.get(i);
			if(obj.children.size()==0)
			{
				indexes.add(str+obj.value);
			}
			else
				printIndexes(obj.children,str+obj.value,indexes);
		}
	}
}


class Node {
    public int value;
    public List<Node> children = new ArrayList<>();
    
    public Node(int value)
    {
        this.value = value;
    }
}
