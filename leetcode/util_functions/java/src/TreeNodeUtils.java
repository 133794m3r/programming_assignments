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
		Integer val;
		TreeNode left = null;
		TreeNode right = null;
		TreeNode(){}
		TreeNode(Integer val){ this.val = val;}
	}
	public static void insertNode(TreeNode node, Integer key){
		if(node == null){
			node = new TreeNode(key);
			return;
		}
		Deque<TreeNode> q = new ArrayDeque<>();
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
			
		int arr_len = arr.length;
		class x_ {
			TreeNode _rec_insert(TreeNode root, Integer i) {
				if(i < arr_len){
					root = new TreeNode(arr[i]);
					int l = (i << 1) + 1;
					root.left = _rec_insert(root.left, l);
					root.right = _rec_insert(root.right, l + 1);
				}
				return root;
			}
		}
		TreeNode root = null;
		root = new x_()._rec_insert(root,0);
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
		ArrayList<Integer> data = new ArrayList<>();
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
	public static void main(String[] args){
		Integer[] arr = {1,2,2,3,3,null,null,4,4};//{1,2,3,4,5,6};
		TreeNode t = arrayToTreeNode(arr);
		Integer[] out = treeNodeToArray(t,arr.length);
		ArrayList<Integer> out2 = treeNodeToArrayList(t);

		System.out.println(Arrays.toString(arr));
		System.out.println(Arrays.toString(out));
		System.out.println(out2);
	}
}
