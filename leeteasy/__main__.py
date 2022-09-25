import time as clock

import click
import schedule

from leeteasy.services.notification_service import Notifier
from leeteasy.utils.validatiors import TimeValidator

# check every 10 min
sleep_duration = 10 * 60


@click.command()
@click.option(
    '-d',
    '--difficulty',
    type=click.Choice(['Medium', 'Hard'], case_sensitive=False),
    help='Additional problem difficulty for notification.'
)
@click.argument('time')
def main(time, difficulty) -> None:
    """
    Schedule notification at given TIME [24hrs].

    Example: leeteasy 13:15
    """
    TimeValidator.validate(time)
    Notifier.target_difficulty.append(difficulty)
    schedule.every().day.at(time).do(Notifier.notify)

    while True:
        schedule.run_pending()
        clock.sleep(sleep_duration)


if __name__ == '__main__':
    main()
