def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Cek panjang plat (minimal 2 karakter dan maksimal 6 karakter)
    if len(s) < 2 or len(s) > 6:
        return False

    # Cek dua karakter pertama harus alfabet
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Cek karakter setelah dua karakter pertama
    for i in range(2, len(s)):
        if s[i].isdigit():
            # Jika ada angka, pastikan semua karakter setelahnya adalah angka
            if s[i] == '0' and i == 2:  # Angka pertama tidak boleh '0'
                return False
            for j in range(i, len(s)):
                if not s[j].isdigit():
                    return False
            break
        elif not s[i].isalpha():  # Hanya huruf atau angka yang diperbolehkan
            return False

    return True

main()
