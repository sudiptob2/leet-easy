import os
import time as clock
from sys import platform

import click
import schedule

from leeteasy.services.notification_service import Notifier
from leeteasy.utils.validatiors import TimeValidator


@click.command('start')
@click.option(
    '-d',
    '--difficulty',
    type=click.Choice(['Medium', 'Hard'], case_sensitive=False),
    help='Additional problem difficulty for notification.'
)
@click.option(
    "--sleep_duration",
    default=3600,
    type=click.IntRange(1, 3600, clamp=True),
    help='Sleep duration in seconds.'
)
@click.argument('time')
def execute_start(time, difficulty, sleep_duration) -> None:
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


@click.command('stop')
def execute_stop() -> None:
    """Stops leeteasy process"""
    os.system('pkill -9 -f leeteasy')


@click.group('leeteasy')
def execute_root():
    """v0.4.0 | supported version strings: 0.7.2"""
    pass


execute_root.add_command(execute_start)
execute_root.add_command(execute_stop)

if __name__ == '__main__':
    if platform != 'win32':
        import pwd

        os.environ[
            'DBUS_SESSION_BUS_ADDRESS'] = f'unix:path=/run/user/{pwd.getpwuid(os.getuid()).pw_uid}/bus'  # NOQA: E501
    execute_root()
