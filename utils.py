from datetime import date
import pickle
from gamedb import Eventdb
from rosterdb import Rosterdb

# Function for adding game events to the events database
def add_event(file, date, event_type, f1, f2, f3, d1, d2, g, ext):
    #label = date.today()
    label = date
    edb = Eventdb(file)
    edb.add(label, event_type, f1, f2, f3, d1, d2, g, ext)
    #edb.store()

# Function that adds player to the roster database
def add_player(file, name, number, position):
    rdb = Rosterdb(file)
    rdb.add(name, number, position)
    rdb.store()

# Function that removes players from the roster database
def remove_player(file, name):
    rdb = Rosterdb(file)
    removed = rdb.remove(name)
    if removed:
        rdb.store()
        return True
    else:
        return False
       
# Function that will return the current roster
def display_roster(file):
    f1 = ''
    f2 = ''
    f3 = ''
    f4 = ''
    f5 = ''
    f6 = ''
    f7 = ''
    f8 = ''
    f9 = ''
    f10 = ''
    f11 = ''
    f12 = ''
    f13 = ''
    f14 = ''
    f15 = ''
    d1 = ''
    d2 = ''
    d3 = ''
    d4 = ''
    d5 = ''
    d6 = ''
    d7 = ''
    d8 = ''
    g1 = ''
    g2 = ''
    g3 = ''
    g4 = ''
    with open(file, 'rb') as f:
        roster = pickle.load(f)
        for player in roster:
            if player.position == 'F':
                if f1 == '':
                    f1 = player.number + ' - ' + player.name
                elif f2 == '':
                    f2 = player.number + ' - ' + player.name
                elif f3 == '':
                    f3 = player.number + ' - ' + player.name
                elif f4 == '':
                    f4 = player.number + ' - ' + player.name
                elif f5 == '':
                    f5 = player.number + ' - ' + player.name
                elif f6 == '':
                    f6 = player.number + ' - ' + player.name
                elif f7 == '':
                    f7 = player.number + ' - ' + player.name
                elif f8 == '':
                    f8 = player.number + ' - ' + player.name
                elif f9 == '':
                    f9 = player.number + ' - ' + player.name
                elif f10 == '':
                    f10 = player.number + ' - ' + player.name
                elif f11 == '':
                    f11 = player.number + ' - ' + player.name
                elif f12 == '':
                    f12 = player.number + ' - ' + player.name
                elif f13 == '':
                    f13 = player.number + ' - ' + player.name
                elif f14 == '':
                    f14 = player.number + ' - ' + player.name
                elif f15 == '':
                    f15 = player.number + ' - ' + player.name
            elif player.position == 'D':
                if d1 == '':
                    d1 = player.number + ' - ' + player.name
                elif d2 == '':
                    d2 = player.number + ' - ' + player.name
                elif d3 == '':
                    d3 = player.number + ' - ' + player.name
                elif d4 == '':
                    d4 = player.number + ' - ' + player.name
                elif d5 == '':
                    d5 = player.number + ' - ' + player.name
                elif d6 == '':
                    d6 = player.number + ' - ' + player.name
                elif d7 == '':
                    d7 = player.number + ' - ' + player.name
                elif d8 == '':
                    d8 = player.number + ' - ' + player.name
            elif player.position == 'G':
                if g1 == '':
                    g1 = player.number + ' - ' + player.name
                elif g2 == '':
                    g2 = player.number + ' - ' + player.name
                elif g3 == '':
                    g3 = player.number + ' - ' + player.name
                elif g4 == '':
                    g4 = player.number + ' - ' + player.name
    return f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, d1, d2, d3, d4, d5, d6, d7, d8, g1, g2, g3, g4

