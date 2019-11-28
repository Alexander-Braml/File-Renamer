from Renamer import Renamer


if __name__ == '__main__':
    ren = Renamer()
    ren.rename_all()
    print(f'Renamed {len(ren.vals.files)} files!')

for i in range(1001):
    with open(f'C:\\RenameDir\\DeleteThis_RemoveThis_Important_#{i}.txt', 'w+'):
        pass
