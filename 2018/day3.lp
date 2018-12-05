#include "input/day3_input.lp".

dim(0..1000).

contains(ID, X, Y) :-
    dim(X), dim(Y),
    claim(ID, X1, Y1, W, H),
    X >= X1, X < X1 + W,
    Y >= Y1, Y < Y1 + H.

part_1(A) :-
    A = #count{X, Y : contains(ID1, X, Y), contains(ID2, X, Y), ID1 != ID2}.

part_2(ID1) :-
    claim(ID1, X1, Y1, W, H),
    #count{X, Y : contains(ID1, X, Y), contains(ID2, X, Y), ID1 != ID2} == 0.

#show part_1/1.
#show part_2/1.
