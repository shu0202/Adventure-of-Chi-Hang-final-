transform hit:
    linear 0.05 xoffset 20
    linear 0.05 xoffset -20
    linear 0.05 xoffset 0

transform shake:
    linear 0.1 xoffset 30
    linear 0.1 xoffset -30
    linear 0.1 xoffset 0

init python :
    def eyewarp(x) :
        return x**1.33
    eye_open = ImageDissolve("eye.png", .5, ramplen=128, reverse=False, time_warp=eyewarp)

image rino_special2 :
    "rino1.png" with dissolve
    1.2
    "rino3_b.png" with dissolve

label ch1 :
    scene black
    show schooldoor
    with dissolve
    play music "as.mp3" loop
    window show dissolve
    $ quick_menu = True
    "還剛踏進校門，一排風紀整齊地露出溫柔的微笑..."
    "{color=#66661b}風紀們" "「同學，檢查校服呀」"
    show yuusuke1 at left:
        xalign 0.2
    with dissolve
    show akari2_c at right :
        xalign 0.8
        alpha 0.7
    with dissolve
    h "「呀糟糕...我好像忘了要當值」"
    show yuusuke1:
        alpha 0.7
    with dissolve
    show akari2_c :
        alpha 1.0
    with dissolve
    a "「雄介...就説你啦」"
    show akari2_c :
        alpha 0.7
    with dissolve
    "{color=66661b}風紀" "「算啦，灝楠，放下書包快點過來吧」"
    "{color=66661b}風紀" "「其他人過來，照舊老規矩，校章、皮帶、白襪」"
    c "「大鑊...」"
    "我轉身把校章扣好"
    "{color=66661b}風紀" "「嗯...{w}我當作沒看見了，過去吧」"
    show akari2_c :
        alpha 1.0
    with dissolve
    a "「喂志恆，能先幫我把袋放回課室吧，{p}\ \ \ 我先看一下壁報有沒有被風吹壞，在學會攤位等你呢」"
    hide akari2_c
    with dissolve
    show yuusuke1 :
        alpha 1.0
    with dissolve
    h "「我的也拜託你了，我的站崗要遲到了啦...」"
    hide yuusuke1
    with dissolve
    c "「喂，你們......」"
    "少年看著兩個迅速離去的人影，只能無奈地嘆息"
    c "「呀...{w}我難道額上刻着工具人啦...」"
    $ quick_menu = True
    window hide dissolve
    hide schooldoor
    with dissolve
    show Schoolco
    with dissolve
    window show dissolve
    $ quick_menu = True
    "於是少年就\"左擁右抱\"地走在走廊上"
    show rino1_c
    with dissolve
    r "「咦？那個是志恆前輩？」"
    r "「嗯，果然還是樂於助人呢」"
    hide rino1_c
    with dissolve
    $ quick_menu = False
    window hide dissolve
    hide Schoolco
    with dissolve
    stop music fadeout 1.0
    show JCAD
    with dissolve
    play music "as.mp3" loop
    window show dissolve
    $ quick_menu = True
    show akari1
    with dissolve
    a "「好～{w}這裏也完成了」"
    a "「咦？奇怪了，志恆這麼久還不來......」"
    a "「嗯...看來還是先回課室...{nw}」"
    show akari1 :
        linear 0.3 xalign 0.2
    show akari6_e at left:
        xalign 0.2
        alpha 0.7
    hide akari1
    show yuusuke1 at right:
        xalign 0.8
    with dissolve
    stop music fadeout 1.0
    play music "asf.mp3" loop
    h "「Yo！」"
    show akari6_e :
        alpha 1.0
    with dissolve
    show yuusuke1 at right:
        alpha 0.7
        xalign 0.8
    with dissolve
    a "「哇！」"
    show akari3 at left:
        xalign 0.2
    with dissolve
    hide akari6_e
    a "「那個...{w}風紀委員的責任好像不是嚇人呢...{p}\ \ \ {cps=10}灝！楠！先生！？{/cps}」"
    show akari3 :
        alpha 0.7
    with dissolve
    show yuusuke1 :
        alpha 1.0
    with dissolve
    h "「嘛～嘛～嘛，先别發怒」"
    h "「志恆叫我傳達給你，他現在在課室開功課研討會呀，完成了才下來」"
    show akari_special at left :
        xalign 0.2
    with dissolve
    hide akari3
    a "「{cps=10}呀，嘖，{/cps}{w=0.5}那個志恆...」"
    show akari1_c at left :
        alpha 0.7
        xalign 0.2
    hide akari_special
    show yuusuke1 :
        alpha 1.0
    with dissolve
    h "「嘛，畢竟是\"那個志恆\"，哈哈」"
    show akari3_b at left :
        xalign 0.2
    with dissolve
    hide akari1_c
    show yuusuke1 :
        alpha 0.7
    with dissolve
    a "「不是那個意思啦...{w}志恆也不是真的這樣特殊的吧？」"
    show akari3_b :
        alpha 0.7
    with dissolve
    show yuusuke1 :
        alpha 1.0
    with dissolve
    h "「真的？{w}那來看看今天早上的愷婷大學霸如何\ {cps=5}對 侍 他 呢{/cps}～」"
    show akari6_b at left :
        xalign 0.2
    with dissolve
    hide akari3_b
    show yuusuke1 :
        alpha 0.7
    with dissolve
    a "「你這個風紀就只懂駁嘴？你有空為什麼不去......」"
    show akari3_c at left :
        xalign 0.2
    with dissolve
    hide akari6_b
    a "「就那邊的那一個，校服不合規定吧！」"
    show akari3_c :
        alpha 0.7
    with dissolve
    show yuusuke1 :
        alpha 1.0
    with dissolve
    h "「是嗎，是嗎，我看不見額？{p}\ \ \ 我還是去看看志恆好了」"
    hide yuusuke1
    with moveoutright
    show akari6_e at left :
        xalign 0.2
    with dissolve
    hide akari3_c
    a "「不要逃啦！」"
    hide akari6_e
    with moveoutright
    $ quick_menu = False
    window hide dissolve
    hide JCAD
    with dissolve
    stop music fadeout 1.0
    show inschool
    with dissolve
    play music "asf.mp3" loop
    window show dissolve
    $ quick_menu = True
    show akari1 at right :
        xalign 0.8
    with dissolve
    show yuusuke1 at left :
        alpha 0.7
        xalign 0.2
    with dissolve
    a "「志恆...我就知道你會這樣」"
    show akari1 :
        alpha 0.7
    with dissolve
    show yuusuke1 :
        alpha 1.0
    with dissolve
    h "「是我告訴你的吧，哈哈」"
    show akari3_b at right :
        xalign 0.8
    with dissolve
    hide akari1
    show yuusuke1 at hit
    "爆頭critical hit"
    show akari3_b :
        alpha 0.7
    with dissolve
    h "「好痛啊...」"
    show akari3 at right :
        xalign 0.8
    with dissolve
    hide akari3_b
    show yuusuke1 :
        alpha 0.7
    with dissolve
    a "「自由時間只剩下二十分鐘，壁報還沒完成，{p}\ \ \ 我們學會今天還用招人啦？」"
    show akari3 :
        alpha 0.7
    with dissolve
    c "「啊......{w}沒辦法呀，我再多欠一份就要留堂了...」"
    show akari5_c at right :
        xalign 0.8
    with dissolve
    hide akari3
    a "「呀...你真是的！！」"
    show akari1_c at right :
        xalign 0.8
    with dissolve
    hide akari5_c
    a "「沒辦法了，你之後再\"參考\"我的吧，{p}\ \ \ 是參考，別照抄呀！{w}快點收拾好下來，我在攤位等你」"
    show akari1_c :
        alpha 0.7
    with dissolve
    c "「{cps=5}嗯...{/cps}呀！{w}好了，灝楠也過來幫忙吧！」"
    show yuusuke1 :
        alpha 1.0
    with dissolve
    h "「呃？我？{w}為什麼嘛」"
    show yuusuke1 :
        alpha 0.7
    with dissolve
    c "「不要問啦，快走啦」"
    hide yuusuke1
    with dissolve
    hide akari1_c
    with dissolve
    "於是三人奔跑着回去攤位，就是為了趕壁報的進度。"
    $ quick_menu = False
    window hide dissolve
    hide inschool
    with dissolve
    stop music fadeout 1.0
    show JCAD1
    with dissolve
    window show dissolve
    $ quick_menu = True
    "\"20xx年學會聯招正式開始\"{p}\ 在學生會陳某老師的一聲號令之下，人潮湧進了這狹小的操場。{p}\ 同學之間的吵鬧聲象徵著學會之間戰爭的開始。"
    show JCAD
    with dissolve
    play music"JCAD.mp3" loop
    hide JCAD1
    show akari5_c at center
    with dissolve
    a "「呀...{w}希望能招到部...」"
    show akari6 at center
    with dissolve
    hide akari5_c
    a "「喂志恆怎你還在做功課！？{w}學會聯招開始了呀」"
    show akari6 :
        alpha 0.7
    with dissolve
    c "「小息後要交，你不知道嗎？......」"
    c "「呀對了，你一向功課一下子就完成了，{p}\ \ \ 從不理會繳交日期的吧」"
    hide akari6
    with dissolve
    $ quick_menu = False
    window hide dissolve
    hide JCAD
    with dissolve
    window show dissolve
    $ quick_menu = True
    "數分鐘後"
    $ quick_menu = False
    window hide dissolve
    show JCAD
    with dissolve
    window show dissolve
    $ quick_menu = True
    show akari5 at center
    with dissolve
    a "「怎麼其他同學直接走過我們攤位，{w}都沒多看一眼...{p}\ \ \ 這樣下去可不行呢...」"
    show akari1 at center
    with dissolve
    hide akari5
    a "「要不這樣吧」"
    show akari1 :
        alpha 0.7
    with dissolve
    c "「什麼？」"
    show akari1 :
        alpha 1.0
    with dissolve
    a "「我到那邊招覽一下人群，{p}\ \ \ 有人入部的話你能替我寫下他的個人資料嗎？」"
    menu :
        "「呃...好吧」" :
            jump nstay
        "「呃...不要吧」" :
            jump stay
