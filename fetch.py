# -*- coding:utf-8 -*-
# followers.py

import tweepy
import pandas as pd
import time
import datetime

def getApiInstance():

    with open("../secret.txt") as f:
        passwd = f.read()
    client = tweepy.Client(bearer_token = passwd, wait_on_rate_limit = True)

    return client

# userで指定されたユーザのフォロワーのIDを取得
# userは@~~~
def getFollowers_ids(client, user, flag):
    
    flag_first = True
    follower_ids_list = []
    count = 0

    while count < 10:
        count += 1
        if flag_first:
            flag_first = False
            ret_client = client.get_users_followers(id = user, max_results = 1000)
        else:
            ret_client = client.get_users_followers(id = user, max_results = 1000, pagination_token=next_token)
        follower_ids = ret_client.data

        try:
            for i in range(len(follower_ids)):
                follower_ids_list.append(follower_ids[i]["id"])
        except tweepy.error.TweepError as e:
            print(e.reason)

        try:
            next_token = ret_client.meta['next_token']
        except KeyError:
            break
        print(f"{count}/10")
        if flag:
            time.sleep(60)

    return follower_ids_list

if __name__ == "__main__":
    client = getApiInstance()
    
    names = [
        "MitoTsukino",
        "Chihiro_yuki23",
        "Elu_World",
        "HiguchiKaede",
        "ShizuRin23",
        "sibuya_hajime",
        "aki_suzuya",
        "Moiramoimoimoi",
        "suzukautako",
        "ushimi_ichigo",
        "ienaga_mugi23",
        "Yuuhi_Riri",
        "AliceMononobe",
        "nekokan_chu",
        "gaku_fushimi",
        "Gilzaren_III",
        "rei_Toya_rei",
        "KazakiMorinaka",
        "Kanae_2434",
        "Youko_Akabane",
        "saku_sasaki",
        "_rnrrdark",
        "honmahimawari",
        "makaino_ririmu",
        "Vamp_Kuzu",
        "setsuna2434",
        "yuika_siina",
        "___Dola",
        "god_yaksa23",
        "azuma_dazo",
        "ikasumi_zzz",
        "KT_seeds",
        "SisterCleaire",
        "ZulmIhP1nlMOT5y",
        "846kizuQ",
        "momo_azuchi_",
        "Darkness_Eater",
        "midori_2434",
        "udukikohh",
        "839yuzu",
        "Kanda_Shoichi",
        "nArUtO_kOgAnE",
        "hina__asuka",
        "harusakiair2434",
        "Sayo_Amemori",
        "TakamiyaRion",
        "maimoto_k",
        "RindouMikoto",
        "debidebiru_sama",
        "SAKURA_RITSUKI",
        "chima_machita23",
        "tukimi_sizuku",
        "JoeRikiichi",
        "ac1kt",
        "narusenaru_2434",
        "belmond_b_2434",
        "Rine_Yaguruma",
        "kakeru_yumeoi",
        "BlackShiba_chan",
        "kudou_chitose",
        "g9v9g_mirei",
        "yuzuki_roa",
        "onomachi_haruka",
        "KataribeTsumugu",
        "seto_miyako",
        "inui_toko",
        "Ange_Katrina_",
        "Lize_Helesta",
        "333akina",
        "manami_aizono",
        "lulu_suzuhara",
        "MahiroYukishiro",
        "Ex_Albio",
        "Levi_E_2434",
        "Hayama_Marin",
        "Nui_Sociere",
        "Hakase_Fuyuki",
        "H_KAGAMI2434",
        "rena_yorumi",
        "ars_almal",
        "AibaUiha",
        "amamiya_kokoro",
        "Eli_Conifer",
        "ratna_petit",
        "SouHayase",
        "sukosuko_sukoya",
        "ShellinBurgundy",
        "FumiVirtual",
        "Sara_Hoshikawa",
        "Karuta_Yamagami",
        "emma_august_",
        "Luis_Cammy",
        "matsukai_mao",
        "Fuwa_Minato",
        "Tomoe_Shirayuki",
        "Gwelu_os_gar",
        "mashiro2434",
        "Naraka_2434",
        "kurusu72me",
        "furen_2434",
        "honmono_ibrahim",
        "kei_nagao2434",
        "1O46V",
        "Kaida_Haru",
        "kirame_2434",
        "meiro_oO",
        "Akane_Asahina__",
        "Suo_Sango",
        "kohaku_todo",
        "Hisui_Kitakoji",
        "Chigusa_24zono",
        "AXIA_96NE",
        "Lauren_iroas",
        "Leos_Vincent",
        "oliverD_23",
        "Lain_Paterson",
        "Muyu_Amagase",
        "ponto_nei",
        "Yotsuha_Umise",
        "1000000lome",
        "KNTFR2434",
        "watarai_hibari",
        "Shikinagi_2434",
        "SerAph_DazZ", # 28+96
        "Taka_Radjiman",
        "ZEA_Cornelia",
        "Hana_Macchia",
        "Rai_Galilei",
        "AmiciaMichella",
        "MiyuOttavia",
        "RiksaDhirendra",
        "Azura_Cecillia",
        "Nara_Haramaung",
        "LaylaAlstro2434",
        "Etna_Crimson",
        "bobon_pranaja",
        "SiskaLeontyne",
        "NagisaArcinia",
        "DeremKado",
        "RezaAvanluna",
        "HyonaElatiora",
        "Xia_Ekavira",
        "MikaMelatika",
        "Wiffy2434",
        "YuyaShin2434",
        "SuhaMin2434",
        "Gaon2434",
        "KaenVtuber",
        "LOROU_vtuber",
        "HanChiho2434",
        "VtuberHakuRen",
        "NagiSo2434",
        "AraChae2434",
        "SiuLee2434",
        "BoraNun2434",
        "RayAkira2434",
        "RohaLee2434",
        "NariYang2434",
        "HariRyu2434",
        "KiruShin2434",
        "JiyuOh2434",
        "Seffyna2434",
        "SongMia2434",
        "BanHada2434",
        "KoYami2434",
        "HaYun2434",
        "NaSera2434",
        "LeeOn2434",
        "VirtuaRealEine",
        "NanamiVr",
        "RichigoV",
        "MURI_wrrry",
        "VRhanon",
        "plusprs",
        "Nyatsuki4",
        "wakuhime1",
        "supermikimiki2",
        "KaguraMahiru",
        "Hoshimi515",
        "Aza_VirtuaReal",
        "VRduelTabibito",
        "Saya_VirtuaReal",
        "VirtuarealKaru",
        "Chiharu_VR",
        "ShaunVirtuaReal",
        "yyyy2114",
        "Mari75996916",
        "remifishy",
        "Kiti13799",
        "Koxia548",
        "Girimi3",
        "KiyuuVR",
        "Aadya_VTuber",
        "Vihaan_VTuber",
        "Noor_VTuber",
        "EliraPendora",
        "PomuRainpuff",
        "FinanaRyugu",
        "Selen_Tatsuki",
        "Rosemi_Lovelock",
        "Petra_Gurin",
        "EnnaAlouette",
        "NinaKosaka",
        "ReimuEndou",
        "MillieParfait",
        "ike_eveland",
        "Mysta_Rias",
        "Vox_Akuma",
        "luca_kaneshiro",
        "shu_yamino",
        "alban_knox",
        "Yugo_Asuma",
        "Fulgur_Ovid",
        "sonny_brisko",
        "uki_violeta",
        "KyoKanek0",
        "MariaMari0nette",
        "AsterArcadia",
        "AiaAmare",
        "RenZott0",
        "ScarleYonaguni",
        "riku_tazumi",
        "iwataiki",
        "VTA_ANYCOLOR"
    ]

    NIJIEN = [
        "EliraPendora",
        "PomuRainpuff",
        "FinanaRyugu",
        "Selen_Tatsuki",
        "Rosemi_Lovelock",
        "Petra_Gurin",
        "EnnaAlouette",
        "NinaKosaka",
        "ReimuEndou",
        "MillieParfait",
        "ike_eveland",
        "Mysta_Rias",
        "Vox_Akuma",
        "luca_kaneshiro",
        "shu_yamino",
        "alban_knox",
        "Yugo_Asuma",
        "Fulgur_Ovid",
        "sonny_brisko",
        "uki_violeta",
        "KyoKanek0",
        "MariaMari0nette",
        "AsterArcadia",
        "AiaAmare",
        "RenZott0",
        "ScarleYonaguni",
        "riku_tazumi",
        "VTA_ANYCOLOR"]

    NIJIIDKR = ["Taka_Radjiman",
        "ZEA_Cornelia",
        "Hana_Macchia",
        "Rai_Galilei",
        "AmiciaMichella",
        "MiyuOttavia",
        "RiksaDhirendra",
        "Azura_Cecillia",
        "Nara_Haramaung",
        "LaylaAlstro2434",
        "Etna_Crimson",
        "bobon_pranaja",
        "SiskaLeontyne",
        "NagisaArcinia",
        "DeremKado",
        "RezaAvanluna",
        "HyonaElatiora",
        "Xia_Ekavira",
        "MikaMelatika",
        "Wiffy2434",
        "YuyaShin2434",
        "SuhaMin2434",
        "Gaon2434",
        "KaenVtuber",
        "LOROU_vtuber",
        "HanChiho2434",
        "VtuberHakuRen",
        "NagiSo2434",
        "AraChae2434",
        "SiuLee2434",
        "BoraNun2434",
        "RayAkira2434",
        "RohaLee2434",
        "NariYang2434",
        "HariRyu2434",
        "KiruShin2434",
        "JiyuOh2434",
        "Seffyna2434",
        "SongMia2434",
        "BanHada2434",
        "KoYami2434",
        "HaYun2434",
        "NaSera2434",
        "LeeOn2434"]

    padding = "pad"
    # S,E = 108,126
    # target_names = names[S:E]
    target_names = NIJIIDKR

    starttime = datetime.datetime.now()

    # 一度に100まで

    users = client.get_users(usernames = target_names).data
    print(users)
    print(f"{len(target_names)} 人を取得中：")
    data = {}
    for i in range(len(users)):
        print(users[i]["name"])
        print(users[i]["id"])
        if i >= len(users)-2:
            flag = False
        else:
            flag = True
        follower_ids_list = getFollowers_ids(client, users[i]["id"],flag)
        print(f"{len(follower_ids_list)}個のデータを取得")
        length = len(follower_ids_list)
        while length < 10000:
            follower_ids_list.append(padding)
            length += 1
        follower_ids_list = list(map(str,follower_ids_list))
        for j in range(len(follower_ids_list)):
            follower_ids_list[j] += 'A'
        data[users[i]["username"]] = follower_ids_list
        print(f"{len(target_names)} 人中 {i+1} 人目を取得")
        
        dftemp = pd.DataFrame(data)
        filename = "NIJItemps"
        # dftemp.to_csv(filename + str(i+S) + ".csv")
        dftemp.to_csv(filename + "IDKR" + str(i+1) + ".csv")

    df = pd.DataFrame(data)
    filename = "NIJIfollowers"
    df.to_csv(filename + "IDKR" + ".csv")
    print(f"{starttime} to {datetime.datetime.now()}")