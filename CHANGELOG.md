# CHANGELOG.md

## 0.1.3 (Pre-Alpha)

Features:

  - schedule for 2 problem difficulty
  - python 3.8 support
  - notification icon support

## 1.0.0 (Alpha)

Breaking change:

- `leeteasy start` implemented

Feature:

- `--sleep_duration` option added
- `leeteasy stop` command implemented

Fix:

- Null notification sent when problem difficulty is not in the target difficulty fixed.

## 1.0.1 (Alpha)

Fix:

- Notification not working when `leeteasy` is scheduled with cronjob

## 1.0.2 (Alpha)

Fix:

- `import pwd` fix for windows.

## 1.2.0 (Alpha)

Features:

  - Retry logic implemented on connection failed with leetcode API
  - Notification on power on if the scheduled time had passed #50