kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")
kata1 = kata1.replace(" ", "").lower()
kata2 = kata2.replace(" ", "").lower()
if sorted(kata1) == sorted(kata2):
    print("Kedua kata adalah anagram!")
else:
    print("Kedua kata bukan anagram.")