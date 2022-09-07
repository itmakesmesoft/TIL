# [Django] Template Tag 기본 연산

- 덧셈

```html
{{ 5|add:5 }} <!-- 10 -->
```

- 뺄셈

```html
{{ 5|add:-3 }} <!-- 2 -->
```

- 곱셈 *(widthratio 내장 템플릿 태그 이용)*
    - widthratio : 주어진 값이 최댓값에서 차지하는 비율을 Bar 차트로 표현하는데 사용하는 태그

```html
<!-- {% widthratio A B C %} <== A/B*C | A: 주어진 값, B: 최댓값, C:최대 가로길이 -->
{%  widthratio 3 1 2 %} <!-- 3/1*2 = 6 -->
```

- 나눗셈

```html
{%  widthratio 6 3 1 %} <!-- 6/3*1 = 2 -->
```