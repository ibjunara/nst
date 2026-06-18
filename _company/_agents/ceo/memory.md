# 🧭 CEO (Chief Executive Agent) 개인 메모리

_CEO 에이전트만 읽고 쓰는 개인 노트. 학습·교훈·자주 쓰는 패턴이 누적됩니다._

## 학습 기록

- [2026-06-18] 현빈아, 이번 달 PayPal 매출 실데이터 가져와서 분석하고 다음 액션 1개 추천해줘. → 보고서 sessions/2026-06-18T13-41/_report.md
- [2026-06-18] 시스템 완전 점검 및 최적화 완료 → gemma4:e4b 설치, workspace 등록, git 초기화

## 시스템 현황 (2026-06-18 기준)

### ✅ 정상 작동 항목
- **LLM:** gemma4:e4b (9.6GB, RTX 3060 12GB VRAM, Ollama 11434포트)
- **llmBase:** http://127.0.0.1:11434
- **llmModel:** gemma4:e4b
- **workspace:** c:\Users\qwkde\입주나라
- **Git:** 초기 커밋 완료 → master 브랜치
- **API 테스트:** 한국어 응답 정상 확인

### 최적화 파라미터 (RTX 3060 12GB 기준)
- localCtxSize: 32768 (128K 지원 모델이지만 안정성 위해 32K)
- localTemp: 0.7 (업무용 최적 온도)
- localMaxTokens: 2048
- localFlashAttn: true (GPU 가속)

### GitHub 동기화
- 원격 저장소: https://github.com/ibjunara/nst
- 동기화 정책: _shared/, _agents/*/memory.md, _agents/*/prompt.md, sessions/ → sync
- config.md, _cache/ → sync 제외

## CONNECT AI LAB 채널 핵심 학습
- 채널 운영자: Jay Jung (Connect AI 개발자)
- 이 시스템(1인 기업 OS)을 Jay가 직접 설계·교육
- 핵심 원칙: 에이전트 메모리 축적 → 자가학습 → 점점 스마트해짐
- Brain Pack 주입으로 지식 확장 가능

## CEO 운영 원칙
1. 모든 요청은 적절한 에이전트에게 위임
2. 400 오류 발생 시 → llmModel, llmBase 설정 먼저 확인
3. 큰 작업은 세션 보고서(sessions/) 생성
4. 사장님 호칭 유지