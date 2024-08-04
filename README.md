# LittleGame
<br/>

<p>This is a demo game for a user-computer interactive fun game of "Rock, Paper, and Scissors".
The objective is to have fun and try to beat the computer as many times as possible.

You can select some strategies to uer play-style, and come up with your own strategies as well.

Have fun at it!</p>


# Play the game

<p>You can play the game for yourself!
It can be played for anynumber of rounds and you cna choose the strategies the computer plays against you.</p>

<h3>Examples of match setups</h3>

<p>Invoke a 3-round game, computer using a Random-choice strategy on every match.</p>

`python -m littlegame --rounds=3 --strategies Random`

<p>Invoke a 3-round game, computer using a Random-choice strategy on the first match, followed by a fixed Rock and Paper move strategy for the second and third matches respectively.</p>

`python -m littlegame --rounds=3 --strategies Random Rock Paper`

<p>Invoke a 5-round game, computer cycling in-order between using a Random-choice strategy, followed by a fixed Rock strategy, and then a fixed Scissors strategy.<br/>For clarity this would lead into a 5-match setups where the computer plays strategies in the order of [Random, Rock, Scissors, Random, Rock]</p>

`python -m littlegame --rounds=5 --strategies Random Rock`


# Development

<h3>New strategies</h3>
<p>You can contribute to new strategies that can be implemented in code and tried out by yourself.</p>

<h3>Run tests</h3>
<p>The tests for the entire project are under `tests` directory.
To run your version of the tests, run the following from the terminal</p>

`python -m unittest discover littlegame/tests`


# Known Issues

<h3>Stateful strategies</h3>
<p>When used as the only strategy, there are no side effects.</p>
<p>But when run in conjuction ot other strategies, they don't keep track of the wins/losses of other matches. It only tracks the matches the given strategy has played for.</p>