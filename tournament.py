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
    DB = connect()
    c = DB.cursor()
    c.execute("UPDATE records SET matches = 0, wins = 0")
    c.execute("DELETE FROM matches")
    DB.commit()

def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM records")
    DB.commit()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT count(*) FROM records")
    result = c.fetchone()[0]
    return result



def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO records VALUES (DEFAULT, %s, 0, 0);", (name,))
    DB.commit()


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
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT id, name, wins, matches FROM records ORDER BY wins DESC")
    return [(str(row[0]), str(row[1]), row[2], row[3]) for row in c.fetchall()]


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()

    # update winner data
    c.execute("UPDATE records SET wins = wins + 1, matches = matches + 1 WHERE id = (%s)", (str(winner),))

    # update loser data
    c.execute("UPDATE records SET matches = matches + 1 WHERE id = (%s)", (str(loser),))

    # update matches table
    # the second column refers to winner while the last column refers to loser
    c.execute("INSERT into matches VALUES (DEFAULT, %s, %s)", (str(winner), str(loser),))
    DB.commit()


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
    DB = connect()
    c = DB.cursor()
    pair_list = []
    # update winner data
    c.execute("SELECT id, name, wins FROM records ORDER BY wins DESC")
    player_list = [(str(row[0]), str(row[1])) for row in c.fetchall()]

    for index in range(0, len(player_list) - 1, 2):
        pair_list.append((player_list[index][0], player_list[index][1],
                  player_list[index+1][0], player_list[index+1][1]))
    return pair_list