label nstay :
    show akari1 :
        alpha 0.7
    with dissolve
    c "「呃...好吧，反正暫時我也留守在這裏了」"
    show akari5 at center
    with dissolve
    hide akari1
    a "「總感覺有點不能依靠...」"
    a "「要是這樣我怕同學都被你趕工的樣子嚇到，還是算了」"
    $ quick_menu = False
    window hide dissolve
    show 5min
    with dissolve
    pause 3.0
    hide 5min
    with dissolve
    window show dissolve
    $ quick_menu = True
    show akari8_c
    with dissolve
    hide akari5
    a "「呀呀呀！{w}還是不行，要靠你在這裏看一會了」"
    show akari8_c :
        alpha 0.7
    with dissolve
    c "「嗯？忍不住了？」"
    show akari3_b at center
    with dissolve
    hide akari8_c
    a "「呃！」"
    show akari4_b at center
    with dissolve
    hide akari3_b
    a "「{cps=5}你...{/cps}怎知道的...」"
    show akari4_b :
        alpha 0.7
    with dissolve
    c "「嘛，{w}看你坐着好像佷辛苦的樣子」"
    c "「學會聯招才剛開始，{w}在開頭能不能招到部員，{p}\ \ \ 真的是那麼重要嗎？」"
    show akari6_b at center
    with dissolve
    hide akari4_b
    a "「呀！！！{w}早知道你是這樣， {p}\ \ \ 我只是想去洗手間啦...」"
    show akari6_b :
        alpha 0.7
    with dissolve
    c "「{cps=10}嗯......{/cps}什麼！！！？」"
    hide akari6_b
    with dissolve
    jump ch1_2

label stay :
    $ a_pts = a_pts + 5
    show akari1 :
        alpha 0.7
    with dissolve
    c "「呃...不要吧，要是不懂回答同學詢問，{w}趕走準部員就糟了吧」"
    show akari1_c at center
    with dissolve
    hide akari1
    a "「想不到這傢伙還有點責任感...」"
    "愷婷輕聲說著"
    show akari1_c :
        alpha 0.7
    with dissolve
    c "「嗯？你剛說啥？」"
    show akari2_c at center
    with dissolve
    hide akari1_c
    a "「嘛，沒什麼，{w}就拜託你好了～」"
    hide akari2_c
    with dissolve
    c "「等...」"
    jump ch1_2

