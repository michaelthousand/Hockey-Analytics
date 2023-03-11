import PySimpleGUI as sg
import utils
from datetime import date

sg.theme('LightBlue')


# Home screen
def home_win():
    banner = sg.Text("[Your Team's] Analytics Tracker", font=('Helvetica', 20), size=20, expand_x=True, justification = 'center')
    banner_img = sg.Image('./content/genlogo.png')
    year_in_txt = sg.Text('Season:')
    year_in = sg.Input(default_text='2023-24', key='-YEAR-')
    roster_btn = sg.Button('', image_filename='./content/roster.png', key='-ROSTER-')
    new_game = sg.Button('', image_filename='./content/game.png', key='-NEW-GAME-')
    #view_game = sg.Button('', image_filename='./content/players3.png', key='-VIEW-GAME-')
    view_stats = sg.Button('', image_filename='./content/stats.png', key='-VIEW-STATS-')


    layout = [
        [banner_img, sg.Text(''), sg.Text(''), banner, sg.Text(''), year_in_txt, year_in],
        [sg.Text(''), sg.Text(''), sg.Text(''), sg.Text(''), sg.Text(''), sg.Text(''), sg.Text('')],
        [roster_btn, sg.Text(''), new_game, sg.Text(''), view_stats]

    ]
    return sg.Window("[Your Team's] Analytics Tracker - Home", layout, size=(1200,500), finalize = True, enable_close_attempted_event = True, icon='./content/genlogo.ico', element_justification='c')

def roster_win():
    upload_rst = sg.Button('Load Roster', key='-LOADRST-')
    player_txt = sg.Text('Enter player last name:')
    player_name = sg.Input(key='-RNAME-')
    player_num_txt = sg.Text('Enter player number:')
    player_num = sg.Input(key='-RNUM-', size=7)
    player_pos_txt = sg.Text('Enter player position:')
    player_pos = sg.Input(key='-RPOS-', size=7)
    add_btn = sg.Button('Add Player', key='-ADDPLY-')
    delete_btn = sg.Button('Remove Player', key='-RMVPLY-') # Make sure this never deletes them from the db - only takes them off the screen
    forwards_txt = sg.Text('Forwards:', font=('Helvetica', 20))
    defense_txt = sg.Text('Defensemen:', font=('Helvetica', 20))
    goalie_txt = sg.Text('Goalies:', font=('Helvetica', 20))
    f1 = sg.Text('', key='-RF1-')
    f2 = sg.Text('', key='-RF2-')
    f3 = sg.Text('', key='-RF3-')
    f4 = sg.Text('', key='-RF4-')
    f5 = sg.Text('', key='-RF5-')
    f6 = sg.Text('', key='-RF6-')
    f7 = sg.Text('', key='-RF7-')
    f8 = sg.Text('', key='-RF8-')
    f9 = sg.Text('', key='-RF9-')
    f10 = sg.Text('', key='-RF10-')
    f11 = sg.Text('', key='-RF11-')
    f12 = sg.Text('', key='-RF12-')
    f13 = sg.Text('', key='-RF13-')
    f14 = sg.Text('', key='-RF14-')
    f15 = sg.Text('', key='-RF15-')
    d1 = sg.Text('', key='-RD1-')
    d2 = sg.Text('', key='-RD2-')
    d3 = sg.Text('', key='-RD3-')
    d4 = sg.Text('', key='-RD4-')
    d5 = sg.Text('', key='-RD5-')
    d6 = sg.Text('', key='-RD6-')
    d7 = sg.Text('', key='-RD7-')
    d8 = sg.Text('', key='-RD8-')
    g1 = sg.Text('', key='-RG1-')
    g2 = sg.Text('', key='-RG2-')
    g3 = sg.Text('', key='-RG3-')
    g4 = sg.Text('', key='-RG4-')

    layout = [
        [upload_rst],
        [player_txt, player_name, player_num_txt, player_num, player_pos_txt, player_pos, add_btn, delete_btn],
        [forwards_txt],
        [f1, f2, f3],
        [f4, f5, f6],
        [f7, f8, f9],
        [f10, f11, f12],
        [f13, f14, f15],
        [defense_txt],
        [d1, d2],
        [d3, d4],
        [d5, d6],
        [d7, d8],
        [goalie_txt],
        [g1, g2, g3, g4],
    ]
    return sg.Window("[Your Team's] Analytics Tracker - Roster", layout, size=(1200,500), finalize = True, enable_close_attempted_event = True, icon='./content/genlogo.ico')

