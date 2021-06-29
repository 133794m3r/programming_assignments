/*
* Created by macarthur on 6/26/21.
* Copyright (c) 2021 
*/
#include <vector>
#include <iostream>
#include "../utils/listnode_utils.hxx"
int main(){
	std::vector<int> test = {1,2,3};
	ListNode *head = container_to_listnode(test);
	ListNode *cur = head;
	while(head != nullptr){
		std::cout << head->value << std::endl;
		head=head->next;
	}
	std::vector<int> res = listnode_to_vector(cur);
	return 0;
}
