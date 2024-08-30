import os
import pytest
import re
import time

from urllib.parse import unquote, urlparse
from pathlib import Path

from sbis.pages.main import SbisMainPage

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

def parse_download_link_text(text = ""):
    pattern = re.compile(
        r"""\s*(?P<action>\w+)          # whitespaces, action
        \s*\(                           # whitespaces, open parenthesis
        \s*(?P<fileformat>\w+)          # whitespaces, file format
        \s*(?P<filesize>\d+(?:\.\d+)?)  # whitespaces, file size
        \s*(?P<sizeunit>\w+)            # whitespaces, size unit
        \s*\)""", re.VERBOSE            # whitespaces, close parenthesis
    )

    result = re.search(pattern, text)

    return (result.group('action'), result.group('fileformat'), 
        result.group('filesize'), result.group('sizeunit'))


def wait_for(condition, timeout = 30, poll = 3, logger = None):
    start_time = time.time()

    result = False
    while not (result := condition()) and ((time.time() - start_time) < timeout):
        if logger is not None:
            logger.info(f"Waiting for condition"
                " {str(time.time() - start_time)}, result is {result}")

        time.sleep(poll)

    return result
 
@pytest.mark.parametrize('size, size_unit, expected',
    [
        (pow(1024, 1), "kb", round(1, 2)),
        (pow(1024, 2), "mb", round(1, 2)),
        (pow(1024, 3), "gb", round(1, 2)),
        (11684504, "мб", 11.14),
    ]
)
def test_get_size_in_units(size, size_unit, expected):
    result = get_size_in_units(size, size_unit)

    assert result == expected

@pytest.mark.parametrize('text, expected',
    [
        ("Скачать (exe 1.14 мб)", ('Скачать', 'exe', '1.14', 'мб')),
        ("download (msi 2 gb)", ('download', 'msi', '2', 'gb')),
    ]
)
def test_regex(text, expected):
    result = parse_download_link_text(text)

    assert result == expected

def test_scenario_3(driver, tmp_path_download):
    sbis_main = SbisMainPage(driver).navigate()

    sbis_download = sbis_main.go_to_download_local_versions()

    sbis_download.switch_left_tab(tab_name="СБИС Плагин")
    sbis_download.switch_right_tab(tab_name="Windows")

    link = sbis_download.download_plugins_web_installer_for_windows()

    file_path = get_downloaded_file_path(link.get_attribute('href'),
        tmp_path_download)

    file_downloaded = wait_for(
        lambda: file_path.exists(), timeout=30, logger=sbis_download.logger,
    )

    assert file_downloaded

    link_file_size, size_unit = parse_download_link_text(link.text)[-2:]
    file_size = get_file_size(file_path, size_unit)

    assert file_size == float(link_file_size)
