import logging
import os
from pyunpack import Archive
import tempfile
import urllib.request


from data import DATASETSDIR

def download_and_extract_dataset(url: str, dirname: str):
    """Downloads the dataset from a given url.

    Dataset is not downloaded if it already exists locally.
    """
    logger = logging.getLogger(__name__)
    if os.path.isdir(os.path.join(DATASETSDIR, dirname)):
        logger.info('Dataset exists, not downloading')
        return
    _, ext = os.path.splitext(url)
    logger.info('Downloading dataset...')
    filepath, _ = urllib.request.urlretrieve(url, tempfile.mktemp(ext))
    logger.info('Extracting dataset...')
    Archive(filepath).extractall(DATASETSDIR)
    os.remove(filepath)
