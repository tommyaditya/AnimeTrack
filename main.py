from models.anime import Anime
from models.userlist import UserAnimeList


def menu():
    print("\n=== AnimeTrack — Tracker Anime ===")
    print("1. Lihat daftar anime")
    print("2. Tambah anime")
    print("3. Update anime")
    print("4. Hapus anime")
    print("5. Cari anime")
    print("6. Keluar")


def main():
    anime_list = UserAnimeList()

    while True:
        menu()
        choice = input("Pilih menu: ")

        if choice == '1':
            data = anime_list.list_anime()
            if not data:
                print("Belum ada anime.")
            for idx, anime in enumerate(data, 1):
                print(f"\n[{idx}]")
                print(anime)

        elif choice == '2':
            title = input("Judul: ")
            total = int(input("Total episode: "))
            watched = int(input("Episode terakhir ditonton: "))
            status = input("Status (Watching/Completed/On Hold/Dropped/Plan to Watch): ")
            rating = input("Rating (1-10 atau kosong): ")
            rating = int(rating) if rating else None

            new_anime = Anime(title, total, watched, status, rating)
            anime_list.add_anime(new_anime)
            print("Anime berhasil ditambahkan.")

        elif choice == '3':
            title = input("Masukkan judul anime yang ingin diupdate: ")
            anime = anime_list.find_anime(title)
            if anime:
                print("Biarkan kosong jika tidak ingin diubah.")
                new_watched = input(f"Episode terakhir ditonton ({anime.watched_episodes}): ")
                new_status = input(f"Status ({anime.status}): ")
                new_rating = input(f"Rating ({anime.rating}): ")

                update_data = {}
                if new_watched:
                    update_data['watched_episodes'] = int(new_watched)
                if new_status:
                    update_data['status'] = new_status
                if new_rating:
                    update_data['rating'] = int(new_rating)

                anime_list.update_anime(title, **update_data)
                print("Anime berhasil diupdate.")
            else:
                print("Anime tidak ditemukan.")

        elif choice == '4':
            title = input("Masukkan judul anime yang ingin dihapus: ")
            anime_list.remove_anime(title)
            print("Anime berhasil dihapus.")

        elif choice == '5':
            title = input("Masukkan judul anime yang dicari: ")
            anime = anime_list.find_anime(title)
            if anime:
                print("\nDitemukan:")
                print(anime)
            else:
                print("Anime tidak ditemukan.")

        elif choice == '6':
            print("Terima kasih telah menggunakan AnimeTrack.")
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")


if __name__ == '__main__':
    main()