@echo off
echo Python ve pip kontrol ediliyor...
python --version || goto error
pip --version || goto error

echo discord.py kuruluyor...
pip install -U discord.py
pause
goto end

:error
echo Python veya pip yüklü degil! Lutfen once yukleyin.
pause

:end
