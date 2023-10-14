# 您可以在此編寫遊戲的腳本。

# image命令可用於定義一個圖像。
# eg. image eileen happy = "eileen_happy.png"

# define命令可定義遊戲中出現的角色名稱與對應文本顏色。
image ending :
    "end" with dissolve
    pause 24.0
    "end1" with dissolve
    pause 2.0
    "end2" with dissolve
    pause 2.0
    "end3" with dissolve
    pause 16.0
    "end4" with dissolve
    pause 2.0
    "end5" with dissolve
    pause 2.0
    "end" with dissolve
    pause 2.0
    "end6" with dissolve
    pause 2.0
    "end7" with dissolve
    pause 18.0
    "end6" with dissolve
    pause 2.0
    "end" with dissolve
    pause 4.0
    "end8" with dissolve
    pause 2.0
    "end9" with dissolve
    pause 18.0
    "end8" with dissolve
    pause 2.0
    "end" with dissolve

image cg03_special :
    "cg03" with dissolve
    pause 5.0
    "cg03_3" with dissolve
    pause 5.0
    "cg03_4" with dissolve
    pause 5.0
    "cg03_5" with dissolve
    pause 5.0
    repeat

image cg02 :
    "cg02_1" with dissolve
    pause 5.0
    "cg02_2" with dissolve
    pause 5.0
    repeat
image rino_special :
    "rino3_b" with dissolve
    pause 1.3
    "rino1" with dissolve
image akari_special :
    "akari3" with dissolve
    pause 1.0
    "akari1_c" with dissolve
