import praw

reddit = praw.Reddit(
    client_id="gDFh3DIFtkBSYSVg_21jqg",
    password="that snipers a bloodly -sentry hahaha *killbinds*",
    client_secret="qon9FmyzD5evqa3bL6yC2csnCtdS_A",
    user_agent="A test bot, created by Mipppy on github, and u/-Mippy on reddit",
    username="-Mippy",
)
file = open ("data.txt", "a")  
subreddit = reddit.subreddit("TF2")

# assume you have a Subreddit instance bound to variable `subreddit`
for submission in subreddit.top(limit=5):
    
    print(submission.title)
    file.writelines(f'{submission.title}\n')
    # Output: the submission's title
    
    print(submission.score)
    file.writelines(f'{submission.score}\n')
    # Output: the submission's score

    print(submission.id)
    file.writelines(f'{submission.id}\n')
    # Output: the submission's ID

    print(submission.url)
    file.writelines(f'{submission.score}\n\n')

file.writelines("\n\n\n")


