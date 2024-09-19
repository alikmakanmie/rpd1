#!/usr/env python3
# -*- coding: utf-8 -*-
# coded by : KhamdihiDev 2024 - New

import requests, random, uuid, time, re, urllib.parse, os, sys, base64, json
from bs4 import BeautifulSoup as bsp
import ApiKey as keys

sucess = 0
errors = 0
namarandom = []

class asset:
    def __init__(self) -> None:
        pass

    def RandomNama(self):
        try:
            self.p = requests.get('https://paste.tc/raw/dihiaha-91').json()['names']
            for self.x in self.p:
                self.x = self.x.lower()
                if self.x not in namarandom: namarandom.append(self.x)
        except: namarandom.append('nunu')

    def Uniqapp(self):
        return str(uuid.uuid4())

    def UserAgent(self):
        return f'Instagram 320.0.0.41.113 Android (31/12; 320dpi; 720x1460; INFINIX/Infinix; Infinix X6515; Infinix-X6515; mt6761; in_ID; 5416358{random.randint(63,77)})'

    def headers_app(self):
        self.uuid = self.Uniqapp() # device id
        self.famy = self.Uniqapp() # family
        self.andr = self.uuid.replace('-','')[:16]
        return {
            'host':'i.instagram.com',
            'user-agent': f'{self.UserAgent()}',
            'x-ig-app-locale': 'in_ID',
            'x-ig-device-locale': 'in_ID',
            'x-ig-mapped-locale': 'id_ID',
            'x-pigeon-session-id': f'UFS-{self.uuid}-0',
            'x-pigeon-rawclienttime': f'{str(time.time())[:14]}',
            'x-ig-bandwidth-speed-kbps': f'{random.randint(50,100)}.000',
            'x-ig-bandwidth-totalbytes-b': str(random.randint(10000,99999)),
            'x-ig-bandwidth-totaltime-ms': str(random.randint(300,9999)),
            'x-bloks-version-id': '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a',
            'x-ig-www-claim': 'hmac.AR3lerMyCQwBKzT9Z8MT_gfp7lYjvCfH9AZa_K4kVXuZbSPh',
            'x-bloks-is-prism-enabled': 'true',
            'x-bloks-is-layout-rtl': 'false',
            'x-ig-device-id': self.uuid,
            'x-ig-family-device-id': self.famy,
            'x-ig-android-id': f'android-{self.andr}',
            'x-ig-timezone-offset': str(-time.timezone),
            'x-fb-connection-type': 'MOBILE.LTE',
            'x-ig-connection-type': 'MOBILE(LTE)',
            'x-ig-capabilities': '3brTv10=',
            'x-ig-app-id': '567067343352427',
            'priority': 'u=3',
            'accept-language': 'en-US',
            'ig-intended-user-id': '0',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-fb-http-engine': 'Liger',
            'x-fb-client-ip': 'True',
            'x-fb-server-cluster': 'True',
        }