image JCAD1 = "JCAD_f.png"
define s = Character('詩盈',color="#888888")
define m = Character('惠惠',color="#ff7707")
define y = Character('子彤',color="#04de00")
define e = Character('志恆母', color="#005f7f")
define c = Character('志恆', color="#4c8fa5")
define h = Character('灝楠', color="#892d00")
define a = Character('愷婷', color="#ff5454")
define r = Character('芷柔', color="#00fffc")
define a_pts = 0
define r_pts = 0
image JCAD = "JCAD_s.png"
image Schoolco = "School corridor.png"
image inschool = "IS.png"
image chome = "kiyoto room 1.png"
image rts = "Road to school.png"
# 遊戲從這裡開始。
label start:
    stop music fadeout 1.0
    scene black
    with fade
    window show dissolve
    $ quick_menu = True
    e "「志恆，已經是早上了！起床啦！」"
    c "「嗯嗯...」"
    $ quick_menu = False
    window hide dissolve
    show chome
    with fade
    window show dissolve
    $ quick_menu = True
    "天色微亮，看來太陽也是剛睡醒的樣子{p}但一如既往，也是要開始一天的生活了。"
    "我揉一揉惺忪的眼睛，緩步到洗手盆前梳洗"
    "一如既往，昨夜通宵溫習，桌上書本還有餘溫{p}一如既往，望著書架上的相機，穿上校服{p}一如既往，我吃過早餐後便踏出家門，前往學校"
    $ quick_menu = False
    window hide dissolve
    hide chome with dissolve
    show rts
    with dissolve
    play music "gts.mp3" loop
    window show dissolve
    $ quick_menu = True
    c "「好像和前幾天一樣呢{p}\ \ \ 讚數停留在99個已經一整月了........」"
    show yuusuke1
    with dissolve
    h "「喂！早晨啊」"
    show yuusuke1:
        alpha 0.7
    with dissolve
    c "「早晨」"
    show yuusuke1:
        alpha 1.0
    with dissolve
    h "「看甚麼啊?{p}\ \ \ 還在更新那個冇人睇冇人like的專頁呀？」"
    show yuusuke1:
        alpha 0.7
    with dissolve
    c "「又未去到冇人睇吧」"
    show yuusuke1:
        alpha 1.0
    with dissolve
    h "「但99個讚好有98個是你的朋友給的呢，{p}\ \ \ 根本冇街外人like」"
    show yuusuke1:
        alpha 0.7
    with dissolve
    c "「唔好再講啦，我都知個專頁冇人睇」"
    show yuusuke1:
        alpha 1.0
    with dissolve
    h "「雖然事實真係咁殘酷，{p}\ \ \ 但有時候靚仔比內容更加重要」"
    show yuusuke1:
        alpha 0.7
    with dissolve
    c "「你又想讚自己呀?」"
    show yuusuke1:
        alpha 1.0
    with dissolve
    h "「冇錯，我隨便一張自拍或者廢相加句歌詞」"
    show yuusuke1:
        alpha 0.7
    with dissolve
    c "「都有好多人like 呀嘛」"
    show yuusuke1:
        alpha 1.0
    with dissolve
    h "「哈哈，人受歡迎就什麼帖都有人like」"
    show yuusuke1:
        alpha 0.7
    with dissolve
    c "「唉，{w}我都習慣了，這專頁也只是自娛一下」"
    show yuusuke1:
        alpha 1.0
    with dissolve
    h "「如果是這樣就不需要開專頁啦」"
    show yuusuke1:
        alpha 0.7
    with dissolve
    c "「我都知有點自欺欺人，{p}\ \ \ 所謂孤芳自賞，其實只是毒男的幻想」"
    show yuusuke1:
        alpha 1.0
    with dissolve
    h "「算啦，不要再灰啦,{p}\ \ \ 今日是學會聯招日，{p}\ \ \ 你那個學會準備好未？」"
    show yuusuke1:
        alpha 0.7
    with dissolve
    c "「學會聯招？{w}呀！？{p}\ \ \ 我好似要去幫愷婷手」"
    show yuusuke1:
        alpha 1.0
    with dissolve
    h "「那你要快點了！{p}\ \ \ 不然你那個八婆會長會......」"
    show yuusuke1 :
        linear 0.3 xalign 0.2
        alpha 0.7
    with dissolve
    show akari6 at right:
        xalign 0.8
    with dissolve
    "愷婷用手刀打灝楠"
    show yuusuke1 at hit
    a "「你講咩啊？你個爛仔風紀有資格這樣話人嗎？」"
    show yuusuke1 :
        xalign 0.2
        alpha 1.0
    with dissolve
    show akari6 at right:
        xalign 0.8
        alpha 0.7
    with dissolve
    h "「哎呀哎呀，{w}真是日頭唔好講人， 又會這麼不好彩碰到你」"
    show yuusuke1 :
        xalign 0.2
        alpha 0.7
    with dissolve
    show akari6_b at right:
        xalign 0.8
        alpha 1.0
    with dissolve
    a "「你當然不想給我見到你在這裏自吹自擂，奚落志恆啦」"
    show yuusuke1 :
        xalign 0.2
        alpha 1.0
    with dissolve
    show akari6_b at right:
        xalign 0.8
        alpha 0.7
    with dissolve
    h "「這些是我們友誼的印證，{p}\ \ \ 你們女仔不會明白啦」"
    show yuusuke1 :
        xalign 0.2
        alpha 0.7
    with dissolve
    hide akari6_b
    show akari6 at right:
        xalign 0.8
        alpha 1.0
    with dissolve
    a "「不要再講這些歪理了，{p}\ \ \ 志恆我們走吧，快去準備攤位吧」"
    show yuusuke1 :
        xalign 0.2
        alpha 0.7
    with dissolve
    show akari6 at right:
        xalign 0.8
        alpha 0.7
    with dissolve
    c "「知道了知道了，{w}走先啦灝楠」"
    show yuusuke1 :
        xalign 0.2
        alpha 0.7
    with dissolve
    h "「拜拜，你要小心呀」"
    hide yuusuke1
    with dissolve
    "愷婷怒視灝楠，拉志恆走開。{p}望著眼前這個有點靦腆，看似不知所措的男生。{p}她真不知好氣還是好笑"
    hide akari6
    with dissolve
    $ quick_menu = False
    window hide dissolve
    hide rts
    with dissolve
    stop music fadeout 1.0
    window show dissolve
    $ quick_menu = True
    "在這之前，愷婷家"
    $ quick_menu = False
    window hide dissolve
    show akari room 1
    with dissolve
    window show dissolve
    $ quick_menu = True
    show akari1 at center:
        alpha 0.7
    with dissolve
    "{color=#ff5dc7}早晨的家裏沒有一家人的喧鬧聲，{p}更沒有趕著出門的兄妹。 {p}只有密密吃早餐的少女，"
    "{color=#ff5dc7}電視對面的梳化躺著一個人，{p}用毛毯包著頭，看不清外貌。"
    show akari1:
        alpha 1.0
    with dissolve
    a "「{color=#ff5dc7}我出門口了，記得要吃早餐{/color}」"
    show akari1:
        alpha 0.7
    with dissolve
    "{color=4f17ff}梳化上的人{/color}" "「{color=#ff5dc7}嗯，拜拜{/color}」"
    show akari1:
        alpha 1.0
    with dissolve
    a "「{color=#ff5dc7}拜拜{/color}」"
    show akari1:
        alpha 0.7
    with dissolve
    "{color=#ff5dc7}愷婷向那人和電視櫃上的獎盃瞥了一眼，{p}便獨自出門了"
    hide akari1
    with dissolve
    $ quick_menu = False
    window hide dissolve
    hide akari room 1
    with dissolve
    show inschool
    with dissolve
    play music "as.mp3" loop
    show akari1_c at center
    with dissolve
    window show dissolve
    $ quick_menu = True
    a "「{color=#ff5dc7}不知那個男生今日認不認真呢？{p}\ \ \ 唉，真怕他繼續做廢青{/color}」"
    show akari1_c:
        alpha 0.7
    with dissolve
    "{color=#f8af66}友人A{/color}""「{color=#ff5dc7}你在說誰呀{/color}」"
    "{color=#1f7d4f}友人B{/color}""「{color=#ff5dc7}是不是那天和你同組的男生？{/color}」"
    "{color=#f8af66}友人A{/color}""「{color=#ff5dc7}難道愷婷你看上了那個毒男？{/color}」"
    show akari3_b at center
    with dissolve
    a "「{color=#ff5dc7}不是啦～{w}是找他幫忙開學會罷了{/color}」"
    show akari3_b:
        alpha 0.7
    with dissolve
    "{color=#1f7d4f}友人B{/color}""「{color=#ff5dc7}他有什麼了不起可以令愷婷大小姐找他幫手啊？{/color}」"
    "{color=#f8af66}友人A{/color}""「{color=#ff5dc7}那傢伙不只是死讀書的呆子嗎？{/color}」"
    hide akari3_b
    show akari1_c:
        alpha 1.0
    with dissolve
    "{color=#ff5dc7}愷婷只以笑來回應"
    a "({color=#ff5dc7}為甚麼我會看上那傢伙呢?{cps=10}{p}\ 嗯.....{/cps}{w}可能因為他夠奇怪吧{/color})"
    hide akari1_c
    with dissolve
    $ quick_menu = False
    window hide dissolve
    stop music fadeout 1.0
    hide inschool
    with dissolve
    window show dissolve
    $ quick_menu = True
    "時間回到開學日"
    $ quick_menu = False
    window hide dissolve
    show inschool
    with dissolve
    play music "as.mp3" loop
    window show dissolve
    $ quick_menu = True
    "{color=#39817e}老師{/color}""「大家好，{w}今日是中四第一日上堂，{p}\ \ \ 未來三年\“如無意外\”你們都是同一班了」"
    "{color=#39817e}老師{/color}""「為了令你們更了解自己的書友仔，{p}\ \ \ 我決定要你們兩個人一組來個小組討論，{p}\ \ \ 增進一下感情"
    "全班議論紛紛，個個找自己的好友一組"
    show yuusuke1 at center
    with dissolve
    h "「個老師都傻既，{p}\ \ \ 這樣分組， 大家自然找自己的好朋友一組， 怎會識到人呢？」"
    h "「志恆......{p}\ \ \ 咦，{w}那邊的女生無人同組呢～{p}\ \ \ 走先啦志恆，你要靠自己識新朋友呀～」"
    hide yuusuke1
    with dissolve
    c "「{cps=10}.........{/cps}重色輕友」"
    "另一邊廂，{w}愷婷正被她的好友們纏繞著"
    show akari1_c at center:
        alpha 0.7
    with dissolve
    "{color=#f8af66}友人A{/color}""「愷婷，和我同一組啦好不好？」"
    "{color=#1f7d4f}友人B{/color}""「不對，愷婷應該和我一組才對」"
    "{color=#f8af66}友人A{/color}""「你現在是跟我過不去嗎？」"
    "{color=#1f7d4f}友人B{/color}""「是你為甚麼要和我爭？!"
    "兩人對峙"
    show akari1_c at center:
        alpha 1.0
    with dissolve
    a "(要在他們扯頭髮前想辦法呢，{p}\ 看來要找個人同我一組先可以平息他們的爭吵)"
    hide akari1_c
    show akari2_c at center
    with dissolve
    stop music fadeout 1.0
    play music "asf.mp3" loop
    a "「咦～{w}那位的同學，可以和你一組嗎？」"
    show akari2_c at center:
        alpha 0.7
    with dissolve
    c "「{cps=10}我......?{/cps}{w}你應該不認識我吧」"
    hide akari2_c
    show akari1_c at center
    with dissolve
    a "「就是不認識才要認識一下嘛，{p}\ \ \ 你好!{w}我是愷婷，多多指教」"
    show akari1_c:
        alpha 0.7
    with dissolve
    c "「{cps=10}.......{/cps}你好，我是志恆」"
    "{color=#f8af66}友人A{/color}，{color=#1f7d4f}友人B{/color}" "「？......」"
    "愷婷仔細打量著眼前的男生"
    show akari1_c:
        alpha 1.0
    with dissolve
    a "(他看起來不像什麼人氣王，{p}\ 放學后除了回家外便無事可做應該挺空閑的，{p}\ {cps=10}不如......{/cps})"
    show akari1_c:
        alpha 0.7
    with dissolve
    "{color=#39817e}老師{/color}""「好了好了，大家都分好組了，{p}\ \ \ 那你們就自由地互相問候，{p}\ \ \ 啊不是，{w}瞭解一下對方吧」"
    show akari1_c:
        alpha 1.0
    with dissolve
    a "(好，{w}就從和他的對話中趁勢試試他有冇興趣加入，{p}\ 等他先出手好了)"
    show akari1_c:
        alpha 0.7
    with dissolve
    pause(1.0)
    c "「{cps=5}......{/cps}」{nw}"
    hide akari1_c
    show akari4_b at center:
        alpha 1.0
    with dissolve
    a "(他為何不說話啊？{p}\ 真是的，{w}要女生先出聲嗎？)"
    a "「你為何不說話啊？」"
    show akari4_b:
        alpha 0.7
    with dissolve
    c "「對不起，我不太擅長這種場合」"
    hide akari4_b
    show akari1 at center
    with dissolve
    a "「算啦，{w}你剛才在想甚麼」"
    show akari1 :
        alpha 0.7
    with dissolve
    c "「在想事情而已」"
    show akari1 :
        alpha 1.0
    with dissolve
    a "「想甚麼呀？」"
    show akari1 :
        alpha 0.7
    with dissolve
    c "「白日夢喇，別問了」"
    show akari1 :
        alpha 1.0
    with dissolve
    a "(真是一個怪人)"
    a "「那你平常喜歡做甚麼啊？{p}\ \ \ 打機啊？」"
    show akari1 :
        alpha 0.7
    with dissolve
    c "「不是啦，哪有時間，{p}\ \ \ 讀完書餘下的時間只夠我頹一會」"
    hide akari1
    show akari2_c at center
    with dissolve
    a "「那假日做甚麼？{p}\ \ \ 難道你沒有甚麼興趣嗎？{p}\ \ \ 毒男應該有些特殊興趣才多啦」"
    show akari2_c:
        alpha 0.7
    with dissolve
    c "「我才沒有......{w}甚麼特別興趣啦!{p}\ \ \ 這是偏見，我只是喜歡周圍拍拍照」"
    show akari2_c:
        alpha 1.0
    with dissolve
    a "「拍照？{w} 拍甚麼，應該不是犯法吧？」"
    show akari2_c:
        alpha 0.7
    with dissolve
    c "「別當我是變態啊!{p}\ \ \ 只是找些有意境的景物拍下來，再加些感想罷了」"
    show akari2_c:
        alpha 1.0
    with dissolve
    a "「意境，聽起來挺有趣的」"
    "愷婷偷望志恆，{p}看見志恆抽屜裏有張相片。"
    a "「你藏了甚麼東西?{p}\ \ \ 讓姐姐看一看{nw}」"
    with hpunch
    "志恆措手不及，{p}愷婷從抽屜裏拿出那張照片。"
    hide akari2_c
    show photo
    with dissolve
    "那是一張頗為漂亮的照片，{p}照片中影到了日落時天空的雲層"
    hide photo
    with dissolve
    show akari1_c at center
    with dissolve
    a "「你影的照片還蠻漂亮的嘛」"
    show akari1_c:
        alpha 0.7
    with dissolve
    c "「還可以啦」"
    show akari1_c:
        alpha 1.0
    with dissolve
    a "「想不到你有這樣的長處呢」"
    show akari1_c:
        alpha 0.7
    with dissolve
    c "「我的形象有那麼差嗎？」"
    show akari1_c:
        alpha 1.0
    with dissolve
    a "「{cps=10}嗯...{/cps}」"
    a "(這個人有點可疑)"
    "就這樣，我認識了這個傻仔"
    hide akari1_c
    with dissolve
    $ quick_menu = False
    window hide dissolve
    hide inschool
    with dissolve
    stop music fadeout 1.0
    pause(0.5)
    show inschool
    with dissolve
    play music "as.mp3" loop
    show akari1 at center :
        alpha 0.7
    with dissolve
    window show dissolve
    $ quick_menu = True
    c "「會長，現在我們是要去準備招聘會員的攤位吧」"
    hide akari1
    show akari3 at center
    with dissolve
    a "「無錯， 我們要把握最後機會，{p}\ \ \ 找到足夠會員參加，你要加把勁噢」"
    show akari3 :
        alpha 0.7
    with dissolve
    c "「盡力吧，反正最後的結果也是看運氣吧」"
    show akari3 :
        alpha 1.0
    with dissolve
    a "「這是失敗者的藉口，{p}\ \ \ 不要未嘗試就這樣推卸責任」"
    show akari3 :
        alpha 0.7
    with dissolve
    c "「{cps=10}...{/cps}對不起」"
    hide akari3
    show akari1_c at center
    with dissolve
    a "「抱歉，好像太認真了，{p}\ \ \ relax relax 一起好好努力吧」"
    hide akari1_c
    with dissolve
    $ quick_menu = False
    window hide dissolve
    hide inschool
    with dissolve
    stop music fadeout 1.0
    window show dissolve
    $ quick_menu = True
    "說真的，那天真是嚇了一大跳，{p}明明想著結識新同學，結果第一天就中伏{cps=10}......{/cps}"
    $ quick_menu = False
    window hide dissolve
    show inschool
    with dissolve
    play music "asf.mp3" loop
    show akari2_c at center:
        alpha 0.7
    with dissolve
    window show dissolve
    $ quick_menu = True
    c "「等等，不是\"我們\"吧？{p}\ \ \ 話說回來我還沒有贊成這件事」"
    show akari2_c:
        alpha 1.0
    with dissolve
    a "「一起辦電影部吧，一定會很有趣哦！」"
    show akari2_c:
        alpha 0.7
    with dissolve
    c "「剛才的話被無視了嗎...」"
    show akari2_c:
        alpha 1.0
    with dissolve
    a "「總之今天放學後我到教員室提交咯～」"
    hide akari2_c
    with dissolve
    $ quick_menu = False
    window hide dissolve
    hide inschool
    with dissolve
    stop music fadeout 1.0
    show Schoolco
    with dissolve
    play music "cg01.mp3" loop
    window show dissolve
    $ quick_menu = True
    show akari1 at center :
        alpha 0.7
    with dissolve
    c "「愷婷，開部的條件你看過了嗎？」"
    show akari1 :
        alpha 1.0
    with dissolve
    a "「沒有啊」"
    show akari1 :
        alpha 0.7
    with dissolve
    c "「......」"
    c "「哪有這麼簡單就能開部呢？{p}\ \ \ 而且這是在我們學校哦！」"
    hide akari1
    show akari3_c at center
    with dissolve
    a "「不嘗試怎會成功，{w}說不定最近老師心情好，{p}\ \ \ 會對這些事稍微寬容一點」"
    show akari3_c :
        alpha 0.7
    c "「{cps=5}你...{/cps}{w}這樣子虧你還能在中學部考得全級第一......」"
    $ persistent.unlock_1 = True
    hide akari3_c
    with dissolve
    $ quick_menu = False
    window hide dissolve
    hide Schoolco
    with dissolve
    show cg01
    with dissolve
    window show dissolve
    $ quick_menu = True
    a "「你理得我？{w}又不怕吃虧，就先試試看吧！{p}\ \ \ 快跑起來吧，廢柴！」"
    "只見赤理用力抓緊我的手"
    show cg01_2
    with dissolve
    hide cg01
    a "「最重要的就是......」"
    "然後往前一拉，{w}喊道"
    a "{size=+20}「{cps=20}TRIAL AND ERROR!!!{/cps}」{/size}"
    "在思考以前，身體已經被眼前的少女拖著走，於走廊上風馳電掣。"
    show cg01_1
    with dissolve
    hide cg01_2
    "微風吹拂，輕撫著我們牽起的手。{p}想不到，我竟然是在這種場合，第一次與女孩子攜手而行。"
    show cg01_3
    with dissolve
    hide cg01_1
    "還真是柔軟，{p}比起男生的肌膚更幼嫩、更光滑細緻。"
    "吹彈可破的肌膚，{p}原來帶有這樣柔和的觸感、這樣溫暖的包容力嗎...？"
    "也許，我一直對她的個性存了點偏見..."
    "表面上這麼任性，又野蠻，{p}想不到還真是個名副其實的女孩子。"
    show cg01
    with dissolve
    hide cg01_3
    "路上的學生驚訝的看著我們倆，一臉茫然。{p}隨後馬上展開了熱烈的討論聲。"
    "{color=#37833d}路人A{/color}" "「欸？那不就是我校的天才？{p}\ \ \ 怎麼拖著個不起眼的男生到處跑呢？」"
    "{color=#8c96d8}路人B{/color}" "「可惡，那個志恆居然堂堂在高中第一天就被女孩牽著手！{p}\ \ \ 而且還是這麼漂亮的妹子啊啊啊！！」"
    "{cps=10}呃...{/cps}路旁的同學們開始對我指手畫腳了......{p}只能等完事之後再向他們解釋吧。"
    "等待，{cps=10}並心存希望吧......{/cps}{p}希望等會兒不會被打成豬頭。"
    show cg01_2
    with dissolve
    hide cg01
    "然而，眼前的少女莞爾一笑，使氣氛更為曖昧。"
    a "「志恆，怎麼放慢腳步了呢？{p}\ \ \ 遞交申請的時限快過去咯」"
    "她是絲毫不在意別人的眼光嗎？"
    "不，{w}這種情況是誰都會感到尷尬吧。"
    "所以她是沒聽到別人的評價才對......"
    "但是，在空中飄逸的紅色長髮仿佛是在進一步試探我。{p}每一次的晃動，都伴隨愷婷的髮香緩緩飄散。"
    "青澀的空氣與少女的體香融和在一起，散發著迷人的芬芳。"
    "正值思春期的少年，應該沒有人能抵擋此刻的誘惑吧。"
    show cg01_1
    with dissolve
    hide cg01_2
    "{cps=5}......{/cps}志恆，先等等。"
    "剛開學就非禮女同學，後果可嚴重了，{w}知道嗎？"
    "嗯，知道了。"
    "青春的慾望，連同口水一同嚥下。"
    "忍耐啊！毒男！{p}這都是我的幻想，這都是毒男的幻想！"
    "看見了。{w}終點就在前面！目的地就在不遠處了！"
    show cg01
    with dissolve
    hide cg01_1
    "飛奔的雙腿帶我奪門而出，來到了校園的中庭，我們申請社團的地方。"
    $ quick_menu = False
    window hide dissolve
    hide cg01
    with dissolve
    stop music fadeout 1.0
    show playground
    with dissolve
    play music "as.mp3" loop
    show akari1 at center :
        alpha 0.7
    with dissolve
    window show dissolve
    $ quick_menu = True
    "{color=#39817e}老師{/color}" "「開創微電影部是挺不錯的。{p}\ \ \ 不過很抱歉，{w}你們的願望暫時未能夠實現」 "
    show akari3 at center
    with dissolve
    a "「？...為什麼？」"
    hide akari3
    with dissolve
    "{color=#39817e}老師{/color}" "「成立社團的條件有數則:」"
    "{color=#39817e}老師{/color}" "「1 該社團在學校中尚未被開辦{p}\ \ \ 2 社團仍然要遵守學校的宗旨{p}\ \ \ 3 開創社團最少需要3人」"
    show akari1 :
        alpha 1.0
    with dissolve
    a "「所以我們不得不湊夠3位成員嗎...」"
    show akari1 :
        alpha 0.7
    with dissolve
    "{color=#39817e}老師{/color}" "「{cps=10}嗯...{/cps}{w}也不一定呢，{p}\ \ \ 我可以在學會聯招留給你位置，{p}\ \ \ 如果這樣也找不齊...」{nw}"
    show akari1 :
        alpha 1.0
    with dissolve
    a "「真的嗎？{p}\ \ \ 好，我們再去找找看」"
    hide akari1
    with dissolve
    $ quick_menu = False
    window hide dissolve
    hide playground
    with dissolve
    stop music fadeout 1.0
    show Schoolco
    with dissolve
    play music "as.mp3" loop
    show akari3 at center :
        alpha 0.7
    with dissolve
    window show dissolve
    $ quick_menu = True
    c "「話雖如此，可是第三個人要到哪裡找？」"
    show akari3 :
        alpha 1.0
    with dissolve
    a "「要找到3人其實並不是困難的事，{p}\ \ \ 但我又不想那些拍我馬屁的人加入」"
    show akari3 :
        alpha 0.7
    with dissolve
    c "「沒有辦法啊，{w}因為你根本沒興趣和班上的同學交談啊，{p}\ \ \ 平日看的資料書在這種時候倒變得沒有幫助了」"
    hide akari3
    show akari6_b at center
    with dissolve
    a "「真囉嗦，我看資料書是我的自由」"
    show akari6_b :
        alpha 0.7
    with dissolve
    c "「好了好了，我去問問我的朋友吧」"
    hide akari6_b
    show akari7_c at center
    with dissolve
    a "「誒...{p}\ \ \ 連你這種人也有朋友啊......{w}呵呵呵」"
    stop music fadeout 1.0
    play music "asf.mp3" loop
    show akari7_c :
        linear 0.2 xalign 0.2
    pause 0.2
    show akari1 at left :
        xalign 0.2
        alpha 0.7
    with dissolve
    hide akari7_c
    show yuusuke1 at right :
        xalign 0.8
    with dissolve
    h "「你們站在這兒幹什麼？」"
    show yuusuke1 :
        xalign 0.8
        alpha 0.7
    with dissolve
    c "「哦哦，是灝楠啊，{p}\ \ \ 現在我們剛好在談你的事情，{p}\ \ \ 有件事想要拜託你」"
    show yuusuke1 :
        xalign 0.8
        alpha 1.0
    with dissolve
    h "「什麼？」"
    show yuusuke1 :
        xalign 0.8
        alpha 0.7
    with dissolve
    c "「電影部可能開不成了，{p}\ \ \ 因為成員人數還不夠啊」"
    show yuusuke1 :
        xalign 0.8
        alpha 1.0
    with dissolve
    h "「對不起...{w}這個要求我有點難答應，{p}\ \ \ 因為對於社團活動，我沒有多大的興趣...」"
    show yuusuke1 :
        xalign 0.8
        alpha 0.7
    with dissolve
    c "「{cps=10}......{/cps}」"
    show yuusuke1 :
        xalign 0.8
        alpha 1.0
    with dissolve
    h "「雖然這樣說有點自大，{p}\ \ \ 但我的目標是維護世界和平，做正義的夥伴喔」"
    show yuusuke1 :
        xalign 0.8
        alpha 0.7
    with dissolve
    c "「打人的風紀真正義呢～」"
    show yuusuke1 :
        xalign 0.8
        alpha 1.0
    with dissolve
    h "「這是警惡懲奸，{p}\ \ \ 我才不會去浪費時間，{w}而且也沒有動力去幫忙」"
    show yuusuke1 :
        xalign 0.8
        alpha 0.7
    with dissolve
    c "「{cps=10}呃...{/cps}那麼就是不參加的意思吧」"
    hide akari1
    show akari2_c at left :
        xalign 0.2
        alpha 1.0
    with dissolve
    a "「哈哈，{w}你所謂的\"友誼\"真是不可靠呢」"
    show akari2_c at left :
        xalign 0.2
        alpha 0.7
    with dissolve
    c "「......」"
    "(\"你有資格說我嗎？\"{p}\ 這句話差點兒衝口而出)"
    hide akari2_c
    with dissolve
    hide yuusuke1
    with dissolve
    $ quick_menu = False
    window hide dissolve
    hide Schoolco
    with dissolve
    stop music fadeout 1.0
    show podium
    with dissolve
    play music "afs.mp3" loop
    window show dissolve
    $ quick_menu = True
    "夕陽照進空曠的操場，氣氛溫暖，{p}卻因放學後學生少而顯得有些冷清。"
    "把硬幣投進自動販賣機中，{p}我按下了一罐碳酸葡萄飲料和一罐橙汁。"
    show akari1 at center
    with dissolve
    a "「啊，等你好久了」"
    show akari1 :
        alpha 0.7
    with dissolve
    c "「走過去買飲料要等多久啦...{w}拿著吧」"
    show akari1 :
        alpha 1.0
    with dissolve
    "一邊說，一邊把橙汁遞給坐在長椅上的女孩。"
    "雖然行為和舉動都很有大姐頭的風範，{p}但在喜好上卻有點孩子氣。"
    "有時我真的懷疑她是不是喝得太多橙汁所以過度活躍{p}我不禁笑了笑。"
    hide akari1
    show akari6_b at center
    with dissolve
    a "「怎麼啦？在取笑我申請開部失敗嗎？」"
    show akari6_b :
        alpha 0.7
    with dissolve
    c "「不是啦，而且這不是重點吧，{p}\ \ \ 剩下的兩人，你打算怎麼招攬呢？」"
    hide akari6_b
    show akari1 at center :
        alpha 1.0
    with dissolve
    a "「找找那些對微電影有興趣的人吧，{p}\ \ \ 你認識這類人嗎？」"
    show akari1 at center :
        alpha 0.7
    with dissolve
    c "「哪有這種人...{p}\ \ \ 再說，剛入學不久怎麼會很清楚其他同學的事？」"
    show akari1 at center :
        alpha 1.0
    with dissolve
    a "「有這麼難嗎？{p}\ \ \ 我倒是把全校的師生名字和外貌都記下來了」"
    show akari1 at center :
        alpha 0.7
    with dissolve
    c "「被成績第一的人這麼一問，{p}\ \ \ 我該給什麼反應才好......」"
    show akari1 at center :
        alpha 1.0
    with dissolve
    a "「你去招攬那傢伙吧，{p}\ \ \ 她站在教員室門前很久了，{p}\ \ \ 說不定她有興趣入部？」"
    show akari1 at center :
        alpha 0.7
    with dissolve
    "愷婷指著不遠處的一位黑髮的女孩，{p}她胸前綁著綠色絲帶...{p}應該是初中的學生。"
    c "「唉，{w}你還真好意思使喚我」"
    show akari1 :
        alpha 1.0
    with dissolve
    a "「去吧去吧，這正好是你的脫毒訓練，加油喔」"
    show akari1 :
        alpha 0.7
    with dissolve
    c "「唉～{w}冇辦法啦，去試一試吧」"
    "我緩緩走向她。"
    hide akari1
    with dissolve
    $ quick_menu = False
    window hide dissolve
    hide podium
    with dissolve
    show cg02_1
    with dissolve
    window show dissolve
    $ quick_menu = True
    $ persistent.unlock_2 = True
    "{color=#00fffc}???{/color}" "「誒？」"
    "對方好像認識我。"
    "{color=#00fffc}???{/color}" "「{cps=20}...是經常來我們班幫忙的志恆前輩嗎...？{/cps}」"
    "她輕聲低語，像是確認一些事情般盯著我看。"
    "我們在哪裡見過面嗎？{p}必須打破這尷尬的氣氛。"
    "{color=#00fffc}???{/color}，{color=#888888}志恆{/color}" "「那個！......」"
    "我們的聲線撞在一起了。"
    show cg02_2
    with dissolve
    "{color=#00fffc}???{/color}" "「{cps=10}請問...{/cps}有什麼事嗎？」"
    c "「其實...{w}我們打算開設電影部，{p}\ \ \ 不知道你有沒有興趣參加呢？」"
    "{color=#00fffc}???{/color}" "「請問你是志恆前輩嗎？{p}\ \ \ 以前經常來我們班幫忙的那位」"
    "我的問題被無視了。不過對方果然認識我。"
    c "「是的」"
    hide cg02_2
    with dissolve
    "{color=#00fffc}???{/color}" "「哈哈，是我啦，往年是中二的芷柔」"
    "我自從下學期開始便沒有到樓下幫忙了，{p}畢竟要預備選科考試。"
    "考試結束後已經對書本以外的事情沒有印象了。"
    c "「哦哦，{w}芷柔同學？好久不見」"
    "我做老師的跑腿，{w}順道建立的人際關係，{p}在此得以運用。即使我不太記得她。"
    $ quick_menu = False
    window hide dissolve
    hide cg02_1
    with dissolve
    show podium
    with dissolve
    show rino1 at center :
        alpha 0.7
    with dissolve
    window show dissolve
    $ quick_menu = True
    c "「請問可以在這張紙上掛個名，{w}當我們的部員嗎？{p}\ \ \ 現在需要2人才可以開部」"
    hide rino1
    show rino3_b at center:
        alpha 1.0
    with dissolve
    r "「{cps=10}嗯.......{/cps}{w}這點小事的話，{p}\ \ \ 原本是完全沒問題的，{p}\ \ \ 可是我已經限額滿了...」"
    show rino3_b at center:
        alpha 0.7
    with dissolve
    "她的臉龐泛紅，{w}手抓著自己的裙，{p}氣氛十分尷尬"
    show rino_special at center:
        alpha 1.0
    with dissolve
    hide rino3_b
    r "「{cps=5}......{/cps}啊」"
    r "「不過如果是向其他同學推介的話......{w}我想也是沒有問題的」"
    show rino1 at center:
        alpha 0.7
    with dissolve
    hide rino_special
    with dissolve
    c "「嘛......{w}總之謝謝啦，幫大忙了」"
    show rino1 :
        alpha 1.0
    with dissolve
    r "「再見，有空我會過來玩的」"
    hide rino1
    with dissolve
    "她被教員室裡的老師呼喚，便走進室內去了"
    show akari2_c at center
    with dissolve
    a "「幹的漂亮，不愧是熱心助人的學長，{p}\ \ \ 我們距離成立電影部又近了一大步了！」"
    show akari2_c :
        alpha 0.7
    with dissolve
    c "「嗯...{w}真的是這樣才好」"
    c "「人家衹是說幫忙推薦而已，{p}\ \ \ 實際上根本和之前沒有分別，{p}\ \ \ 你打算怎麼辦？」"
    show akari2_c :
        alpha 1.0
    with dissolve
    a "「明天才辦吧」"
    show akari2_c :
        alpha 0.7
    with dissolve
    c "「你也太消極了吧，部長」"
    show akari2_c :
        alpha 1.0
    with dissolve
    a "「這個時間學校裡的同學真的很少，{p}\ \ \ 況且第一天便招攬到準部員也算有很大收穫了吧？」"
    show akari2_c :
        alpha 0.7
    with dissolve
    "那是因為我埋沒自己的良心，{p}才可能找到的部員。{p}不過天色已晚，愷婷也有道理。"
    "於是我們在此解散。"
    hide akari2_c
    with dissolve
    $ quick_menu = False
    window hide dissolve
    hide podium
    with dissolve
    stop music fadeout 1.0
    window show dissolve
    $ quick_menu = True
    "放學鐘聲響起，又到了我和愷婷工作的時間。"
    $ quick_menu = False
    window hide dissolve
    show prologue
    with dissolve
    ##show text "{size=30}{color=#ffffff}序章終" at center :
        ##yalign 0.5
    ##with dissolve
    pause 2.0
    ##hide text
    hide prologue
    with dissolve
    pause 2.0
    jump ch1









    return
