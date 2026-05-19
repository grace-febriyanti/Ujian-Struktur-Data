def main():
    # 1. Inisialisasi daftar nilai awal
    nilai_mhs = [70, 80, 90, 75, 85]
    print(f"Daftar Nilai: {nilai_mhs}")
    
    # 2. Tambah nilai
    tambah = 95
    print(f"\nTambah nilai: {tambah}")
    nilai_mhs.append(tambah)
    print("Data setelah ditambah:")
    print(f"{nilai_mhs}")
    
    # 3. Hapus nilai
    hapus = 75
    print(f"\nHapus nilai: {hapus}")
    if hapus in nilai_mhs:
        nilai_mhs.remove(hapus)
    print("Data setelah dihapus:")
    print(f"{nilai_mhs}")
    
    # 4. Statistik nilai
    if nilai_mhs:
        rata_rata = sum(nilai_mhs) / len(nilai_mhs)
        print(f"\nRata-rata nilai: {rata_rata}")
        print(f"Nilai tertinggi: {max(nilai_mhs)}")
        print(f"Nilai terendah: {min(nilai_mhs)}")

if __name__ == "__main__":
    main()