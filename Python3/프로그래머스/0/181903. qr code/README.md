# [level 0] qr code - 181903 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181903) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.11 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 01월 08일 08:41:30

### 문제 설명

<p>두 정수 <code>q</code>, <code>r</code>과 문자열 <code>code</code>가 주어질 때, <code>code</code>의 각 인덱스를 <code>q</code>로 나누었을 때 나머지가 <code>r</code>인 위치의 문자를 앞에서부터 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 ≤ <code>r</code> &lt; <code>q</code> ≤ 20</li>
<li><code>r</code> &lt; <code>code</code>의 길이 ≤ 1,000</li>
<li><code>code</code>는 영소문자로만 이루어져 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>q</th>
<th>r</th>
<th>code</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>3</td>
<td>1</td>
<td>"qjnwezgrpirldywt"</td>
<td>"jerry"</td>
</tr>
<tr>
<td>1</td>
<td>0</td>
<td>"programmers"</td>
<td>"programmers"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>예제 1번의 <code>q</code>와 <code>r</code>은 각각 3, 1이고 인덱스와 그 값을 <code>q</code>로 나눈 나머지가 잘 보이도록 표로 만들면 다음과 같습니다.</li>
</ul>

<p>|<code>code</code>|q|j|n|w|e|z|g|r|p|i|r|l|d|y|w|t|</p>

<p>|-----|-|-|-|-|-|-|-|-|-|-|--|--|--|--|--|--|</p>

<p>|index|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|</p>

<p>|<code>q</code>로 나눈 나머지|0|1|2|0|1|2|0|1|2|0|1|2|0|1|2|0|</p>
<div class="highlight"><pre class="codehilite"><code>`q`로 나눈 나머지가 1인 인덱스의 문자들을 앞에서부터 순서대로 이어 붙이면 "jerry"가 되므로 이를 return 합니다.
</code></pre></div>
<p>입출력 예 #2</p>

<ul>
<li>예제 2번의 <code>q</code>와 <code>r</code>은 각각 1, 0이고 인덱스와 그 값을 <code>q</code>로 나눈 나머지가 잘 보이도록 표로 만들면 다음과 같습니다.</li>
</ul>

<p>|<code>code</code>|p|r|o|g|r|a|m|m|e|r|s|</p>

<p>|------|-|-|-|-|-|-|-|-|-|-|-|</p>

<p>|index|0|1|2|3|4|5|6|7|8|9|10|</p>

<p>|<code>q</code>로 나눈 나머지|0|0|0|0|0|0|0|0|0|0|0|</p>
<div class="highlight"><pre class="codehilite"><code>`q`로 나눈 나머지가 1인 인덱스의 문자들을 앞에서부터 순서대로 이어 붙이면 "programmers"가 되므로 이를 return 합니다.
</code></pre></div>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges