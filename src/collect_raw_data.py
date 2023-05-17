import os.path
from tqdm import tqdm
from google_play_scraper import reviews, Sort
import pandas as pd
from src import EACHCLASS_CNT, CLS_CNT

app_full_names = [
    "com.noodlecake.altosodyssey",
    "com.matteljv.uno",
    "com.nekki.vector",
    "com.roblox.client",
    "com.playrix.township",
    "com.playrix.gardenscapes",
    "com.pixelbite.mutant",
    "com.madfingergames.deadtrigger2",
    "com.sidheinteractive.sif.DR",
    "com.bluebraingames.thehouseofdavinci3",
    "com.mojang.minecraftpe",
    "com.aim.racing",
    "vpn.free.nexus",
    "free.xd.vpn",
    "com.whatsapp",
    "org.telegram.messenger",
    "net.melodify.android",
    "com.free.vpn.ozzmo",
    "com.instagram.android",
    "free.vpn.ninja",
    "app.biubiuvpn.biubiuvpn",
    "com.hkfuliao.chamet",
    "com.duolingo",
    "sg.bigo.live",
    "com.canva.editor",
    "com.discord",
    "com.fitbit.FitbitMobile",
    "com.naver.linewebtoon",
    "com.dropbox.android",
    "com.read.goodnovel",
    "com.microsoft.outlooklite",
    "com.whatsapp.w4b",
    "video.player.videoplayer",
    "eu.livesport.FlashScore_com",
    "com.microsoft.office.outlook",
    "org.videolan.vlc",
    "com.joytunes.simplypiano",
    "deezer.android.app",
    "com.spotify.music",
    "com.disney.disneyplus",
    "com.netflix.mediaclient",
    "com.hulu.plus",
    "tv.pluto.android",
    "org.xbmc.kodi",
    "com.foxnews.android",
    "com.adobe.reader",
    "com.twitter.android",
    "com.soundcloud.android",
    "tv.twitch.android.app",
    "com.adobe.lrmobile",
    "com.tubitv",
    "com.epix.epix.now",
    "com.vectorunit.cobalt.googleauto",
    "com.google.android.apps.automotive.gamesnacks",
    "com.google.android.apps.youtube.music"
]

total_reviews = [[], [], [], [], []]

for app_name in tqdm(app_full_names):
    classes = []
    for star_cnt in range(1, 5+1):
        this_app_reviews, _ = reviews(
            app_name,
            sort=Sort.MOST_RELEVANT,
            count = EACHCLASS_CNT,
            filter_score_with=star_cnt
        )
        classes.append([review["content"] for review in this_app_reviews])
    if all(len(cls) == EACHCLASS_CNT for cls in classes):
        for i in range(CLS_CNT):
            total_reviews[i].extend(classes[i])

for i in range(CLS_CNT):
    pd.DataFrame(total_reviews[i]).to_csv(os.path.dirname(__file__) + f'/../data/raw/{i + 1}star.csv', index=False)