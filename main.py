# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import telebot
import json
import os
import os.path
import random
import requests
import time
import shutil
from threading import Thread
api_key = 'a00a79613aade8e8c086b1663e1731c1'
hi_text = '''
◧ ◨ ◩ ◪ ◧ ◨ ◩ ◪ ◧ ◨ ◩ ◪ ◧ ◨ ◩ ◪ ◧ ◨ ◩ ◪ ◧ ◨ ◩ ◪ ◧ ◨

Я бот проекта 🔥DetectChecker🔥

💳Стоимость 1 месяца сканов: 100₽
🕹Подписка: не активирована

/help - помощь по боту и базовые команды.
Поддержка: @HSC_EXPLOIT
Сотрудничество: @nasilvas / @HSC_EXPLOIT

◧ ◨ ◩ ◪ ◧ ◨ ◩ ◪ ◧ ◨ ◩ ◪ ◧ ◨ ◩ ◪ ◧ ◨ ◩ ◪ ◧ ◨ ◩ ◪ ◧ ◨
🗣Список команд бота:
/buy - купить подписку/сканирования
/key - активировать ключ
/balance - узнать баланс
/scan - просканировать файл
'''


help_text = '''
🗣Список команд бота:
/buy - купить подписку/сканирования
/key - активировать ключ
/balance - узнать баланс
/scan - просканировать файл
'''

buy_text = '''
ℹ️Покупка подпискиℹ️
🔑Для покупки подписки - @nasilvas / @HSC_EXPLOIT
'''
#########################
bot = telebot.TeleBot('1148734622:AAHMloZArfoN3L6vAKcSnN5rdJf7fezrOGI')
#########################
@bot.message_handler(commands=['admin_990116'])
def add_user(message):
	bot.send_message(message.from_user.id, "Режим админа активирован!")
	@bot.message_handler(content_types=['text'])
	def add(message):
		if '/stata_192192293' in message.text:
			prem_users_ids_file121 = open('prem_u.txt', 'r')
			text_stata = prem_users_ids_file121.read()
			text_stata = text_stata.split('/n')
			print(len(text_stata))
			bot.send_message(message.from_user.id,(str(len(text_stata))))

		if '/admin_add_user_to_premium_list_1702' in message.text:
			msg = message.text
			try:
				adds_user_id = msg.split(" ")[1]
			except:
				bot.send_message(message.from_user.id, "Что-то пошло не так!")
			try:
				global prem_users_ids_file1
				prem_users_ids_file1 = open('prem_u.txt', 'a')
				prem_users_ids_file1.write(str(adds_user_id) + '\n')
				bot.send_message(message.from_user.id, "ID  " + str(adds_user_id) + "  успешно добавлен в список premium пользователей!")
				prem_users_ids_file1.close()
			except:
				bot.send_message(message.from_user.id, "Что-то пошло не так!")
				prem_users_ids_file1.close()
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.from_user.id, hi_text)
@bot.message_handler(commands=['admin_view_all_premium_users_1702'])
def view_users(message):
	view_u_file = open('prem_u.txt', 'r')
	view_text = view_u_file.read()
	view_u_file.close()
	bot.send_message(message.from_user.id, view_text)
@bot.message_handler(commands=['buy'])
def buy_cmd(message):
	bot.send_message(message.from_user.id, buy_text)
@bot.message_handler(commands=['help'])
def help_message(message):
	bot.send_message(message.from_user.id, help_text)
@bot.message_handler(commands=['balance'])
def check_balance(message):
	balance = ''
	sub = ''
	balance_info_file = open('prem_u.txt', 'r')
	balance_info_text = balance_info_file.read()
	balance_info_file.close()
	#kd_file2 = open('kd.txt', 'r')
	#kd_file2_text = kd_file2.read()
	#kd_file2.close()
	if str(message.chat.id) in balance_info_text:
	#	balance = 'По подписке'
		sub = 'Активирована'
#	elif str(message.chat.id) in kd_file2_text:
#		balance ='0 сканирований'
	#	sub = 'Не активирована'
	else:
		#balance = '1 сканирование'
		sub = 'Не активирована'


	bot.send_message(message.from_user.id, '⭕️Профиль⭕️\n\n❕Ваш ID:  ' + str(message.chat.id) + '\n💎Подписка:  ' + str(sub) + '\n') # + '\n💶Баланс:  ' + str(balance)
