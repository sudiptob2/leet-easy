import time as clock

import click
import schedule

from leeteasy.services.notification_service import Notifier
from leeteasy.utils.validatiors import TimeValidator

# check every 10 min
sleep_duration = 10 * 60


@click.command()
@click.argument('time')
def main(time) -> None:
    """
    Schedule notification at given TIME.

    Args:
        time: 24 hours time, ex: 13:20

    Raises:
        SystemExit: When an invalid time is given.
    """
    TimeValidator.validate(time)
    schedule.every().day.at(time).do(Notifier.notify)

    while True:
        schedule.run_pending()
        clock.sleep(sleep_duration)


if __name__ == '__main__':
    main()
