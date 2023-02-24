import pytest
from tictactoe import game

@pytest.mark.parametrize("move_input, expected_win", [
    pytest.param([(0,0,0)], None, id="horizontal_no_win-1"),
    pytest.param([(0,0,0), (0,2,0)], None, id="horizontal_no_win-2"),
    pytest.param([(0,0,0), (0,1,0), (0,2,0)], 0, id="horizontal_win"),

    pytest.param([(0,0,0)], None, id="vertical_no_win-1"),
    pytest.param([(0,0,0), (2,0,0)], None, id="vertical_no_win-2"),
    pytest.param([(0,0,0), (1,0,0), (2,0,0)], 0, id="vertical_win"),
])
def test_winner_k_eq_n(move_input, expected_win):
    board = game.Board(3)

    for row, col, player in move_input:
        board.make_move(row, col, player)

    assert board.winner() == expected_win


@pytest.mark.parametrize("move_input, expected_win", [
    pytest.param([(0,0,0)], None, id="horizontal_no_win-1"),
    pytest.param([(0,0,0), (0,2,0)], None, id="horizontal_no_win-2"),
    pytest.param([(0,0,0), (0,1,0)], 0, id="horizontal_win-1"),
    pytest.param([(0,0,0), (0,1,0), (0,2,0)], 0, id="horizontal_win-2"),

    pytest.param([(0,0,0)], None, id="vertical_no_win-1"),
    pytest.param([(0,0,0), (2,0,0)], None, id="vertical_no_win-2"),
    pytest.param([(0,0,0), (1,0,0)], 0, id="vertical_win-1"),
    pytest.param([(0,0,0), (1,0,0), (2,0,0)], 0, id="vertical_win-2"),

])
def test_winner_k_lt_n(move_input, expected_win):
    board = game.Board(3, k=2)

    for row, col, player in move_input:
        board.make_move(row, col, player)

    assert board.winner() == expected_win

