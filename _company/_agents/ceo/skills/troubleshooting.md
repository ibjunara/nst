# 🧭 CEO 핵심 운영 패턴

## CEO 400 오류 디버깅 패턴

**증상:** "CEO 응답 실패: Request failed with status code 400"

**원인 체크리스트:**
1. `connect-ai-config.json`에서 `llmModel` 비어있는지 확인
2. `connect-ai-config.json`에서 `llmBase` 비어있는지 확인
3. `ollama list`로 해당 모델이 실제 설치되어있는지 확인
4. `ollama serve` 상태 확인 (11434 포트 리스닝)

**해결:**
```json
"llmBase": "http://127.0.0.1:11434",
"llmModel": "gemma4:e4b"
```

**검증:**
```powershell
$body = '{"model":"gemma4:e4b","prompt":"안녕","stream":false}'
Invoke-RestMethod -Uri "http://127.0.0.1:11434/api/generate" -Method POST -Body $body -ContentType "application/json"
```

## 에이전트 위임 패턴

| 요청 유형 | 담당 에이전트 |
|----------|------------|
| 유튜브 전략/기획 | 레오 |
| 코드/자동화/웹 | 코다리 |
| 수익/비즈니스 분석 | 현빈 |
| 일정/텔레그램 | 영숙 |
| 디자인 | Designer |
| 트렌드/조사 | Researcher |
| 글/카피 | Writer |

## 시스템 최적 설정 (RTX 3060 12GB, 32GB RAM)

- 모델: `gemma4:e4b` (9.6GB, 128K 컨텍스트)
- localCtxSize: 32768
- localTemp: 0.7
- localMaxTokens: 2048
- localFlashAttn: true
