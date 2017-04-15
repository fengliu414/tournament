#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def do_query(*query_content):
    DB = connect()
    c = DB.cursor()
    if len(query_content) == 1:
        c.execute(query_content[0])
    elif len(query_content) == 2:
        c.execute(query_content[0], query_content[1])
    else:
        raise ValueError("Incorrect query content!")
    DB.commit()
    return c

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    do_query("DELETE FROM matches")

def deletePlayers():
    """Remove all the player records from the database."""
    do_query("DELETE FROM player")


def countPlayers():
    """Returns the number of players currently registered."""
    c = do_query("SELECT count(*) FROM player")
    result = c.fetchone()[0]
    return result



def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    do_query("INSERT INTO player VALUES (DEFAULT, %s);", (name,))


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
    c = do_query("SELECT player_id, player_name, wins, total_matches FROM player_complete_info ORDER BY wins DESC")
    return [(str(row[0]), str(row[1]), row[2], row[3]) for row in c.fetchall()]


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    # update matches table
    # the second column refers to winner while the last column refers to loser
    do_query("INSERT into matches VALUES (DEFAULT, %s, %s)", (str(winner), str(loser),))


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
    pair_list = []
    # update winner data
    c = do_query("SELECT player_id, player_name, wins FROM player_complete_info ORDER BY wins DESC")
    player_list = [(str(row[0]), str(row[1])) for row in c.fetchall()]

    for index in range(0, len(player_list) - 1, 2):
        pair_list.append((player_list[index][0], player_list[index][1],
                          player_list[index+1][0], player_list[index+1][1]))
    return pair_list
