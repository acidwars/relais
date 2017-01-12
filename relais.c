#include <stdio.h>
#include <string.h>
#include <wiringPi.h>

int main (int argc, char *argv[] )
{
       	wiringPiSetup () ;
	pinMode (25, OUTPUT) ;
	if (strcmp(argv[1], "off") && digitalRead(25) == HIGH) {
		digitalWrite(25, LOW);
	}
	else if (strcmp(argv[1], "on")  && digitalRead(25) == LOW) {
		digitalWrite(25, HIGH);
	}

	return 0;
}
