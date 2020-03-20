REM Napisz program batch zarządzający otwieraniem programów “na przycisk”.
REM Jeżeli użytkownik wpisze poprawne hasło “IwB”, to program zmieni kolor, wyczysci ekran, wypisze możliwości i będzie nasłuchiwał na input:
REM automatycznie po wciśnięciu przycisku [1] na klawiaturze, otworzyć ma się Notatnik
REM otworzy się dowolna przeglądarka internetowa z adresem www.wp.pl
REM program pokaże listę aktywnych procesów
REM wyświetli się dowolny folder z /users/
REM wyświetli drzewo katalogów
REM sprawdzi połączenie z Internetem
REM program wyłączy komputer

@echo off
@chcp 65001>nul
echo.
set /p haslo="Prosze podac haslo : "
if %haslo%==IwB goto menu
if %haslo%== exit
:menu
color 3b
cls
echo.
echo ....----====MENU====----....
echo.
echo 1. Notatnik
echo 2. Wirtualna Polska
echo 3. Aktywne procesy
echo 4. Folder z /users/
echo 5. Drzewo katalogow
echo 6. Polaczanie z internetem
echo 0. Wylacz komputer

set /p opcja="Wybierz opcje : "
if %opcja%==1 goto 1x
if %opcja%==2 goto 2x
if %opcja%==3 goto 3x
if %opcja%==4 goto 4x
if %opcja%==5 goto 5x
if %opcja%==0 goto 0x
if %opcja%==6 goto 6x

:1x
start notepad.exe
pause
goto menu

:2x
start www.wp.pl
pause
goto menu

:3x
tasklist
pause
goto menu

:4x
cd C:
cd Users
dir
pause
goto menu

:5x
tree C:
pause
goto menu

:0x
shutdown /s 
cls
echo KOMPUTER ZOSTANIE WYLACZONY ZA CHWILE!
pause

:6x
ping -n 1 google.pl >nul
if %errorlevel% EQU 0 echo Jestesmy polaczeni z internetem 
if %errorlevel% NEQ 0 echo Nie jestesmy polaczeni z internetem

pause
goto menu
