import pytest
from tictactoe import game

@pytest.mark.parametrize("move_input, expected_win", [
    pytest.param([(0,0,0)], None, id="horizontal_no_win-1"),
    pytest.param([(0,0,0), (0,1,0)], None, id="horizontal_no_win-2"),
    pytest.param([(0,0,0), (0,1,0), (0,2,0)], 0, id="horizontal_win"),

    pytest.param([(0,0,0), (1,0,0)], None, id="vertical_no_win-2"),
    pytest.param([(0,0,0), (1,0,0), (2,0,0)], 0, id="vertical_win"),

    pytest.param([(0,0,0), (1,1,0)], None, id="asc_diagonal_no_win-2"),
    pytest.param([(0,0,0), (1,1,0), (2,2,0)], 0, id="asc_diagonal_win"),
])
def test_winner_k_eq_n(move_input, expected_win):
    board = game.Board(3)

    for row, col, player in move_input:
        board.make_move(row, col, player)

    assert board.winner() == expected_win


@pytest.mark.parametrize("move_input, expected_win", [
    pytest.param([(0,0,0)], None, id="single_no_win"),

    pytest.param([(0,0,0), (0,2,0)], None, id="horizontal_no_win"),
    pytest.param([(0,0,0), (0,1,0)], 0, id="horizontal_win-1"),
    pytest.param([(0,1,0), (0,0,0)], 0, id="horizontal_win-2"),
    pytest.param([(0,0,0), (0,2,0), (0,1,0)], 0, id="horizontal_win-3"),
    pytest.param([(1,0,0), (1,1,0)], 0, id="horizontal_win-4"),

    pytest.param([(0,0,0), (2,0,0)], None, id="vertical_no_win"),
    pytest.param([(0,0,0), (1,0,0)], 0, id="vertical_win-1"),
    pytest.param([(1,0,0), (0,0,0)], 0, id="vertical_win-2"),
    pytest.param([(0,0,0), (2,0,0), (1,0,0)], 0, id="vertical_win-3"),
    pytest.param([(0,1,0), (1,1,0)], 0, id="vertical_win-4"),

    pytest.param([(0,0,0), (2,2,0)], None, id="desc_diagonal_no_win"),
    pytest.param([(0,0,0), (1,1,0)], 0, id="desc_diagonal_win-1"),
    pytest.param([(1,1,0), (0,0,0)], 0, id="desc_diagonal_win-2"),
    pytest.param([(0,0,0), (2,2,0), (1,1,0)], 0, id="desc_diagonal_win-3"),
    pytest.param([(1,0,0), (2,1,0)], 0, id="desc_diagonal_win-4"),

    pytest.param([(2,0,0), (0,2,0)], None, id="asc_diagonal_no_win"),
    pytest.param([(2,0,0), (1,1,0)], 0, id="asc_diagonal_win-1"),
    pytest.param([(1,1,0), (2,0,0)], 0, id="asc_diagonal_win-2"),
    pytest.param([(2,0,0), (0,2,0), (1,1,0)], 0, id="asc_diagonal_win-3"),
    pytest.param([(1,0,0), (0,1,0)], 0, id="asc_diagonal_win-3"),
    # add non center start

])
def test_winner_k_lt_n(move_input, expected_win):
    board = game.Board(3, k=2)

    for row, col, player in move_input:
        board.make_move(row, col, player)

    assert board.winner() == expected_win

