
from urllib.parse import unquote, urlparse
from pathlib import Path

def get_size_in_units(size, size_unit):
    n = 0
    u = size_unit.lower()
    match u:
        case 'кб'|'kb':
            n = 1    
        case 'мб'|'mb':
            n = 2
        case 'гб'|'gb':
            n = 3
        case _:
            raise Exception("Specified size unit is not supported")
            
    return round((size / pow(1024, n)), 2)

def get_downloaded_file_path(url, download_dir):
    url_parsed = urlparse(url)
    url_path = Path(url_parsed.path)

    return Path(download_dir, unquote(url_path.name))

def get_file_size(file_path, size_unit):
    if not file_path.is_file():
        raise Exception(f"File {file_path} not found")

    size = file_path.stat().st_size

    return get_size_in_units(size, size_unit)
