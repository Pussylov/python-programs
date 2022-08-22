def game():
    return 300
score = game()
with open('highscore.txt') as f:
    h =int(f.read())

if h<score:
    with open('highscore.txt','w') as f:
        f.write(str(score))
