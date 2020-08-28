@echo off
move libs\createKod.xyz libs\createKod.py
move libs\listen.xyz libs\listen.py
cls
color A
echo YTU RACING
timeout 3
cls
echo Ana Makine Baslatiliyor
timeout 3
cls
echo (127.0.0.1 , 50007)
echo Baglanti Bekleniyor...
python libs\listen.py 50007
move libs\createKod.py libs\createKod.xyz
move libs\listen.py libs\listen.xyz
cls
echo BAGLANTI SONLANDI
@pause
