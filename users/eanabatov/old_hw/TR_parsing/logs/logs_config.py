import logging


def start_logs():
    logging.basicConfig(
        level=logging.INFO,
        filename="logs/eanabatov_web_parser.log",
        filemode="w",
        format="%(asctime)s %(levelname)s %(message)s",
    )
