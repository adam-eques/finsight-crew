from finsight.tools.sentiment import score


def test_positive():
    assert score("record growth and strong profit") > 0


def test_negative():
    assert score("lawsuit and downgrade amid decline") < 0


def test_neutral():
    assert score("the company held a meeting") == 0.0


def test_negation_flips():
    from finsight.tools.sentiment import score_with_negation
    assert score_with_negation("not strong") < 0
    assert score_with_negation("no lawsuit") > 0
