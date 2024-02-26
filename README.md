# Django-seminar Repository 사용법
인하대학교 멋쟁이사자처럼 세미나 자료 저장소입니다.

각 세미나 자료들은 `week-{주차}-{세미나 제목}`의 브랜치 명으로 생성하여 사용하고 PR을 올리지 않은 채 origin에만 push하는 형식으로 저장해둡니다. 
ex) week-3-django-advanced

main 브랜치: 장고로 startproject와 기본 세팅정도만 된 파일

되도록이면 세미나의 모든 실습 자료들이 유기적으로 연결되어 있는 상태였으면 좋겠습니다.
이를 위해 세션을 작성할 때는 이전 실습 자료의 브랜치를 pull 받아 사용하면 좋을 것 같습니다.
ex) 3주차 장고 심화 실습 자료는 3주차 장고 기본 실습 자료를 pull 받아 작성되었습니다.

아기사자들이 모든 실습을 한 레포지토리에서 진행하고, 배포 세션 때 완성된 api를 배포하는 방식으로 진행하였으면 좋겠습니다.
