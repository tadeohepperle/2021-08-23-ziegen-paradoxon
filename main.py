import random


def playWithoutSwitching():
    choices = [1, 2, 3]
    correctChoice = random.choice(choices)
    playerChoice = random.choice(choices)
    return correctChoice == playerChoice


def playWithSwitching():
    choices = [1, 2, 3]
    correctChoice = random.choice(choices)
    playerChoice = random.choice(choices)
    oneOfTwoIncorrectChoices = random.choice(
        list(filter(lambda x: x != correctChoice, choices)))
    switchedPlayerChoice = list(filter(
        lambda x: x != oneOfTwoIncorrectChoices and x != playerChoice, choices))[0]
    return switchedPlayerChoice == correctChoice


TESTRUNS = 100000


def testStrategy(strategy, strategyname):
    successes = 0
    for i in range(TESTRUNS):
        if(strategy()):
            successes += 1
    print(
        f"\nTried Strategy {strategyname} for {str(TESTRUNS)} times\nSuccesses: {successes}/{TESTRUNS}    ({round(successes/TESTRUNS * 100,3)} %)\n\n")


testStrategy(playWithSwitching, "play with switching")
testStrategy(playWithoutSwitching, "play without switching")