label ch1_2 :
    $ quick_menu = False
    window hide dissolve
    hide JCAD
    with dissolve
    pause 0.5
    show JCAD
    with dissolve
    window show dissolve
    $ quick_menu = True
    c "「呀...那個愷婷也真是的」"
    c "「媽，這題又要怎樣做...」"
    r "「嗯，{w}把X=6放在一式中就行了」"
    c "「所以y就等於...」"
    c "「呃！？{w}芷柔同學，你是什麼時候到的」"
    show rino1_c at center
    with dissolve
    r "「就在看到你們會長輕飄飄～的跑走了之後」"
    show rino1_c :
        alpha 0.7
    with dissolve
    c "「喔...{w}咦，{w}旁邊的這位女生是...」"
    show rino1_c :
        alpha 0.7
        linear 0.15 xalign 0.3
    with dissolve
    show hinaka1 at right :
        xalign 0.7
    with dissolve
    stop music fadeout 1.0
    play music "hinaka.mp3" loop
    y "「嗨！志恆前輩！」"
    show rino1_c :
        alpha 1.0
    with dissolve
    show hinaka1 :
        alpha 0.7
    with dissolve
    r "「噗，噗...」"
    show rino1_c :
        alpha 0.7
    with dissolve
    c "「怎麼啦」"
    show rino1 at left :
        xalign 0.3
    with dissolve
    hide rino1_c
    r "「呀抱歉抱歉，{w}這是我的好姫友，子彤」"
    show rino1 :
        alpha 0.7
    with dissolve
    show hinaka2 at right :
        xalign 0.7
    with dissolve
    hide hinaka1
    y "「喂呀～」"
    show rino1 :
        alpha 1.0
    with dissolve
    show hinaka2 :
        alpha 0.7
    with dissolve
    r "「就測驗一下吧」"
    "芷柔在子彤耳邊喃喃細語"
    show rino1 :
        alpha 0.7
    with dissolve
    c "「{cps=5}呃...{/cps}那個？」"
    show rino3_c at left :
        xalign 0.3
    with dissolve
    hide rino1
    r "「之前跟你說過我已經限額滿了的吧...？」"
    show rino1 at left :
        xalign 0.3
    with dissolve
    hide rino3_c
    r "「現在...好像可以了」"
    show rino1 :
        alpha 0.7
    with dissolve
    c "「是...發生了什麼是事情嗎？」"
    show hinaka1 at right :
        alpha 1.0
        xalign 0.7
    with dissolve
    hide hinaka2
    y "「呀啦～{w}因為我家芷柔不幸跟戲劇部那邊反......」"
    "芷柔連忙捂著子彤的嘴"
    show hinaka1 :
        alpha 0.7
    with dissolve
    show rino3_b at left :
        xalign 0.3
    with dissolve
    hide rino1
    r "「總之現在是可以加入啦～」"
    show rino3_b :
        alpha 0.7
    with dissolve
    c "「嗯...{w}那麼請你把個人資料寫在這裏吧」"
    show rino3_c at left :
        xalign 0.3
    with dissolve
    hide rino3_b
    r "(糟了，好像忘了向其他同學推介...)"
    show rino1_c at left :
        xalign 0.3
    with dissolve
    hide rino3_c
    r "「對了，{w}子彤之前不是説有興趣的嗎？」"
    show rino1_c :
        alpha 0.7
    with dissolve
    show hinaka1 :
        alpha 1.0
    with dissolve
    y "「呃...是這樣嗎？{p}\ \ \ 雖然看起來也蠻有趣就是了」"
    show rino1_c :
        alpha 1.0
    with dissolve
    show hinaka1 :
        alpha 0.7
    with dissolve
    r "「嗯那就加入好了」"
    "芷柔快速地寫下子彤的名字"
    show rino1_c :
        alpha 0.7
    with dissolve
    c "「你還真是找到人呢，{w}這下子也放下心頭大石了」"
    show rino3_c at left :
        xalign 0.3
    with dissolve
    hide rino1_c
    r "「什麼\"你還真是\"，{w}不要少看你的後輩嘛」"
    show rino3_c :
        alpha 0.7
    with dissolve
    c "「是了，是了，{w}就你最厲害，{p}\ \ \ 難道要給你摸頭嗎？」"
    show rino3_b at left :
        xalign 0.3
    with dissolve
    hide rino3_c
    r "「......」"
    show rino3_b :
        alpha 0.7
    with dissolve
    c "「......」"
    show hinaka1 :
        alpha 1.0
    with dissolve
    y "「呐芷柔，就不覺得進度有點太...」"
    "子彤的最嘴再次被捂著"
    show hinaka1 :
        alpha 0.7
    with dissolve
    show rino1_b at left :
        xalign 0.3
    with dissolve
    hide rino3_b
    r "「{cps=10}嘛！...{/cps}我跟子彤再去周圍看一下，{w}拜！」"
    show rino1_b :
        alpha 0.7
    with dissolve
    c "「嗯，再見」"
    hide rino1_b
    with dissolve
    show hinaka1 :
        alpha 1.0
    with dissolve
    y "「拜拜志恆前輩！」"
    hide hinaka1
    with dissolve
    c "「嗯...{w}怎女孩子穿褲了，{p}\ \ \ 是動漫學會的惡搞活動？」"
    $ quick_menu = False
    window hide dissolve
    hide JCAD
    with dissolve
    stop music fadeout 1.0
    window show dissolve
    $ quick_menu = True
    "幾分鐘後"
    $ quick_menu = False
    window hide dissolve
    show JCAD
    with dissolve
    play music "JCAD.mp3" loop
    show akari2 at center
    with dissolve
    window show dissolve
    $ quick_menu = True
    a "「噢！！！志恆！{w}你真的招到了！」"
    show akari2 :
        alpha 0.7
    with dissolve
    c "「雖然是自動送上門的就是了...」"
    show akari1 at center
    with dissolve
    hide akari2
    a "「{cps=5}芷柔...{/cps}上次教員室門外的那個？」"
    a "「人家是女孩子啦，這樣說不好吧」"
    show akari1 :
        alpha 0.7
    with dissolve
    c "「還有那個叫子彤什麼的來着，{p}\ \ \ 釘了在後面的那一頁」"
    show akari1 :
        alpha 1.0
    with dissolve
    a "「噢！！！志恆！竟然是兩個」"
    show akari7_c at center
    with dissolve
    hide akari1
    a "「雖然這個名字沒有太大印象呢...」"
    show akari3 at center
    with dissolve
    hide akari7_c
    a "「我現在就交給老師，{w}看他還有什麼籍口！」"
    hide akari3
    with dissolve
    c "「呀...{w}又走了，{w}這也算是部長嗎，{p}\ \ \ 怎連核對一下資料也不用...」"
    c "「也算了，話說下一題又該怎樣做」"
    stop music fadeout 1.0
    "上課的鈴聲結束了這片喧鬧，{p}回到了平常幽靜的校園"
    $ quick_menu = False
    window hide dissolve
    hide JCAD
    with dissolve
    show inschool
    with dissolve
    play music "as.mp3" loop
    window show dissolve
    $ quick_menu = True
    c "「唉，只顧着學會，功課還是做不完...{p}\ \ \ 結果也唯有留堂了嗎...」"
    c "「如果愷婷知道我不能去幫她收拾攤位...{p}\ \ \ 說不定會捏死我吧」"
    show akari1 at center
    with dissolve
    a "「志恆你叫我？」"
    show akari1 :
        alpha 0.7
    with dissolve
    c "「今天看來是要留堂了，{w}至於攤位的善後...{p}\ \ \ 看來不能幫忙了」"
    show akari5 at center
    with dissolve
    hide akari1
    a "「果然呀...{w}但我一個人的話可能有點勉強...」"
    a "「你能找個人來幫忙？」"
    show akari5 :
        on hide:
            linear 0.2 xoffset-20
            linear 0.2 alpha 0.0
        alpha 0.7
    with dissolve
    c "「可以...」"
    c "(這下子麻煩了)"
    hide akari5
    pause 0.2
    "我轉身向坐在我背後的灝楠求助"
    show yuusuke1 at center :
        alpha 0.7
    with dissolve
    c "「唷，灝楠～{w}能幫忙攤位的善後？{p}\ \ \ 今天我要留堂...」"
    show yuusuke1 :
        alpha 1.0
    with dissolve
    h "「呃...我還要風紀的當值呢」"
    h "「你們剛才不是還有其他部員嗎？{w}叫他們就好吧」"
    menu :
        "「剛入部就叫他們幹活，不是太好吧」" :
            jump ncall
        "「好吧，我一會兒轉課室溜過去問下」" :
            jump ycall

