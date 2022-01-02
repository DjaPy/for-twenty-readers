from pathlib import Path

from starlette.templating import Jinja2Templates

BASE_DIR = Path(__file__).parent
OUT_FILE = BASE_DIR.parent / 'graph_of_reading_of_the_psalter.xlsx'
TEMPLATES_DIR = str(BASE_DIR / 'entrypoints' / 'templates')
TEMPLATE = Jinja2Templates(directory=TEMPLATES_DIR)
