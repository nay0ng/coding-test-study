# coding-test-study

바킹독의 실전 알고리즘 강의를 기반으로 한 코딩 테스트 스터디 레포입니다.

강의 원본: [encrypted-def/basic-algo-lecture](https://github.com/encrypted-def/basic-algo-lecture)

파이썬 풀이 참고: [hanXen/basic-algo-lecture-python](https://github.com/hanXen/basic-algo-lecture-python)

## 구조

- `workbook/` : 문제집 자동화 스크립트 및 설정 파일
- `0x00` ~ `0x1F`, `Appendix A` ~ `Appendix E` : 단원별 풀이 폴더
- `workbook.md` : 전체 진행도 (자동 생성)

## 사용 방법

1. 이 레포를 clone
2. 풀이 파일 (`0x??/solutions/문제번호.py`) 에 코드 작성
3. `main` 브랜치에 push
4. GitHub Actions 봇이 자동으로 `workbook.md` 진행도 업데이트

> **참고**: GitHub Actions 권한 설정 필요
> Settings → Actions → General → Workflow permissions → **Read and write permissions**
