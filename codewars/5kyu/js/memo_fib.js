#!/usr/bin/envnode
var fibonacci=function(n){
	var cache={}
	function f(n){
		if(n in cache){
			return cache[n];
		}
		else{
			if(n<2)
			return n
		if(cache[n-2]===undefined)
			cache[n-2]=f(n-2)
		if(cache[n-1]===undefined)	
			cache[n-1]=f(n-1);
		return cache[n-2]+cache[n-1];
		}
	}
	return f(n);
}
