from pathlib import Path
import re
import shutil
import sys



folder_for_parse = sys.argv[1]

 


images_folder = folder_for_parse + '/images'
im = Path(images_folder)
im.mkdir(exist_ok=True)

documents_folder = folder_for_parse + '/documents'
doc = Path(documents_folder)
doc.mkdir(exist_ok=True)

audio_folder = folder_for_parse + '/audio'
aud = Path(audio_folder)
aud.mkdir(exist_ok=True)

video_folder = folder_for_parse + '/video'
vi = Path(video_folder)
vi.mkdir(exist_ok=True)

archives_folder = folder_for_parse + '/archives'
arch = Path(archives_folder)
arch.mkdir(exist_ok=True)




def sorting_files(path: Path):

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
            else:
                sorting_files(new_path)
        elif i.suffix in images:
            shutil.move(new_path, im)
        elif i.suffix in videos:
            shutil.move(new_path, vi)
        elif i.suffix in documents:
            shutil.move(new_path, doc)
        elif i.suffix in audios:
            shutil.move(new_path, aud)
        elif i.suffix in archives:
            shutil.move(new_path, arch)
 

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
        return path.rename(new_filename)
    return path
        


path = Path(folder_for_parse)
sorting_files(path)