label ncall :
    $ a_pts = a_pts + 1
    show yuusuke1 :
        alpha 0.7
    with dissolve
    c "「剛入部就叫他們幹活，不是太好吧」"
    show yuusuke1 :
        alpha 1.0
    with dissolve
    h "「但你認識的、而且能幫手的只有他們吧？」"
    show yuusuke1 :
        alpha 0.7
    with dissolve
    c "「{cps=5}嗯...{/cps}午飯時再看看怎麼辨吧」"
    show yuusuke1 :
        linear 0.2 xalign 0.2
    show akari2_c at right :
        xalign 0.8
    with dissolve
    a "「拜託了呢，志恆，{p}\ \ \ 雖然好像是你應份的」"
    show akari2_c :
        alpha 0.7
    with dissolve
    c "「真拿你們沒辦法」"
    hide yuusuke1
    with dissolve
    hide akari2_c
    with dissolve
    $ quick_menu = False
    window hide dissolve
    hide inschool
    with dissolve
    stop music fadeout 1.0
    jump ch1_3

label ycall :
    $ r_pts = r_pts + 1
    show yuusuke1 :
        alpha 0.7
    with dissolve
    c "「好吧，我一會兒轉課室溜過去問下」"
    hide yuusuke1
    with dissolve
    hide inschool
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    window hide dissolve
    show Schoolco
    with dissolve
    play music "as.mp3" loop
    window show dissolve
    $ quick_menu = True
    c "「芷柔同學！」"
    show rino1 at center
    with dissolve
    r "「呀，不就是清人前輩嗎？你怎麼來了」"
    show rino1 :
        alpha 0.7
    with dissolve
    c "「其實...{w}我有一些學會的事務想拜託你」"
    show rino3_b
    with dissolve
    hide rino1
    r "「{cps=10}嗯？...{/cps}話說直接叫我芷柔就行了，{p}\ \ \ 什麼什麼同學這樣...{w}不覺得很見外嘛？」"
    show rino3_b :
        alpha 0.7
    with dissolve
    c "「......」"
    c "(早前看其他同學都好像是叫她芷柔同學的吧？)"
    show rino2_b
    with dissolve
    hide rino3_b
    r "「喂！{w}別發呆啦～只是讓你叫個名字而己就這樣，{p}\ \ \ 要不收回好了」"
    show rino1
    with dissolve
    hide rino2_b
    r "「說啦，是有什麼想拜託我？」"
    show rino1 :
        alpha 0.7
    with dissolve
    c "「那個呢，我今天放學要留......{p}\ \ \ 有事要做，走不開，你能替我和赤理一起收拾攤位嗎？」"
    show rino3_c
    with dissolve
    hide rino1
    r "「{cps=10}這樣呀...{/cps}可惜我也沒空」"
    show rino1_c
    with dissolve
    hide rino3_c
    r "「要不我叫子彤午飯時去攤位找你，你自己問他吧」"
    show rino1_c :
        alpha 0.7
    with dissolve
    c "「好呀，謝了」"
    hide rino1_c
    with dissolve
    $ quick_menu = False
    window hide dissolve
    hide Schoolco
    with dissolve
    stop music fadeout 1.0
    jump ch1_3

