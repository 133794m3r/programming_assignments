/*
* Can I be considered as a JavaScript Novice Now?
* AKA Closure Madness
* By Macarthur Inbody
*/
function zero(op){ return (!op)?0:op(0);}
function one(op){ return (!op)?1:op(1);}
function two(op){ return (!op)?2:op(2);}
function three(op){ return (!op)?3:op(3);}
function four(op){ return (!op)?4:op(4);}
function five(op){ return (!op)?5:op(5);}
function six(op){ return (!op)?6:op(6);}
function seven(op){ return (!op)?7:op(7);}
function eight(op){ return (!op)?8:op(8);}
function nine(op){ return (!op)?9:op(9);}

function plus(x){ return function(y){return y+x;};}
function minus(x){ return function(y){return y-x;};}
function times(x){ return function(y){return y*x;};}
function divided_by(x){return function(y){return y / x | 0;};}
function bitwise_and(x){ return function(y){return x&y;};}
function bitwise_or(x){ return function(y){return x|y;};}
function bitwise_xor(x){ return function(y){return x^y;};}
function bitwise_shiftl(x){ return function(y){ x << y;};}
function bitwise_shiftr(x){ return function(y){ x >> y;};}

console.log(zero(plus(one())));
console.log(four(times(seven())));
console.log(nine(divided_by(two())));
console.log(three(minus(four())));
console.log(eight(bitwise_and(two())));
console.log(nine(bitwise_or(one())));
console.log(four(bitwise_xor(nine())));