class Run:
    def __init__(self) -> None:
        self.password_  = []
        self.freeprx = []
        self.RandomProxi()
        self.proxies = {'http': f'socks5://{random.choice(self.freeprx)}'}
        self.config_app = {
            'reg_flow_id': None,
            'khamdihi_qe_dev': None,
            'event': None,
            'wartel': None
        }
        self.nama_acc = {'username':'khamdihi','full_name':'khamdihi dev'}

    def RandomProxi(self):
        try:
            self.send = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text.splitlines()
            for self.myself in self.send:self.freeprx.append(self.myself)
        except Exception as e:print(e)

    def FindCode(self, nama):
        while True:
           try:
               inb = requests.get(f'https://inboxkitten.com/api/v1/mail/list?recipient={nama}').text
               key = re.findall('"key":"(.*?)"', str(inb))
               xxx = re.findall('"region":"(.*?)"', str(inb))
               if len(key) > 0 or len(xxx) > 0:
                  break
           except:pass
        try:
            url = 'https://inboxkitten.com/api/v1/mail/getHtml'
            par = {'region': xxx[0], 'key':key[0]}
            pdi = {'upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
            req = requests.get(url, params=par,headers=pdi)
            sdr = bsp(req.text,'html.parser')
            for yxz in sdr.find_all('td'):
                self.td = re.findall('<td><td style=".*?">(\d+)</td></td>',str(yxz))
                if self.td: return self.td[0]
        except:
            return None
        
    def Insta(self):
        self.acak1 = 'abcdefghijklmnopqrstuvwxyz'
        self.email = ''.join(random.choice(self.acak1) for _ in range(8))
        self.konds = self.send_email(self.email+f'{random.randint(1,9999)}@inboxkitten.com')
        self.kode = self.FindCode(self.konds)
        self.konf = self.konfirmasi(self.kode, self.konds)

    def konten_length(self, data):
        return str(len(
            ('&').join(['%s=%s'%(key, value) for key, value in data.items()])
        ))
    
    def konfirmasi(self, code, email):
         with requests.Session() as self.r:
            try:
                self.fmid = self.head['x-ig-family-device-id']
                self.dvid = self.head['x-ig-android-id']
                self.nama = email.split('@')[0]
                self.date = {
                    'params': '{"client_input_params":{"confirmed_cp_and_code":{},"code":"'+code+'","fb_ig_device_id":[],"device_id":"'+self.dvid+'","lois_settings":{"lois_token":"","lara_override":""}},"server_params":{"event_request_id":"'+self.config_app['event']+'","is_from_logged_out":0,"text_input_id":116592144600090,"layered_homepage_experiment_group":null,"device_id":"'+self.dvid+'","waterfall_id":"'+self.config_app['wartel']+'","wa_timer_id":"wa_retriever","INTERNAL_latency_qpl_instance_id":1.16592144600194E14,"flow_info":"{\\"flow_name\\":\\"new_to_family_ig_default\\",\\"flow_type\\":\\"ntf\\"}","is_platform_login":0,"sms_retriever_started_prior_step":0,"INTERNAL_latency_qpl_marker_id":36707139,"reg_info":"{\\"first_name\\":null,\\"last_name\\":null,\\"full_name\\":null,\\"contactpoint\\":\\"'+self.nama+'@inboxkitten.com\\",\\"ar_contactpoint\\":null,\\"contactpoint_type\\":\\"email\\",\\"is_using_unified_cp\\":false,\\"unified_cp_screen_variant\\":null,\\"is_cp_auto_confirmed\\":false,\\"is_cp_auto_confirmable\\":false,\\"confirmation_code\\":null,\\"birthday\\":null,\\"did_use_age\\":null,\\"gender\\":null,\\"use_custom_gender\\":false,\\"custom_gender\\":null,\\"encrypted_password\\":null,\\"username\\":null,\\"username_prefill\\":null,\\"fb_conf_source\\":null,\\"device_id\\":\\"'+self.dvid+'\\",\\"ig4a_qe_device_id\\":null,\\"family_device_id\\":\\"'+str(uuid.uuid4())+'\\",\\"nta_eligibility_reason\\":null,\\"ig_nta_test_group\\":null,\\"user_id\\":null,\\"safetynet_token\\":null,\\"safetynet_response\\":null,\\"machine_id\\":null,\\"profile_photo\\":null,\\"profile_photo_id\\":null,\\"profile_photo_upload_id\\":null,\\"avatar\\":null,\\"email_oauth_token_no_contact_perm\\":null,\\"email_oauth_token\\":null,\\"email_oauth_tokens\\":null,\\"should_skip_two_step_conf\\":null,\\"openid_tokens_for_testing\\":null,\\"encrypted_msisdn\\":null,\\"encrypted_msisdn_for_safetynet\\":null,\\"cached_headers_safetynet_info\\":null,\\"should_skip_headers_safetynet\\":null,\\"headers_last_infra_flow_id\\":null,\\"headers_last_infra_flow_id_safetynet\\":null,\\"headers_flow_id\\":null,\\"was_headers_prefill_available\\":null,\\"sso_enabled\\":null,\\"existing_accounts\\":null,\\"used_ig_birthday\\":null,\\"sync_info\\":null,\\"create_new_to_app_account\\":null,\\"skip_session_info\\":null,\\"ck_error\\":null,\\"ck_id\\":null,\\"ck_nonce\\":null,\\"should_save_password\\":null,\\"horizon_synced_username\\":null,\\"fb_access_token\\":null,\\"horizon_synced_profile_pic\\":null,\\"is_identity_synced\\":false,\\"is_msplit_reg\\":null,\\"user_id_of_msplit_creator\\":null,\\"dma_data_combination_consent_given\\":null,\\"xapp_accounts\\":null,\\"fb_device_id\\":null,\\"fb_machine_id\\":null,\\"ig_device_id\\":null,\\"ig_machine_id\\":null,\\"should_skip_nta_upsell\\":null,\\"big_blue_token\\":null,\\"skip_sync_step_nta\\":null,\\"caa_reg_flow_source\\":\\"login_home_native_integration_point\\",\\"ig_authorization_token\\":null,\\"full_sheet_flow\\":false,\\"crypted_user_id\\":null,\\"is_caa_perf_enabled\\":true,\\"is_preform\\":true,\\"ignore_suma_check\\":false,\\"ignore_existing_login\\":false,\\"ignore_existing_login_from_suma\\":false,\\"ignore_existing_login_after_errors\\":false,\\"suggested_first_name\\":null,\\"suggested_last_name\\":null,\\"suggested_full_name\\":null,\\"frl_authorization_token\\":null,\\"post_form_errors\\":null,\\"skip_step_without_errors\\":false,\\"existing_account_exact_match_checked\\":false,\\"existing_account_fuzzy_match_checked\\":false,\\"confirmation_code_send_error\\":null,\\"is_too_young\\":false,\\"source_account_type\\":null,\\"whatsapp_installed_on_client\\":false,\\"confirmation_medium\\":null,\\"source_credentials_type\\":null,\\"source_cuid\\":null,\\"source_account_reg_info\\":null,\\"soap_creation_source\\":null,\\"source_account_type_to_reg_info\\":null,\\"registration_flow_id\\":\\"'+self.config_app['reg_flow_id']+'\\",\\"should_skip_youth_tos\\":false,\\"is_youth_regulation_flow_complete\\":false,\\"is_on_cold_start\\":false,\\"email_prefilled\\":false,\\"cp_confirmed_by_auto_conf\\":false,\\"auto_conf_info\\":null,\\"in_sowa_experiment\\":false,\\"youth_regulation_config\\":null,\\"conf_allow_back_nav_after_change_cp\\":null,\\"conf_bouncing_cliff_screen_type\\":null,\\"conf_show_bouncing_cliff\\":null,\\"eligible_to_flash_call_in_ig4a\\":false,\\"flash_call_permissions_status\\":null,\\"attestation_result\\":null,\\"request_data_and_challenge_nonce_string\\":null,\\"confirmed_cp_and_code\\":[],\\"in_updated_eu_tos\\":false,\\"notification_callback_id\\":null,\\"reg_suma_state\\":0,\\"is_msplit_neutral_choice\\":false,\\"zero_tap_enabled\\":false,\\"msg_previous_cp\\":null,\\"ntp_import_source_info\\":null,\\"youth_consent_decision_time\\":null,\\"username_screen_experience\\":\\"control\\",\\"reduced_tos_test_group\\":\\"control\\",\\"should_show_spi_before_conf\\":true,\\"google_oauth_account\\":null,\\"is_reg_request_from_ig_suma\\":false,\\"is_igios_spc_reg\\":false,\\"device_emails\\":null,\\"is_toa_reg\\":false,\\"is_threads_public\\":false,\\"spc_import_flow\\":false}","family_device_id":"'+self.fmid+'","offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f,default,default,harm_f","access_flow_version":"F2_FLOW","is_from_logged_in_switcher":0,"current_step":4,"qe_device_id":"'+self.config_app['khamdihi_qe_dev']+'"}}',
                    'bk_client_context': '{"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}',
                    'bloks_versioning_id': '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a',
                }
                self.head.update({'content-length': self.konten_length(self.date),'x-ig-nav-chain': 'SelfFragment:self_profile:2:main_profile:1722780839.851::,ProfileMenuFragment:bottom_sheet_profile:3:button:1722780843.777::,ProfileMenuFragment:bottom_sheet_profile:4:button:1722780843.808::,UserOptionsFragment:settings_category_options:5:button:1722780846.412::'})
                self.send = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.reg.confirmation.async/', data=self.date, headers=self.head)
                if 'Kode tersebut tidak valid. Anda dapat meminta kode yang baru.' in self.send.text.replace('\\',''):
                    data = {
                        'params': '{"client_input_params":{"device_id":"'+self.dvid+'","lois_settings":{"lois_token":"","lara_override":""}},"server_params":{"is_from_logged_out":0,"layered_homepage_experiment_group":null,"device_id":"'+self.dvid+'","waterfall_id":"'+self.config_app['wartel']+'","INTERNAL_latency_qpl_instance_id":1.56059051800095E14,"flow_info":"{\\"flow_name\\":\\"new_to_family_ig_default\\",\\"flow_type\\":\\"ntf\\"}","is_platform_login":0,"INTERNAL_latency_qpl_marker_id":36707139,"reg_info":"{\\"first_name\\":null,\\"last_name\\":null,\\"full_name\\":null,\\"contactpoint\\":\\"'+self.nama+'@inboxkitten.com\\",\\"ar_contactpoint\\":null,\\"contactpoint_type\\":\\"email\\",\\"is_using_unified_cp\\":false,\\"unified_cp_screen_variant\\":\\"control\\",\\"is_cp_auto_confirmed\\":false,\\"is_cp_auto_confirmable\\":false,\\"confirmation_code\\":null,\\"birthday\\":null,\\"did_use_age\\":null,\\"gender\\":null,\\"use_custom_gender\\":false,\\"custom_gender\\":null,\\"encrypted_password\\":null,\\"username\\":null,\\"username_prefill\\":null,\\"fb_conf_source\\":null,\\"device_id\\":\\"'+self.dvid+'\\",\\"ig4a_qe_device_id\\":null,\\"family_device_id\\":\\"'+self.fmid+'\\",\\"nta_eligibility_reason\\":null,\\"ig_nta_test_group\\":null,\\"user_id\\":null,\\"safetynet_token\\":null,\\"safetynet_response\\":null,\\"machine_id\\":null,\\"profile_photo\\":null,\\"profile_photo_id\\":null,\\"profile_photo_upload_id\\":null,\\"avatar\\":null,\\"email_oauth_token_no_contact_perm\\":null,\\"email_oauth_token\\":null,\\"email_oauth_tokens\\":null,\\"should_skip_two_step_conf\\":null,\\"openid_tokens_for_testing\\":null,\\"encrypted_msisdn\\":null,\\"encrypted_msisdn_for_safetynet\\":null,\\"cached_headers_safetynet_info\\":null,\\"should_skip_headers_safetynet\\":null,\\"headers_last_infra_flow_id\\":null,\\"headers_last_infra_flow_id_safetynet\\":null,\\"headers_flow_id\\":null,\\"was_headers_prefill_available\\":null,\\"sso_enabled\\":null,\\"existing_accounts\\":null,\\"used_ig_birthday\\":null,\\"sync_info\\":null,\\"create_new_to_app_account\\":null,\\"skip_session_info\\":null,\\"ck_error\\":null,\\"ck_id\\":null,\\"ck_nonce\\":null,\\"should_save_password\\":null,\\"horizon_synced_username\\":null,\\"fb_access_token\\":null,\\"horizon_synced_profile_pic\\":null,\\"is_identity_synced\\":false,\\"is_msplit_reg\\":null,\\"user_id_of_msplit_creator\\":null,\\"dma_data_combination_consent_given\\":null,\\"xapp_accounts\\":null,\\"fb_device_id\\":null,\\"fb_machine_id\\":null,\\"ig_device_id\\":null,\\"ig_machine_id\\":null,\\"should_skip_nta_upsell\\":null,\\"big_blue_token\\":null,\\"skip_sync_step_nta\\":null,\\"caa_reg_flow_source\\":\\"login_home_native_integration_point\\",\\"ig_authorization_token\\":null,\\"full_sheet_flow\\":false,\\"crypted_user_id\\":null,\\"is_caa_perf_enabled\\":true,\\"is_preform\\":true,\\"ignore_suma_check\\":false,\\"ignore_existing_login\\":false,\\"ignore_existing_login_from_suma\\":false,\\"ignore_existing_login_after_errors\\":false,\\"suggested_first_name\\":null,\\"suggested_last_name\\":null,\\"suggested_full_name\\":null,\\"frl_authorization_token\\":null,\\"post_form_errors\\":null,\\"skip_step_without_errors\\":false,\\"existing_account_exact_match_checked\\":false,\\"existing_account_fuzzy_match_checked\\":false,\\"confirmation_code_send_error\\":null,\\"is_too_young\\":false,\\"source_account_type\\":null,\\"whatsapp_installed_on_client\\":false,\\"confirmation_medium\\":null,\\"source_credentials_type\\":null,\\"source_cuid\\":null,\\"source_account_reg_info\\":null,\\"soap_creation_source\\":null,\\"source_account_type_to_reg_info\\":null,\\"registration_flow_id\\":\\"'+self.config_app['reg_flow_id']+'\\",\\"should_skip_youth_tos\\":false,\\"is_youth_regulation_flow_complete\\":false,\\"is_on_cold_start\\":false,\\"email_prefilled\\":false,\\"cp_confirmed_by_auto_conf\\":false,\\"auto_conf_info\\":null,\\"in_sowa_experiment\\":false,\\"youth_regulation_config\\":null,\\"conf_allow_back_nav_after_change_cp\\":null,\\"conf_bouncing_cliff_screen_type\\":null,\\"conf_show_bouncing_cliff\\":null,\\"eligible_to_flash_call_in_ig4a\\":false,\\"flash_call_permissions_status\\":null,\\"attestation_result\\":null,\\"request_data_and_challenge_nonce_string\\":null,\\"confirmed_cp_and_code\\":[],\\"in_updated_eu_tos\\":false,\\"notification_callback_id\\":null,\\"reg_suma_state\\":0,\\"is_msplit_neutral_choice\\":false,\\"zero_tap_enabled\\":false,\\"msg_previous_cp\\":null,\\"ntp_import_source_info\\":null,\\"youth_consent_decision_time\\":null,\\"username_screen_experience\\":\\"control\\",\\"reduced_tos_test_group\\":\\"control\\",\\"should_show_spi_before_conf\\":true,\\"google_oauth_account\\":null,\\"is_reg_request_from_ig_suma\\":false,\\"is_igios_spc_reg\\":false,\\"device_emails\\":null,\\"is_toa_reg\\":false,\\"is_threads_public\\":false,\\"spc_import_flow\\":false}","family_device_id":"'+self.fmid+'","offline_experiment_group":"caa_iteration_v3_perf_ig_4","INTERNAL_INFRA_THEME":"harm_f,default,default,harm_f","access_flow_version":"F2_FLOW","is_from_logged_in_switcher":0,"current_step":4,"qe_device_id":"'+self.config_app['khamdihi_qe_dev']+'"}}',
                        'bk_client_context': '{"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}',
                        'bloks_versioning_id': '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a',
                    }
                    response = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.reg.resend_confirmation.async/',headers=self.head,data=data,).text
                    if 'Kode konfirmasi dikirim ulang' in str(response):
                        self.new = self.FindCode(email.split('@')[0])
                        if self.new:
                            self.konfirmasi(self.new, email)
                if 'Buat kata sandi dengan paling tidak 6 huruf atau angka. Ini harus sesuatu yang tidak bisa ditebak orang lain.' in self.send.text.replace('\\',''):
                    self.confir_code = re.search('"confirmation_code":"(.*?)"', str(self.send.text.replace('\\',''))).group(1)
                    self.create_pw(email, self.confir_code)
                else:
                    print('email tidak terkonfirmasi')
            except:pass

    def create_pw(self, email, cnfrcde):
        with requests.Session() as self.r:
            try:
                self.dihi = 'khamdihi28' if len(self.password_) == 0 else self.password_[0]
                self.pswd = '#PWD_INSTAGRAM:0:{}:{}'.format(int(time.time()),self.dihi)
                data = {
                    'params': '{"client_input_params":{"safetynet_response":"","email_oauth_token_map":{},"fb_ig_device_id":[],"safetynet_token":"ZGloaWRldi5pZEBpbmJveGtpdHRlbi5jb218MTcyMjc3NDQ3MXyiaMkB4yoAOaafikIB46YPr5jbnwtR7JI=","encrypted_msisdn_for_safetynet":"","lois_settings":{"lois_token":"","lara_override":""},"whatsapp_installed_on_client":1,"machine_id":"'+self.head['x-mid']+'","device_phone_numbers":[],"headers_last_infra_flow_id_safetynet":"","system_permissions_status":{"READ_CONTACTS":"UNKNOWN","GET_ACCOUNTS":"UNKNOWN","READ_PHONE_STATE":"DENIED","READ_PHONE_NUMBERS":"UNKNOWN"},"encrypted_password":"'+self.pswd+'"},"server_params":{"event_request_id":"'+self.config_app['event']+'","is_from_logged_out":0,"layered_homepage_experiment_group":null,"device_id":"'+self.head['x-ig-android-id']+'","waterfall_id":"'+self.config_app['wartel']+'","INTERNAL_latency_qpl_instance_id":1.17535492100089E14,"flow_info":"{\\"flow_name\\":\\"new_to_family_ig_default\\",\\"flow_type\\":\\"ntf\\"}","is_platform_login":0,"INTERNAL_latency_qpl_marker_id":36707139,"reg_info":"{\\"first_name\\":null,\\"last_name\\":null,\\"full_name\\":null,\\"contactpoint\\":\\"'+email+'\\",\\"ar_contactpoint\\":null,\\"contactpoint_type\\":\\"email\\",\\"is_using_unified_cp\\":false,\\"unified_cp_screen_variant\\":null,\\"is_cp_auto_confirmed\\":false,\\"is_cp_auto_confirmable\\":false,\\"confirmation_code\\":\\"'+cnfrcde+'\\",\\"birthday\\":null,\\"did_use_age\\":null,\\"gender\\":null,\\"use_custom_gender\\":false,\\"custom_gender\\":null,\\"encrypted_password\\":null,\\"username\\":null,\\"username_prefill\\":null,\\"fb_conf_source\\":null,\\"device_id\\":\\"'+self.head['x-ig-android-id']+'\\",\\"ig4a_qe_device_id\\":null,\\"family_device_id\\":\\"'+self.head['x-ig-family-device-id']+'\\",\\"nta_eligibility_reason\\":null,\\"ig_nta_test_group\\":null,\\"user_id\\":null,\\"safetynet_token\\":null,\\"safetynet_response\\":null,\\"machine_id\\":null,\\"profile_photo\\":null,\\"profile_photo_id\\":null,\\"profile_photo_upload_id\\":null,\\"avatar\\":null,\\"email_oauth_token_no_contact_perm\\":null,\\"email_oauth_token\\":null,\\"email_oauth_tokens\\":null,\\"should_skip_two_step_conf\\":null,\\"openid_tokens_for_testing\\":null,\\"encrypted_msisdn\\":null,\\"encrypted_msisdn_for_safetynet\\":null,\\"cached_headers_safetynet_info\\":null,\\"should_skip_headers_safetynet\\":null,\\"headers_last_infra_flow_id\\":null,\\"headers_last_infra_flow_id_safetynet\\":null,\\"headers_flow_id\\":null,\\"was_headers_prefill_available\\":null,\\"sso_enabled\\":null,\\"existing_accounts\\":null,\\"used_ig_birthday\\":null,\\"sync_info\\":null,\\"create_new_to_app_account\\":null,\\"skip_session_info\\":null,\\"ck_error\\":null,\\"ck_id\\":null,\\"ck_nonce\\":null,\\"should_save_password\\":null,\\"horizon_synced_username\\":null,\\"fb_access_token\\":null,\\"horizon_synced_profile_pic\\":null,\\"is_identity_synced\\":false,\\"is_msplit_reg\\":null,\\"user_id_of_msplit_creator\\":null,\\"dma_data_combination_consent_given\\":null,\\"xapp_accounts\\":null,\\"fb_device_id\\":null,\\"fb_machine_id\\":null,\\"ig_device_id\\":null,\\"ig_machine_id\\":null,\\"should_skip_nta_upsell\\":null,\\"big_blue_token\\":null,\\"skip_sync_step_nta\\":null,\\"caa_reg_flow_source\\":\\"login_home_native_integration_point\\",\\"ig_authorization_token\\":null,\\"full_sheet_flow\\":false,\\"crypted_user_id\\":null,\\"is_caa_perf_enabled\\":true,\\"is_preform\\":true,\\"ignore_suma_check\\":false,\\"ignore_existing_login\\":false,\\"ignore_existing_login_from_suma\\":false,\\"ignore_existing_login_after_errors\\":false,\\"suggested_first_name\\":null,\\"suggested_last_name\\":null,\\"suggested_full_name\\":null,\\"frl_authorization_token\\":null,\\"post_form_errors\\":null,\\"skip_step_without_errors\\":false,\\"existing_account_exact_match_checked\\":false,\\"existing_account_fuzzy_match_checked\\":false,\\"confirmation_code_send_error\\":null,\\"is_too_young\\":false,\\"source_account_type\\":null,\\"whatsapp_installed_on_client\\":false,\\"confirmation_medium\\":null,\\"source_credentials_type\\":null,\\"source_cuid\\":null,\\"source_account_reg_info\\":null,\\"soap_creation_source\\":null,\\"source_account_type_to_reg_info\\":null,\\"registration_flow_id\\":\\"'+self.config_app['reg_flow_id']+'\\",\\"should_skip_youth_tos\\":false,\\"is_youth_regulation_flow_complete\\":false,\\"is_on_cold_start\\":false,\\"email_prefilled\\":false,\\"cp_confirmed_by_auto_conf\\":false,\\"auto_conf_info\\":null,\\"in_sowa_experiment\\":false,\\"youth_regulation_config\\":null,\\"conf_allow_back_nav_after_change_cp\\":null,\\"conf_bouncing_cliff_screen_type\\":null,\\"conf_show_bouncing_cliff\\":null,\\"eligible_to_flash_call_in_ig4a\\":false,\\"flash_call_permissions_status\\":null,\\"attestation_result\\":null,\\"request_data_and_challenge_nonce_string\\":null,\\"confirmed_cp_and_code\\":[],\\"in_updated_eu_tos\\":false,\\"notification_callback_id\\":null,\\"reg_suma_state\\":0,\\"is_msplit_neutral_choice\\":false,\\"zero_tap_enabled\\":false,\\"msg_previous_cp\\":null,\\"ntp_import_source_info\\":null,\\"youth_consent_decision_time\\":null,\\"username_screen_experience\\":\\"control\\",\\"reduced_tos_test_group\\":\\"control\\",\\"should_show_spi_before_conf\\":true,\\"google_oauth_account\\":null,\\"is_reg_request_from_ig_suma\\":false,\\"is_igios_spc_reg\\":false,\\"device_emails\\":null,\\"is_toa_reg\\":false,\\"is_threads_public\\":false,\\"spc_import_flow\\":false}","family_device_id":"'+self.head['x-ig-family-device-id']+'","offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f,default,default,harm_f","access_flow_version":"F2_FLOW","is_from_logged_in_switcher":0,"current_step":6,"qe_device_id":"'+self.config_app['khamdihi_qe_dev']+'"}}',
                    'bk_client_context': '{"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}',
                    'bloks_versioning_id': '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a',
                }
                self.send = self.r.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.reg.password.async/', data=data, headers=self.head).text
                if 'Gunakan tanggal lahir Anda sendiri, meskipun akun ini untuk bisnis, hewan peliharaan, atau lainnya. Tidak ada yang akan melihat info ini kecuali Anda membagikannya.' in self.send.replace('\\',''):
                    self.create_ttl(email, self.pswd, cnfrcde)
                else:
                    print('kata sandi tidak dapat di buat')
            except:pass

    def create_ttl(self, email, encpw, cncode):
        with requests.Session() as self.r:
            try:
                birt = '{}-0{}-{}'.format(
                    random.randint(1,27),
                    random.randint(1,9),
                    random.randint(1999,2005)
                )
                data = {
                    'params': '{"client_input_params":{"should_skip_youth_tos":0,"is_youth_regulation_flow_complete":0,"birthday_or_current_date_string":"'+birt+'","birthday_timestamp":'+str(int(time.time()))+',"lois_settings":{"lois_token":"","lara_override":""}},"server_params":{"is_from_logged_out":0,"layered_homepage_experiment_group":null,"device_id":"'+self.head['x-ig-android-id']+'","waterfall_id":"'+self.config_app['wartel']+'","INTERNAL_latency_qpl_instance_id":1.17893066400324E14,"flow_info":"{\\"flow_name\\":\\"new_to_family_ig_default\\",\\"flow_type\\":\\"ntf\\"}","is_platform_login":0,"INTERNAL_latency_qpl_marker_id":36707139,"reg_info":"{\\"first_name\\":null,\\"last_name\\":null,\\"full_name\\":null,\\"contactpoint\\":\\"'+email+'\\",\\"ar_contactpoint\\":null,\\"contactpoint_type\\":\\"email\\",\\"is_using_unified_cp\\":false,\\"unified_cp_screen_variant\\":null,\\"is_cp_auto_confirmed\\":false,\\"is_cp_auto_confirmable\\":false,\\"confirmation_code\\":\\"'+cncode+'\\",\\"birthday\\":null,\\"did_use_age\\":false,\\"gender\\":null,\\"use_custom_gender\\":false,\\"custom_gender\\":null,\\"encrypted_password\\":\\"'+encpw+'\\",\\"username\\":null,\\"username_prefill\\":null,\\"fb_conf_source\\":null,\\"device_id\\":\\"'+self.head['x-ig-android-id']+'\\",\\"ig4a_qe_device_id\\":null,\\"family_device_id\\":\\"'+self.head['x-ig-family-device-id']+'\\",\\"nta_eligibility_reason\\":null,\\"ig_nta_test_group\\":null,\\"user_id\\":null,\\"safetynet_token\\":\\"ZGloaWRldi5pZEBpbmJveGtpdHRlbi5jb218MTcyMjc3NDQ3MXyiaMkB4yoAOaafikIB46YPr5jbnwtR7JI=\\",\\"safetynet_response\\":\\"\\",\\"machine_id\\":null,\\"profile_photo\\":null,\\"profile_photo_id\\":null,\\"profile_photo_upload_id\\":null,\\"avatar\\":null,\\"email_oauth_token_no_contact_perm\\":null,\\"email_oauth_token\\":null,\\"email_oauth_tokens\\":[],\\"should_skip_two_step_conf\\":null,\\"openid_tokens_for_testing\\":null,\\"encrypted_msisdn\\":null,\\"encrypted_msisdn_for_safetynet\\":null,\\"cached_headers_safetynet_info\\":null,\\"should_skip_headers_safetynet\\":null,\\"headers_last_infra_flow_id\\":null,\\"headers_last_infra_flow_id_safetynet\\":null,\\"headers_flow_id\\":null,\\"was_headers_prefill_available\\":null,\\"sso_enabled\\":null,\\"existing_accounts\\":null,\\"used_ig_birthday\\":null,\\"sync_info\\":null,\\"create_new_to_app_account\\":null,\\"skip_session_info\\":null,\\"ck_error\\":null,\\"ck_id\\":null,\\"ck_nonce\\":null,\\"should_save_password\\":true,\\"horizon_synced_username\\":null,\\"fb_access_token\\":null,\\"horizon_synced_profile_pic\\":null,\\"is_identity_synced\\":false,\\"is_msplit_reg\\":null,\\"user_id_of_msplit_creator\\":null,\\"dma_data_combination_consent_given\\":null,\\"xapp_accounts\\":null,\\"fb_device_id\\":null,\\"fb_machine_id\\":null,\\"ig_device_id\\":null,\\"ig_machine_id\\":null,\\"should_skip_nta_upsell\\":null,\\"big_blue_token\\":null,\\"skip_sync_step_nta\\":null,\\"caa_reg_flow_source\\":\\"login_home_native_integration_point\\",\\"ig_authorization_token\\":null,\\"full_sheet_flow\\":false,\\"crypted_user_id\\":null,\\"is_caa_perf_enabled\\":true,\\"is_preform\\":true,\\"ignore_suma_check\\":false,\\"ignore_existing_login\\":false,\\"ignore_existing_login_from_suma\\":false,\\"ignore_existing_login_after_errors\\":false,\\"suggested_first_name\\":null,\\"suggested_last_name\\":null,\\"suggested_full_name\\":null,\\"frl_authorization_token\\":null,\\"post_form_errors\\":null,\\"skip_step_without_errors\\":false,\\"existing_account_exact_match_checked\\":false,\\"existing_account_fuzzy_match_checked\\":false,\\"confirmation_code_send_error\\":null,\\"is_too_young\\":false,\\"source_account_type\\":null,\\"whatsapp_installed_on_client\\":true,\\"confirmation_medium\\":null,\\"source_credentials_type\\":null,\\"source_cuid\\":null,\\"source_account_reg_info\\":null,\\"soap_creation_source\\":null,\\"source_account_type_to_reg_info\\":null,\\"registration_flow_id\\":\\"'+self.config_app['reg_flow_id']+'\\",\\"should_skip_youth_tos\\":false,\\"is_youth_regulation_flow_complete\\":false,\\"is_on_cold_start\\":false,\\"email_prefilled\\":false,\\"cp_confirmed_by_auto_conf\\":false,\\"auto_conf_info\\":null,\\"in_sowa_experiment\\":false,\\"youth_regulation_config\\":null,\\"conf_allow_back_nav_after_change_cp\\":null,\\"conf_bouncing_cliff_screen_type\\":null,\\"conf_show_bouncing_cliff\\":null,\\"eligible_to_flash_call_in_ig4a\\":false,\\"flash_call_permissions_status\\":null,\\"attestation_result\\":null,\\"request_data_and_challenge_nonce_string\\":null,\\"confirmed_cp_and_code\\":[],\\"in_updated_eu_tos\\":false,\\"notification_callback_id\\":null,\\"reg_suma_state\\":0,\\"is_msplit_neutral_choice\\":false,\\"zero_tap_enabled\\":false,\\"msg_previous_cp\\":null,\\"ntp_import_source_info\\":null,\\"youth_consent_decision_time\\":null,\\"username_screen_experience\\":\\"control\\",\\"reduced_tos_test_group\\":\\"control\\",\\"should_show_spi_before_conf\\":true,\\"google_oauth_account\\":null,\\"is_reg_request_from_ig_suma\\":false,\\"is_igios_spc_reg\\":false,\\"device_emails\\":[],\\"is_toa_reg\\":false,\\"is_threads_public\\":false,\\"spc_import_flow\\":false}","family_device_id":"'+self.head['x-ig-family-device-id']+'","offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f,default,default,harm_f","access_flow_version":"F2_FLOW","is_from_logged_in_switcher":0,"current_step":8,"qe_device_id":"'+self.config_app['khamdihi_qe_dev']+'"}}',
                    'bk_client_context': '{"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}',
                    'bloks_versioning_id': '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a',
                }
                response = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.reg.birthday.async/',headers=self.head,data=data,)
                if 'Lanjutkan membuat akun' in response.text.replace('\\',''):
                    self.create_nama(email, birt, encpw, cncode)
                else:
                    print('format tanggal lahir salah atau spam')
            except:pass

    def create_nama(self, email, ultah, encpw, cncode):
        with requests.Session() as self.r:
            try:
                acak = random.choice(['ana','ani','ane','ine','inu','dihi','fika','fina','ulfa','fikha','riska','alifah','ali','azam']) if len(namarandom) == 1 else random.choice(namarandom)
                nama = '{} {}'.format(self.nama_acc['full_name'], acak)
                data = {
                    'params': '{"client_input_params":{"name":"'+nama+'","accounts_list":[{"uid":"68642707862","credential_type":"none","token":""},{"uid":"68642707862","token":"ts4MYxGlHjXOPkiFEIbPt5HCjdPWmzotCUP7NCiCC04JjIXgD13IArCcncyWv41q","account_type":"nonce","metadata":{"big_blue_token":null,"device_base_login_session":"Bearer IGT:2:eyJkc191c2VyX2lkIjoiNjg2NDI3MDc4NjIiLCJzZXNzaW9uaWQiOiI2ODY0MjcwNzg2MiUzQWRTNHY5UmpTU3NqRHp6JTNBMjclM0FBWWNNaDFNZ1p4WTNNVURmcS1QYVVrWVZxbzZ5NlFtLThZVG56N0JxNncifQ=="}}],"lois_settings":{"lois_token":"","lara_override":""}},"server_params":{"is_from_logged_out":0,"layered_homepage_experiment_group":null,"device_id":"'+self.head['x-ig-android-id']+'","waterfall_id":"9f1eed2b-0644-4fb7-9c12-9dca73ee0cf0","INTERNAL_latency_qpl_instance_id":1.47876056000066E14,"flow_info":"{\\"flow_name\\":\\"new_to_family_ig_default\\",\\"flow_type\\":\\"ntf\\"}","is_platform_login":0,"INTERNAL_latency_qpl_marker_id":36707139,"reg_info":"{\\"first_name\\":null,\\"last_name\\":null,\\"full_name\\":null,\\"contactpoint\\":\\"'+email+'\\",\\"ar_contactpoint\\":null,\\"contactpoint_type\\":\\"email\\",\\"is_using_unified_cp\\":false,\\"unified_cp_screen_variant\\":\\"control\\",\\"is_cp_auto_confirmed\\":false,\\"is_cp_auto_confirmable\\":false,\\"confirmation_code\\":\\"'+cncode+'\\",\\"birthday\\":\\"'+ultah+'\\",\\"did_use_age\\":false,\\"gender\\":null,\\"use_custom_gender\\":false,\\"custom_gender\\":null,\\"encrypted_password\\":\\"'+encpw+'\\",\\"username\\":null,\\"username_prefill\\":null,\\"fb_conf_source\\":null,\\"device_id\\":\\"'+self.head['x-ig-android-id']+'\\",\\"ig4a_qe_device_id\\":null,\\"family_device_id\\":\\"'+self.head['x-ig-family-device-id']+'\\",\\"nta_eligibility_reason\\":null,\\"ig_nta_test_group\\":null,\\"user_id\\":null,\\"safetynet_token\\":null,\\"safetynet_response\\":null,\\"machine_id\\":null,\\"profile_photo\\":null,\\"profile_photo_id\\":null,\\"profile_photo_upload_id\\":null,\\"avatar\\":null,\\"email_oauth_token_no_contact_perm\\":null,\\"email_oauth_token\\":null,\\"email_oauth_tokens\\":[],\\"should_skip_two_step_conf\\":null,\\"openid_tokens_for_testing\\":null,\\"encrypted_msisdn\\":null,\\"encrypted_msisdn_for_safetynet\\":null,\\"cached_headers_safetynet_info\\":null,\\"should_skip_headers_safetynet\\":null,\\"headers_last_infra_flow_id\\":null,\\"headers_last_infra_flow_id_safetynet\\":null,\\"headers_flow_id\\":null,\\"was_headers_prefill_available\\":null,\\"sso_enabled\\":null,\\"existing_accounts\\":null,\\"used_ig_birthday\\":null,\\"sync_info\\":null,\\"create_new_to_app_account\\":null,\\"skip_session_info\\":null,\\"ck_error\\":null,\\"ck_id\\":null,\\"ck_nonce\\":null,\\"should_save_password\\":true,\\"horizon_synced_username\\":null,\\"fb_access_token\\":null,\\"horizon_synced_profile_pic\\":null,\\"is_identity_synced\\":false,\\"is_msplit_reg\\":null,\\"user_id_of_msplit_creator\\":null,\\"dma_data_combination_consent_given\\":null,\\"xapp_accounts\\":null,\\"fb_device_id\\":null,\\"fb_machine_id\\":null,\\"ig_device_id\\":null,\\"ig_machine_id\\":null,\\"should_skip_nta_upsell\\":null,\\"big_blue_token\\":null,\\"skip_sync_step_nta\\":null,\\"caa_reg_flow_source\\":\\"login_home_native_integration_point\\",\\"ig_authorization_token\\":null,\\"full_sheet_flow\\":false,\\"crypted_user_id\\":null,\\"is_caa_perf_enabled\\":true,\\"is_preform\\":true,\\"ignore_suma_check\\":false,\\"ignore_existing_login\\":false,\\"ignore_existing_login_from_suma\\":false,\\"ignore_existing_login_after_errors\\":false,\\"suggested_first_name\\":null,\\"suggested_last_name\\":null,\\"suggested_full_name\\":null,\\"frl_authorization_token\\":null,\\"post_form_errors\\":null,\\"skip_step_without_errors\\":false,\\"existing_account_exact_match_checked\\":false,\\"existing_account_fuzzy_match_checked\\":false,\\"confirmation_code_send_error\\":null,\\"is_too_young\\":false,\\"source_account_type\\":null,\\"whatsapp_installed_on_client\\":true,\\"confirmation_medium\\":null,\\"source_credentials_type\\":null,\\"source_cuid\\":null,\\"source_account_reg_info\\":null,\\"soap_creation_source\\":null,\\"source_account_type_to_reg_info\\":null,\\"registration_flow_id\\":\\"'+self.config_app['reg_flow_id']+'\\",\\"should_skip_youth_tos\\":false,\\"is_youth_regulation_flow_complete\\":false,\\"is_on_cold_start\\":false,\\"email_prefilled\\":false,\\"cp_confirmed_by_auto_conf\\":false,\\"auto_conf_info\\":null,\\"in_sowa_experiment\\":false,\\"youth_regulation_config\\":null,\\"conf_allow_back_nav_after_change_cp\\":null,\\"conf_bouncing_cliff_screen_type\\":null,\\"conf_show_bouncing_cliff\\":null,\\"eligible_to_flash_call_in_ig4a\\":false,\\"flash_call_permissions_status\\":null,\\"attestation_result\\":null,\\"request_data_and_challenge_nonce_string\\":null,\\"confirmed_cp_and_code\\":[],\\"in_updated_eu_tos\\":false,\\"notification_callback_id\\":null,\\"reg_suma_state\\":0,\\"is_msplit_neutral_choice\\":false,\\"zero_tap_enabled\\":false,\\"msg_previous_cp\\":null,\\"ntp_import_source_info\\":null,\\"youth_consent_decision_time\\":null,\\"username_screen_experience\\":\\"control\\",\\"reduced_tos_test_group\\":\\"control\\",\\"should_show_spi_before_conf\\":true,\\"google_oauth_account\\":null,\\"is_reg_request_from_ig_suma\\":false,\\"is_igios_spc_reg\\":false,\\"device_emails\\":[],\\"is_toa_reg\\":false,\\"is_threads_public\\":false,\\"spc_import_flow\\":false}","family_device_id":"'+self.head['x-ig-family-device-id']+'","offline_experiment_group":"caa_iteration_v3_perf_ig_4","INTERNAL_INFRA_THEME":"harm_f,default,default,harm_f","access_flow_version":"F2_FLOW","is_from_logged_in_switcher":0,"current_step":9,"qe_device_id":"'+self.config_app['khamdihi_qe_dev']+'"}}',
                    'bk_client_context': '{"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}',
                    'bloks_versioning_id': '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a',
                }
                response = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.reg.name_ig_and_soap.async/',headers=self.head,data=data,)
                if 'Hapus teks Nama Pengguna' in response.text.replace('\\',''):
                    self.create_username(email, ultah, encpw, nama, cncode)
                else:
                    print('nama gagal di buat')
            except:pass

    def create_username(self, email, ultah, encpw, fullname, cncode):
        with requests.Session() as self.r:
            try:
                username = self.nama_acc['username']
                data = {
                    'params': '{"client_input_params":{"validation_text":"'+username+'","family_device_id":"'+self.head['x-ig-family-device-id']+'","device_id":"'+ self.head['x-ig-android-id']+'","lois_settings":{"lois_token":"","lara_override":""},"qe_device_id":"'+self.config_app['khamdihi_qe_dev']+'"},"server_params":{"event_request_id":"'+self.config_app['event']+'","is_from_logged_out":0,"text_input_id":147972553800031,"layered_homepage_experiment_group":null,"device_id":"'+self.head['x-ig-android-id']+'","waterfall_id":"'+self.config_app['wartel']+'","INTERNAL_latency_qpl_instance_id":1.47972553800033E14,"flow_info":"{\\"flow_name\\":\\"new_to_family_ig_default\\",\\"flow_type\\":\\"ntf\\"}","is_platform_login":0,"INTERNAL_latency_qpl_marker_id":36707139,"reg_info":"{\\"first_name\\":null,\\"last_name\\":null,\\"full_name\\":\\"'+fullname+'\\",\\"contactpoint\\":\\"'+email+'\\",\\"ar_contactpoint\\":null,\\"contactpoint_type\\":\\"email\\",\\"is_using_unified_cp\\":false,\\"unified_cp_screen_variant\\":\\"control\\",\\"is_cp_auto_confirmed\\":false,\\"is_cp_auto_confirmable\\":false,\\"confirmation_code\\":\\"'+cncode+'\\",\\"birthday\\":\\"'+ultah+'\\",\\"did_use_age\\":false,\\"gender\\":null,\\"use_custom_gender\\":false,\\"custom_gender\\":null,\\"encrypted_password\\":\\"'+encpw+'\\",\\"username\\":null,\\"username_prefill\\":\\"'+username+'\\",\\"fb_conf_source\\":null,\\"device_id\\":\\"'+self.head['x-ig-android-id']+'\\",\\"ig4a_qe_device_id\\":null,\\"family_device_id\\":\\"'+self.head['x-ig-family-device-id']+'\\",\\"nta_eligibility_reason\\":null,\\"ig_nta_test_group\\":null,\\"user_id\\":null,\\"safetynet_token\\":null,\\"safetynet_response\\":null,\\"machine_id\\":null,\\"profile_photo\\":null,\\"profile_photo_id\\":null,\\"profile_photo_upload_id\\":null,\\"avatar\\":null,\\"email_oauth_token_no_contact_perm\\":null,\\"email_oauth_token\\":null,\\"email_oauth_tokens\\":[],\\"should_skip_two_step_conf\\":null,\\"openid_tokens_for_testing\\":null,\\"encrypted_msisdn\\":null,\\"encrypted_msisdn_for_safetynet\\":null,\\"cached_headers_safetynet_info\\":null,\\"should_skip_headers_safetynet\\":null,\\"headers_last_infra_flow_id\\":null,\\"headers_last_infra_flow_id_safetynet\\":null,\\"headers_flow_id\\":null,\\"was_headers_prefill_available\\":null,\\"sso_enabled\\":null,\\"existing_accounts\\":null,\\"used_ig_birthday\\":null,\\"sync_info\\":null,\\"create_new_to_app_account\\":null,\\"skip_session_info\\":null,\\"ck_error\\":null,\\"ck_id\\":null,\\"ck_nonce\\":null,\\"should_save_password\\":true,\\"horizon_synced_username\\":null,\\"fb_access_token\\":null,\\"horizon_synced_profile_pic\\":null,\\"is_identity_synced\\":false,\\"is_msplit_reg\\":null,\\"user_id_of_msplit_creator\\":null,\\"dma_data_combination_consent_given\\":null,\\"xapp_accounts\\":null,\\"fb_device_id\\":null,\\"fb_machine_id\\":null,\\"ig_device_id\\":null,\\"ig_machine_id\\":null,\\"should_skip_nta_upsell\\":null,\\"big_blue_token\\":null,\\"skip_sync_step_nta\\":null,\\"caa_reg_flow_source\\":\\"login_home_native_integration_point\\",\\"ig_authorization_token\\":null,\\"full_sheet_flow\\":false,\\"crypted_user_id\\":null,\\"is_caa_perf_enabled\\":true,\\"is_preform\\":true,\\"ignore_suma_check\\":false,\\"ignore_existing_login\\":false,\\"ignore_existing_login_from_suma\\":false,\\"ignore_existing_login_after_errors\\":false,\\"suggested_first_name\\":null,\\"suggested_last_name\\":null,\\"suggested_full_name\\":null,\\"frl_authorization_token\\":null,\\"post_form_errors\\":null,\\"skip_step_without_errors\\":false,\\"existing_account_exact_match_checked\\":false,\\"existing_account_fuzzy_match_checked\\":false,\\"confirmation_code_send_error\\":null,\\"is_too_young\\":false,\\"source_account_type\\":null,\\"whatsapp_installed_on_client\\":true,\\"confirmation_medium\\":null,\\"source_credentials_type\\":null,\\"source_cuid\\":null,\\"source_account_reg_info\\":null,\\"soap_creation_source\\":null,\\"source_account_type_to_reg_info\\":null,\\"registration_flow_id\\":\\"'+self.config_app['reg_flow_id']+'\\",\\"should_skip_youth_tos\\":false,\\"is_youth_regulation_flow_complete\\":false,\\"is_on_cold_start\\":false,\\"email_prefilled\\":false,\\"cp_confirmed_by_auto_conf\\":false,\\"auto_conf_info\\":null,\\"in_sowa_experiment\\":false,\\"youth_regulation_config\\":null,\\"conf_allow_back_nav_after_change_cp\\":null,\\"conf_bouncing_cliff_screen_type\\":null,\\"conf_show_bouncing_cliff\\":null,\\"eligible_to_flash_call_in_ig4a\\":false,\\"flash_call_permissions_status\\":null,\\"attestation_result\\":null,\\"request_data_and_challenge_nonce_string\\":null,\\"confirmed_cp_and_code\\":[],\\"in_updated_eu_tos\\":false,\\"notification_callback_id\\":null,\\"reg_suma_state\\":0,\\"is_msplit_neutral_choice\\":false,\\"zero_tap_enabled\\":false,\\"msg_previous_cp\\":null,\\"ntp_import_source_info\\":null,\\"youth_consent_decision_time\\":null,\\"username_screen_experience\\":\\"control\\",\\"reduced_tos_test_group\\":\\"control\\",\\"should_show_spi_before_conf\\":true,\\"google_oauth_account\\":null,\\"is_reg_request_from_ig_suma\\":false,\\"is_igios_spc_reg\\":false,\\"device_emails\\":[],\\"is_toa_reg\\":false,\\"is_threads_public\\":false,\\"spc_import_flow\\":false}","family_device_id":"'+self.head['x-ig-family-device-id']+'","offline_experiment_group":"caa_iteration_v3_perf_ig_4","INTERNAL_INFRA_THEME":"harm_f,default,default,harm_f","suggestions_container_id":147972553800030,"action":1,"screen_id":147972553800017,"access_flow_version":"F2_FLOW","input_id":147972553800032,"is_from_logged_in_switcher":0,"current_step":10,"qe_device_id":"'+self.config_app['khamdihi_qe_dev']+'"}}',
                    'bk_client_context': '{"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}',
                    'bloks_versioning_id': '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a',
                }
                response = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.reg.username.async/',headers=self.head,data=data,)
                if 'Setuju dengan syarat dan kebijakan Instagram' in (response.text.replace('\\','')):
                    self.buat_akun(email, ultah, encpw, fullname, username, cncode)
                else:
                    print('username tidak dapat di buat')
            except:pass

    def buat_akun(self, email, ultah, encpw, fullname, username, cncode):
        global sucess, errors
        with requests.Session() as self.r:
            try:
                data = {
                    'params': '{"client_input_params":{"ck_error":"","device_id":"'+self.head['x-ig-android-id']+'","ck_nonce":"","lois_settings":{"lois_token":"","lara_override":""},"waterfall_id":"'+self.config_app['wartel']+'","ck_id":"","no_contact_perm_email_oauth_token":"","headers_last_infra_flow_id":"","machine_id":"'+self.head['x-mid']+'","should_ignore_existing_login":0,"reached_from_tos_screen":1,"encrypted_msisdn":""},"server_params":{"event_request_id":"'+self.config_app['event']+'","is_from_logged_out":0,"layered_homepage_experiment_group":null,"device_id":"'+self.head['x-ig-android-id']+'","waterfall_id":"'+self.config_app['wartel']+'","INTERNALlatency_qpl_instance_id":1.48009339800064E14,"flow_info":"{\\"flow_name\\":\\"new_to_family_ig_default\\",\\"flow_type\\":\\"ntf\\"}","is_platform_login":0,"INTERNAL_latency_qpl_marker_id":36707130,"reg_info":"{\\"first_name\\":null,\\"last_name\\":null,\\"full_name\\":\\"'+fullname+'\\",\\"contactpoint\\":\\"'+email+'\\",\\"ar_contactpoint\\":null,\\"contactpoint_type\\":\\"email\\",\\"is_using_unified_cp\\":false,\\"unified_cp_screen_variant\\":\\"control\\",\\"is_cp_auto_confirmed\\":false,\\"is_cp_auto_confirmable\\":false,\\"confirmation_code\\":\\"'+cncode+'\\",\\"birthday\\":\\"'+ultah+'\\",\\"did_use_age\\":false,\\"gender\\":null,\\"use_custom_gender\\":false,\\"custom_gender\\":null,\\"encrypted_password\\":\\"'+encpw+'\\",\\"username\\":\\"'+username+'\\",\\"username_prefill\\":\\"'+username+'\\",\\"fb_conf_source\\":null,\\"device_id\\":\\"'+self.head['x-ig-android-id']+'\\",\\"ig4a_qe_device_id\\":null,\\"family_device_id\\":\\"'+self.head['x-ig-family-device-id']+'\\",\\"nta_eligibility_reason\\":null,\\"ig_nta_test_group\\":null,\\"user_id\\":null,\\"safetynet_token\\":null,\\"safetynet_response\\":null,\\"machine_id\\":null,\\"profile_photo\\":null,\\"profile_photo_id\\":null,\\"profile_photo_upload_id\\":null,\\"avatar\\":null,\\"email_oauth_token_no_contact_perm\\":null,\\"email_oauth_token\\":null,\\"email_oauth_tokens\\":[],\\"should_skip_two_step_conf\\":null,\\"openid_tokens_for_testing\\":null,\\"encrypted_msisdn\\":null,\\"encrypted_msisdn_for_safetynet\\":null,\\"cached_headers_safetynet_info\\":null,\\"should_skip_headers_safetynet\\":null,\\"headers_last_infra_flow_id\\":null,\\"headers_last_infra_flow_id_safetynet\\":null,\\"headers_flow_id\\":null,\\"was_headers_prefill_available\\":null,\\"sso_enabled\\":null,\\"existing_accounts\\":null,\\"used_ig_birthday\\":null,\\"sync_info\\":null,\\"create_new_to_app_account\\":null,\\"skip_session_info\\":null,\\"ck_error\\":null,\\"ck_id\\":null,\\"ck_nonce\\":null,\\"should_save_password\\":true,\\"horizon_synced_username\\":null,\\"fb_access_token\\":null,\\"horizon_synced_profile_pic\\":null,\\"is_identity_synced\\":false,\\"is_msplit_reg\\":null,\\"user_id_of_msplit_creator\\":null,\\"dma_data_combination_consent_given\\":null,\\"xapp_accounts\\":null,\\"fb_device_id\\":null,\\"fb_machine_id\\":null,\\"ig_device_id\\":null,\\"ig_machine_id\\":null,\\"should_skip_nta_upsell\\":null,\\"big_blue_token\\":null,\\"skip_sync_step_nta\\":null,\\"caa_reg_flow_source\\":\\"login_home_native_integration_point\\",\\"ig_authorization_token\\":null,\\"full_sheet_flow\\":false,\\"crypted_user_id\\":null,\\"is_caa_perf_enabled\\":true,\\"is_preform\\":true,\\"ignore_suma_check\\":false,\\"ignore_existing_login\\":false,\\"ignore_existing_login_from_suma\\":false,\\"ignore_existing_login_after_errors\\":false,\\"suggested_first_name\\":null,\\"suggested_last_name\\":null,\\"suggested_full_name\\":null,\\"frl_authorization_token\\":null,\\"post_form_errors\\":null,\\"skip_step_without_errors\\":false,\\"existing_account_exact_match_checked\\":false,\\"existing_account_fuzzy_match_checked\\":false,\\"confirmation_code_send_error\\":null,\\"is_too_young\\":false,\\"source_account_type\\":null,\\"whatsapp_installed_on_client\\":true,\\"confirmation_medium\\":null,\\"source_credentials_type\\":null,\\"source_cuid\\":null,\\"source_account_reg_info\\":null,\\"soap_creation_source\\":null,\\"source_account_type_to_reg_info\\":null,\\"registration_flow_id\\":\\"'+self.config_app['reg_flow_id']+'\\",\\"should_skip_youth_tos\\":false,\\"is_youth_regulation_flow_complete\\":false,\\"is_on_cold_start\\":false,\\"email_prefilled\\":false,\\"cp_confirmed_by_auto_conf\\":false,\\"auto_conf_info\\":null,\\"in_sowa_experiment\\":false,\\"youth_regulation_config\\":null,\\"conf_allow_back_nav_after_change_cp\\":null,\\"conf_bouncing_cliff_screen_type\\":null,\\"conf_show_bouncing_cliff\\":null,\\"eligible_to_flash_call_in_ig4a\\":false,\\"flash_call_permissions_status\\":null,\\"attestation_result\\":null,\\"request_data_and_challenge_nonce_string\\":null,\\"confirmed_cp_and_code\\":[],\\"in_updated_eu_tos\\":false,\\"notification_callback_id\\":null,\\"reg_suma_state\\":0,\\"is_msplit_neutral_choice\\":false,\\"zero_tap_enabled\\":false,\\"msg_previous_cp\\":null,\\"ntp_import_source_info\\":null,\\"youth_consent_decision_time\\":null,\\"username_screen_experience\\":\\"control\\",\\"reduced_tos_test_group\\":\\"control\\",\\"should_show_spi_before_conf\\":true,\\"google_oauth_account\\":null,\\"is_reg_request_from_ig_suma\\":false,\\"is_igios_spc_reg\\":false,\\"device_emails\\":[],\\"is_toa_reg\\":false,\\"is_threads_public\\":false,\\"spc_import_flow\\":false}","family_device_id":"'+self.head['x-ig-family-device-id']+'","offline_experiment_group":"caa_iteration_v3_perf_ig_4","INTERNAL_INFRA_THEME":"harm_f,default,default,harm_f","access_flow_version":"F2_FLOW","app_id":0,"is_from_logged_in_switcher":0,"current_step":11,"qe_device_id":"'+self.config_app['khamdihi_qe_dev']+'"}}',
                    'bk_client_context': '{"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}',
                    'bloks_versioning_id': '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a',
                }
                self.head.update({'content-length': self.konten_length(data)})
                response = self.r.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.reg.create.account.async/',headers=self.head,data=data,proxies=self.proxies)
                if 'Kami membatasi aktivitas tertentu untuk melindungi komunitas kami. Beri tahu kami jika menurut Anda kami melakukan kesalahan.' in response.text.replace('\\',''):
                    errors +=1

                elif 'Bearer IGT:2' in response.text.replace('\\',''):
                    self.sucs = response.text.replace('\\','')
                    self.user = re.search('"username":"(.*?)"', str(self.sucs)).group(1)
                    self.nama = re.search('"full_name":"(.*?)"', str(self.sucs)).group(1)
                    self.bear = re.search('"Bearer IGT:2:(.*?)"', str(self.sucs)).group(1)
                    self.pkid = re.search('"pk_id":"(\d+)"', str(self.sucs)).group(1)
                    self.coki = 'mid=%s;'%(self.head['x-mid']) + self.CookieBearer(self.bear)
                    self.info = self.r.get(f'https://i.instagram.com/api/v1/users/{self.pkid}/info/?is_prefetch=true', headers=self.head,cookies={'cookie':self.coki})
                    #print('status code',self.info.text)
                    #self.follow(self.coki)
                    print(f'''\r						
status   : success create
username : {self.user}
inbox    : {email}
userid   : {self.pkid}
password : {encpw.split(':')[3]}
fullname : {self.nama}
akses email : https://inboxkitten.com/inbox/{email.split("@")[0]}/list
bearer      : {self.bear}
                          ''')
                    sucess +=1
                    self.save = '%s|%s|%s\n'%(self.user,encpw.split(':')[3],email)
                    open('data/create_success.txt','a').write(self.save)
                    self.delay()
                else:
                    print('Error saat permintaan',end='\r')
                    self.delay()
                print('success %s errors %s'%(sucess, errors), end='\r')
            except Exception as e:
                 print(f'Error saat permintaan {e}',end='\r')

    def CookieBearer(self, cookie):
        self.abcd = json.loads(base64.b64decode(cookie).decode())
        self.coki = ';'.join(['%s=%s'%(x,y) for x,y in self.abcd.items()])
        return self.coki + f';dpr=2;ig_did={str(uuid.uuid4()).upper()}'

    def follow(self, cookies):
        with requests.Session() as self.r:
            try:
                self.headers = {
                   'x-bloks-version-id': 'f0594120c8dba08dee2d395a000ede0009f6e1795ba7c4adf573f3cbd442ebff',
                   'sec-ch-ua-platform-version': '"12.0.0"',
                   'x-fb-friendly-name': 'usePolarisFollowMutation',
                   'x-asbd-id': '129477',
                   'sec-ch-ua-full-version-list': '"Not)A;Brand";v="99.0.0.0", "Google Chrome";v="127.0.6533.84", "Chromium";v="127.0.6533.84"',
                   'sec-ch-ua-model': '"Infinix X6515"',
                   'x-ig-app-id': '1217981644879628',
                   'origin': 'https://www.instagram.com',
                   'sec-fetch-site': 'same-origin',
                   'sec-fetch-mode': 'cors',
                   'sec-fetch-dest': 'empty',
                   'referer': 'https://www.instagram.com/khamdihi.io/',
                   'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,tr;q=0.6',
                   'priority': 'u=1, i', 'cookie': cookies}
                self.send = self.r.get('https://www.instagram.com/khamdihi.io', cookies={'cookie':cookies}, proxies=self.proxies).text
                self.data = {
                   'av': re.search('"actorID":"(\d+)"',str(self.send)).group(1),
                   '__d': 'www',
                   '__user': '0',
                   '__a': '1',
                   '__req': 'v',
                   '__hs': '19940.HYP:instagram_web_pkg.2.1..0.1',
                   'dpr': '2',
                   '__ccg': 'UNKNOWN',
                   '__rev': re.search('"rev":(\d+)',str(self.send)).group(1),
                   '__s': '',
                   '__hsi': re.search('"hsi":"(\d+)"',str(self.send)).group(1),
                   '__dyn': '',
                   '__csr': '',
                   '__comet_req': '7',
                   'fb_dtsg': re.search('"DTSGInitData",\[\],{"token":"(.*?)"',str(self.send)).group(1),
                   'jazoest': re.search('jazoest=(\d+)',str(self.send)).group(1),
                   'lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(self.send)).group(1),
                   '__spin_r': re.search('"__spin_r":(\d+)',str(self.send)).group(1),
                   '__spin_b': 'trunk',
                   '__spin_t': re.search('"__spin_t":(\d+)',str(self.send)).group(1),
                   'fb_api_caller_class': 'RelayModern',
                   'fb_api_req_friendly_name': 'usePolarisFollowMutation',
                   'variables': '{"target_user_id":"68075246921","container_module":"profile","nav_chain":"PolarisProfilePostsTabRoot:profilePage:1:via_cold_start"}',
                   'server_timestamps': 'true',
                   'doc_id': '7275591572570580',
                }
                self.response = requests.post('https://www.instagram.com/graphql/query', data=self.data, headers=self.headers,proxies=self.proxies).json()
                print(self.response)
            except Exception as e:print(e)

    def delay(self):
        sec = 20
        for _ in range(20):
            time.sleep(1)
            sec -=1

    def send_email(self, inbox_email):
        with requests.Session() as self.r:
            try:
                self.head = asset().headers_app()
                self.fmid = self.head['x-ig-family-device-id']
                self.dvid = self.head['x-ig-android-id']
                self.regs = str(uuid.uuid4())
                self.qdev = str(uuid.uuid4())
                self.watl = str(uuid.uuid4())
                self.even = str(uuid.uuid4())
                self.ulfa = (f'normal_token_hash=&device_id={self.dvid}&custom_device_id={self.head["x-ig-device-id"]}&fetch_reason=token_stale')
                self.xmid = self.r.post('https://i.instagram.com/api/v1/zr/dual_tokens/', data=self.ulfa, headers=self.head,proxies=self.proxies)
                if self.xmid.headers.get('ig-set-x-mid'):
                   self.head.update({'x-mid': self.xmid.headers.get('ig-set-x-mid')})
                self.data = {
                    'params': '{"client_input_params":{"accounts_list":[],"email_prefilled":0,"confirmed_cp_and_code":{},"family_device_id":"'+self.fmid+'","fb_ig_device_id":[],"device_id":"'+self.dvid+'","lois_settings":{"lois_token":"","lara_override":""},"msg_previous_cp":"","is_from_device_emails":0,"email":"'+inbox_email+'"},"server_params":{"event_request_id":"'+str(uuid.uuid4())+'","is_from_logged_out":0,"text_input_id":116503358500031,"layered_homepage_experiment_group":null,"device_id":"'+self.dvid+'","waterfall_id":"'+str(uuid.uuid4())+'","INTERNAL_latency_qpl_instance_id":1.16503358500161E14,"flow_info":"{\\"flow_name\\":\\"new_to_family_ig_default\\",\\"flow_type\\":\\"ntf\\"}","is_platform_login":0,"INTERNAL_latency_qpl_marker_id":36707139,"reg_info":"{\\"first_name\\":null,\\"last_name\\":null,\\"full_name\\":null,\\"contactpoint\\":null,\\"ar_contactpoint\\":null,\\"contactpoint_type\\":null,\\"is_using_unified_cp\\":null,\\"unified_cp_screen_variant\\":null,\\"is_cp_auto_confirmed\\":false,\\"is_cp_auto_confirmable\\":false,\\"confirmation_code\\":null,\\"birthday\\":null,\\"did_use_age\\":null,\\"gender\\":null,\\"use_custom_gender\\":false,\\"custom_gender\\":null,\\"encrypted_password\\":null,\\"username\\":null,\\"username_prefill\\":null,\\"fb_conf_source\\":null,\\"device_id\\":\\"'+self.dvid+'\\",\\"ig4a_qe_device_id\\":null,\\"family_device_id\\":\\"'+self.fmid+'\\",\\"nta_eligibility_reason\\":null,\\"ig_nta_test_group\\":null,\\"user_id\\":null,\\"safetynet_token\\":null,\\"safetynet_response\\":null,\\"machine_id\\":null,\\"profile_photo\\":null,\\"profile_photo_id\\":null,\\"profile_photo_upload_id\\":null,\\"avatar\\":null,\\"email_oauth_token_no_contact_perm\\":null,\\"email_oauth_token\\":null,\\"email_oauth_tokens\\":null,\\"should_skip_two_step_conf\\":null,\\"openid_tokens_for_testing\\":null,\\"encrypted_msisdn\\":null,\\"encrypted_msisdn_for_safetynet\\":null,\\"cached_headers_safetynet_info\\":null,\\"should_skip_headers_safetynet\\":null,\\"headers_last_infra_flow_id\\":null,\\"headers_last_infra_flow_id_safetynet\\":null,\\"headers_flow_id\\":null,\\"was_headers_prefill_available\\":null,\\"sso_enabled\\":null,\\"existing_accounts\\":null,\\"used_ig_birthday\\":null,\\"sync_info\\":null,\\"create_new_to_app_account\\":null,\\"skip_session_info\\":null,\\"ck_error\\":null,\\"ck_id\\":null,\\"ck_nonce\\":null,\\"should_save_password\\":null,\\"horizon_synced_username\\":null,\\"fb_access_token\\":null,\\"horizon_synced_profile_pic\\":null,\\"is_identity_synced\\":false,\\"is_msplit_reg\\":null,\\"user_id_of_msplit_creator\\":null,\\"dma_data_combination_consent_given\\":null,\\"xapp_accounts\\":null,\\"fb_device_id\\":null,\\"fb_machine_id\\":null,\\"ig_device_id\\":null,\\"ig_machine_id\\":null,\\"should_skip_nta_upsell\\":null,\\"big_blue_token\\":null,\\"skip_sync_step_nta\\":null,\\"caa_reg_flow_source\\":\\"login_home_native_integration_point\\",\\"ig_authorization_token\\":null,\\"full_sheet_flow\\":false,\\"crypted_user_id\\":null,\\"is_caa_perf_enabled\\":true,\\"is_preform\\":true,\\"ignore_suma_check\\":false,\\"ignore_existing_login\\":false,\\"ignore_existing_login_from_suma\\":false,\\"ignore_existing_login_after_errors\\":false,\\"suggested_first_name\\":null,\\"suggested_last_name\\":null,\\"suggested_full_name\\":null,\\"frl_authorization_token\\":null,\\"post_form_errors\\":null,\\"skip_step_without_errors\\":false,\\"existing_account_exact_match_checked\\":false,\\"existing_account_fuzzy_match_checked\\":false,\\"confirmation_code_send_error\\":null,\\"is_too_young\\":false,\\"source_account_type\\":null,\\"whatsapp_installed_on_client\\":false,\\"confirmation_medium\\":null,\\"source_credentials_type\\":null,\\"source_cuid\\":null,\\"source_account_reg_info\\":null,\\"soap_creation_source\\":null,\\"source_account_type_to_reg_info\\":null,\\"registration_flow_id\\":\\"'+self.regs+'\\",\\"should_skip_youth_tos\\":false,\\"is_youth_regulation_flow_complete\\":false,\\"is_on_cold_start\\":false,\\"email_prefilled\\":false,\\"cp_confirmed_by_auto_conf\\":false,\\"auto_conf_info\\":null,\\"in_sowa_experiment\\":false,\\"youth_regulation_config\\":null,\\"conf_allow_back_nav_after_change_cp\\":null,\\"conf_bouncing_cliff_screen_type\\":null,\\"conf_show_bouncing_cliff\\":null,\\"eligible_to_flash_call_in_ig4a\\":false,\\"flash_call_permissions_status\\":null,\\"attestation_result\\":null,\\"request_data_and_challenge_nonce_string\\":null,\\"confirmed_cp_and_code\\":null,\\"in_updated_eu_tos\\":false,\\"notification_callback_id\\":null,\\"reg_suma_state\\":0,\\"is_msplit_neutral_choice\\":false,\\"zero_tap_enabled\\":false,\\"msg_previous_cp\\":null,\\"ntp_import_source_info\\":null,\\"youth_consent_decision_time\\":null,\\"username_screen_experience\\":\\"control\\",\\"reduced_tos_test_group\\":\\"control\\",\\"should_show_spi_before_conf\\":true,\\"google_oauth_account\\":null,\\"is_reg_request_from_ig_suma\\":false,\\"is_igios_spc_reg\\":false,\\"device_emails\\":null,\\"is_toa_reg\\":false,\\"is_threads_public\\":false,\\"spc_import_flow\\":false}","family_device_id":"'+self.fmid+'","offline_experiment_group":null,"cp_funnel":0,"INTERNAL_INFRA_THEME":"harm_f,default,default,harm_f","cp_source":0,"access_flow_version":"F2_FLOW","is_from_logged_in_switcher":0,"current_step":0,"qe_device_id":"'+self.qdev+'"}}',
                    'bk_client_context': '{"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}',
                    'bloks_versioning_id': '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a',
                }
                self.head.update({'content-length': self.konten_length(self.data)})
                self.send = self.r.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.reg.async.contactpoint_email.async/', headers=self.head,data=self.data)
                if 'Kode diperlukan. Periksa email atau pesan teks Anda untuk menemukan kodenya.' in self.send.text.replace('\\',''):
                    self.config_app.update({
                      'reg_flow_id': self.regs,
                      'khamdihi_qe_dev': self.qdev,
                      'event': self.even,
                      'wartel': self.watl

                    })
                    return inbox_email
                else:
                    print('email kemungkinan telah di gunakan')
                    return False
            except Exception as e:
                print(f'kesalahan dalam permintaan {e}')
                return False

    def Menu(self):
        global sucess, errors
        os.system('clear' if 'linux' in sys.platform.lower() else 'cls')
        print('author : khamdihiDev')
        print('github : https://github.com/khamdihi-dev\n')
        print('1. start create account')
        print('2. check hasil pembuatan')
        print('3. upgrage license\n')
        self.xyz = input('choose : ')
        if self.xyz in ['1','01']:
           print('\nMasukan Username Untuk Akun Anda, Username Akan Otomatis Di Tambahkan Angka!')
           self.uusername = input('Username : ')
           print('\nMasukan Nama Depan Misalnya khamdihi')
           self.nama_depan = input('Nama Depan : ')
           print('\nMasukan Sandi Untuk Akun Kamu, Sandi Harus 6 Karakter Atau Lebih..')
           self.passw = input('Password Akun : ')
           if len(self.passw) <6:print('Password Harus 6 Karakter Atau lebih!');exit()
           else:self.password_.append(self.passw)
           print('\nProses Sedang Di Mulai, Silahkan Tunggu\n')
           while True:
               self.nama_acc.update({'username':f'{self.uusername}{random.randint(1,999)}','full_name':self.nama_depan})
               try:self.Insta()
               except KeyboardInterrupt: break
           exit(1)

        elif self.xyz in ['2','02']:
           for res in open('data/create_success.txt','r').read().splitlines():
               print(res)  
           exit()
        elif self.xyz in ['3','03']:
           os.system('xdg-open https://wa.me/+6283853140469')
        else:self.Menu()

asset().RandomNama()
Run().Menu()