label ch1_3 :
    show inschool
    with dissolve
    play music "asf.mp3" loop
    window show dissolve
    $ quick_menu = True
    "午飯時段的鈴聲響起，再次以學生的喧嘩聲為幽靜的校園注入活力"
    c "「呀～數學堂！{w}呀～放學又留堂！{p}\ \ \ 冇力啦我」"
    show akari8_c
    with dissolve
    a "「志恆别來這樣，你還要在攤位當值呀」"
    show inschool at shake
    show akari8_c :
        alpha 0.7
    with dissolve
    c "「欸～？不是已經夠部員了嗎？」"
    show akari2_c
    with dissolve
    hide akari8_c
    a "「哪有夠不夠的，不是越多越好的嘛～」"
    show inschool at shake
    show akari2_c :
        alpha 0.7
    with dissolve
    c "「好啦，我過一會就去啦，別戳啦」"
    show akari1_c
    with dissolve
    hide akari2_c
    a "「我先去小賣部買個三文治，用幫你嗎？」"
    show akari1_c :
        alpha 0.7
    with dissolve
    c "「餐蛋治好了，我收拾好就下來」"
    show akari1_c :
        alpha 1.0
    with dissolve
    a "「OK～那在下面等你」"
    hide akari1_c
    with dissolve
    $ quick_menu = False
    window hide dissolve
    hide inschool
    with dissolve
    stop music fadeout 1.0
    show inschool
    with dissolve
    window show dissolve
    $ quick_menu = True
    c "（唉，為什麼偏偏要在這種時候被留堂啦...)"
    "一邊收拾手邊的教科書，一邊思考著。"
    "探望窗外的天空，烏雲密佈，{p}有如此刻的心情，被重重心事煩擾。"
    c "「好吧，那麼去找愷婷吧」"
    "搖一搖頭，嘗試忘卻眼前的煩惱，我推開教室的門扉ーー"
    hide inschool
    show white at hit
    "趴噠噠！"
    c "糟糕了"
    show cg03_6
    with eye_open
    play music "cg03.mp3" loop
    hide white
    $ persistent.unlock_3 = True
    c "(只顧著自己的事，忘記看周圍的人了)"
    c "「啊...請問你沒事吧ーー」"
    "{color=#888888}???{/color}" "「痛...」"
    "{color=#888888}???{/color}" "「陳志恆你是瞎著走路的嗎......」"
    "{color=#888888}???{/color}" "「{alpha=0.7}...不好，又說錯話{/alpha}」"
    show cg03_1
    with dissolve
    hide cg03_6
    "{color=#888888}???{/color}" "「沒什麼，剛才的話請你當作沒聽過吧」"
    c "「抱歉抱歉...等等，你剛才說什麼？」"
    "一位楚楚可憐的少女，被我撞倒在空無一人的走廊上，摸著頭抱怨著。{p}連帶著把她搬著的文件都散落一地。{p}真教人深感抱歉。"
    show cg03_2
    with dissolve
    hide cg03_1
    "沒記錯的話...{w}她是叫卓詩盈，我的同班同學。"
    "平日基本上不會說話，{w}即使有溝通也就是一句起兩句止的程度。"
    "雖然這樣說未免過於「外貌協會」，{p}但那眉清目秀的臉龐，怎麼看也不會是說出這麼毒舌台詞的吧。"
    show cg03
    with dissolve
    hide cg03_2
    c "「我來幫你撿起來吧」"
    s "「真是麻煩你了」"
    show cg03_3
    with dissolve
    hide cg03
    s "「看上去很沒用，卻很懂情理呢...」"
    show cg03
    with dissolve
    hide cg03_3
    s "「對不起，這句也請無視」"
    c "「你還真敢說呢...」"
    "啊啊，我額頭的冷汗都冒出來了。"
    "她的毒舌到底有多厲害啊..."
    show cg03_4
    with dissolve
    hide cg03
    s "「畢竟我每次說話就是這樣，連自己也控制不及」"
    show cg03
    with dissolve
    hide cg03_4
    s "「還是說我繼續不說話會比較好呢」"
    show cg03_5
    with dissolve
    hide cg03
    s "「...算了，你當作沒聽過吧」"
    "原本呆板的表情顯得消沈。"
    "她，果然是沒什麼朋友吧，因為經常說錯話的緣故。"
    "那麼，我是不是也有能力幫她一把呢？"
    $ quick_menu = False
    window hide dissolve
    hide cg03_5
    with dissolve
    stop music fadeout 1.0
    show Schoolco
    with dissolve
    play music "as.mp3" loop
    window show dissolve
    $ quick_menu = True
    show shiori1 at center :
        alpha 0.7
    with dissolve
    c "「不行」"
    show shiori1 :
        alpha 1.0
    with dissolve
    s "「嗯？？」"
    show shiori1 :
        alpha 0.7
    with dissolve
    c "「我不能當作沒聽過」"
    show shiori2 at center
    with dissolve
    hide shiori1
    s "「......說教？」"
    show shiori2 :
        alpha 0.7
    with dissolve
    c "「我並不打算對你說教」"
    c "「只是，若這樣一直保持沈默的話，你會活得開心嗎？」"
    c "「在作為朋友之前...作為同班同學，我也會為妳覺得可惜呀」"
    c "「好，全部文件都收拾好了」"
    c "「來吧，多給自己一點自信吧，詩盈」"
    show shiori1 at center
    with dissolve
    hide shiori2
    s "「...嗯」"
    show shiori4 at center
    with dissolve
    hide shiori1
    s "「你剛才說作為朋友...{w}雖然這樣有點奇怪。{p}\ \ \ 我，可以當你的朋友嗎？{w=0.2}志恆...？」"
    show shiori4 :
        alpha 0.7
    with dissolve
    c "「當然可以了！{w}總之以後有什麼事情就來找我吧！{p}\ \ \ 我很樂意幫忙」"
    show shiori3 at center
    with dissolve
    hide shiori4
    s "「說出這種工具人的發言真的好嗎...？」"
    show shiori3 :
        alpha 0.7
    with dissolve
    c "「哈哈哈，反正我一早便被某學霸當成工具人使用了。{p}\ \ \ 再多一個，也沒差吧」"
    show shiori5
    with dissolve
    hide shiori3
    s "「哈哈，{w}那麼我接下來還有學會聯招委員的工作要做，等下見吧」"
    hide shiori5
    with dissolve
    c "(感覺真好)"
    c "(能夠幫助到朋友，說不定她將會是我們的部員候補...？)"
    c "(......)"
    c "(......部員？)"
    c "(忘記辦正經事啦！！)"
    $ quick_menu = False
    window hide dissolve
    hide Schoolco
    with dissolve
    stop music fadeout 1.0
    show JCAD
    with dissolve
    play music "JCAD.mp3" loop
    window show dissolve
    $ quick_menu = True
    c "「不知還有沒有人參加哩」"
    c "「咦，那邊的是子彤？{p}\ \ \ 子彤同學！」"
    show hinaka1
    with dissolve
    y "「嗯？志恆前輩，是怎麼了？」"
    show hinaka1 :
        alpha 0.7
    with dissolve
    c "「{cps=5}那個呢...{/cps}我今天放學有事要做...{p}\ \ \ 所以攤位的收拾能拜託你？」"
    show hinaka1 :
        alpha 1.0
    with dissolve
    y "「什麼嘛，只這樣當然行了」"
    y "「你支支唔唔的還以為是什麼大事啦，{p}\ \ \ 照直說就好了，志恆真是的」"
    show hinaka1 :
        alpha 0.7
    with dissolve
    c "(哇～這傢伙是天使，意外地率直呀)"
    c "「呀...{w}那就拜託你了，{p}\ \ \ 新部員的子彤同學」"
    show hinaka1 :
        alpha 1.0
    with dissolve
    y "「叫子彤好了，{w}沒猜錯芷柔也讓你直接叫名字了吧啦」"
    show hinaka1 :
        alpha 0.7
    with dissolve
    c "「你怎知到的」"
    show hinaka1 :
        alpha 1.0
    with dissolve
    y "「嘻嘻～」"
    show hinaka1 :
        alpha 0.7
    with dissolve
    c "「嗯...也是呢，{w}看你們平時出雙入對的，{p}\ \ \ 猜到也不出奇呢」"
    show hinaka1 :
        alpha 1.0
    with dissolve
    y "「芷柔一開學就主動過來認識我，{p}\ \ \ 而且我又沒太多朋友」"
    y "「於是我們就成了好姫友」"
    show hinaka1 :
        alpha 0.7
    with dissolve
    c "「噢～是這樣呀」"
    c "(子彤這個人意外的老實呢，{p}\ 不像那些班上的女生...杯葛我)"
    show hinaka1 :
        alpha 1.0
    with dissolve
    y "「呀，時候不早了，三文治賣光就麻煩了，{p}\ \ \ 擺攤加油呢！志恆前輩」"
    show hinaka1 :
        alpha 0.7
    with dissolve
    c "「拜拜」"
    hide hinaka1
    with dissolve
    c "「如果那個會長也是這樣直腸直肚就好了...」"
    stop music fadeout 1.0
    play music "megumi.mp3" fadein 1.0 loop
    show megumi1
    with dissolve
    "{color=#ff7707}???" "「虧你還能這樣想」"
    show megumi1 :
        alpha 0.7
    with dissolve
    c "「嗯...{w}你是誰？」"
    show megumi1 :
        alpha 1.0
    with dissolve
    "{color=#ff7707}???" "「What？{w}竟然有人不認識我，seriously？」"
    show megumi1 :
        alpha 0.7
    with dissolve
    c "(我只對這刺鼻的止汗劑味有印象哩)"
    show megumi2
    with dissolve
    hide megumi1
    "{color=#ff7707}???" "「Well 那麼我只好自我介紹了」"
    show megumi1
    with dissolve
    hide megumi2
    with dissolve
    "{color=#ff7707}???" "「我叫惠惠，是戲劇部的vice captain」"
    m "「本來是來 find out 芷柔跟 drama club 反面的原因」"
    show megumi2
    with dissolve
    hide megumi1
    m "「結果 out of expectation，{w}她竟然是為了加入這個 wretched 既 club，{p}\ \ \ committee 竟然仲係呢類周圍 flirt 旅孩紙既kid」"
    show megumi2 at center:
        alpha 0.7
    with dissolve
    c "(糟了...原來他是來踏場的)"
    show megumi2 :
        linear 0.2 xalign 0.2
    show akari3 at right :
        xalign 0.8
    with dissolve
    a "「請問你還要說多久？」"
    show megumi1 at left:
        xalign 0.2
        alpha 1.0
    with dissolve
    hide megumi2
    show akari3 :
        alpha 0.7
    with dissolve
    with dissolve
    m "「Oh My 這不是愷婷同學？{w}我必定是失言了，{p}\ \ \ I mean 既committee 唔包括你 I am so sorry」"
    show akari6 at right :
        xalign 0.8
    with dissolve
    hide akari3
    show megumi1 :
        alpha 0.7
    with dissolve
    a "「夠了，你要show英文拜託走回你的戲劇部，{p}\ \ \ 别在這裡亂叫」"
    show megumi2 at left :
        xalign 0.2
    with dissolve
    hide megumi1
    m "「why so serious ？{w}不過我個club好似又有new members，我先回去。{p}\ \ \ 不過愷婷同學選committee應該還有 places for improvement，{p}\ \ \ anyway have a nice day」"
    hide megumi2
    with dissolve
    stop music fadeout 1.0
    play music "JCAD.mp3" loop
    show akari6 :
        linear 0.2 xalign 0.5
    pause 0.2
    show akari5 at center
    with dissolve
    hide akari6
    a "「唉...這種人就是」"
    show akari5 :
        alpha 0.7
    with dissolve
    c "「我還以為愷婷會和這類人很友好呢？」"
    show akari3 at center
    with dissolve
    hide akari5
    a "「{cps=10}友好...{/cps}嗎？{w}也僅限學術上的吧，{p}\ \ \ 雖然那傢伙好像很受女孩子歡迎」"
    show akari2_c at center
    with dissolve
    hide akari3
    a "「不要說他了，{w}啊，你的三文治，接著吧！」"
    "志恆用他僅有的手眼協調，辛苦的接住了前方迎面而來的餐蛋治。"
    show akari2_c :
        alpha 0.7
    with dissolve
    c "「呃...我不是要餐蛋治的嗎？」"
    a "「來遲賣光了，沒辦法呢」"
    show akari2_c :
        alpha 0.7
    with dissolve
    c "「唉～原來大學霸愷婷也有沒辦法的事呢」"
    show akari3_b at center
    with dissolve
    hide akari2_c
    a "「嘛...」"
    show akari3_b :
        alpha 0.7
    with dissolve
    c "「......」"
    c "(奇怪了，她怎不回嘴？)"
    show akari4_b at center
    with dissolve
    hide akari3_b
    a "「好啦...就當我錯了，{w}這份公司治就給你，{p}\ \ \ 當作慰勞好了」"
    show akari4_b :
        linear 0.2 xalign 0.2
        alpha 0.7
    with dissolve
    show yuusuke1 at right :
        xalign 0.8
    with dissolve
    h "「什麼嘛～{w}原來，我們的大學霸愷婷接受不了自己的失誤」"
    show akari6_b at left :
        xalign 0.2
    with dissolve
    hide akari4_b
    show yuusuke1 :
        alpha 0.7
    with dissolve
    a "「嘖，不幫忙還加句嘴，{p}\ \ \ 如果我是風紀幹部我早就革你職啦」"
    show yuusuke1 :
        alpha 1.0
    with dissolve
    show akari6_b :
        alpha 0.7
    with dissolve
    h "「哈哈」"
    show akari3_b at left :
        xalign 0.2
    with dissolve
    hide akari6_b
    a "「喂志恆你說句公道話吧」"
    show akari3_b :
        alpha 0.7
    with dissolve
    "志恆只顧著吃著他手中的公司治，沒有答嘴的餘地"
    show akari6_b at left :
        xalign 0.2
    with dissolve
    hide akari3_b
    a "「呀！！！你兩個真是的！」"
    hide akari6_b
    with dissolve
    hide yuusuke1
    with dissolve
    $ quick_menu = False
    window hide dissolve
    hide JCAD
    with dissolve
    stop music fadeout 1.0
    pause 1.0
    show afternooncut
    with dissolve
    play music "afs.mp3" loop
    window show dissolve
    $ quick_menu = True
    "秋冬的太陽早下班，{w}從課室走出來才五時左右，{p}但天色早已一片澄黃。"
    c "「總算脱離了數學地獄了，{w}我的腦海裏只有數字了」"
    c "「呃......{w}我好像把中文課本留了在特別室了」"
    c "「去不去拿回好呢？」"
    menu :
        "回家" :
            jump bhome
        "回校" :
            jump bschool
