import os
from pathlib import Path
import re
import shutil
import sys


def sorting_files(path: Path):
    global im, vi, doc, aud, arch
    images = ['.png', '.jpeg', '.svg', '.jpg', '.JPEG', '.PNG', '.JPG', '.SVG']
    videos = ['.avi', '.mp4', '.mov', '.mkv', '.AVI', '.MP4', '.MOV', '.MKV']
    documents = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx','.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX']
    audios = ['.mp3', '.ogg', '.wav', '.amr', '.MP3', '.OGG', '.WAV', '.AMR']
    archives = ['.zip', '.gz', '.tar', '.ZIP', '.GZ', '.TAR']

    for i in path.iterdir():
        new_path = normalize(i)
        if new_path.is_dir():
            p = new_path.absolute()
            if p == im.absolute() or p == doc.absolute() or p == aud.absolute() or p == vi.absolute() or p == arch.absolute():
                continue
            elif len(os.listdir(p)) == 0:
                new_path.rmdir()
                print(f'Deleted emply folder: {new_path}')
                continue
            else:
                sorting_files(new_path)
        elif i.suffix in images:
            shutil.move(new_path, im)
            print(f"Move image '{new_path}' to folder {im.name}")
        elif i.suffix in videos:
            shutil.move(new_path, vi)
            print(f"Move video '{new_path}' to folder {vi.name}")
        elif i.suffix in documents:
            shutil.move(new_path, doc)
            print(f"Move document '{new_path}' to folder {doc.name}")
        elif i.suffix in audios:
            shutil.move(new_path, aud)
            print(f"Move audio '{new_path}' to folder {aud.name}")
        elif i.suffix in archives:
            shutil.move(new_path, arch)
            print(f"Move archive '{new_path}' to folder {arch.name}")
 

legend = {
ord('а'):'a',
ord('б'):'b',
ord('в'):'v',
ord('г'):'g',
ord('д'):'d',
ord('е'):'e',
ord('ё'):'yo',
ord('ж'):'zh',
ord('з'):'z',
ord('и'):'i',
ord('й'):'y',
ord('к'):'k',
ord('л'):'l',
ord('м'):'m',
ord('н'):'n',
ord('о'):'o',
ord('п'):'p',
ord('р'):'r',
ord('с'):'s',
ord('т'):'t',
ord('у'):'u',
ord('ф'):'f',
ord('х'):'h',
ord('ц'):'c',
ord('ч'):'ch',
ord('ш'):'sh',
ord('щ'):'shch',
ord('ъ'):'y',
ord('ы'):'y',
ord('ь'):"'",
ord('э'):'e',
ord('ю'):'yu',
ord('я'):'ya',
ord('А'):'A',
ord('Б'):'B',
ord('В'):'V',
ord('Г'):'G',
ord('Д'):'D',
ord('Е'):'E',
ord('Ё'):'Yo',
ord('Ж'):'Zh',
ord('З'):'Z',
ord('И'):'I',
ord('Й'):'Y',
ord('К'):'K',
ord('Л'):'L',
ord('М'):'M',
ord('Н'):'N',
ord('О'):'O',
ord('П'):'P',
ord('Р'):'R',
ord('С'):'S',
ord('Т'):'T',
ord('У'):'U',
ord('Ф'):'F',
ord('Х'):'H',
ord('Ц'):'Ts',
ord('Ч'):'Ch',
ord('Ш'):'Sh',
ord('Щ'):'Shch',
ord('Ъ'):'Y',
ord('Ы'):'Y',
ord('Ь'):"'",
ord('Э'):'E',
ord('Ю'):'Yu',
ord('Я'):'Ya',
}

def normalize(path: Path):

    filename = str(path.name)

    new_filename = filename.translate(legend)
    regex = r'[^\w\d_\-\.]+'
    new_filename = re.sub(regex, "_", new_filename)

    if new_filename != filename:
        x = path.rename(new_filename)
        print(f"Renamed '{filename}' to '{new_filename}'")
        return x

    return path
        

def unzip(folder:Path):
    for i in folder.iterdir():
        split_name = i.name.split('.')
        name_folder = split_name[0]
        a = str(folder) + "/" + name_folder
        shutil.unpack_archive(i, a)
        print(f"Unzipped {name_folder} to {a}")


im = None
doc = None
aud = None
vi = None
arch = None

if __name__ == "__main__":
    folder_for_parse = sys.argv[1]
    path = Path(folder_for_parse)
 


    images_folder = folder_for_parse + '/images'
    im = Path(images_folder)
    im.mkdir(exist_ok=True)
    print('Created images folder')


    documents_folder = folder_for_parse + '/documents'
    doc = Path(documents_folder)
    doc.mkdir(exist_ok=True)
    print('Created documents folder')


    audio_folder = folder_for_parse + '/audio'
    aud = Path(audio_folder)
    aud.mkdir(exist_ok=True)
    print('Created audios folder')


    video_folder = folder_for_parse + '/video'
    vi = Path(video_folder)
    vi.mkdir(exist_ok=True)
    print('Created videos folder')

    archives_folder = folder_for_parse + '/archives'
    arch = Path(archives_folder)
    arch.mkdir(exist_ok=True)
    print('Created archives folder')

    sorting_files(path)

    unzip(arch)

    print("Program is complited")