@bot.message_handler(commands=['scan'])
def lic_check(message):
	try:
		global prem_users_ids_file
		prem_users_ids_file = open('prem_u.txt', 'r+')
		global kd_file
		kd_file = open('prem_u.txt', 'r+')
	except:
		print('Ошибка в открытии файла юзеров')
		bot.send_message(message.from_user.id, 'Что-то пошло не так. Ошибка №1')
	try:
		global pui_text
		pui_text = prem_users_ids_file.read()
		prem_users_ids_file.close()
		global kd_text
		kd_text = kd_file.read()
		kd_file.close()
	except:
		print('Ошибка в чтении файла юзеров')
		bot.send_message(message.from_user.id, 'Что-то пошло не так. Ошибка №1.2')
	try:
		if (str(message.chat.id) in pui_text):
			bot.send_message(message.from_user.id, 'Для сканирования отправьте файл.')
			@bot.message_handler(content_types=['document'])
			def save_and_scan(message):
				if (str(message.chat.id) in pui_text):
					if (os.path.exists('files') == False):
						write_id = open('kd.txt', 'r+')
						write_id.write(str(message.chat.id) + '\n')
						write_id.close()

						try:
							os.mkdir('files')
							#########################################
							chat_id = message.chat.id
							file_id = bot.get_file(message.document.file_id)
							downloaded_file = bot.download_file(file_id.file_path)
							file_name = str(message.document.file_name)
							file_dir = 'files/' + message.document.file_name
							with open(file_dir, 'wb') as new_file:
								new_file.write(downloaded_file)
							##########################################

							bot.reply_to(message, "Сканирование запущено!")

							os.system('bash scan.bash files/' + file_name + ' ' + file_name)
							time.sleep(1)
							bot.send_message(message.from_user.id, 'Файл просканирован на 5%')
							time.sleep(2)
							bot.send_message(message.from_user.id, 'Файл просканирован на 30%')
							time.sleep(1)
							bot.send_message(message.from_user.id, 'Файл просканирован на 60%')
							time.sleep(0.7)
							bot.send_message(message.from_user.id, 'Файл просканирован на 80%')
							time.sleep(1)
							bot.send_message(message.from_user.id, 'Файл просканирован на 97%')
							time.sleep(2)
							bot.send_message(message.from_user.id, 'Файл просканирован! Ожидайте отправки результатов.\n\n')
							file_txt = open('files/1.txt', 'r')
							txt_data = file_txt.read()
							txt_data = txt_data.partition(',')[0]
							txt_data = txt_data.replace('\"','^')
							txt_data =txt_data[11:]
							token = txt_data.replace('^','')
							shutil.rmtree('files')
							url = "https://api.metadefender.com/v4/file/" + token
							headers = {
								'apikey': str(api_key)
							}
							scan_resreq = requests.request("GET", url, headers=headers)
							tmp = scan_resreq.text
							scan_res = json.loads(tmp)
							print(str(scan_res))
							zillya_r = str(scan_res['scan_results']['scan_details']['Zillya!']['scan_result_i'])
							xvirus = str(scan_res['scan_results']['scan_details']['Xvirus Personal Guard']['scan_result_i'])
							windef = str(scan_res['scan_results']['scan_details']['Windows Defender']['scan_result_i'])
							vir_bloack_ada = str(scan_res['scan_results']['scan_details']['VirusBlokAda']['scan_result_i'])
							trend_micro_hc = str(scan_res['scan_results']['scan_details']['TrendMicro House Call']['scan_result_i'])
							trend_micro = str(scan_res['scan_results']['scan_details']['TrendMicro']['scan_result_i'])
							total_def = str(scan_res['scan_results']['scan_details']['Total Defense']['scan_result_i'])
							threat_track = str(scan_res['scan_results']['scan_details']['ThreatTrack']['scan_result_i'])


							tachyon = str(scan_res['scan_results']['scan_details']['TACHYON']['scan_result_i'])
							sophos = str(scan_res['scan_results']['scan_details']['Sophos']['scan_result_i'])
							super_anti_spy_ware = str(scan_res['scan_results']['scan_details']['SUPERAntiSpyware']['scan_result_i'])
							rocket_cyber = str(scan_res['scan_results']['scan_details']['RocketCyber']['scan_result_i'])
							quick_heal = str(scan_res['scan_results']['scan_details']['Quick Heal']['scan_result_i'])
							preventon = str(scan_res['scan_results']['scan_details']['Preventon']['scan_result_i'])
							nano_av = str(scan_res['scan_results']['scan_details']['NANOAV']['scan_result_i'])
							mcafee = str(scan_res['scan_results']['scan_details']['McAfee']['scan_result_i'])
							kasper = str(scan_res['scan_results']['scan_details']['Kaspersky']['scan_result_i'])
							k7 = str(scan_res['scan_results']['scan_details']['K7']['scan_result_i'])
							jiangmin = str(scan_res['scan_results']['scan_details']['Jiangmin']['scan_result_i'])
							ikarus = str(scan_res['scan_results']['scan_details']['Ikarus']['scan_result_i'])
							huorong = str(scan_res['scan_results']['scan_details']['Huorong']['scan_result_i'])
							hauri = str(scan_res['scan_results']['scan_details']['Hauri']['scan_result_i'])
							fortinet = str(scan_res['scan_results']['scan_details']['Fortinet']['scan_result_i'])
							filse_clab = str(scan_res['scan_results']['scan_details']['Filseclab']['scan_result_i'])
							f_prot = str(scan_res['scan_results']['scan_details']['F-prot']['scan_result_i'])
							emsi_soft = str(scan_res['scan_results']['scan_details']['Emsisoft']['scan_result_i'])
							eset = str(scan_res['scan_results']['scan_details']['ESET']['scan_result_i'])
							cyren = str(scan_res['scan_results']['scan_details']['Cyren']['scan_result_i'])
							detected_avs = 0
							msg_scan_res = ''
							msg_scan_res = msg_scan_res + '\n'
							if (zillya_r  == '1'):
								msg_scan_res = msg_scan_res + 'Zillya!:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'Zillya!:  Clean✅\n' + '\n'

							if (xvirus == '1'):
								msg_scan_res = msg_scan_res + 'Xvirus Personal Guard:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'Xvirus Personal Guard:  Clean✅\n' + '\n'

							if (windef == '1'):
								msg_scan_res = msg_scan_res + 'Windows Defender(10):  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'Windows Defender(10):  Clean✅\n' + '\n'

							if (vir_bloack_ada == '1'):
								msg_scan_res = msg_scan_res + 'Virus Block Ada(free):  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'Virus Block Ada(free):  Clean✅\n' + '\n'

							if (vir_bloack_ada == '1'):
								msg_scan_res = msg_scan_res + 'Virus Block Ada(pro):  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'Virus Block Ada(pro):  Clean✅\n' + '\n'

							if (trend_micro_hc == '1'):
								msg_scan_res = msg_scan_res + 'TrendMicro Stable:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'TrendMicro Stable:  Clean✅\n' + '\n'

							if (trend_micro == '1'):
								msg_scan_res = msg_scan_res + 'TrendMicro Enterprise:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'TrendMicro Enterprise:  Clean✅\n' + '\n'

							if (total_def == '1'):
								msg_scan_res = msg_scan_res + 'Total Defense(2019):  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'Total Defense(2019):  Clean✅\n' + '\n'

							if (threat_track == '1'):
								msg_scan_res = msg_scan_res + 'Threat track:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'Threat Track:  Clean✅\n' + '\n'

							if (tachyon == '1'):
								msg_scan_res = msg_scan_res + 'TACHYON:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'TACHYON:  Clean✅\n' + '\n'

							if (sophos == '1'):
								msg_scan_res = msg_scan_res + 'Sophos:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'Sophos:  Clean✅\n' + '\n'

							if (super_anti_spy_ware == '1'):
								msg_scan_res = msg_scan_res + 'Super AntiSpy ware:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'Super AntiSpy ware:  Clean✅\n' + '\n'

							if (rocket_cyber == '1'):
								msg_scan_res = msg_scan_res + 'Rocket cyber:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'Rocket cyber:  Clean✅\n' + '\n'

							if (quick_heal == '1'):
								msg_scan_res = msg_scan_res + 'Quick Heal:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'Quick Heal:  Clean✅\n' + '\n'

							if (preventon == '1'):
								msg_scan_res = msg_scan_res + 'Preventon:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'Preventon:  Clean✅\n' + '\n'

							if (nano_av == '1'):
								msg_scan_res = msg_scan_res + 'NANO AV:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'NANO AV:  Clean✅\n' + '\n'

							if (mcafee == '1'):
								msg_scan_res = msg_scan_res + 'McAffee:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'McAffee:  Clean✅\n' + '\n'

							if (kasper == '1'):
								msg_scan_res = msg_scan_res + 'Kaspersky:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'Kaspersky:  Clean✅\n' + '\n'

							if (k7 == '1'):
								msg_scan_res = msg_scan_res + 'K7 antivirus:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'K7 antivirus:  Clean✅\n' + '\n'

							if (jiangmin == '1'):
								msg_scan_res = msg_scan_res + 'Jiangmin:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'Jiangmin:  Clean✅\n' + '\n'

							if (ikarus == '1'):
								msg_scan_res = msg_scan_res + 'Ikarus AV:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'Ikarus AV:  Clean✅\n' + '\n'

							if (huorong == '1'):
								msg_scan_res = msg_scan_res + 'Huorong:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'Huorong:  Clean✅\n' + '\n'

							if (hauri == '1'):
								msg_scan_res = msg_scan_res + 'Hauri :  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'Hauri:  Clean✅\n' + '\n'

							if (fortinet == '1'):
								msg_scan_res = msg_scan_res + 'FortiNet AV system:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'FortiNet AV system:  Clean✅\n' + '\n'

							if (filse_clab == '1'):
								msg_scan_res = msg_scan_res + 'Filse-clab:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'Filse-clab:  Clean✅\n' + '\n'

							if (f_prot == '1'):
								msg_scan_res = msg_scan_res + 'F-prot:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'F-prot:  Clean✅\n' + '\n'

							if (emsi_soft == '1'):
								msg_scan_res = msg_scan_res + 'Emsi soft:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'Emsi soft:  Clean✅\n' + '\n'

							if (eset == '1'):
								msg_scan_res = msg_scan_res + 'ESET:  ❌\n' + '\n'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'ESET:  Clean✅\n' + '\n'

							if (cyren == '1'):
								msg_scan_res = msg_scan_res + 'Cyren:  ❌'
								detected_avs = detected_avs + 1
							else:
								msg_scan_res = msg_scan_res + 'Cyren:  Clean✅'

							msg_scan_res_full = '❗️Результаты сканирования❗️\n\n' + '📁Имя файла: ' + str(file_name) + '\n\n🗄Расширение: ' + str(scan_res['file_info']['file_type_extension']) + '\n\n🔒SHA1: ' + str(scan_res['file_info']['sha1']) + '\n\n🔒SHA256: ' + str(scan_res['file_info']['sha256']) + '\n\n📊Детект - ' + str(detected_avs) + '/29\n\n----------------------------------------------------------' + msg_scan_res

							bot.send_message(message.from_user.id, msg_scan_res_full)
							msg_scan_res = ''
							msg_scan_res_full = ''

						except Exception as exc:
							print(exc)
							print('Ошибка начала сканирования или получения файла.')
							bot.send_message(message.from_user.id, 'Что-то пошло не так. Ошибка №3')
					else:
						bot.send_message(message.from_user.id, 'Бот пока занят. Дождитесь своей очереди и попробуйте позже.')
				else:
					bot.send_message(message.from_user.id, "У вас нет подписки! Ваш ID: " + str(message.chat.id))


		else:
			bot.send_message(message.from_user.id, "У вас нет подписки! Ваш ID: " + str(message.chat.id))
	except:
		print('Ошибка провверки наличия подписки у юзера')
		bot.send_message(message.from_user.id, 'Что-то пошло не так. Ошибка №2')









try:
	###############
	bot.polling()
	###############
except:
	pass
