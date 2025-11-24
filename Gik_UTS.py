try:
    angka = int(input("silaq tamang nilai 7 digit: "))

    if 0 <= angka <= 9_999_999:  
        juta = angka // 1_000_000
        sisa1 = angka % 1_000_000

        ratus_rb = sisa1 // 100_000
        sisa2 = sisa1 % 100_000

        puluh_rb = sisa2 // 10_000
        sisa3 = sisa2 % 10_000

        ribuan = sisa3 // 1_000
        sisa4 = sisa3 % 1_000

        ratusan = sisa4 // 100
        sisa5 = sisa4 % 100

        puluhan = sisa5 // 10
        satuan = sisa5 % 10

        # Output dengan format berbeda
        if angka >= 1_000_000:
            print(f"{juta} → nilai jutaan")

        if angka >= 100_000:
            print(f"{ratus_rb} → nilai ratus ribu")

        if angka >= 10_000:
            print(f"{puluh_rb} → nilai puluh ribu")

        if angka >= 1_000:
            print(f"{ribuan} → nilai ribuan")

        if angka >= 100:
            print(f"{ratusan} → nilai ratusan")

        if angka >= 10:
            print(f"{puluhan} → nilai puluhan")

        if angka >= 1:
            print(f"{satuan} → nilai satuan")

    else:
        print("Input harus 0 - 9.999.999")

except ValueError:
    print("Format input salah, hanya boleh angka!")
