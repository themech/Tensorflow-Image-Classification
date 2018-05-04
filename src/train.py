import argparse
import logging
import os

from data import DATASETSDIR
from data.downloader import download_and_extract_linnaeus

def main():
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset-url', type=str, help='dataset download address',
                        default='http://chaladze.com/l5/img/Linnaeus%205%2064X64.rar')
    parser.add_argument('--dataset-dirname', type=str, help='"datasets" subdirectory name',
                        default='Linnaeus 5 64X64')
    parser.add_argument('--image-size', type=int, help='width and height of images (in pixels)',
                        default=64)
    args = parser.parse_args()

    if not os.path.isdir(DATASETSDIR):
        os.mkdir(DATASETSDIR)

    download_and_extract_linnaeus(url=args.dataset_url,
                                  dirname=args.dataset_dirname)

if __name__ == '__main__':
  main()
