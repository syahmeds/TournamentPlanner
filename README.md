# TournamentPlanner
Swiss Style Tournament Planner:-

In this project, we are writing a Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.

The tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

This project has two parts: defining the database schema (SQL table definitions), and writing the code that will use it

The project has three main files: tournament.sql, tournament.py, and tournament_test.py.

The file tournament.sql is where the database schema is housed, in the form of SQL create table commands.
We have three tables: 
<br />
players - storing playerID and playername 
<br />
playerstandings - storing playerID, playerName, numberOfwins and numberOfmatches, and
<br />
matchoutcomes - storing matchID, winnerID and loserID.

The file tournament.py has several functions to simulate the tournament. The functions are:
<br />
connect():
<br />&nbsp;&nbsp;&nbsp;&nbsp;
    """Connect to the PostgreSQL database.  Returns a database connection."""
<br />
deleteMatches():
<br />&nbsp;&nbsp;&nbsp;&nbsp;
    """Remove all the match records from the database."""
<br />
deletePlayers():
<br />&nbsp;&nbsp;&nbsp;&nbsp;
    """Remove all the player records from the database."""
<br />
countPlayers():
<br />&nbsp;&nbsp;&nbsp;&nbsp;
    """Returns the number of players currently registered."""
<br />
registerPlayer(name):
<br />&nbsp;&nbsp;&nbsp;&nbsp;
    """Adds a player to the tournament database."""
<br />
playerStandings():
<br />&nbsp;&nbsp;&nbsp;&nbsp;
    """Returns a list of the players and their win records, sorted by wins."""
<br />
reportMatch(winner, loser):
<br />&nbsp;&nbsp;&nbsp;&nbsp;
    """Records the outcome of a single match between two players."""
<br />
swissPairings():
<br />&nbsp;&nbsp;&nbsp;&nbsp;
    """Returns a list of pairs of players for the next round of a match."""

Finally, the file tournament_test.py contains unit tests that will test the functions you’ve written in tournament.py. You can run the tests from the command line, using the command 'python tournament_test.py'.
