#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	uint64_t x,y,z;
	x = 0;
	y = 0;
	z = 0;
	uint8_t w[14] = {1,3,5,7,9,2,4,6,8,9,9,9,9,9};

   int arg1 = atoi(argv[1]);
   uint8_t w0 = arg1;

//for (uint8_t w0 = 1; w0 <= 9; w0++)
{
 for (uint8_t w1 = 1; w1 <= 9; w1++) {
  for (uint8_t w2 = 1; w2 <= 9; w2++) {
   for (uint8_t w3 = 1; w3 <= 9; w3++) {
    for (uint8_t w4 = 1; w4 <= 9; w4++) {
     for (uint8_t w5 = 1; w5 <= 9; w5++) {
      for (uint8_t w6 = 1; w6 <= 9; w6++) {
       for (uint8_t w7 = 1; w7 <= 9; w7++) {
        for (uint8_t w8 = 1; w8 <= 9; w8++) {
         for (uint8_t w9 = 1; w9 <= 9; w9++) {
          for (uint8_t w10 = 1; w10 <= 9; w10++) {
           for (uint8_t w11 = 1; w11 <= 9; w11++) {
            for (uint8_t w12 = 1; w12 <= 9; w12++) {
             for (uint8_t w13 = 1; w13 <= 9; w13++) {
               w[0] = w0;
               w[1] = w1;
               w[2] = w2;
               w[3] = w3;
               w[4] = w4;
               w[5] = w5;
               w[6] = w6;
               w[7] = w7;
               w[8] = w8;
               w[9] = w9;
               w[10] = w10;
               w[11] = w11;
               w[12] = w12;
               w[13] = w13;

	// # inp w;
	x = 0;
	x = x + z;
	x = x % 26;
	z = z / 1;
	x = x + 12;
	x = (int)(x == w[1-1]);
	x = (int)(x == 0);
	y = 0;
	y = y + 25;
	y = y * x;
	y = y + 1;
	z = z * y;
	y = 0;
	y = y + w[1-1];
	y = y + 4;
	y = y * x;
	z = z + y;

	// # inp w;
	x = 0;
	x = x + z;
	x = x % 26;
	z = z / 1;
	x = x + 11;
	x = (int)(x == w[2-1]);
	x = (int)(x == 0);
	y = 0;
	y = y + 25;
	y = y * x;
	y = y + 1;
	z = z * y;
	y = 0;
	y = y + w[2-1];
	y = y + 10;
	y = y * x;
	z = z + y;

	// # inp w;
	x = 0;
	x = x + z;
	x = x % 26;
	z = z / 1;
	x = x + 14;
	x = (int)(x == w[3-1]);
	x = (int)(x == 0);
	y = 0;
	y = y + 25;
	y = y * x;
	y = y + 1;
	z = z * y;
	y = 0;
	y = y + w[3-1];
	y = y + 12;
	y = y * x;
	z = z + y;

	// # inp w;
	x = 0;
	x = x + z;
	x = x % 26;
	z = z / 26;
	x = x + -6;
	x = (int)(x == w[4-1]);
	x = (int)(x == 0);
	y = 0;
	y = y + 25;
	y = y * x;
	y = y + 1;
	z = z * y;
	y = 0;
	y = y + w[4-1];
	y = y + 14;
	y = y * x;
	z = z + y;

	// # inp w;
	x = 0;
	x = x + z;
	x = x % 26;
	z = z / 1;
	x = x + 15;
	x = (int)(x == w[5-1]);
	x = (int)(x == 0);
	y = 0;
	y = y + 25;
	y = y * x;
	y = y + 1;
	z = z * y;
	y = 0;
	y = y + w[5-1];
	y = y + 6;
	y = y * x;
	z = z + y;

	// # inp w;
	x = 0;
	x = x + z;
	x = x % 26;
	z = z / 1;
	x = x + 12;
	x = (int)(x == w[6-1]);
	x = (int)(x == 0);
	y = 0;
	y = y + 25;
	y = y * x;
	y = y + 1;
	z = z * y;
	y = 0;
	y = y + w[6-1];
	y = y + 16;
	y = y * x;
	z = z + y;

	// # inp w;
	x = 0;
	x = x + z;
	x = x % 26;
	z = z / 26;
	x = x + -9;
	x = (int)(x == w[7-1]);
	x = (int)(x == 0);
	y = 0;
	y = y + 25;
	y = y * x;
	y = y + 1;
	z = z * y;
	y = 0;
	y = y + w[7-1];
	y = y + 1;
	y = y * x;
	z = z + y;

	// # inp w;
	x = 0;
	x = x + z;
	x = x % 26;
	z = z / 1;
	x = x + 14;
	x = (int)(x == w[8-1]);
	x = (int)(x == 0);
	y = 0;
	y = y + 25;
	y = y * x;
	y = y + 1;
	z = z * y;
	y = 0;
	y = y + w[8-1];
	y = y + 7;
	y = y * x;
	z = z + y;

	// # inp w;
	x = 0;
	x = x + z;
	x = x % 26;
	z = z / 1;
	x = x + 14;
	x = (int)(x == w[9-1]);
	x = (int)(x == 0);
	y = 0;
	y = y + 25;
	y = y * x;
	y = y + 1;
	z = z * y;
	y = 0;
	y = y + w[9-1];
	y = y + 8;
	y = y * x;
	z = z + y;

	// # inp w;
	x = 0;
	x = x + z;
	x = x % 26;
	z = z / 26;
	x = x + -5;
	x = (int)(x == w[10-1]);
	x = (int)(x == 0);
	y = 0;
	y = y + 25;
	y = y * x;
	y = y + 1;
	z = z * y;
	y = 0;
	y = y + w[10-1];
	y = y + 11;
	y = y * x;
	z = z + y;

	// # inp w;
	x = 0;
	x = x + z;
	x = x % 26;
	z = z / 26;
	x = x + -9;
	x = (int)(x == w[11-1]);
	x = (int)(x == 0);
	y = 0;
	y = y + 25;
	y = y * x;
	y = y + 1;
	z = z * y;
	y = 0;
	y = y + w[11-1];
	y = y + 8;
	y = y * x;
	z = z + y;

	// # inp w;
	x = 0;
	x = x + z;
	x = x % 26;
	z = z / 26;
	x = x + -5;
	x = (int)(x == w[12-1]);
	x = (int)(x == 0);
	y = 0;
	y = y + 25;
	y = y * x;
	y = y + 1;
	z = z * y;
	y = 0;
	y = y + w[12-1];
	y = y + 3;
	y = y * x;
	z = z + y;

	// # inp w;
	x = 0;
	x = x + z;
	x = x % 26;
	z = z / 26;
	x = x + -2;
	x = (int)(x == w[13-1]);
	x = (int)(x == 0);
	y = 0;
	y = y + 25;
	y = y * x;
	y = y + 1;
	z = z * y;
	y = 0;
	y = y + w[13-1];
	y = y + 1;
	y = y * x;
	z = z + y;

	// # inp w;
	x = 0;
	x = x + z;
	x = x % 26;
	z = z / 26;
	x = x + -7;
	x = (int)(x == w[14-1]);
	x = (int)(x == 0);
	y = 0;
	y = y + 25;
	y = y * x;
	y = y + 1;
	z = z * y;
	y = 0;
	y = y + w[14-1];
	y = y + 8;
	y = y * x;
	z = z + y;
	if (z == 0)
	{
		for (int i = 0; i < 14; i++)
		{
			printf("%u", w[i]);
		}
		printf(" -> %llu", z);		
		printf("\n");
	}
}}}}}}}}}}}}}}

}
