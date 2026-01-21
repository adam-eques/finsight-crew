"""Score a saved JSON report: python scripts/score_report.py brief.json"""

import json
import sys

from finsight.evaluation import completeness
from finsight.schemas import Report


def main(path: str) -> int:
    report = Report(**json.loads(open(path, encoding="utf-8").read()))
    print(f"completeness={completeness(report):.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