label bschool :
    c "「算了，幾步路而已，應該不會耽誤太多時間吧」"
    $ quick_menu = False
    window hide dissolve
    hide afternooncut
    with dissolve
    stop music fadeout 1.0
    show afschool
    with dissolve
    window show dissolve
    $ quick_menu = True
    c "「漏了課本而已，怎麽這麽煩？{p}\ \ \ 又要到校務處報告，{w}又要問校工借鑰匙，{w}又要登記...{p}\ \ \ 不如要我寫報告吧」"
    "在樓梯上走著，突然聽到優雅的笛子聲。{p}雖然聽不懂是什麽歌曲，但音樂流暢，{p}音色起伏不定，富有活力，但又帶點悲傷之情。"
    "突然想起學校的傳言，{w}據説每天晚上，天臺就會傳來笛子的奏樂聲。{p}有緣聼此奏樂的同學都説，{w}演奏者不是神，就是鬼，總之就不是人，{p}那音樂造詣絕對不是人所能達到的境界。{p}聽到的人都匯報自己不禁有落淚的衝動。"
    menu :
        "「去看看吧」" :
            c "「去看看吧」"
            $ quick_menu = False
            window hide dissolve
            hide afschool
            with dissolve
            window show dissolve
            $ quick_menu = True
            "悄悄地走上樓梯，直至到達頂層。{p}天臺的門沒有鎖好。"
            "我把腳步放慢走到門前。"
            show nschool
            with eye_open
            play music "rooftop.mp3" loop
            "從門縫望去，衹覺夕陽的光芒直曬在眼上。{p}在這燦爛的光芒下，勉强看到一個少女的身影。"
            c "(這身影好像在那裏見過)"
            "那人好像感覺到自己被觀察，驀然停止演奏。{p}衹見她一轉身，秀麗的長髮在她背後散開。{p}接著她快步地從天臺另一邊的門離開了。"
            c "「真可惜，差一點就看得出是誰了！」"
            "雖然還未能揭開迷之笛聲的真相，{p}但可以肯定的是那演奏的少女已在心中留下不可抹掉的痕跡。"
            $ quick_menu = False
            window hide dissolve
            hide nschool
            with dissolve
            stop music fadeout 1.0
            jump ch1_4

        "「還是別多管閒事」" :
            c "「還是別多管閒事吧，要是看到什麼靈異事件的話......」"
            c "「還是別想了」"
            "想罷便往校門走去，試圖忘記這魔性的音樂"
            $ quick_menu = False
            window hide dissolve
            hide afschool
            with dissolve
            jump ch1_4

