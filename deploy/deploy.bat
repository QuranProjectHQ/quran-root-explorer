@echo off
cd /d "%~dp0"
set DEPLOY_RC=1
set FULL_LOG=deploy_full.log

echo Starting at %DATE% %TIME% > %FULL_LOG%
echo. >> %FULL_LOG%
echo ============================================================ >> %FULL_LOG%
echo   Quran Root Explorer  v1.2  deployment  -  git push >> %FULL_LOG%
echo ============================================================ >> %FULL_LOG%
echo Working directory: %CD% >> %FULL_LOG%
echo. >> %FULL_LOG%
echo [1/4]  Checking required files... >> %FULL_LOG%

set MISSING=0
for %%F in (app.py state.py analysis.py interpret.py plotly_charts.py stats_charts.py stats_module.py analytics.py topics.py surface_divergence.py requirements.txt Book6.xlsx deploy_git.py check_syntax.py pair_classification.py practical_lens.py CHANGELOG_v1.2.md twobooks_stats.py CHANGELOG_v1.3.md) do call :check_file "%%F"
for %%F in (pages\0_Help.py pages\1_Per_Root_Profile.py pages\2_Network.py pages\3_Motifs.py pages\4_Ayah_Browser.py pages\5_Compare_Heatmaps.py pages\6_Morphology.py pages\7_Statistics.py pages\8_Export.py pages\8a_Interpret.py pages\8e_Calibration.py pages\8f_Practical_Lens.py pages\9_Topic_Modeling.py pages\9_Usage.py pages\14_Disjoint_Letters.py pages\15_Signal.py pages\16_Biology.py pages\17_Two_Books_Summary.py) do call :check_file "%%F"

echo Missing count: %MISSING% >> %FULL_LOG%
if not "%MISSING%"=="0" goto :fail_missing
echo   All required files present. >> %FULL_LOG%

echo. >> %FULL_LOG%
echo [2/4]  Python-syntax-checking all .py files... >> %FULL_LOG%
python check_syntax.py >> %FULL_LOG% 2>&1
set CHECK_RC=%errorlevel%
echo check_syntax.py exit code: %CHECK_RC% >> %FULL_LOG%
if not "%CHECK_RC%"=="0" goto :fail_syntax

echo. >> %FULL_LOG%
echo [3/4]  Pushing v1.2 to the Hugging Face Space... >> %FULL_LOG%
where git >> %FULL_LOG% 2>&1
set WHERE_RC=%errorlevel%
echo where git exit code: %WHERE_RC% >> %FULL_LOG%
if not "%WHERE_RC%"=="0" goto :fail_git

where python >> %FULL_LOG% 2>&1
set PY_RC=%errorlevel%
echo where python exit code: %PY_RC% >> %FULL_LOG%
if not "%PY_RC%"=="0" goto :fail_python

echo Invoking deploy_git.py ... >> %FULL_LOG%
python -u deploy_git.py >> %FULL_LOG% 2>&1
set DEPLOY_RC=%errorlevel%
echo deploy_git.py exit code: %DEPLOY_RC% >> %FULL_LOG%
goto :summary

:fail_missing
echo   FAILED: %MISSING% required files missing.  Aborting. >> %FULL_LOG%
goto :summary

:fail_syntax
echo   FAILED: Python syntax errors above.  Aborting. >> %FULL_LOG%
goto :summary

:fail_git
echo   ERROR: git is not on PATH. >> %FULL_LOG%
goto :summary

:fail_python
echo   ERROR: python is not on PATH. >> %FULL_LOG%
goto :summary

:summary
echo. >> %FULL_LOG%
echo [4/4]  Summary >> %FULL_LOG%
echo ------------------------------------------------------------ >> %FULL_LOG%
if "%DEPLOY_RC%"=="0" (echo   Deployment succeeded. >> %FULL_LOG%) else (echo   Deployment exited with code %DEPLOY_RC%. >> %FULL_LOG%)
echo   Full log: %~dp0%FULL_LOG% >> %FULL_LOG%
echo   Space:    https://huggingface.co/spaces/QuranProject/quran-root-explorer >> %FULL_LOG%
echo   Live URL: https://quranproject-quran-root-explorer.hf.space/ >> %FULL_LOG%
echo ------------------------------------------------------------ >> %FULL_LOG%
type %FULL_LOG%
echo.
echo Press any key to close this window.
pause >nul
exit /b %DEPLOY_RC%

:check_file
if not exist %~1 (
    echo   MISSING: %~1 >> %FULL_LOG%
    set /a MISSING+=1
)
goto :eof
