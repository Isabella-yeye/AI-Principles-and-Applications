% ==========================================
% Tic-Tac-Toe Minimax (Starter)
% Board: list of 9 cells, each x/o/e
% Max player: x
% Min player: o
% ==========================================

:- dynamic(expanded/1).

% ---------- instrumentation ----------
clear_count :- retractall(expanded(_)), assertz(expanded(0)).
inc_count   :- retract(expanded(N)), N1 is N+1, assertz(expanded(N1)).
get_count(N):- expanded(N).

% ---------- helpers ----------
other(x,o).
other(o,x).

% pretty print (optional)
print_board([A,B,C,D,E,F,G,H,I]) :-
    format("~w ~w ~w~n~w ~w ~w~n~w ~w ~w~n", [A,B,C,D,E,F,G,H,I]).

% ---------- winning lines ----------
line(1,2,3). line(4,5,6). line(7,8,9).
line(1,4,7). line(2,5,8). line(3,6,9).
line(1,5,9). line(3,5,7).

% win(+Board, +Player)
win(Board, P) :-
    line(I,J,K),
    nth1(I,Board,P),
    nth1(J,Board,P),
    nth1(K,Board,P).

% full(+Board)
full(Board) :- \+ member(e, Board).

% ---------- TODO A1: move/3 ----------
% move(Board, Player, NextBoard) holds if NextBoard results from placing Player in an empty cell.
move(Board, _Player, _NextBoard) :-
    % pick an empty cell
    member(e, Board),

    % place Player there, i.e. split Board into Front and Back, with e in between, then replace e with Player
    append(Front, [e|Back], Board),

    % create NextBoard by replacing e with Player
    append(Front, [Player|Back], NextBoard).

% ---------- TODO A2: terminal/1 and utility/2 ----------
terminal(_Board) :-
    % Terminal if x wins, o wins, or board is full (draw); uses win and full to check conditions
    win(_Board, x);
    win(_Board, o);
    full(_Board).

utility(Board, U) :-
    % TODO: U=1 if x wins, -1 if o wins, 0 if draw
    win(Board, x),
    U = 1.

utility(Board, U) :-
    % if challenger o wins
    win(Board, o),
    U = -1.

utility(Board, U) :-
    % if x and o didnt win set to tie
    \+ win(Board, x),
    \+ win(Board, o),
    U = 0.

% ---------- minimax ----------
% minimax_value(+Board, +Player, -Value)
minimax_value(Board, Player, Value) :-
    inc_count,
    ( terminal(Board) ->
        utility(Board, Value)
    ; Player == x ->
        % Max node: take maximum over children
        findall(V,
                ( move(Board, Player, B2),
                  other(Player, P2),
                  minimax_value(B2, P2, V)
                ),
                Vs),
        max_list(Vs, Value)
    ; % Min node: take minimum over children
        findall(V,
                ( move(Board, Player, B2),
                  other(Player, P2),
                  minimax_value(B2, P2, V)
                ),
                Vs),
        min_list(Vs, Value)
    ).

% ---------- TODO A4: best_move/4 ----------
% choose successor with best minimax value for Player

%  generate all moves from board state
best_move(Board, Player, BestBoard, BestValue) :-
    clear_count,
    %get all moves and isolate first
    findall(B2, move(Board, Player, B2), Moves),
    Moves = [First|Rest],
    
    other(Player, P2),
    %get min max value of first board
    minimax_value(First, P2, FirstValue),
    best_move_comp(Player, Rest, First, FirstValue, BestBoard, BestValue).

% base case for if there are no other moves
best_move_comp(_, [], BestBoard, BestValue, BestBoard, BestValue).

% evalutate the next move, keeping the better board
best_move_comp(Player, [Next|Rest], CurBoard, CurValue, BestBoard, BestValue) :-
    other(Player, P2),
    minimax_value(Next, P2, NextValue),
    %choose the better board and recurse
    better(Player, Next, NextValue, CurBoard, CurValue, BetterBoard, BetterValue),
    best_move_comp(Player, Rest, BetterBoard, BetterValue, BestBoard, BestValue).

% X keeps the higher max value
better(x, B1, V1, _,  V2, B1, V1) :- V1 >= V2, !.
better(x, _,  _,  B2, V2, B2, V2) :- !.

% O keeps the lower min value
better(o, B1, V1, _,  V2, B1, V1) :- V1 =< V2, !.
better(o, _,  _,  B2, V2, B2, V2) :- !.
