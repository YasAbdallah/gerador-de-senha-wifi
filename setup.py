import sys

from cx_Freeze import setup, Executable

options = {'packages': ['os', 'email', 'smtplib', 'selenium', 'pymsgbox', 'wifi_qrcode_generator', 'reportlab', 'calendar'], 'excludes': ['tkinter']}
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name='Gerador de Voucher',
    version='1.0',
    description='Gerador de vales para wifi com um gerador de pdf com o vale e envio de email para responsaveis.',
    options={'build.exe': options},
    executables=[Executable('main.py', base=base)]
)