def new_game():
    f1_txt = sg.Text('F1:', font=('Helvetica', 20))
    f1 = sg.Input(key='-F1-', size=5, font=('Helvetica', 20), text_color='black')
    f2_txt = sg.Text('F2:', font=('Helvetica', 20))
    f2 = sg.Input(key='-F2-', size=5, font=('Helvetica', 20), text_color='black')
    f3_txt = sg.Text('F3:', font=('Helvetica', 20))
    f3 = sg.Input(key='-F3-', size=5, font=('Helvetica', 20), text_color='black')
    d1_txt = sg.Text('D1:', font=('Helvetica', 20))
    d1 = sg.Input(key='-D1-', size=5, font=('Helvetica', 20), text_color='black')
    d2_txt = sg.Text('D2:', font=('Helvetica', 20))
    d2 = sg.Input(key='-D2-', size=5, font=('Helvetica', 20), text_color='black')
    g1_txt = sg.Text('G:', font=('Helvetica', 20))
    g1 = sg.Input(key='-G-', size=5, font=('Helvetica', 20), text_color='black')
    ext_txt = sg.Text('EXT:', font=('Helvetica', 20))
    ext =sg.Input(key='-EXT-', size=5, font=('Helvetica', 20), text_color='black')

    goal_for_hd = sg.Button('High Danger\nGoal For', key='-HDGF-', size=(25, 10), font=('Helvetica', 16), button_color=('white', 'darkred'))
    goal_for_ld = sg.Button('Low Danger\nGoal For', key='-LDGF-', size=(25, 10), font=('Helvetica', 16), button_color=('white', 'darkblue'))
    goal_against_hd = sg.Button('High Danger\nGoal Against', key='-HDGA-', size=(25, 10), font=('Helvetica', 16), button_color=('white', 'darkred'))
    goal_against_ld = sg.Button('Low Danger\nGoal Against', key='-LDGA-', size=(25, 10), font=('Helvetica', 16), button_color=('white', 'darkblue'))

    sfhd = sg.Button('High Danger\nShot For', key='-HDSF-', size=(25, 10), font=('Helvetica', 16), button_color=('darkred', 'white'))
    sfld = sg.Button('Low Danger\nShot For', key='-LDSF-', size=(25, 10), font=('Helvetica', 16), button_color=('darkblue', 'white'))
    sahd = sg.Button('High Danger\nShot Against', key='-HDSA-', size=(25, 10), font=('Helvetica', 16), button_color=('darkred', 'white'))
    sald = sg.Button('Low Danger\nShot Against', key='-LDSA-', size=(25, 10), font=('Helvetica', 16), button_color=('darkblue', 'white'))

    msfhd = sg.Button('High Danger\nMissed\nShot For', key='-MHDSF-', size=(25, 10), font=('Helvetica', 16), button_color=('white', 'darkred'))
    msfld = sg.Button('Low Danger\nMissed\nShot For', key='-MLDSF-', size=(25, 10), font=('Helvetica', 16), button_color=('white', 'darkblue'))
    msahd = sg.Button('High Danger\nMissed\nShot Against', key='-MHDSA-', size=(25, 10), font=('Helvetica', 16), button_color=('white', 'darkred'))
    msald = sg.Button('Low Danger\nMissed\nShot Against', key='-MLDSA-', size=(25, 10), font=('Helvetica', 16), button_color=('white', 'darkblue'))
    
    date_input_txt = sg.Text("Enter the date of the game:")
    default_date = date.today()
    date_input = sg.Input(default_text=default_date, key='-D-IN-')

    layout = [
        [sg.Text('')],
        [f1_txt, f1, f2_txt, f2, f3_txt, f3],
        [d1_txt, d1, d2_txt, d2],
        [sg.Text('')],
        [g1_txt, g1, ext_txt, ext],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Text('')],
        [goal_for_hd, goal_for_ld, sfhd, sfld, msfhd, msfld],
        [sg.Text('')],
        [sg.Text('')],
        [goal_against_hd, goal_against_ld, sahd, sald, msahd, msald],
        [sg.Text('')],
        [sg.Text('')],
        [date_input_txt, date_input]
    ]
    return sg.Window("[Your Team's] Analytics Tracker - Game", layout, size=(2000,1000), finalize = True, enable_close_attempted_event = True, icon='./content/genlogo.ico', element_justification='c')

