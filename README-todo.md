# TODO : fullstack GPT 로 할일.

할일 관리가 잘 안되네... 어쩌지...
[TODO - my private](../privateGitHub/TODO/README.todo.md)

## 웹 크롤링 - study

<pre>이건 여기하고는 상관없지만... 프로그램이 원래 그런거지...
chatGPT api 를 사용하면 더 간단해 지겠지만...
</pre>

## chatGPT 흉내내기

<pre>fullstack GPT study 를 이용한 개발.
study 자체에서 기본적인 기능은 제공하지만... 강의를 듣고,
기능을 따라하고, 나중에 이를 활용해서 추가 기능을 개발하자.

기본적인 내용으로 구성이 가능하니, 적절히 샘플로 만들어보자.
</pre>

## local text 암호화 처리

<pre>API 키를 암호화해서 내용을 저장해서 가지고 있는 방법
중요내용이라 나만이 가지고 있을수 있도록 하며, 작업은 env 에 내가 암기할수 있는 키로 암호화/복호화 할수 있도록 한다.
RSA 인터넷 https 용인데... 이거 필요한가?
SHA-512 로 암호화 복호화 하지 않았나? 일방향이라네...
</pre>

## 증권 종목 정보 수집기

### 가능하겠나?

<pre>기본 기능으로 국내증권 종목을 보고, 내용을 크롤링해서 기본정보를 수집.
수집 내용을 기본으로 메모를 생성하고, 데이터를 저장해서 핸드폰으로 정보를 발송. 뭘쓸까나?
</pre>

#### 뉴스 수집기

<pre>종목 정보를 기준으로 뉴스를 검색하고, 이를 관련 데이터를 찾아서 정보를 수집한다.
수집한 정보를 저장하고, 분석한 이력을 남긴다.
투자 정보 분석의 베이스가 어디 있는지 로깅하기 위함이다.
</pre>

#### 실시간 증권 차트 수집 및 분석

<pre>네이버 등, 증권 사이트를 들어가서 차트 데이터를 수집
수집 정보를 만들어서 다양한 방법으로 정보를 분석
분석 작업을 하는게 쉽지 않다. chatGPT api 등으로 이미지 분석, 텍스트 분석, 기존 데이터 검토 등 해야 할게 많다.
</pre>

#### 분석을 통한 매매 정보 판단

<pre>증권사 매매 api 를 이용하여 모의투자 방법을 시뮬레이션 함
매매 api 를 샘플로 만들어서 사용하는 것은 문제 없겠지... 시간이 필요할 뿐...
</pre>

#### 매매 정보 판단을 통한 실시간 매매 처리

<pre>모의 투자를 통한 매매를 이용하여 프로그램 안전성을 높이고, 실제 매매에 사용할 수 있도록 개발한다
실제 서비스를 적용해서 테스트하는 것은 쉽지 않겠지? 하지만 try 하는 거지.
</pre>
