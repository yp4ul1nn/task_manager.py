@echo off
title Nexus Workspace Server
color 0b

echo ===================================================
echo   INICIANDO O NEXUS WORKSPACE (SaaS Premium)
echo ===================================================
echo.
echo O servidor local esta sendo iniciado...
echo.
echo Quando quiser DESLIGAR o site, basta fechar esta janela preta.
echo.

:: Muda o diretório ativo para onde este arquivo .bat está salvo
cd /d "%~dp0"

:: Abre o navegador padrao no endereco do site
echo Abrindo o seu navegador...
start http://127.0.0.1:5000

:: Inicia o servidor Python/Flask
python -m web.app

pause
