/* This Flag was all about getting the number of bits in 
* as few characters as possible. The correction solution
* had 34 non-whitespace characters. Of which I was able to go was 35.
* I'm assuming this counts ";" I know there's more to get but I don't know
* where else to squeeze chars from.
*/
function bitCount(n){c=0;while(n) n&1?c++:0,n>>=1;return c}
