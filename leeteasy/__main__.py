import time as clock
from datetime import datetime

import click
import schedule

from leeteasy.services.request_handler import RequestHandler
from leeteasy.services.request_parser import RequestParser


@click.command()
@click.argument('time')
def main(time) -> None:
    """Schedule notification at TIME."""
    _validate_time(time)
    schedule.every().day.at(time).do(schedule_notification)
    while True:
        schedule.run_pending()
        clock.sleep(1)


def schedule_notification():

    challenge_info = RequestHandler.get_challenge_info()
    test_challenge = RequestParser.parse(challenge_info)
    print(test_challenge)


def _validate_time(time: str):
    """Validates the given string is in valid time format."""
    time_format = '%H:%M'
    try:
        return datetime.strptime(time, time_format).time()
    except ValueError:
        click.echo('Invalid time format')


if __name__ == '__main__':
    main()
