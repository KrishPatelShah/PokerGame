# PokerGame

## Rules for Determining the Winner
- If hands are on different levels of the hand range chart, then the higher level hand wins (e.g., flush beats straight, and four of a kind beats flush).
- If hands are on the same level of the hand range chart, then the hand with higher ranks wins (e.g., pair of eights beats pair of sevens, an ace-high Straight beats a king-high straight, a pair of nines with an ace beats a pair of nines with a king).

## Hand Range Chart

| Level | Hand Name            | Example                |
|-------|----------------------|------------------------|
| 9     | Straight Flush        | 5H-6H-7H-8H-9H         |
| 8     | Four of a Kind        | 8H-8S-8C-8D-X          |
| 7     | Full House            | 10H-10D-2S-2H-2D       |
| 6     | Flush                 | 2C-3C-5C-JC-KC         |
| 5     | Straight              | 7S-8C-9S-10H-JH        |
| 4     | 3 of a Kind           | 9S-9C-9D-X-X           |
| 3     | Two Pair              | 9S-9C-10H-10S-X        |
| 2     | Pair                  | 5C-5S-X-X-X            |
| 1     | Nothing               | 6C-9H-10H-QS-KS        |

## Test Cases

### Manual Test Cases

```python
from PokerGameFinal import Poker

# Test Case 1
game1 = Poker()
game1.setPlayerHandManual("AC-KH-TS-9C-2S", "KS-9S-7H-6H-2S")
print(game1)
game1.pokerGameRunner()

# Test Case 2
game2 = Poker()
game2.setPlayerHandManual("2C-2S-TH-8C-5H", "AC-KH-TS-9C-2D")
print(game2)
game2.pokerGameRunner()

# Additional test cases follow a similar structure...
