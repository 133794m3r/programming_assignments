/**
 * Umpire Repl.it Utility Functions Java Edition
 * TreeNode functions are in here.
 *
 * Macarthur Inbody admin-contact@transcendental.us
 * License: CC0
 *
 * Basically just copy the methods from this file into your repl to make it easier
 * to work with. The code is bad I know that but it works so it's better than nothing.
 */

//you'll have to include these 2 methods in your imports.
import java.util.ArrayDeque;
import java.util.Deque;
//this isn't needed unless you want to use an ArrayList sort of like Python's list class.
import java.util.ArrayList;
//this is only used for the main method here but if you just copy the methods you won't need it.
import java.util.Arrays;


public class TreeNodeUtils {
	public static class TreeNode{
		int val;
		TreeNode left = null;
		TreeNode right = null;
		TreeNode(){}
		TreeNode(int val){ this.val = val;}
	}
	public static void insertNode(TreeNode node, Integer key){
		if(node == null){
			node = new TreeNode(key);
			return;
		}
		Deque<TreeNode> q = new ArrayDeque<TreeNode>();
		q.add(node);
		while(!q.isEmpty()){
			node = q.removeFirst();
			if(node.left == null){
				node.left = new TreeNode(key);
				break;
			}
			else
				q.add(node.left);
			if(node.right == null){
				node.right = new TreeNode(key);
				break;
			}
			else
				q.add(node.right);
		}
	}

	public static TreeNode arrayToTreeNode(Integer[] arr){
		if(arr.length == 0)
			return null;
		TreeNode root = new TreeNode(arr[0]);
		for(int i=1;i<arr.length;i++){
			if(arr[i] != null){
				insertNode(root,arr[i]);
			}
		}
		return root;
	}

	public static Integer[] treeNodeToArray(TreeNode root,Integer len){
		Deque<TreeNode> q = new ArrayDeque<>();
		q.add(root);
		Integer[] data = new Integer[len];
		int i = 0;
		while(!q.isEmpty()){
			TreeNode cur = q.removeFirst();
			data[i++] = cur.val;
			if(cur.left != null)
				q.add(cur.left);
			if(cur.right != null)
				q.add(cur.right);

		}
		return data;
	}

	public static ArrayList<Integer> treeNodeToArrayList(TreeNode root){
		Deque<TreeNode> q = new ArrayDeque<>();
		q.add(root);
		ArrayList<Integer> data = new ArrayList<Integer>();
		while(!q.isEmpty()){
			TreeNode cur = q.removeFirst();
			data.add(cur.val);
			if(cur.left != null)
				q.add(cur.left);
			if(cur.right != null)
				q.add(cur.right);
		}
		return data;
	}
	public static void main(String args[]){
		Integer arr[] = {1,2,3,4,5,6};
		TreeNode t = arrayToTreeNode(arr);
		Integer out[] = treeNodeToArray(t,arr.length);
		ArrayList<Integer> out2 = treeNodeToArrayList(t);

		System.out.println(Arrays.toString(arr));
		System.out.println(Arrays.toString(out));
		System.out.println(out2);
	}
}
