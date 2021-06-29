/**
 * Umpire Repl.it Utility Functions C++ Edition
 * TreeNode functions are in here.
 *
 * Macarthur Inbody admin-contact@transcendental.us
 * License: CC0
 *
 *
 * Basically just copy the methods from this file into your repl to make it easier
 * to work with. The code is bad I know that but it works so it's better than nothing.
 */


#ifndef TREENODE_UTILS_HXX
#define TREENODE_UTILS_HXX
#include <iterator>
#include <queue>

struct TreeNode{
	int val;
	TreeNode *left = nullptr;
	TreeNode *right = nullptr;
	TreeNode(int value){
		this->val = value;
	}
};


template <typename C, typename T = typename C::value_type>
//super hacky version of this function but it basically works with any container object that holds an integer.
typename std::enable_if_t<std::is_same<T,int>::value, TreeNode> *container_to_treenode(C const &container, TreeNode *root,size_t i){
	if(i < container.size()){
		root = new TreeNode(container[i]);
		root->left = container_to_treenode(container,root->left,(i<<1)+1);
		root->right = container_to_treenode(container,root->right,(i<<1)+2);
	}
	return root;
}

std::vector<int> bt_to_vector(TreeNode *root){
	std::queue<TreeNode *> q;
	q.push(root);
	std::vector<int> out;
	while(!q.empty()){
		TreeNode *cur = q.front();
		q.pop();
		if(cur != nullptr){
			out.push_back(cur->val);
			if(cur->left)
				q.push(cur->left);
			if(cur->right)
				q.push(cur->right);
		}
	}
	return out;
}

//vector functions. Make sure to not include this again if you're already using the ListNode utility stuff.

/**
 * Lets you send the contents of a vector to any ostream. Like std::cout << some_vector << std::endl
 */
template <class T,class Allocator> std::ostream& operator<<(std::ostream& os, const std::vector<T,Allocator> &m){
	size_t m_size=m.size();
	os << "[";
	for(size_t i=0; i < m.size(); i++) {
		os << m[i]  <<(i == m_size - 1 ? "" : ",");
	}
	os << "]" << std::endl;
	return os;
}

/**
 * Same as before but this time lets you read in a list of values from std::in and put them into a vector.
 */
template <class T,class Allocator> std::istream& operator>>(std::istream& is, std::vector<T,Allocator> &m){
	size_t n=m.size();
	for(size_t i=0;i<n;i++){
		is >> m[i];
	}
	return is;
#endif //TREENODE_UTILS_HXX
