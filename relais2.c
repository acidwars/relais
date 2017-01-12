#include <wiringPi.h>
#include <stdio.h>

int main (void )
{
       	wiringPiSetup () ;
	pinMode (25, OUTPUT) ;

	if ( digitalRead(25) == HIGH) {
		digitalWrite(25, LOW);
	}
	else if ( digitalRead(25) == LOW) {
		digitalWrite(25, HIGH);
	}

	return 0;
}
