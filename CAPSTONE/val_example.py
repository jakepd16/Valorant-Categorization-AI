import os
import valorant

KEY = os.environ["RGAPI-072e2d17-e095-4f1f-8782-4c07d1cbfb1d"]
client = valorant.Client(KEY, locale=None)

skins = client.get_skins()
name = input("Search a Valorant Skin Collection: ")

results = skins.find_all(name=lambda x: name.lower() in x.lower())

print("\nResults: ")
for skin in results:
    print(f"\t{skin.name.ljust(21)} ({skin.localizedNames['ja-JP']})")