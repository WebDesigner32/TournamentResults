#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""

    # Connects to the database and establishes a cursor.

    conn = connect()
    cursor = conn.cursor()

    # Executes an SQL command that removes match records from database.

    cursor.execute("DELETE FROM matches")

    # Makes an instant commit and then closes the database connection.

    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""

    # Connects to the database and establishes a cursor.

    conn = connect()
    cursor = conn.cursor()

    # Executes an SQL command that removes player records from database.

    cursor.execute("DELETE FROM players")

    # Makes an instant commit and then closes the database connection.

    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""

    # Connects to the database and establishes a cursor.

    conn = connect()
    cursor = conn.cursor()

    """
    Executes an SQL command that gets the number of players currently
    registered.
    """

    cursor.execute("SELECT COUNT(*) FROM players")

    # Fetches the result and stores it in count.

    count = cursor.fetchone()[0]

    # Closes the database connection.

    conn.close()

    # Returns the result that was fetched.

    return count

def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """

    # Connects to the database and establish a cursor.

    conn = connect()
    cursor = conn.cursor()

    """
    Executes an SQL command that inserts a new player to the tournament
    database.
    """

    cursor.execute("INSERT INTO players(name) VALUES (%s)", (name,))

    # Makes an instant commit and then closes the database connection.

    conn.commit()
    conn.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or
    a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    # Connects to the database and establishes a cursor.

    conn = connect()
    cursor = conn.cursor()

    """
    Executes an SQL command that lists the players and their win records,
    sorted by descending wins.
    """

    cursor.execute("SELECT * FROM standings ORDER BY won_count DESC")

    # Fetches the result and stores it in stand_results.

    stand_results = cursor.fetchall()

    # Closes the database connection.

    conn.close()

    # Returns the result that was fetched.

    return stand_results

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    # Connects to the database and establishes a cursor.

    conn = connect()
    cursor = conn.cursor()

    """
    Executes an SQL command that records the outcome of a single match
    between two players.
    """

    cursor.execute("INSERT INTO matches (winner, loser) VALUES (%s, %s)",
                   (winner, loser,))

    # Makes an instant commit and then closes the database connection.

    conn.commit()
    conn.close()

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

    # Connects to the database and establishes a cursor.

    conn = connect()
    cursor = conn.cursor()

    """
    Executes an SQL command that gets a list of pairs of players for the next
    round of a match.
    """

    cursor.execute("SELECT * FROM standings ORDER BY won_count DESC")

    # Fetches the result and stores it in stand_results.

    stand_results = cursor.fetchall()

    # Empty list called pairs.

    pairs = []

    """
    Groups the results from stand_results into pairs by ranking in descending
    order, then appending to pairs.
    """

    for x in range(0, len(stand_results) - 1, 2):
        pairings = (stand_results[x][0], stand_results[x][1],
                    stand_results[x + 1][0], stand_results[x + 1][1])
        pairs.append(pairings)

    # Closes the database connection.

    conn.close()

    # Returns the list of pairs for the next round of a match.

    return pairs
