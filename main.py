import webbrowser
import PySimpleGUI as sg
from pytube import YouTube

font = ('Courier New', 10, 'underline')
url = 'https://www.linkedin.com/in/vinicius-rubia-149ab0213/'

def execute_download(link, path):
  video = YouTube(link)
  video.streams.get_highest_resolution().download(output_path=path)

layout = [[sg.Text('Informe o link do vídeo: '), sg.InputText(do_not_clear=False, size=92)],
          [sg.Text('Informe a pasta de destino: '), sg.InputText(size=80), sg.FolderBrowse()],
          [sg.Button('Baixar'), sg.Button('Cancelar')],
          [sg.Text(f'Desenvolvido por Vinicius Rubia | Linkedin - {url}', tooltip=f'{url}', enable_events=True, font=font, key=f'URL {url}')]
]

window = sg.Window('Download de vídeos do YouTube', icon='download.ico', layout=layout)

while True:
  event, values = window.read()
  if event == 'Cancelar' or event == sg.WIN_CLOSED:
    break
  elif event == 'Baixar':
    execute_download(values[0], values[1])
    sg.popup_ok('Download concluído com sucesso!')
  elif event.startswith("URL "):
      urll = event.split(' ')[1]
      webbrowser.open(urll)

window.close()