def stat_win():
    player_num_txt = sg.Text('Please enter a player number to see statistics:')
    player_num = sg.Input(key='-NUM-SRCH-')
    srch_btn = sg.Button('Search', key='-SRCH-BTN-')
    player_name = sg.Text('', key='-SRCH-NAME-')
    gf_p_text = sg.Text('Goals for %:')
    gf_p = sg.Text('', key = '-GF-P-')
    all_shot_p_text = sg.Text('Shots for %:')
    all_shot_p = sg.Text('', key='-SH-P-')
    shot_p_text = sg.Text('Shots on net %:')
    shot_p = sg.Text('', key='-OSH-P-')
    hdsp_txt = sg.Text('High danger shots %:')
    hdsp = sg.Text('', key='-HD-SP-')
    xgf_text = sg.Text('Expected goals for:')
    xgf = sg.Text('', key='-XGF-')
    xgfp_text = sg.Text('Expected goals for %:')
    xgfp = sg.Text('', key='-XGFP-')
    asp_txt = sg.Text('Adjusted save %:')
    asp = sg.Text('', key='-ASP-')
    xga_txt = sg.Text('Expected goals against:')
    xga = sg.Text('', key='-XGA-')

    layout = [
        [player_num_txt, player_num, srch_btn],
        [player_name],
        [gf_p_text, gf_p],
        [all_shot_p_text, all_shot_p],
        [shot_p_text, shot_p],
        [hdsp_txt, hdsp],
        [xgf_text, xgf],
        [xgfp_text, xgfp],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Text('')],
        [asp_txt, asp],
        [xga_txt, xga]
    ]
    return sg.Window("[Your Team's] Analytics Tracker - View Statistics", layout, size=(1200,500), finalize = True, enable_close_attempted_event = True, icon='./content/genlogo.ico', element_justification='c')


window1 = home_win()
window2 = None

# Oscillators for PP and PK
pp_oscil = False
pk_oscil = False

