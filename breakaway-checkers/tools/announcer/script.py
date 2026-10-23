# The announcer's script: clip id -> (what Piper reads, style). Style "x" is an excited call (faster, a touch higher).
# Team, player-name and number clips are generated from the lists below; the game strings them together (see VOX in the game).
TEAMS=[("BRI","Bridgeport Islanders","Islanders"),("CLT","Charlotte Checkers","Checkers"),("HFD","Hartford Wolf Pack","Wolf Pack"),
("HER","Hershey Bears","Bears"),("LV","Lehigh Valley Phantoms","Phantoms"),("PRO","Providence Bruins","Bruins"),("SPR","Springfield Thunderbirds","Thunderbirds"),
("WBS","Wilkes-Barre Scranton Penguins","Penguins"),("BEL","Belleville Senators","Senators"),("CLE","Cleveland Monsters","Monsters"),("LAV","Laval Rocket","Rocket"),
("ROC","Rochester Americans","Americans"),("SYR","Syracuse Crunch","Crunch"),("TOR","Toronto Marlies","Marlies"),("UTC","Utica Comets","Comets"),
("CHI","Chicago Wolves","Wolves"),("GR","Grand Rapids Griffins","Griffins"),("IA","Iowa Wild","Wild"),("MB","Manitoba Moose","Moose"),("MIL","Milwaukee Admirals","Admirals"),
("RFD","Rockford Ice Hogs","Ice Hogs"),("TEX","Texas Stars","Stars"),("ABB","Abbotsford Canucks","Canucks"),("BAK","Bakersfield Condors","Condors"),
("CGY","Calgary Wranglers","Wranglers"),("CV","Coachella Valley Firebirds","Firebirds"),("COL","Colorado Eagles","Eagles"),("HSK","Henderson Silver Knights","Silver Knights"),
("ONT","Ontario Reign","Reign"),("SD","San Diego Gulls","Gulls"),("SJ","San Jose Barracuda","Barracuda"),("TUC","Tucson Roadrunners","Roadrunners")]
# how Piper should say a few of the team words
SAY={"Wilkes-Barre":"Wilks-Berry","Laval":"Lah-val","Coachella":"Coe-chella"}
NAMES="NOVAK LAROCHE BERGMAN MACKAY DUBOIS SORENSEN LINDQVIST FORTIER HALVORSEN KOWALSKI BRENNAN TREMBLAY OKAFOR MARCHAND EKLUND REILLY STROMBERG CALLAHAN DESROSIERS HOLM PELLETIER VASQUEZ AHONEN GALLAGHER BOUCHARD NYSTROM KRAVCHUK OSULLIVAN LEMIEUX HARTLEY VIRTANEN DAWSON BEAULIEU MORENO KARLSSON PATTERSON GAUTHIER ROWE SATO FINNEGAN".split()
NAMESAY={"LAROCHE":"La Rosh","MACKAY":"Mack-Eye","DUBOIS":"Doo-bwah","LINDQVIST":"Lindkvist","FORTIER":"Fort-yay","TREMBLAY":"Trom-blay","MARCHAND":"Mar-shand",
 "DESROSIERS":"Day-rose-yay","PELLETIER":"Pell-tee-ay","AHONEN":"Ah-ho-nen","BOUCHARD":"Boo-shard","OSULLIVAN":"O'Sullivan","LEMIEUX":"Le-myoo","BEAULIEU":"Bowl-yoo","GAUTHIER":"Go-tee-ay","KRAVCHUK":"Krav-chuck","SATO":"Sah-toe","VIRTANEN":"Veer-tah-nen","OKAFOR":"Oh-kah-for"}
