# gtranspose

usage:

`./gtranspose file offset`

offset is in frets e.g. -12 to shift a note at fret 12 to fret 0.

it's smart enough to recognize when a fret needs to go to the string below, but not much more than that.

outputs to STDOUT

this program makes a lot of assumptions on the input format.  see example .txt file (from https://tabs.ultimate-guitar.com/tab/misc-computer-games/nyan-cat-theme-tabs-1060116)
this program assumes the tab is in standard tuning
