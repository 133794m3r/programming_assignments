#include <stddef.h>

size_t countBits(unsigned value){
//set the one bits at the front. It doesn't say the size but it looks like it's just an int.
  unsigned int one_bits=0;
  //thus we only do the 32 bits of the value.
  for(int i=0;i<32;i++){
    //check if there's a one in this place.
    if (value & (1 << i)){
    //if so increment it by one.
      one_bits++;
    }
  }
  //return the number we got.
  return one_bits;
}