label bhome :
    c "「算了，也不會有小偷在晚上偷課本吧，{p}\ \ \ 還是早點回家好了」"
    $ quick_menu = False
    window hide dissolve
    hide afternooncut
    with dissolve
    jump ch1_4

label ch1_4 :
    show afschooldoor
    with dissolve
    play music "afs.mp3" loop
    window show dissolve
    $ quick_menu = True
    "徐步走到校門，{w}看見一個黑髮的女生在校門前徘徊着，{p}短髮中稍長的髮絲隨著步伐搖曳著，{w}臉上有幾分猶疑。"
    c "「她好像芷柔，但好像在等人的樣子，{p}\ \ \ 要不要去打聲招呼呢？」"
    menu :
        "前去打聲招呼" :
            $ r_pts = r_pts + 1
            c "「還是去打聲招呼好了」"
            show rino1 at center :
                alpha 0.7
            with dissolve
            c "「芷柔同學，你好」"
            show rino1 at center :
                alpha 1.0
            with dissolve
            r "「啊！志恆前輩，{w}你也放學了嗎？」"
            show rino1 :
                alpha 0.7
            with dissolve
            c "「對呀，那你呢？在校門前是在等人嗎？」"
            show rino1_b at center :
            with dissolve
            hide rino1
            r "「不是不是，只是在想事情而已......{p}\ \ \ 也算是在等人吧，不過現在等到了」"
            r "「你是去巴士站那邊嗎？{w}{cps=10}不如一起....{/cps}」"
            show rino1_b :
                alpha 0.7
            with dissolve
            c "「你想説一起走嗎？無所謂呀」"
            show rino1 at center :
                alpha 1.0
            with dissolve
            hide rino1_b
            r "「對呀，太好了，謝謝你」"
            show rino1 :
                alpha 0.7
            with dissolve
            c "「不用說得這麼嚴重吧，反正是順路」"
            c "(她的反應為何這麽怪？)"
            "就這樣，二人在秋風颯颯的黄昏中走着"
        "裝作看不見" :
            c "「還是裝作看不見好了，要是認錯人那就相當尷尬了，{p}\ \ \ 何況她在想事情呢，還是不要打擾她了」"
            "志恆靜靜地走出校門，在旁邊經過"
            r "「志恆前輩，你放學啦？」"
            show rino1 at center :
                alpha 0.7
            with dissolve
            c "「是呀，那你呢？在校門前是在等人嗎？」"
            show rino1_b at center
            with dissolve
            hide rino1
            r "「不是不是，只是在想一些事情而已，才不是在等你.......{p}\ \ \ 你是走去巴士站那邊嗎？」"
            show rino1_b :
                alpha 0.7
            with dissolve
            c "「是呀」"
            show rino1 at center
            with dissolve
            hide rino1_b
            r  "「那一起走好嗎？」"
            show rino1 :
                alpha 0.7
            with dissolve
            c "「無所謂呀」"
            show rino1 :
                alpha 1.0
            with dissolve
            r "「太好了，謝謝你」"
            show rino1 :
                alpha 0.7
            with dissolve
            c "「不用說得這麼嚴重吧，反正是順路」"
            c "(她的反應為何這麽怪？)"
            "就這樣，二人在秋風颯颯的黄昏中走着"

    hide rino1
    with dissolve
    stop music fadeout 1.0
    $ quick_menu = False
    window hide dissolve
    show cg04
    with dissolve
    play music "cg04.mp3" loop
    $ persistent.unlock_4 = True
    hide afschooldoor
    window show dissolve
    $ quick_menu = True
    "順斜坡而下，二人並排而走"
    show afterschool_1
    with dissolve
    c "(太靜了，{w}是不是要說些東西呢？)"
    c "(但我又沒有和女生搭話的經驗，{w}該說甚麼好呢？)"
    c "(但如果要女生先説話，我又好像太廢了，{w}算了，死就死啦！)"
    hide afterschool_1
    with dissolve
    c "「對了，你剛才留下來做什麼呢？」"
    r "「上課後班而已，你呢？」"
    c "「我？{w}唉，{w}我做不完功課，所以被老師留堂了」"
    r "「怎會呢？{w}你成績......不是挺好的嗎？」"
    c "「不是啦，{w}我今日午飯不就是要你教我做數學嗎？」"
    r "「那條可是很難的，我就只有這個科目擅長了......」"
    c "(弊了，我好像令氣氛更尷尬了)"
    "雖然二人又回歸沉默了，但話匣子一旦開了便停不下來"
    r "「對了......{w}志恆前輩，你為什麼會幫愷婷師姐搞電影部呢？」"
    c "「嗯......我也答不了呢，{w}她可能是看得上吧」"
    r "「愷婷師姐看上了你？！難道她喜歡上......」"
    c "「不是那種意思啦，{w}怎會有人對我這種毒男有興趣呢？{p}\ \ \ 她可能是覺得我攝影能力有點用，又夠奇怪才找我」"
    r "「前輩你不要這樣看低自己啦，{w}你的照片不就拍得不錯嗎？{p}\ \ \ 其實我也有看」"
    c "「是嗎？{w}謝謝你呀，{w}想不到真的有人留意我的專頁。{p}\ \ \ 有點滾動呢」"
    r "「有麝自然香，將來肯定有更多人留意你的。」"
    c "「也許吧」"
    r "「不，{w}是一定會，{w}至少我也會一直幫你宣傳的」"
    c "「那我一定會努力的」"
    "二人走到巴士站等車，二人同行的時間亦進入了倒數"
    $ quick_menu = False
    window hide dissolve
    hide cg04
    with dissolve
    stop music fadeout 1.0
    show nrts
    with dissolve
    play music "afs.mp3" loop
    window show dissolve
    $ quick_menu = True
    show rino1 at center :
        alpha 0.7
    with dissolve
    c "「不知你現在的課業怎樣呢？{w}中三應該比以前辛苦多吧」"
    show rino1 :
        alpha 1.0
    with dissolve
    r "「是啊....比以前麻煩多了，{w}不過我還應付得了」"
    show rino1 :
        alpha 0.7
    with dissolve
    c "「是嗎，那就好了，{w}要是有什麼困難也可以找我幫手，{p}\ \ \ 雖然我也未必幫到你」"
    show rino_special2
    with dissolve
    r "「{cps=5}......{/cps}呐...不如我們交换........」"
    show rino3_b at center :
        alpha 0.7
    with dissolve
    hide rino_special2
    with dissolve
    hide rino1
    with dissolve
    "此時，巴士的引擎聲蓋過了少女的說話"
    c "「呀，{w}車到了，{w}拜拜芷柔，明天再説吧」"
    show rino3_b :
        alpha 1.0
    with dissolve
    r "「好吧.......再見」"
    stop music fadeout 1.0
    "就這樣，巴士站只留下有點失落的少女"
    hide rino3_b
    with dissolve
    $ quick_menu = False
    window hide dissolve
    hide nrts
    with dissolve
    show ch1_f
    with dissolve
    pause 2.0
    hide ch1_f
    with dissolve
    pause 2.0
    call credits from _call_credits
