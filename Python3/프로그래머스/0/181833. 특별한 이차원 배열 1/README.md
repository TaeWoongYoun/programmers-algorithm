# [level 0] 특별한 이차원 배열 1 - 181833 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181833) 

### 성능 요약

메모리: 10.8 MB, 시간: 0.99 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 01월 06일 15:58:44

### 문제 설명

<p>정수 <code>n</code>이 매개변수로 주어질 때, 다음과 같은 <code>n</code> × <code>n</code> 크기의 이차원 배열 arr를 return 하는 solution 함수를 작성해 주세요.</p>

<ul>
<li>arr[i][j] (0 ≤ i, j &lt; <code>n</code>)의 값은 i = j라면 1, 아니라면 0입니다.</li>
</ul>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>n</code> ≤ 100</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>3</td>
<td>[[1, 0, 0], [0, 1, 0], [0, 0, 1]]</td>
</tr>
<tr>
<td>6</td>
<td>[[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]</td>
</tr>
<tr>
<td>1</td>
<td>[[1]]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>예제 1번의 <code>n</code>의 값은 3으로 다음과 같이 2차원 배열을 채울 수 있습니다.</li>
</ul>

<p>|i \ j|0|1|2|</p>

<p>|---|---|---|---|</p>

<p>|0|1|0|0|</p>

<p>|1|0|1|0|</p>

<p>|2|0|0|1|</p>
<div class="highlight"><pre class="codehilite"><code>따라서 [[1, 0, 0], [0, 1, 0], [0, 0, 1]]을 return 합니다.
</code></pre></div>
<p>입출력 예 #2</p>

<ul>
<li>예제 2번의 <code>n</code>의 값은 6으로 다음과 같이 2차원 배열을 채울 수 있습니다.</li>
</ul>

<p>|i \ j|0|1|2|3|4|5|</p>

<p>|---|---|---|---|---|---|---|</p>

<p>|0|1|0|0|0|0|0|</p>

<p>|1|0|1|0|0|0|0|</p>

<p>|2|0|0|1|0|0|0|</p>

<p>|3|0|0|0|1|0|0|</p>

<p>|4|0|0|0|0|1|0|</p>

<p>|5|0|0|0|0|0|1|</p>
<div class="highlight"><pre class="codehilite"><code>따라서 [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]을 return 합니다.
</code></pre></div>
<p>입출력 예 #3</p>

<ul>
<li>예제 1번의 <code>n</code>의 값은 1이고 다음과 같이 2차원 배열을 채울 수 있습니다.</li>
</ul>

<p>|i \ j|0|</p>

<p>|---|---|</p>

<p>|0|1|</p>
<div class="highlight"><pre class="codehilite"><code>따라서 [[1]]을 return 합니다.
</code></pre></div>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges