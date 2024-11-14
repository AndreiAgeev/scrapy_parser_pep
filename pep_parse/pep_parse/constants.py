from pathlib import Path

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
RESULT_DIR = x = Path(__file__).parent.parent / 'results'
FEED_URI = f'file:///{RESULT_DIR / "pep_%(time)s.csv"}'
