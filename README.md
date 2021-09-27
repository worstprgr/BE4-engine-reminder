# be4-reminder
###### Reminding Jeffrey Bezos to deliver his BE-4 engines to Tory. [Scheduled Twitter Bot with Docker]

#### Dependencies
* Python 3.9 or Python 3.9-alpine3.14
* [Tweepy 3.10.0](https://github.com/tweepy/tweepy)
* [Giphypop 0.3](https://github.com/shaunduncan/giphypop)
* Schedule 1.1.0

You need also: [Twitter API Keys] & [Giphy API Key].

Testet on x86x64.

[Twitter API Keys]: https://developer.twitter.com/
[Giphy API Key]: https://developers.giphy.com/
___

#### API Placeholders
Replace your API Keys with the placeholders inside **'main.py'**. The Twitter API placeholders are found in *line 6 & 7* and the Giphy API placeholder is found in *line 19*.
___

#### How it works
This script chooses between 14 random phrases from the **'messages.txt'** file. And it appends a random 'Jeff Bezos'-themed meme from Giphy.
Thanks to the Schedule module, this script executes everyday at 17:00 UTC+0.
___

#### Configure
You can edit or add more phrases in the **'messages.txt'** file if you want.

If you want to change the targeted Twitter user, head to *line 29* in the **'main.py'** file and edit the name you want.
For changing the Giphy memes, just jump to *line 20*. 

In the **'timer.py'** at *line 11*, you can adjust the timing of the script. Check the [Schedule documentation] for more information.

[Schedule documentation]: https://schedule.readthedocs.io/en/stable/
___

#### Docker
You can build your own Docker image with the Dockerfile in the root folder.
