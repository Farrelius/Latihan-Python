students = {}

def add_student(name, grade):
    students[name] = grade

def display_students():
    for name, grade in students.items():
        print(f"Nama: {name}, Nilai: {grade}")

while True:
    action = input("Pilih aksi (tambah/tampilkan/keluar): ").lower()
    if action == "tambah":
        name = input("Masukkan nama mahasiswa: ")
        grade = float(input("Masukkan nilai: "))
        add_student(name, grade)
    elif action == "tampilkan":
        display_students()
    elif action == "keluar":
        break
    else:
        print("Aksi tidak valid.")