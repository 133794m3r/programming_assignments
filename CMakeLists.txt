cmake_minimum_required(VERSION 3.18)
project(prog_assignment)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_C_STANDARD  C99)

if(MSVC)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /std:c++11 /W4")
	set(CMAKE_CXX_FLAGS_RELEASE "{CMAKE_CXX_FLAGS_RELEASE} /O2")
else()
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wpedantic")
	#make sure all optimizations are disabled during debug so that I can easily see all variables/values.
	set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS} -O0 -g3 ")
	set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS} -O2")

	if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")
		set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -stdlib=libc++")
	else()
		set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
	endif()
endif()

add_executable(sort_tests
		algos/sorting/sort_algos.hxx
		algos/sorting/sort_tests.cpp)

add_executable(linked_list
		data_structures/linked_list/d_linked_list.hxx
		data_structures/linked_list/linked_list.hxx
		data_structures/linked_list/linked_list.cpp )

add_executable(queue_test
		data_structures/queue/queue.hxx
		data_structures/queue/queue.cpp)

add_executable(stack_test
		data_structures/stack/stack.hxx
		data_structures/stack/stack.cpp)

add_executable(bst
data_structures/binary_search_tree/bst.cpp data_structures/binary_search_tree/bst.hxx)
