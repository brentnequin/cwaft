import os

import logging


logger = logging.getLogger(__name__)


def find_files_by_name(
    file_name: str,
    starting_at: str = r'/'
):
    for path, _, files in os.walk(starting_at):
        for filename in files:
            if filename == file_name:
                f = os.path.join(path, filename)
                logger.debug(f)
                yield f


def main():

    file_name_to_find = '00000000o00.xd'
    output_file_name = 'output.txt'
    find_starting_at = r'/'

    logger.info(f'Searching for files with name {file_name_to_find} starting at {find_starting_at}.')

    with open(output_file_name, 'w') as output_file:
        for f in find_files_by_name(file_name_to_find, find_starting_at):
            output_file.write(str(f) + os.linesep)

    logger.info(f'Results written to {output_file_name}')
    logger.info('Done.')


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    main()
