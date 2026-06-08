from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_too_high_hint_says_go_lower():
    # Regression for the high/low bug: a too-high guess must tell the
    # player to go LOWER, not HIGHER.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_too_low_hint_says_go_higher():
    # Regression for the high/low bug: a too-low guess must tell the
    # player to go HIGHER, not LOWER.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message


def test_same_guess_is_consistent():
    # Regression for the oscillation glitch: the caller used to flip the
    # secret to a string on every other attempt, which forced check_guess
    # into a string comparison and made the same guess alternate between
    # "Too High" and "Too Low". With proper int inputs the result must be
    # stable no matter how many times the same guess is checked.
    results = {check_guess(100, 57) for _ in range(5)}
    assert results == {("Too High", "📉 Go LOWER!")}
