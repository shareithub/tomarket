git clone https://github.com/LFG-AAI/tomarket.git
MASUK KE FOLDER BOT :
cd tomarket
COMMAND TERMUX || COMMAND IN VPS :
python -m venv tomarket  || python3 -m venv tomarket
MASUK MODE VENV :
source tomarket/bin/activate
INSTALL SEMUA MODULE :
pip install -r requirements.txt
KELUAR MODE VENV :
deactivate
EDIT TOKEN DI TOKENS.TXT :
nano tokens.txt
Paste your token, support multi account. paste in new line
SAVE DENGAN PERINTAH :
CTRL+ x pilih (Y) lalu ENTER
RUN BOT :
python main.py ( TERMUX )
or
python3 main.py ( VPS OR WINDOWS )

NOTE :
RUBAH BAGIAN TOKEN TELEGRAM DAN CHAT ID PADA
main.py JIKA KALIAN INGIN MENDAPATKAN NOTIF BOT DIKIRIM KE TELEGRAM KALIAN
