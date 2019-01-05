video_games = ["Halo", "Call of Duty", "Sea of Theives", "Red Dead Redemption"]
print("last video games in the list is: " + video_games[-1])

video_games.append("Battlefield")

print('after adding "Battlefield" to the list: ' +  str(video_games))
  
video_games.insert(3, "Rainbow Six Siege")

print('after adding "Rainbow Six Siege" to the list: ' + str(video_games))

del video_games[2]
video_games.sort()
print('ALPHABET: after deleting video_games[2] from the list '+ str(video_games))

video_games.sort(reverse = True)
print('REVERSE: after deleting video_games[2] from the list '+ str(video_games))

print("length of the list is " + str(len(video_games)))