FIXED={
 # the opening call, then the two clubs
 "c_welcome":("Welcome to the shootout!",""),"c_shootouttime":("It's shootout time!",""),"c_herewego":("Here we go!",""),"c_versus":("versus","l"),
 # each attempt
 "c_herecomes":("Here comes",""),"c_upnext":("Up next,",""),"c_pickup":("picks up the puck at center ice.",""),"c_suddendeath":("Sudden death!","x"),
 # moves
 "m_toedrag":("Toe drag!","x"),"m_pulls":("Pulls it across!","x"),"m_spin":("Spin o rama!","x"),"m_spins":("He spins!","x"),"m_picks":("He picks it up!","x"),
 "m_lacrosse":("Lacrosse style!","x"),"m_michigan":("Here comes the Michigan!","x"),"m_bhcut":("Backhand cut!","x"),"m_fhcut":("Forehand cut!","x"),"m_hardcut":("Hard cut!","x"),
 # goals
 "g_walks":("He walks it in!","x"),"g_squeaks":("It squeaks through!","x"),"g_offgoalie":("Off the goalie, and in!","x"),"g_postin":("Off the post, and in!","x"),
 "g_postandin":("Post and in!","x"),"g_topshelf":("Top shelf!","x"),"g_cookies":("Top shelf, where mama hides the cookies!","x"),"g_topcorner":("Picks the top corner!","x"),
 "g_alongice":("Along the ice, and in!","x"),"g_lowin":("Low, and in!","x"),"g_scores":("He scores!","x"),"g_corner":("Picks the corner!","x"),"g_scores2":("Scores!","x"),
 "g_rocket":("What a rocket!","x"),"g_whatamove":("What a move!","x"),"c_scores":("scores!","x"),"g_buries":("buries it!","x"),
 # saves
 "s_pad":("Pad save!","x"),"s_butterfly":("Down in the butterfly, and the save!","x"),"s_blocker":("Blocker save!","x"),"s_piece":("Gets a piece of it!","x"),
 "s_kicked":("Kicked away!","x"),"s_desp":("Desperation save!","x"),"s_how":("How did he stop that?","x"),"s_poke1":("Poke check! Stripped him clean!","x"),
 "s_poke2":("Poke checked!","x"),"s_smother":("Smothered!","x"),"s_swallow":("Swallowed up!","x"),"s_dies":("It dies before the net.",""),"s_nosteam":("No steam on that one.",""),
 "s_save":("Save!","x"),"s_whatastop":("What a stop!","x"),
 # misses
 "x_post":("Off the post! Stays out!","x"),"x_iron":("Rings it off the iron!","x"),"x_wide":("Wide!",""),"x_justwide":("Just wide!",""),"x_misses":("Misses the net.",""),
 "x_clock":("The clock runs out!",""),"x_held":("Held it too long!",""),"x_carried":("Carried it wide!",""),"x_nogoal":("No goal.",""),
 "c_isstopped":("is stopped.",""),"c_nogoalfor":("No goal for",""),"c_cantbeat":("can't beat the goalie.",""),
 # the end of the game
 "e_thatsit":("And that's the game!","x"),"e_gameover":("Game over!","x"),"e_bench":("Here comes the whole bench!","x"),
 # fights
 "f_gloves":("Uh oh, the gloves might come off here.",""),"f_shoving":("Some pushing and shoving before the shootout!",""),"f_drop":("And they drop the gloves!","x"),
 "f_fight":("Here we go, a fight!","x"),"f_wins":("wins that one, and the crowd loves it!","x"),
 "c_cmton":("Commentary on.",""),
 # v51: more versions of the common calls, and what's at stake on an attempt
 "c_settle":("Let's settle this in a shootout!",""),"c_fiveshooters":("Five shooters a side. Let's go!",""),"c_onfeet":("The building is on its feet for the shootout!",""),
 "c_nextshooter":("Next shooter,",""),"c_nowskating":("Now skating in,",""),"c_takes":("takes the puck.",""),
 "c_scorewins":("Score here, and it's over!","x"),"c_canwin":("He can win it right here!","x"),"c_mustscore":("He has to score!","x"),"c_missover":("Miss, and it's over!","x"),
 "m_hands":("Look at those hands!","x"),"m_dangles":("He dangles!","x"),"m_leaning":("He's got the goalie leaning!","x"),
 "g_goal":("Goal!","x"),"g_initgoes":("In it goes!","x"),"g_finish":("What a finish!","x"),"g_upstairs":("Goes upstairs!","x"),"g_underbar":("Right under the bar!","x"),
 "g_slides":("Slides it home!","x"),"g_laser":("A laser!","x"),"g_beauty":("Oh, what a beauty!","x"),"g_undressed":("He undressed him!","x"),
 "s_robbed":("Robbed!","x"),"s_door":("He shuts the door!","x"),"s_big":("Big save!","x"),"s_saysno":("The goalie says no!","x"),"s_stoned":("Stoned him!","x"),
 "x_timeup":("Time's up! No shot!",""),"x_waited":("Waited too long!",""),"x_cantget":("Can't get it on net!",""),"x_offtarget":("Off target.",""),
 "e_thatlldoit":("That'll do it!","x"),"e_whatafinish":("What a finish to this one!","x"),
 # v52: the Cup
 "c_cupchamps":("are Calder Cup champions!","x"),
 # v63: banner night, rivalry nights, scouting reports and All-Star Skills Night
 "b_banner":("Before the puck drops, the champions raise their banner to the rafters!",""),
 "r_rivalry":("It's rivalry night!","x"),"r_dontlike":("These two clubs do not like each other!","x"),"r_bragging":("Bragging rights on the line tonight!","x"),
 "w_scout":("Right where the scouting report said!","x"),"w_found":("He found the weak spot!","x"),
 "s_welcome":("Welcome to All-Star Skills Night!","x"),"s_hardest":("First up, the hardest shot competition!",""),
 "s_accuracy":("Now it's accuracy shooting. Four targets, high and low!",""),
 "s_rocket":("What a rocket!","x"),"s_fly":("He let that one fly!","x"),"s_missnet":("Oh, he missed the net!",""),
 "s_allfour":("All four targets down!","x"),"s_target":("Target!","x"),"s_hitit":("He hits it!","x"),"s_wins":("He wins the event!","x"),
}
NUMW="zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS="_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
def numword(n):return NUMW[n] if n<20 else TENS[n//10]+("" if n%10==0 else "-"+NUMW[n%10])
def say(t):
    for a,b in SAY.items():t=t.replace(a,b)
    return t
def script():
    S=dict(FIXED)
    for ab,full,nick in TEAMS:
        S["t_full_"+ab]=(say("The "+full+"!"),"")
        S["t_goal_"+ab]=(nick+" goal!","x")
        S["t_win_"+ab]=("The "+nick+" win it!","x")
    for n in NAMES:S["n_"+n]=(NAMESAY.get(n,n.capitalize()),"n")
    for k in range(1,100):S["num_%d"%k]=("Number "+numword(k),"n")
    return S
if __name__=="__main__":
    S=script();print(len(S),"clips,",sum(len(t) for t,_ in S.values()),"characters")
