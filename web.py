import notify2
from script import codechef, codeforces, hackerearth, hackerrank, spoj
from usernames import codechef_username, codeforces_username, hackerEarth_username, hackerRank_username, spoj_username

icon_path = "/home/vish/Downloads/index.png"

# Extracting Details
cc = codechef(codechef_username)
cf = codeforces(codeforces_username)
he = hackerearth(hackerEarth_username)
hr = hackerrank(hackerRank_username)
sp = spoj(spoj_username)

result = ""
result += "Codechef:\n Problems Solved: " + str(cc[0]) + "\n Current Rating: " + str(cc[1])
result += "\nCodeForces:\n Contest Played: " + str(cf[0]) + "\n Current Rating: " + str(cf[1])
result += "\nHackerEarth:\n Problems Solved: " + str(he[0]) + "\n Current Rating: " + str(he[1])
result += "\nHackerRank:\n Problems Solved: " + str(hr[0]) + "\n Current Rating: " + str(hr[1])
result += "\nSPOJ:\n Problems Solved: " + str(sp[0]) + "\n Current Rating: " + str(sp[1])

result += "\nTotal Problems: "
total = cc[0] + he[0] + hr[0] + sp[0]
result += str(total)

notify2.init("HackerProfile Notifier")
n = notify2.Notification("Profile Details", icon=icon_path)
n.update("Profile Details", result)
n.show()


