import os
import json
from dotenv import load_dotenv

HERE = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(HERE, ".env")
AGENTS_DIR = os.path.join(HERE, "_company", "_agents")

def load_json(path):
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    print("🔄 전역 환경변수 동기화 엔진 가동 시작...")
    
    if not os.path.exists(ENV_PATH):
        print("❌ .env 파일을 찾을 수 없습니다.")
        return

    # Load environment variables
    load_dotenv(ENV_PATH)
    
    env_keys = {
        "YOUTUBE_API_KEY": os.getenv("YOUTUBE_API_KEY", ""),
        "MY_CHANNEL_ID": os.getenv("YOUTUBE_CHANNEL_ID", ""),
        "TELEGRAM_BOT_TOKEN": os.getenv("TELEGRAM_BOT_TOKEN", ""),
        "TELEGRAM_CHAT_ID": os.getenv("TELEGRAM_CHAT_ID", ""),
        "API_KEY": os.getenv("GEMINI_API_KEY", ""),
        "CLIENT_ID": os.getenv("PAYPAL_CLIENT_ID", "")
    }

    # Filter out empty placeholders
    for k in list(env_keys.keys()):
        val = env_keys[k]
        if "여기에_" in val or not val.strip():
            env_keys[k] = ""

    targets = [
        {
            "file": os.path.join(AGENTS_DIR, "youtube", "tools", "youtube_account.json"),
            "mappings": ["YOUTUBE_API_KEY", "MY_CHANNEL_ID", "TELEGRAM_BOT_TOKEN", "TELEGRAM_CHAT_ID"]
        },
        {
            "file": os.path.join(AGENTS_DIR, "secretary", "tools", "telegram_setup.json"),
            "mappings": ["TELEGRAM_BOT_TOKEN", "TELEGRAM_CHAT_ID"]
        },
        {
            "file": os.path.join(AGENTS_DIR, "business", "tools", "gemini_account.json"),
            "mappings": ["API_KEY"]
        },
        {
            "file": os.path.join(AGENTS_DIR, "business", "tools", "paypal_revenue.json"),
            "mappings": ["CLIENT_ID"]
        }
    ]

    updated_files = 0
    missing_critical = []

    for target in targets:
        filepath = target["file"]
        data = load_json(filepath)
        changed = False
        
        for key in target["mappings"]:
            new_val = env_keys.get(key, "")
            
            # If the env has a real value, sync it
            if new_val:
                if data.get(key) != new_val:
                    data[key] = new_val
                    changed = True
            else:
                # If it's missing in .env and also missing in json, report it
                if not data.get(key):
                    missing_critical.append(key)
        
        if changed:
            save_json(filepath, data)
            updated_files += 1
            print(f"✅ 동기화 완료: {os.path.relpath(filepath, HERE)}")

    print(f"\n총 {updated_files}개의 설정 파일이 .env 와 완벽하게 동기화되었습니다.")
    
    # Remove duplicates
    missing_critical = list(set(missing_critical))
    
    if missing_critical:
        print("\n⚠️ [경고] 다음 API 키가 .env 파일에 입력되지 않았습니다:")
        for missing in missing_critical:
            if missing == "TELEGRAM_BOT_TOKEN":
                print("  - 텔레그램 봇 토큰 (비서/유튜브 알림 기능 멈춤)")
            elif missing == "TELEGRAM_CHAT_ID":
                print("  - 텔레그램 채팅방 ID (비서/유튜브 알림 기능 멈춤)")
            elif missing == "CLIENT_ID":
                print("  - 페이팔 클라이언트 ID (수익 추적 멈춤)")
            else:
                print(f"  - {missing}")
        print("\n💡 해결책: .env 파일을 열고 해당 값을 채워 넣은 뒤, 이 스크립트를 다시 실행하세요.")
    else:
        print("\n🎉 모든 인증키가 완벽하게 준비되었습니다. 시스템 All Green!")

if __name__ == "__main__":
    main()
