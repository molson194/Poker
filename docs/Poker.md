# Overview

* N bots with position on the table
* 3 operations - check, fold, raise
* 4 rounds - pre-flop, post-flop, post-river, post-turn
* 1 Deck

# Reinforcement Inputs

* Positions
* What others have done in current hand
* Playing styles of other players (so far in game)
* [Optional] Historical playing styles of other players
* My playing style (so far in game)
* [Optional] My historical playing style
* What I have done in the current hand
* Value of hand
* Alpha

# Playing style inputs

* https://redchippoker.com/basic-hud-stats/
* https://pokercopilot.com/essential-poker-statistics

# Outputs

* Amount won/lost
* Luck factor?
* Round (higher value for cards that won at show-down)

# Class Structure

* Player - Learner, Stats
  * Action (Context)
  * HUD Stats
* Context
  * Current Round
  * Players
  * Actions so far
* Enum Round
* Table
* Coordinator