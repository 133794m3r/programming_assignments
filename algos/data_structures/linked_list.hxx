#ifndef PROG_ASSIGNMENT_LINKEDLIST_HXX
#define PROG_ASSIGNMENT_LINKEDLIST_HXX
#include <vector>
#include <iostream>


template<typename T> class LinkedList {
  private:
	struct Node{
		T data;
		Node *next=nullptr;
		explicit Node(T val, Node *n=nullptr){
			data = val;
			next = n;
		}
	};

	Node *head_;
	long long length_;
	Node *tail_;
  public:

	LinkedList(){
		head_= nullptr;
		tail_ = nullptr;
		length_ = 0;
	}

	LinkedList(T *A, unsigned long long n) {
		head_ = new Node(A[0]);
		tail_ = head_;
		length_ = 1;
		Node *tmp, *last=head_;
		for (unsigned long long i = 1; i < n; i++) {
			tmp = new Node(A[i]);
			last->next = tmp;
			last = tmp;
		}
		tail_ = last;
		length_ = n;

	}

	LinkedList(std::vector<T> &A) {

		head_ = new Node(A[0]);
		Node *t, *last;
		length_ = A.size();
		for (unsigned long long i = 1; i < length_; i++) {
			t = new Node(A[i]);
			last->next = t;
			last = t;
		}
		tail_ = last;
	}

	Node *get(long long idx){
		if(idx <0 || idx >= length_){
			return nullptr;
		}
		Node *current = head_;
		long long i=0;
		while(i != idx){
			current = current->next;
			i++;
		}
		return current;
	}
	void set(T val,long long idx){
		Node *p = get(idx);
		p->data = val;
	}

	//to let them get a specific element in a normal way.
	//won't let them set the value here because that's too complex to do.
	T operator[](long long idx){
		Node *tmp = this->get(idx);
		return tmp->data;
	}

	void insert(T val,long long idx){
		if(idx > length_ || idx < 0){
			return;
		}
		if(head_ == nullptr){
			head_ = new Node(val);
			tail_ = head_;
		}
		else if(idx == 0){
			auto *t = new Node(val,head_);
			head_ = t;
		}
		else{
			Node *prev = get(idx-1);
			auto *p = new Node(val, prev->next);
			prev->next = p;

		}
		length_++;

	}

	void push(T val){
		if(!head_){
			head_->data = val;
			tail_ = head_;
		}
		else{
			Node *p = new Node(val);
			tail_->next=p;
			tail_ = p;
		}
		length_++;
	}

	void shift(){
		if(!head_){
			return;
		}
		Node *cur_head = head_;
		head_ = cur_head->next;
		delete cur_head;
		length_--;
		if(length_ == 0){
			tail_ = nullptr;
		}
	}

	void unshift(T val){
		if(!head_){
			head_ = new Node(val);
			tail_ = head_;
		}
		head_ = new Node(val, head_);
		length_++;
	}

	void remove(long long idx){
		if(idx <0 || idx > length_){
			return;
		}
		if(idx == length_ - 1){
			pop();
		}
		if(idx == 0){
			shift();
		}
		else{
			Node *prev = get(idx-1);
			Node *remove = nullptr;
			remove = prev->next;
			prev->next = remove->next;
			delete(remove);
		}
		length_--;
	}

	T pop(){
		if(head_ == nullptr){
			return -1;
		}
		Node *prev = get(length_-2);
		T pop_val = tail_->data;
		tail_=prev;
		delete(prev->next);
		tail_->next= nullptr;
		length_--;
		return pop_val;
	}

	void display() const{
		Node *p = head_;
		unsigned int i=1;
		std::cout << "length: " << length_ << " ";
		std::cout << "[";
		while (p) {
			std::cout << p->data;
			if(i++ < length_){
				std::cout << ", ";
			}
			p = p->next;
		}
		std::cout << "]" << std::endl;
	}

	void reverse(){
		Node *prev=nullptr, *next=nullptr, *cur;
		cur = head_;
		head_ = tail_;
		tail_ = cur;

		while(cur != nullptr){
			next = cur->next;
			cur->next = prev;
			prev = cur;
			cur = next;
		}
	}

	void append(LinkedList<T> &_list){
		Node* temp = _list.head_;
		while (temp != nullptr) {
			push(temp->data);
			temp = temp->next;
		}
	}

	LinkedList<T> operator+(const LinkedList<T> &second_list) const{
		LinkedList<T> *ret = this;
		Node *tmp = second_list.head_;
		while(tmp != nullptr){
			ret->push(tmp->data);
			tmp=tmp->next;
		}
		return &ret;
	}
	LinkedList<T>& operator+=(const LinkedList<T>& _list) {

		Node* temp = _list.head_;

		while (temp != nullptr) {
			push(temp->data);
			temp = temp->next;
		}

		return *this;

	}
	~LinkedList(){
		Node* current = head_;
		Node* next=nullptr;
		while (current != NULL) {
			next = current->next;
			delete(current);
			current = next;
		}
		length_ = 0;
		head_=tail_=nullptr;
	}

};


#endif //PROG_ASSIGNMENT_LINKEDLIST_HXX
