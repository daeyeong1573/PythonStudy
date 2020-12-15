# 가상환경 

VSCODE Python 가상환결 설정 
ctrl+shift+`(터미널창 실행) ---> python -m venv venv  
venv파일이 생긴걸 확인후 F1 --> Select interpreter ---> venv선택  
터미널창 재실행  
#  

* 파이썬 가상환경 
  * 가상환경 생성
  * 가상환경 실행 / 해제 -->(윈도우 : Script, 맥: bin)폴더
  * 패키지 설치 및 삭제
  * 패키지 리스트 출력
  * 패키지 검색

# pip 명령어  
pip list : 설치된 항목 확인  
pip install django : django 설치  
pip uninstall django : django 삭제  
pip install --upgrade django : django 버전 업데이트  
pip freeze > requirments.txt : 패키지 리스트 만들기  
pip install -r requirements.txt : 패키지 리스트 설치  

