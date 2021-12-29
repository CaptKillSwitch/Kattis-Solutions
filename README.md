# Kattis-Solutions
10 Kinds of People
https://open.kattis.com/problems/10kindsofpeople


Problem disc:
The world is made up of 10 kinds of people, those who understand binary and those who do not. These different kinds of people do not always get along so well. Bob might ask for a 10000 ounce coffee (meaning binary) and Alice might make misinterpret his request as being in decimal and give him a 10011100010000 ounce coffee (binary). After Sue explains that this much coffee costs 100 dollars (decimal), Bob might assume he only has to pay 4 dollars (interpreting the price as being in binary). In response to these differences that are difficult to resolve, these two groups have divided the world into two regions, the binary-friendly zones and the decimal-friendly zones. They have even published a map like the following to help people keep up with where the areas are (they have used ones and zeros so nobody would have trouble reading it).

1111100000
1111000000
1110000011
0111100111
0011111111
Users of binary have to stay in the zones marked with a zero. Users of decimal have to stay in the zones marked with a one. You have to figure out if it is possible for either type of person to get between various locations of interest. People can move north, south, east or west, but cannot move diagonally.

Solution:
Flood fill the input matrix
Flood fill: https://en.wikipedia.org/wiki/Flood_fill

Check if the given points are in the same "color"

Author: Capt_KillSwitch.
