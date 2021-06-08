# 오픈 북 테스트 준비용

강의안을 제공하지 않는 교수님들의 영상을 자동으로 캡쳐 해 PDF로 만들어주는 시스템 개발

* 오픈북 강의에 유용하게 쓸 수 있음
* 생성된 PDF를 OCR 기능을 이용해서 `command+f` (`ctrl+f`) 할 수 있도록 만들면 편하지만 
  시간상 구현하지 않고 상용프로그램을 사용함. 알PDF 사용 가능

## Requirements

```bash
pip install scenedetect[opencv]
```