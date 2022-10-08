# LeetEasy
![](docs/leeteasy-demo.png)
<br/>
<br/>
Desktop notification for easy daily challenges in [leetcode](https://leetcode.com/).

We all know `Leetcode's` daily challenges are awesome :sunglasses: However, sometimes these challenges are quite difficult for people who are just starting out problem-solving 	:smiling_face_with_tear:  
This tool will send desktop notification when an **Easy** daily problem is published. This way you won't miss any opportunity to grab some easy **Leetcoins** :coin: and stay motivated for the day :fire:

## Requirements
- python >= 3.8
## Installation
```shell
pip install leeteasy
```
## run
Schedule leeteasy to send notification for easy leetcode problem at 14:30 (24 hours format time)
```shell
python -m leeteasy start 14:30 &
```
To add additional difficulty

```shell
python -m leeteasy start 14:30 --difficulty medium &
```
This will schedule leeteasy for **Easy and Medium** problem.
<br/>
<br/>
To stop leeteasy
```shell
python -m leeteasy stop
```
> **_NOTE:_**  By default `leeteasy` checks for scheduled task in every 1 hour/3600 seconds.
> So there might be 1-hour delay from the actual scheduled time while getting the notification. However,
> this can be controlled using `--sleep_duration` option.

## Linux cronjob guide
Set a cronjob to automatically start `leeteasy` at system boot.
```shell
# open cronjob editor
crontab -e

# add the following line
@reboot python -m leeteasy start 14:30 &

```
## Contributing

We are very happy to see you here. Before sending your pull requests, make sure that you read the whole workflow and the contributing guidelines given below. If you have any doubt regarding the contributing guide, please feel free to [state it clearly in an issue](https://github.com/sudiptob2/leet-easy/issues/new/choose)


### Workflow
1. Go to the issues tab and find an issue you would like to work on.

    1.1. Clarify any doubts in the comments section of the issue.

2. Fork the project

3. Create a branch and make small changes on it.

4. Create a **draft PR**

5. Then make other changes and push to the remote branch you created.

In this way, the maintainers will be able to provide early reviews and comments for your commits which will save time later on.

6. Once the above steps are done, you can change the PR from *draft to active*


7. Once the PR is approved, make sure to update and sync your branch

8. Wait for the maintainers to merge your contribution

9. Congratulations! You made your first contribution to Leet Easy

Keep contributing. We're eager to see your contributions!

For **naming conventions and standard practices for commits, branches and PRs** refer to the [contributing guidelines](docs/CONTRIBUTING.md).