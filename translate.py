from __future__ import print_function
from googleapiclient.discovery import build


def main():
  sentence = g_translate('Excellent')
  print(sentence)

def g_translate(source):
  service = (build('translate', 'v2', developerKey='AIzaSyAsSYwejYTuuGqDrxKeHy_0A93ywhAN0NA'))
  response = service.translations().list(q=source, target='es').execute()
  return response['translations'][0]['translatedText']

if __name__ == '__main__':
  main()