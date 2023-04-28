# CIS1051-final-project
# JoyBot
Discord music bot with commands: join, leave, play, pause, stop, skip, and list.
- Play command is usable with both urls and youtube search.
- Play command also acts like a queue

# Demo
[![Watch the video](https://youtu.be/b2dwB4qOavI/maxresdefault.jpg)](https://youtu.be/b2dwB4qOavI)

# Discussion
Some difficulties that I faced where trying to get both urls and youtube search to work, adding songs to a queue, and having the bot only message the chat that the user typed in. I got both urls and youtube search to work by using a try-except statement. Adding a queue was tricky, but I figured out that I could use a dictionary to store the songs and titles and popping them through a function. I also used a dictionary for the chat problem by storing the channel. I learned how to use dictionaries better, a bit about async functions, lambda functions, and about classes. I enjoyed developing the play command the most, since it was the main part of my program. It also took the most time.

# Resources
I used this tutorial to help me grasp the discord module and write code: 
* [Youtube Link](https://www.youtube.com/playlist?list=PL-7Dfw57ZZVRB4N7VWPjmT0Q-2FIMNBMP) 

Stack Overflow Questions:
* [StackOverflow](https://stackoverflow.com/users/21622720/iflookscouldkill?tab=questions)

Youtube-dl Documentation:
* [Youtube-dl](https://github.com/ytdl-org/youtube-dl/blob/master/README.md)