/**
 * Umpire Repl.it Utility Functions C++ Edition
 * ListNode functions are in here.
 *
 * Macarthur Inbody admin-contact@transcendental.us
 * License: CC0
 *
 *
 * Basically just copy the methods from this file into your repl to make it easier
 * to work with. The code is bad I know that but it works so it's better than nothing.
 */

#ifndef LISTNODE_UTILS_HXX
#define LISTNODE_UTILS_HXX
//this is here to make it easier to work with.
#include <iterator>

struct ListNode{
	int value;
	ListNode *next;
	ListNode(int val, ListNode *next=nullptr){
		this->value = val;
		this->next = next;
	}
};




/**
 * This function below lets you use any container type in C++ vector, array,List,Stack, Q etc.
 *
 * @tparam C The container object we're working with.
 * @tparam T The type that it is holding.
 * @param container The container we're passing to it to iterate over.
 * @return a ListNode list.
 */
template <typename C, typename T = typename C::value_type>
//super hacky version of this function but it basically works with any container object that holds an integer.
typename std::enable_if_t<std::is_same<T,int>::value, ListNode> *container_to_listnode(C const &container){
	ListNode *head=new ListNode(*container.begin());
	ListNode *cur = head;
	for(auto it = container.begin()+1;it != container.end(); ++it){
		cur->next = new ListNode(*it);
		cur = cur->next;
	}
	return head;
}

/**
 * Converts a ListNode into a vector for easier printing.
 * @param start The root/head node.
 * @param initial_size How large to make it's capacity at the start. As each time we hit it, we hae to resize O(n).
 * @return A vector of type int containing the items.
 */
 std::vector<int> listnode_to_vector(const ListNode *start,unsigned int initial_size=4){
	std::vector<int> res;
	res.reserve(initial_size);
	while(start != nullptr){
		res.push_back(start->value);
		start = start->next;
	}
	return res;
}

/**
 * Fully teomplated version is below here.
 *
 * This is only here to make it behave sorta more like Python with the std::vector<T> replacing the list object.
 */

//template <typename T> struct ListNode{
//	int value;
//	ListNode *next;
//	ListNode(T val,ListNode *next=nullptr){
//		this->value = val;
//		this->next = next;
//	}
//};

//template <typename C, typename T = typename C::value_type> typename std::enable_if_t<std::is_integral<T>::value, ListNode<T>> *container_to_listnode(C const &container){
//	ListNode *head=new ListNode<T>(*container.begin());
//	ListNode *cur = head;
//	for(auto it = container.begin()+1;it != container.end(); ++it){
//		cur->next = new ListNode<T>(*it);
//		cur = cur->next;
//	}
//	return head;
//}

//template <typename T>
//std::vector<T> listnode_to_vector(const ListNode<T> *head,unsigned int initial_size=4){
//	std::vector<T> res;
//	res.reserve(initial_size);
//	while(head != nullptr){
//		res.push_back(head->value);
//		head = head->next;
//	}
//	return res;
//}


//vector functions

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
}
#endif //LISTNODE_UTILS_HXX
