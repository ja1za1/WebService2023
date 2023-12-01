import scrapping
import pickle

BASE_URL = "https://www.ifsudestemg.edu.br/editais/editais-de-barbacena"
NOTICES_FILE = 'editais.pickle'

PAGE_INDEX_INCREASER = 30
current_index = 0
notices = []

while True:
    resp = scrapping.get_links(f'{BASE_URL}/?b_start:int={current_index}')
    current_index += PAGE_INDEX_INCREASER
    if not resp:
        break
    notices += resp


notices_info = []
for notice in notices:
    notices_info.append(scrapping.get_data_notice(notice))

with open(NOTICES_FILE, 'wb') as arquivo:
    pickle.dump(notices_info, arquivo)
