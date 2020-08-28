@echo off
move lib\createKod.xyz lib\createKod.py
move lib\listen.xyz lib\listen.py
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
python lib\listen.py 50007
move lib\createKod.py lib\createKod.xyz
move lib\listen.py lib\listen.xyz
cls
echo BAGLANTI SONLANDI
@pause
