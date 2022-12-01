import pandas as pd

csv1 = pd.read_csv("NIJIfollowers1_12.csv")
csv2 = pd.read_csv("NIJIfollowers12_30.csv")
csv3 = pd.read_csv("NIJIfollowers30_36.csv")
csv4 = pd.read_csv("NIJIfollowers36_54.csv")
csv5 = pd.read_csv("NIJIfollowers54_72.csv")
csv6 = pd.read_csv("NIJIfollowers72_90.csv")
csv7 = pd.read_csv("NIJIfollowers90_96.csv")
csv8 = pd.read_csv("NIJIfollowers96_102.csv")
csv9 = pd.read_csv("NIJIfollowers102_108.csv")
csv10 = pd.read_csv("NIJIfollowers108_126.csv")
csv11 = pd.read_csv("NIJIfollowersEN.csv")
csv12 = pd.read_csv("NIJIfollowersIDKR.csv")

df = pd.concat([csv1, csv2, csv3, csv4, csv5, csv6, csv7, csv8, csv9, csv10, csv11, csv12], axis=1)
df.to_csv("NIJIfollowers.csv", index=False)