import os
import time as clock
from datetime import datetime
from sys import platform

import click
import schedule

from leeteasy.constant import Constant
from leeteasy.services.notification_service import Notifier
from leeteasy.utils.validatiors import TimeValidator


@click.command('start')
@click.option(
    '-d',
    '--difficulty',
    type=click.Choice(['Medium', 'Hard'], case_sensitive=False),
    help='Additional problem difficulty for notification.',
)
@click.option(
    '--sleep_duration',
    default=Constant.DEFAULT_SLEEP,
    type=click.IntRange(1, Constant.DEFAULT_SLEEP, clamp=True),
    help='Sleep duration in seconds.',
)
@click.argument('time')
def execute_start(time, difficulty, sleep_duration) -> None:
    """
    Schedule notification at given TIME [24hrs].

    Example: leeteasy 13:15
    """
    valid_time = TimeValidator.validate(time)
    Notifier.target_difficulty.append(difficulty)

    if datetime.now().time() > valid_time:
        Notifier.notify()

    schedule.every().day.at(time).do(Notifier.notify)

    while True:  # NOQA: WPS457
        schedule.run_pending()
        clock.sleep(sleep_duration)


@click.command('stop')
def execute_stop() -> None:
    """Stop leeteasy process."""
    os.system('pkill -9 -f leeteasy')


@click.group('leeteasy')
def execute_root():
    """Group child command."""


execute_root.add_command(execute_start)
execute_root.add_command(execute_stop)

if __name__ == '__main__':
    if platform != 'win32':
        import pwd  # NOQA: WPS433

        bus_addr = 'unix:path=/run/user/{0}/bus'.format(
            pwd.getpwuid(os.getuid()).pw_uid,
        )

        os.environ['DBUS_SESSION_BUS_ADDRESS'] = bus_addr
    execute_root()