# Main program loop
while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Exit':
        try:
            window.close()
            print('User exit command')
        except AttributeError:
            exit()
    if window == window2:
        window2 = None

    # Launches the roster window
    if event == '-ROSTER-': 
        # Ensures the season name isn't blank
        if values['-YEAR-'] == '2023-24':
            window2 = roster_win()
            file = values['-YEAR-'] + '.pickle'
        else:
            sg.popup('Please enter a valid season name')
        
    
    # Launches the roster window
    if event == '-NEW-GAME-': 
        # Ensures the season name isn't blank
        if values['-YEAR-'] == '2023-24':
            window2 = new_game()
            file = values['-YEAR-'] + '.pickle'
        else:
            sg.popup('Please enter a valid season name')

    # Launches the view stats window
    if event == '-VIEW-STATS-':
        # Ensures the season name isn't blank
        if values['-YEAR-'] == '2023-24':
            window2 = stat_win()
            file = values['-YEAR-'] + '.pickle'
        else:
            sg.popup('Please enter a valid season name')
    
    # Oscillators for PP and PK - CURRENTLY NOT BEING USED
    if event == '-PP-':
        pp_oscil = not pp_oscil
        if pp_oscil:
            window['-PP-'].update(button_color=('darkred', 'white'))
        else:
            window['-PP-'].update(button_color=('white', 'darkred'))
    
    if event == '-PK-':
        pk_oscil = not pk_oscil
        if pk_oscil:
            window['-PK-'].update(button_color=('darkred', 'white'))
        else:
            window['-PK-'].update(button_color=('white', 'darkred'))
    

    # Game events
    if event == '-HDGF-':
        date = values['-D-IN-']
        utils.add_event(file, date, 'HDGF', values['-F1-'], values['-F2-'], values['-F3-'], values['-D1-'], values['-D2-'], values['-G-'], values['-EXT-'])
    if event == '-LDGF-':
        date = values['-D-IN-']
        utils.add_event(file, date, 'LDGF', values['-F1-'], values['-F2-'], values['-F3-'], values['-D1-'], values['-D2-'], values['-G-'], values['-EXT-'])
    if event == '-HDGA-':
        date = values['-D-IN-']
        utils.add_event(file, date, 'HDGA', values['-F1-'], values['-F2-'], values['-F3-'], values['-D1-'], values['-D2-'], values['-G-'], values['-EXT-'])
    if event == '-LDGA-':
        date = values['-D-IN-']
        utils.add_event(file, date, 'LDGA', values['-F1-'], values['-F2-'], values['-F3-'], values['-D1-'], values['-D2-'], values['-G-'], values['-EXT-'])

    if event == '-HDSF-':
        date = values['-D-IN-']
        utils.add_event(file, date, 'HDSF', values['-F1-'], values['-F2-'], values['-F3-'], values['-D1-'], values['-D2-'], values['-G-'], values['-EXT-'])
    if event == '-LDSF-':
        date = values['-D-IN-']
        utils.add_event(file, date, 'LDSF', values['-F1-'], values['-F2-'], values['-F3-'], values['-D1-'], values['-D2-'], values['-G-'], values['-EXT-'])
    if event == '-HDSA-':
        date = values['-D-IN-']
        utils.add_event(file, date, 'HDSA', values['-F1-'], values['-F2-'], values['-F3-'], values['-D1-'], values['-D2-'], values['-G-'], values['-EXT-'])
    if event == '-LDSA-':
        date = values['-D-IN-']
        utils.add_event(file, date, 'LDSA', values['-F1-'], values['-F2-'], values['-F3-'], values['-D1-'], values['-D2-'], values['-G-'], values['-EXT-'])
    
    if event == '-MHDSF-':
        date = values['-D-IN-']
        utils.add_event(file, date, 'MHDSF', values['-F1-'], values['-F2-'], values['-F3-'], values['-D1-'], values['-D2-'], values['-G-'], values['-EXT-'])
    if event == '-MLDSF-':
        date = values['-D-IN-']
        utils.add_event(file, date, 'MLDSF', values['-F1-'], values['-F2-'], values['-F3-'], values['-D1-'], values['-D2-'], values['-G-'], values['-EXT-'])
    if event == '-MHDSA-':
        date = values['-D-IN-']
        utils.add_event(file, date, 'MHDSA', values['-F1-'], values['-F2-'], values['-F3-'], values['-D1-'], values['-D2-'], values['-G-'], values['-EXT-'])
    if event == '-MLDSA-':
        date = values['-D-IN-']
        utils.add_event(file, date, 'MLDSA', values['-F1-'], values['-F2-'], values['-F3-'], values['-D1-'], values['-D2-'], values['-G-'], values['-EXT-'])

    # Fires when they click the add player button on the roster screen
    if event == '-ADDPLY-':
        if values['-RPOS-'].lower() == 'f' or values['-RPOS-'].lower() == 'c' or values['-RPOS-'].lower() == 'lw' or values['-RPOS-'].lower() == 'rw' or values['-RPOS-'] == 'w':
            pos = 'F'
        elif values['-RPOS-'].lower() == 'd' or values['-RPOS-'].lower() == 'rd' or values['-RPOS-'].lower() == 'ld':
            pos = 'D'
        elif values['-RPOS-'].lower() == 'g':
            pos = 'G'
        else:
            sg.popup('Please enter a valid position.')

        if values['-RNAME-'] == '':
            sg.popup('Please enter a name')
        else:
            name = values['-RNAME-']

        if values['-RNUM-'] == '':
            sg.popup('Please enter a number')
        else:
            num = values['-RNUM-']
        
        rfile = 'roster_' + file
        utils.add_player(rfile, name, num, pos)
        event = '-LOADRST-'
    
    # Fires when they click the remove player button on the roster screen
    if event == '-RMVPLY-':
        if values['-RNAME-'] == '':
            sg.popup('Please enter a player name')
        else:
            name = values['-RNAME-']
        
        rfile = 'roster_' + file
        removed = utils.remove_player(rfile, name)
        if removed:
            sg.popup(f'{name} was removed from the roster.')
        else:
            sg.popup(f"Could not find {name} on the roster.")
        event = '-LOADRST-'

    # Fires when they click the load roster button on the roster screen or when they add/remove a player
    if event == '-LOADRST-':
        rfile = 'roster_' + file
        players = utils.display_roster(rfile)
        window['-RF1-'].update(players[0])
        window['-RF2-'].update(players[1])
        window['-RF3-'].update(players[2])
        window['-RF4-'].update(players[3])
        window['-RF5-'].update(players[4])
        window['-RF6-'].update(players[5])
        window['-RF7-'].update(players[6])
        window['-RF8-'].update(players[7])
        window['-RF9-'].update(players[8])
        window['-RF10-'].update(players[9])
        window['-RF11-'].update(players[10])
        window['-RF12-'].update(players[11])
        window['-RF13-'].update(players[12])
        window['-RF14-'].update(players[13])
        window['-RF15-'].update(players[14])
        window['-RD1-'].update(players[15])
        window['-RD2-'].update(players[16])
        window['-RD3-'].update(players[17])
        window['-RD4-'].update(players[18])
        window['-RD5-'].update(players[19])
        window['-RD6-'].update(players[20])
        window['-RD7-'].update(players[21])
        window['-RD8-'].update(players[22])
        window['-RG1-'].update(players[23])
        window['-RG2-'].update(players[24])
        window['-RG3-'].update(players[25])
        window['-RG4-'].update(players[26])
        
    # Fires when they use the search button on the view stats screen
    if event == '-SRCH-BTN-':
        data = utils.get_stats(file, values['-NUM-SRCH-'])
        rfile = 'roster_' + file
        position = utils.get_position(rfile, values['-NUM-SRCH-'])
        window['-SRCH-NAME-'].update(data[0])
        if position == 'F' or position == 'D':
            window['-GF-P-'].update(str(data[1]) + '%')
            window['-SH-P-'].update(str(data[2]) + '%')
            window['-OSH-P-'].update(str(data[3]) + '%')
            window['-HD-SP-'].update(str(data[4]) + '%')
            window['-XGF-'].update(str(data[5]))
            window['-XGFP-'].update(str(data[6]) + '%')
            window['-ASP-'].update('')
            window['-XGA-'].update('')
        else:
            window['-GF-P-'].update('')
            window['-SH-P-'].update('')
            window['-OSH-P-'].update('')
            window['-HD-SP-'].update('')
            window['-XGF-'].update('')
            window['-XGFP-'].update('')
            window['-ASP-'].update(str(data[7]) + '%')
            window['-XGA-'].update(str(data[8]))
    
        