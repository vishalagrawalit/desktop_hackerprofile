import notify2
from script import codechef, codeforces, hackerearth, hackerrank, spoj
from usernames import codechef_username, codeforces_username, hackerEarth_username, hackerRank_username, spoj_username

icon_path = "/home/vish/Downloads/index.png"

# Extracting Details
user = "Enter your Username."
result = ""
total = 0

if codechef_username != user:
    cc = codechef(codechef_username)
    result += "Codechef:\n Problems Solved: " + str(cc[0]) + "\n Current Rating: " + str(cc[1])
    total += cc[0]
if codeforces_username != user:
    cf = codeforces(codeforces_username)
    result += "\nCodeForces:\n Contest Played: " + str(cf[0]) + "\n Current Rating: " + str(cf[1])
if hackerEarth_username != user:
    he = hackerearth(hackerEarth_username)
    result += "\nHackerEarth:\n Problems Solved: " + str(he[0]) + "\n Current Rating: " + str(he[1])
    total += he[0]
if hackerRank_username != user:
    hr = hackerrank(hackerRank_username)
    result += "\nHackerRank:\n Problems Solved: " + str(hr[0]) + "\n Current Rating: " + str(hr[1])
    total += hr[0]
if spoj_username != user:
    sp = spoj(spoj_username)
    result += "\nSPOJ:\n Problems Solved: " + str(sp[0]) + "\n Current Rating: " + str(sp[1])
    total += sp[0]

result += "\nTotal Problems: "
result += str(total)

notify2.init("HackerProfile Notifier")
n = notify2.Notification("Profile Details", icon=icon_path)
n.update("Profile Details", result)
n.show()


