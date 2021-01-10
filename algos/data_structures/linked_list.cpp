#include "linked_list.hxx"

int main(){
	int test[3]={1,2,3};
	LinkedList<int> list= LinkedList<int>(test,3);
	int test2[1] = {50};
	LinkedList<int> list2 = LinkedList<int>(test2,1);
	list.insert(1,0);
	list.display();
	list.insert(9,1);
	std::cout << "new list" << std::endl;
	list.display();

	std::cout << "item at 1" << std::endl;
	std::cout << list[1] << std::endl;
	std::cout << "last item" << std::endl;
	std::cout << list.pop() << std::endl;
	std::cout << "popped " << std::endl;
	list.push(10);
	list.display();
	std::cout << "reversed " << std::endl;
	list.reverse();
	list.display();
	std::cout << "shift " << std::endl;
	list.shift();
	list.display();
	list.push(10);
	list.pop();
	std::cout << "unshift of 999" << std::endl;
	list.unshift(999);
	list.display();
	std::cout << "concat " << std::endl;
	list+=list2;
	list.display();
	list.append(list2);
	list.display();
	list.remove(2);
	std::cout << std::endl;
	list.display();
	list.set(5,5);
	list.display();
}