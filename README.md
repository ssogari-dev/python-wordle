# Python Wordle

지인의 부탁으로 제작한 **Wordle 게임**입니다. 제작 언어는 **Python** 입니다.
긴 軍 복무 기간 중 많이 하지 못했던 코딩 재활 치료 겸해서 습작으로 만들었습니다.
> **Note:** Python **3.10** 버전에서 제작 및 테스트를 진행했습니다.

<br>

## GUI 버전 (wordle-gui.py)
- Python의 **random, tkinter, re, requests** 모듈을 이용했습니다.
> **Note:** tkinter, requests 모듈은 pip를 이용한 설치가 필요합니다.

- 8, 9번 라인의 주석을 설정/해제함에 따라 MIT의 단어 목록 또는 [DWYL님의 단어 목록](https://github.com/dwyl/english-words) 중 선택이 가능합니다.
- NYTIMES WORDLE 규칙에 따라 알파벳/위치 일치 시 초록색으로 표시, 알파벳 일치 시 노란색으로 표시, 일치하지 않는 경우 회색으로 표시되도록 하였습니다.
- 오류 발생 시 메시지 팝업 창을 표시하도록 하였습니다.

<br>

## CLI 버전 (wordle-cli.py)

- Python의 **random, re, requests, colorama** 모듈을 이용했습니다.
> **Note:** requests 모듈은 pip를 이용한 설치가 필요합니다.

- 8, 9번 라인의 주석을 설정/해제함에 따라 MIT의 단어 목록 또는 [DWYL님의 단어 목록](https://github.com/dwyl/english-words) 중 선택이 가능합니다.
- NYTIMES WORDLE 규칙에 따라 알파벳/위치 일치 시 초록색으로 표시, 알파벳 일치 시 노란색으로 표시, 일치하지 않는 경우 회색으로 표시되도록 하였습니다.
- 정답을 확인하고자 하는 경우 'showtheanswer'를 입력하면 플레이 중 정답을 확인할 수 있습니다.
- Windows에서는 Powershell에서 실행할 때 정상 작동을 확인했습니다.
  
<br>
<br>

---

<br>
<br>

# Python Wordle (English)
* *The English description has been created by machine translation using [DeepL](https://www.DeepL.com/Translator).*

This is a **Python Wordle game**.
I created it as a simple project to serve as coding rehabilitation therapy for a long military deployment.
> **Note:** Python **3.10** version was used for production and testing.

<br>

## GUI version (wordle-gui.py)
- Using Python's **random, tkinter, re, requests** modules.
> **Note:** 'tkinter', 'requests' modules need to be installed using pip.

- By toggling comments on/off in lines 8 and 9, you can choose between MIT's word list or [DWYL's word list](https://github.com/dwyl/english-words).
- Based on the NYTIMES WORDLE convention, we have marked green for alphabet/position match, yellow for alphabet match, and gray for no match.
- If an error occurs, a message popup window is displayed.

<br>

## CLI version (wordle-cli.py)

- Using Python's **random, re, requests, colorama** modules.
> **Note:** The 'requests' module requires installation via pip.

- By turning comments on/off in lines 8 and 9, you can choose between MIT's word list or [DWYL's word list](https://github.com/dwyl/english-words).
- I've followed the NYTIMES WORDLE convention to show green for alphabet/position matches, yellow for alphabet matches, and gray for no match.
- If you want to see the correct answer, you can type 'showtheanswer' to see the answer as you play.
- On Windows, I confirmed that it works fine when running from Powershell.
