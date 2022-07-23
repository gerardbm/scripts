/* Montecarlo method to calculate a Pi approximation  */
/* -------------------------------------------------- */
/* Name    : Pi approximation with Montecarlo         */
/* Version : 1.0.0                                    */
/* License : MIT                                      */
/* Author  : Gerard Bajona                            */
/* Created : 22/07/2022                               */
/* URL     : http://github.com/gerardbm/scripts       */
/* -------------------------------------------------- */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int main(void)
{
	int i,j,h;
	double x,y,d,pi;
	void srand48(long);
	double drand48(void);

	srand48(time(NULL));

	j=0;
	h=10000;
	for (i=1; i<=h; i++) {
		x=drand48();
		y=drand48();

		d=sqrt((x-0.5)*(x-0.5)+(y-0.5)*(y-0.5));
		if (d<0.5) {
			j++;
		}
	}

	pi=(j/(h*1.0))/(0.5*0.5);
	printf("%d of %d points\n",j,h);
	printf("Pi approximation: %f\n",pi);
	return 0;
}
