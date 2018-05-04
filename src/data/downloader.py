import logging
import os
from pyunpack import Archive
import urllib.request
import tempfile

from data import DATASETSDIR

logger = logging.getLogger(__name__)

def download_and_extract_linnaeus(url: str, dirname: str):
    """If needed"""
    if os.path.isdir(os.path.join(DATASETSDIR, dirname)):
        logger.info('Dataset exists, not downloading')
        return
    _, ext = os.path.splitext(url)
    logger.info('Downloading dataset...')
    filepath, _ = urllib.request.urlretrieve(url, tempfile.mktemp(ext))
    logger.info('Extracting dataset...')
    Archive(filepath).extractall(DATASETSDIR)
    os.remove(filepath)