# This function returns the advanced stats for the player the user searched for
def get_stats(file, player_num):
    edb = Eventdb(file)
    hdgf = 0
    ldgf = 0
    hdga = 0
    ldga = 0
    hdsf = 0
    ldsf = 0
    hdsa = 0
    ldsa = 0
    mhdsf = 0
    mldsf = 0
    mhdsa = 0
    mldsa = 0
    for event in edb.db:
        if event.event_type == 'HDGF' and (player_num in [event.f1, event.f2, event.f3, event.d1, event.d2, event.g, event.ext]):
            hdgf += 1
            hdsf += 1
        elif event.event_type == 'LDGF' and (player_num in [event.f1, event.f2, event.f3, event.d1, event.d2, event.g, event.ext]):
            ldgf += 1
            ldsf += 1
        elif event.event_type == 'HDGA' and (player_num in [event.f1, event.f2, event.f3, event.d1, event.d2, event.g, event.ext]):
            hdga += 1
            hdsa += 1
        elif event.event_type == 'LDGA' and (player_num in [event.f1, event.f2, event.f3, event.d1, event.d2, event.g, event.ext]):
            ldga += 1
            ldsa += 1
        elif event.event_type == 'HDSF' and (player_num in [event.f1, event.f2, event.f3, event.d1, event.d2, event.g, event.ext]):
            hdsf += 1
        elif event.event_type == 'LDSF' and (player_num in [event.f1, event.f2, event.f3, event.d1, event.d2, event.g, event.ext]):
            ldsf += 1
        elif event.event_type == 'HDSA' and (player_num in [event.f1, event.f2, event.f3, event.d1, event.d2, event.g, event.ext]):
            hdsa += 1
        elif event.event_type == 'LDSA' and (player_num in [event.f1, event.f2, event.f3, event.d1, event.d2, event.g, event.ext]):
            ldsa += 1
        elif event.event_type == 'MHDSF' and (player_num in [event.f1, event.f2, event.f3, event.d1, event.d2, event.g, event.ext]):
            mhdsf += 1
        elif event.event_type == 'MLDSF' and (player_num in [event.f1, event.f2, event.f3, event.d1, event.d2, event.g, event.ext]):
            mldsf += 1
        elif event.event_type == 'MHDSA' and (player_num in [event.f1, event.f2, event.f3, event.d1, event.d2, event.g, event.ext]):
            mhdsa += 1
        elif event.event_type == 'MLDSA' and (player_num in [event.f1, event.f2, event.f3, event.d1, event.d2, event.g, event.ext]):
            mldsa += 1
    
    if (hdgf + ldgf + hdga + ldga) == 0:
        gf_percent = 0
    else:
        gf_percent = (hdgf + ldgf) / (hdgf + ldgf + hdga + ldga)
        gf_percent = round(gf_percent * 100, 2)
    # Shots for % of all shots
    all_shots = (hdsf + ldsf + mhdsf + mldsf) / (hdsf + ldsf + mhdsf + mldsf + hdsa + ldsa + mhdsa + mldsa)
    all_shots = round(all_shots * 100, 2)
    # Shots for % of only shots that hit the net
    net_shots = (hdsf + ldsf) / (hdsf + ldsf + hdsa + ldsa)
    net_shots = round(net_shots * 100, 2)
    # High dangers shots for %, both those that hit the net and those that miss
    hd_shots = (hdsf + mhdsf) / (hdsf + mhdsf + hdsa + mhdsa)
    hd_shots = round(hd_shots * 100, 2)
    # Expected goals for
    xgf = round((ldsf * 0.05) + (hdsf * 0.15), 2)
    # Expected goals for %
    xgf_p = ((ldsf * 0.05) + (hdsf * 0.15)) / ((ldsf * 0.05) + (hdsf * 0.15) + (ldsa * 0.05) + (hdsa * 0.15))
    xgf_p = round(xgf_p * 100, 2)
    # Adjusted save % for goalies
    asp = (ldsa + (hdsa * 1.5) - (ldga * 1.5) - (hdga * 0.5)) / (ldsa + (hdsa * 1.5))
    asp = round(asp * 100, 2)
    # Expected goals against - NEEDS TO BE ADJUSTED AS A PER GAME
    xga = round((ldsa * 0.025) + (hdsa * 0.1), 2)

    # Gets the player's name using the get_name() function below
    rfile = 'roster_' + file
    player_name = get_name(rfile, player_num)
    
    # Temp to check
    #print('\nHDGF: %s\nLDGF: %s\nHDGA: %s\nLDGA: %s\nHDSF: %s\nLDSF: %s\nHDSA: %s\nLDSA: %s\nMHDSF: %s\nMLDSF: %s\nMHDSA: %s\nMLDSA: %s' % (hdgf, ldgf, hdga, ldga, hdsf, ldsf, hdsa, ldsa, mhdsf, mldsf, mhdsa, mldsa))

    return player_name, gf_percent, all_shots, net_shots, hd_shots, xgf, xgf_p, asp, xga


# Function for retrieving the player's name from the roster database
def get_name(file, player_num):
    with open(file, 'rb') as f:
        roster = pickle.load(f)
        for player in roster:
            if player_num == player.number:
                name = player.name
    return name

# Function for retrieving the player's position from the roster database
def get_position(file, player_num):
    with open(file, 'rb') as f:
        roster = pickle.load(f)
        for player in roster:
            if player_num == player.number:
                pos = player.position
    return pos


def viewall():
    with open('roster_2023-24.pickle', 'rb') as f:
        events = pickle.load(f)
        for event in events:
            print(event)
#viewall()
