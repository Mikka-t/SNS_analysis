import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

csv = pd.read_csv("NIJImatrix.csv")

nameJP = [
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
    "SerAph_DazZ"
]

nodes = []
for i in range(len(nameJP)):
    name = nameJP[i]
    for j in range(len(nameJP)):
        tar = nameJP[j]
        if i < j:
            if int(csv[name].values[j])/10000 > 0.4:
                line = name + " " + tar + " " + str(int(csv[name].values[j])/10000) + "\n"
                nodes.append(line)
with open('nodes_temp.txt', 'w', encoding='utf-8',newline='\n') as f:
    f.writelines(nodes)



G = nx.DiGraph()

G = nx.read_weighted_edgelist('nodes_temp.txt', nodetype=str)

pos = nx.spring_layout(G, weight='weight')
edge_labels = {(i, j): w['weight'] for i, j, w in G.edges(data=True)}
# nx.draw_networkx_edge_labels(G,pos, edge_labels=edge_labels)
nx.draw_networkx_nodes(G, pos, alpha=0.6)
nx.draw_networkx_labels(G, pos, font_family="Yu Gothic", font_weight="bold")
nx.draw_networkx_edges(G, pos, alpha=0.4, edge_color='blue')

# 表示
plt.axis("off")
plt.show()