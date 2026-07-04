@echo off
title Coyote Pairing Station
cd /d "%~dp0"
echo Coyote Pairing Station
echo http://localhost:4517
echo.
python serve.py
pause
