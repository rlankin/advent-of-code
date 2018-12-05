claim(1, 1, 3, 4, 4).
claim(2, 3, 1, 4, 4).
claim(3, 5, 5, 2, 2).
claim(4, 6, 4, 2, 2).

overlap(ID1, ID2) :-
    claim(ID1, X1, Y1, W1, H1),
    claim(ID2, X2, Y2, W2, H2),
    ID1 != ID2,
    X1 + W1 > X2,
    X1 < X2 + W2,
    Y1 + H1 > Y2,
    Y1 < Y2 + H2.

overlap_x(ID1, ID2, |X1 - X2|) :-
    claim(ID1, X1, Y1, W1, H1),
    claim(ID2, X2, Y2, W2, H2),
    overlap(ID1, ID2),
    ID1 < ID2.

overlap_y(ID1, ID2, |Y1 - Y2|) :-
    claim(ID1, X1, Y1, W1, H1),
    claim(ID2, X2, Y2, W2, H2),
    overlap(ID1, ID2),
    ID1 < ID2.

overlap_area(ID1, ID2, X * Y) :-
    claim(ID1, X1, Y1, W1, H1),
    claim(ID2, X2, Y2, W2, H2),
    overlap_x(ID1, ID2, X),
    overlap_y(ID1, ID2, Y).

overlap_area(A) :-
    A = #sum{O : overlap_area(ID1, ID2, O)}.

%#show overlap/2.
%#show overlap_x/3.
%#show overlap_y/3.
#show overlap_area/3.
#show overlap_area/1.
