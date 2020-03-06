#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int calculate_damage(const char *yt, const char *ot, int attack, int defense) {
    float modifier=0.5;
    if(! strcmp(yt,"fire")){
      if(! strcmp(ot,"water"))
        modifier = 0.5;
      
      else if(! strcmp(ot,"grass"))
        modifier = 2;
      
      else if(! strcmp(ot,"electric"))
        modifier=1;
      
    }
    else if(!strcmp(yt,"water") ){
      if(!strcmp(ot,"grass"))
        modifier = 0.5;
      
      else if(!strcmp(ot,"fire"))
        modifier = 2;
      
      else if(!strcmp(ot,"electric"))
        modifier=0.5;
      
    }
    else if(!strcmp(yt,"grass")){
      if(!strcmp(ot,"fire"))
        modifier = 0.5;
      
      else if(!strcmp(ot,"water"))
        modifier = 2;
      
      else if(!strcmp(ot,"electric"))
        modifier=1;
      
    }
    else if(!strcmp(yt,"electric")){
      if(!strcmp(ot,"water"))
        modifier = 2;
      
      else if(!strcmp(ot,"electric"))
        modifier=0.5;
      
      else
        modifier=1;
    
    }
  return ceil(50 * (float)(attack/defense) * modifier);
}
