from finsight import cli


def test_unknown_returns_error(monkeypatch):
    class NS:
        command = "bogus"

    monkeypatch.setattr(cli, "build_parser", lambda: _P(NS()))
    assert cli.main([]) == 1


class _P:
    def __init__(self, ns):
        self._ns = ns

    def parse_args(self, argv):
        return self._ns
