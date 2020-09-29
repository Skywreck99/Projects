#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include "clock.h"

/*
int set_tod_from_secs(int time_of_day_sec, tod_t *tod) {
// Accepts time of day in seconds as an argument and modifies the
// struct pointed at by tod to fill in its hours, minutes,
// etc. fields.  If time_of_day_sec is invalid (negative or larger
// than the number of seconds in a day) does nothing to tod and
// returns 1 to indicate an error. Otherwise returns 0 to indicate
// success. This function DOES NOT modify any global variables
//
// CONSTRAINT: Uses only integer operations. No floating point
// operations are used as the target machine does not have a FPU.
//
// CONSTRAINT: Limit the complexity of code as much as possible. Do
// not use deeply nested conditional structures. Seek to make the code
// as short, and simple as possible. Code longer than 40 lines may be
// penalized for complexity.

  if (time_of_day_sec < 0) {
    return 1;
  } else if (time_of_day_sec > 86400) {
    return 1;
  } else {

    // Checks whether the time is in AM or PM then assign the right hour
    if (time_of_day_sec > 43199) {
        if ((time_of_day_sec / 3600) % 12 == 0) tod->hours = 12; else tod->hours = (time_of_day_sec / 3600) - 12;
        tod->ispm = 1;
    } else {
      if (time_of_day_sec / 3600 == 0) tod->hours = 12; else tod->hours = time_of_day_sec / 3600;
      tod->ispm = 0;
    }

    // Get the right minutes and seconds of the clock
    tod->minutes = (time_of_day_sec % 3600) / 60;
    tod->seconds = (time_of_day_sec % 3600) % 60;
    return 0;
  }
}
*/
/*
int set_display_bits_from_tod(tod_t tod, int *display) {
// Accepts a tod and alters the bits in the int pointed at by display
// to reflect how the clock should appear. If any fields of tod are
// negative or too large (e.g. bigger than 12 for hours, bigger than
// 59 for min/sec), no change is made to display and 1 is returned to
// indicate an error. Otherwise returns 0 to indicate success. This
// function DOES NOT modify any global variables
//
// May make use of an array of bit masks corresponding to the pattern
// for each digit of the clock to make the task easier.
//
// CONSTRAINT: Limit the complexity of code as much as possible. Do
// not use deeply nested conditional structures. Seek to make the code
// as short, and simple as possible. Code longer than 85 lines may be
// penalized for complexity.

  if ((tod.hours & (0b1 << 31)) || (tod.minutes & (0b1 << 31)) || (tod.seconds & (0b1 << 31)) || (tod.ispm & (0b1 << 31))) {
    return 1;
  } else if (tod.hours > 12 || tod.minutes > 59 || tod.seconds > 59) {
    return 1;
  } else {

    // assign every digit of the clock to their corresponding variables for future display
    int masks[11] = {0b0111111, 0b0000110, 0b1011011, 0b1001111, 0b1100110, 0b1101101, 0b1111101, 0b0000111, 0b1111111, 0b1101111, 0b0000000};
    int min_ones =  tod.minutes % 10;
    int min_tens = tod.minutes / 10;
    int hour_ones = tod.hours % 10;
    int hour_tens = tod.hours / 10;

    // Shifts the binary equivalence of the numbers to match the given/current clock
    *display = masks[min_ones];
    *display = (masks[min_tens] << 7) | *display;
    *display = (masks[hour_ones] << 14) | *display;

    // Checks if the tens digit of the hour is 0 or 1. If it is 0, then don't display anything
    if (tod.hours / 10 == 0) *display = masks[10] << 21 | *display; else *display = (masks[hour_tens] << 21) | *display;

    // CHecks whether the time is in AM or PM using bits
    if (tod.ispm) *display = (0b10 << 28) | *display; else *display = (0b01 << 28) | *display;
    return 0;
  }
}
*/
/*
int clock_update() {
// Examines the TIME_OF_DAY_SEC global variable to determine hour,
// minute, and am/pm.  Sets the global variable CLOCK_DISPLAY_PORT bits
// to show the proper time.  If TIME_OF_DAY_SEC appears to be in error
// (to large/small) makes no change to CLOCK_DISPLAY_PORT and returns 1
// to indicate an error. Otherwise returns 0 to indicate success.
//
// Makes use of the set_tod_from_secs() and
// set_display_bits_from_tod() functions.
//
// CONSTRAINT: Does not allocate any heap memory as malloc() is NOT
// available on the target microcontroller.  Uses stack and global
// memory only.
  tod_t tod;
  int result = set_tod_from_secs(TIME_OF_DAY_SEC, &tod);

  // Checks if the time is non-negative or valid
  if (result) {
    return 1;
  } else {
    // When valid, display the clock by copying all the bits formed to CLOCK_DISPLAY_PORT for actual display
    result = set_display_bits_from_tod(tod, &CLOCK_DISPLAY_PORT);
    if (result) {
      return 1;
    }
    return 0;
  }
}
*/
