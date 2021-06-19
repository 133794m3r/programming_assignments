/**
 * Umpire Repl.it Utility Functions Java Edition
 * ListNode functions are in here.
 *
 * Macarthur Inbody admin-contact@transcendental.us
 * License: CC0
 *
 *
 * Basically just copy the methods from this file into your repl to make it easier
 * to work with. The code is bad I know that but it works so it's better than nothing.
 */


//ArrayList is imported to allow you to have a dynamically allocated array. Otherwise it's no needed.
import java.util.ArrayList;
import java.util.Arrays;
public class ListNodeUtils {
	public static class ListNode {
		int val;
		ListNode next=null;
		ListNode() {}
		ListNode(int val){this.val = val;}
		ListNode(int val, ListNode next) { this.val = val;this.next = next;}
	}

	/**
	 * @param array The input array we're working with.
	 * @return a ListNode linked list.
	 */
	public static ListNode arrayToListNode(int[] array) {
		if (array.length == 0) {
			return null;
		}

		ListNode head = new ListNode(array[0]);
		ListNode cur = head;
		for (int i = 1; i < array.length; i++) {
			cur.next = new ListNode(array[i]);
			cur = cur.next;
		}
		return head;
	}

	/**
	 * Converts a ListNode to an array
	 *
	 * @param root The root node.
	 * @param len  the length of the list.
	 * @return an integer array
	 */
	public static int[] listNodeToArray(ListNode root, int len) {
		int[] arr = new int[len];
		int i = 0;
		while (root != null) {
			arr[i++] = root.val;
			root = root.next;
		}
		return arr;
	}

	/**
	 * @param root The root node.
	 * @return An ArrayList of all of the node's values.
	 */
	public static ArrayList<Integer> listNodeToArrayList(ListNode root) {
		ArrayList<Integer> list = new ArrayList<Integer>(2);
		while (root != null) {
			list.add(root.val);
			root = root.next;
		}
		return list;
	}

	/**
	 * Here just to test things.
	 *
	 * @param args Not used.
	 */
	public static void main(String[] args) {
		int[] arr = {1, 2, 3, 4, 5};
		ListNode head = arrayToListNode(arr);
		int[] out = listNodeToArray(head, arr.length);
		System.out.print(Arrays.toString(out));
	}


}
