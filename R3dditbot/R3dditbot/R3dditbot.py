import praw

userAgent = 'R3dditBot1.0'
cID = #Enter Reddit Personal Use script name here 
cSC = #Enter Reddit Personal Use secret key
userN = #Enter Reddit Username here
userP = #Enter Reddit Password here
numFound = 0
reddit = praw.Reddit(user_agent=userAgent,
                    client_id = cID,
                    client_secret = cSC,
                    username = userN,
                    password = userP)
subreddit = reddit.subreddit('CS50')
bot_phrase = 'CS50 is tough'
keywords = { 'pset', 'how', 'where', 'help'}

for submission in subreddit.hot(limit=15):
    n_title = submission.title.lower()
    for i in keywords:
        if i in n_title:
            numFound = numFound + 1
            print('Bot replying to: ')
            print("Title", submission.title)
            print("Text", submission.selftext)
            print("Score:", submission.score)
            print("--------------------------------")
            print('Bot saying:', bot_phrase)
            print()
            submission.reply(bot_phrase)
if numFound == 0:
    print()
    print("Sorry didn't find any posts with those keywords, try again")
