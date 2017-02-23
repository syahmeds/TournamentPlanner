#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    pg = psycopg2.connect("dbname=tournament")
    cursor = pg.cursor()
    cursor.execute("delete from matchoutcomes")
    one = 1
    zero = 0
    cursor.execute("update playerstandings set wins = (%s), matches = (%s) where (%s)=(%s)",(zero,zero,one,one))
    pg.commit()
    pg.close()


def deletePlayers():
    """Remove all the player records from the database."""
    pg = psycopg2.connect("dbname=tournament")
    cursor = pg.cursor()
    cursor.execute("delete from playerstandings")
    cursor.execute("delete from matchoutcomes")
    cursor.execute("delete from players")
    pg.commit()
    pg.close()


def countPlayers():
    """Returns the number of players currently registered."""
    pg = psycopg2.connect("dbname=tournament")
    cursor = pg.cursor()
    cursor.execute("select count(*) from players")
    rows = cursor.fetchall()
    # for row in rows:
        # return row[0]
    return rows[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    pg = psycopg2.connect("dbname=tournament")
    cursor = pg.cursor()
    cursor.execute("insert into players (playername) values (%s)", (name,))
    cursor.execute("insert into playerstandings (playername) values (%s)", (name,))
    # cursor.execute("insert into playerstandings (playername) values (%s)", (name,))
    pg.commit()
    pg.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    pg = psycopg2.connect("dbname=tournament")
    cursor = pg.cursor()
    cursor.execute("select * from playerstandings")
    return cursor.fetchall()
    # print cursor.fetchall()


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    pg = psycopg2.connect("dbname=tournament")
    cursor = pg.cursor()
    cursor.execute("insert into matchoutcomes (winner, loser) values (%s,%s)", (winner,loser))
    cursor.execute("select wins, matches from playerstandings where playerid = (%s)",(winner,))
    winvartp = cursor.fetchall()
    winvar = winvartp[0][0]
    matchvar = winvartp[0][1]
    # print "from reportMatch, value of wins in playerstandings got fetched as\n"
    # print winvar
    # print "from reportMatch, value of matches in playerstandings got fetched as\n"
    # print matchvar
    # print "from reportMatch, record in playerstandings got fetched as\n"
    # print winvartp
    winvar += 1
    matchvar += 1
    cursor.execute("update playerstandings set wins = (%s), matches = (%s) where playerid = (%s)",(winvar,matchvar,winner))
    cursor.execute("update playerstandings set matches = (%s) where playerid = (%s)",(matchvar,loser))
    pg.commit()
    pg.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    pg = psycopg2.connect("dbname=tournament")
    cursor = pg.cursor()
    # print "Inside swiss pairings"
    cursor.execute("select playerid, playername, wins from playerstandings order by wins")
    tempvar = cursor.fetchall()
    pairinglist = []
    # print tempvar
    for i in range(0,len(tempvar),2):
        temprow = (tempvar[i][0],tempvar[i][1],tempvar[i+1][0],tempvar[i+1][1])
        # print temprow
        pairinglist.append(temprow)
    # print pairinglist
    return pairinglist
