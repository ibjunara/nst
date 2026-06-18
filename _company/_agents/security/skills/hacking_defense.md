# Skill: Hacking Defense & Audit

## 1. 취약점 스캔 (Vulnerability Scan)
- 코드가 실행되기 전, 특히 외부 입력을 받는 파이썬 스크립트(셀레니움, API 호출 등)에 대해 정적 분석을 수행합니다.
- 하드코딩된 비밀번호나 토큰이 파일 내에 존재하는지(Hardcoded Secrets) 검열합니다.

## 2. 보안 감사 보고서 (Audit Report)
다음 양식을 통해 대표님께 보고합니다.
```markdown
# [SECURITY ALERT] 보안 감사 보고서
- **발생 위치**: (스크립트명 또는 모듈명)
- **위협 수준**: (CRITICAL / WARNING / INFO)
- **위협 내용**: (어떤 취약점인지 설명)
- **조치 사항**: (코드 수정 방안 또는 접근 차단 여부)
```

## 3. 사고 대응 프로세스 (Incident Response)
1. **격리 (Isolation)**: 문제가 발생한 에이전트의 네트워크 접근 권한 일시 중지.
2. **분석 (Analysis)**: 로그 파일(`_shared/active.json` 및 `tasks/*.log`) 추적.
3. **복구 (Recovery)**: 패치 코드를 적용하고 재가동 승인.
