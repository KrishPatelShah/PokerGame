from PokerGameFinal import Card, Deck, Poker

print("Manual Test Cases\n")
game1 = Poker()
game1.setPlayerHandManual("AC-KH-TS-9C-2S", "KS-9S-7H-6H-2S")
print(game1)
game1.pokerGameRunner()

game2 = Poker()
game2.setPlayerHandManual("2C-2S-TH-8C-5H", "AC-KH-TS-9C-2D")
print(game2)
game2.pokerGameRunner()

game3 = Poker()
game3.setPlayerHandManual("2C-2S-TH-8C-5H", "5C-5S-AH-KH-QH")
print(game3)
game3.pokerGameRunner()

game4 = Poker()
game4.setPlayerHandManual("3C-3S-3H-8S-5C", "2C-2S-TH-8C-5H")
print(game4)
game4.pokerGameRunner()

game5 = Poker()
game5.setPlayerHandManual("3C-3S-3H-8S-5C", "7C-8H-9D-TD-JD")
print(game5)
game5.pokerGameRunner()

game6 = Poker()
game6.setPlayerHandManual("7C-8H-9D-TD-JD", "9H-2H-3H-KH-AH")
print(game6)
game6.pokerGameRunner()

game7 = Poker()
game7.setPlayerHandManual("KC-TC-8C-7C-6C", "9H-2H-3H-KH-AH")
print(game7)
game7.pokerGameRunner()

game8 = Poker()
game8.setPlayerHandManual("AS-AH-AD-AC-TH", "KC-TC-8C-7C-6C")
print(game8)
game8.pokerGameRunner()

game9 = Poker()
game9.setPlayerHandManual("8S-8H-8D-8C-9D", "AS-AH-AD-AC-TH")
print(game9)
game9.pokerGameRunner()

game10 = Poker()
game10.setPlayerHandManual("2H-3H-4H-5H-6H", "AH-KH-JH-TH-9H")
print(game10)
game10.pokerGameRunner()


print("\n\nRandom Test Cases\n")

game11 = Poker()
game11.setPlayerHandRandom()
print(game11)
game11.pokerGameRunner()

game12 = Poker()
game12.setPlayerHandRandom()
print(game12)
game12.pokerGameRunner()

game13 = Poker()
game13.setPlayerHandRandom()
print(game13)
game13.pokerGameRunner()

game14 = Poker()
game14.setPlayerHandRandom()
print(game14)
game14.pokerGameRunner()

game15 = Poker()
game15.setPlayerHandRandom()
print(game15)
game15.pokerGameRunner()

game16 = Poker()
game16.setPlayerHandRandom()
print(game16)
game16.pokerGameRunner()

game17 = Poker()
game17.setPlayerHandRandom()
print(game17)
game17.pokerGameRunner()

game18 = Poker()
game18.setPlayerHandRandom()
print(game18)
game18.pokerGameRunner()

game19 = Poker()
game19.setPlayerHandRandom()
print(game19)
game19.pokerGameRunner()

game20 = Poker()
game20.setPlayerHandRandom()
print(game20)
game20.pokerGameRunner()
