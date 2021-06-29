/*
* This is just the test driver file.
*/
#include <vector>
#include <iostream>
#include "../utils/treenode_utils.hxx"
int main() {
	std::vector<int> test = {1, 2, 3, 4, 5};

	TreeNode *root2 = null;
	root2 = container_to_treenode(test,root2,0);
	std::vector<int> res = bt_to_vector(root2);
	for(auto it:res){
		std::cout << it << std::endl;
	}
	return 0;
}

