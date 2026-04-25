"""inspector_63a5f9 - Configuration manager."""
import os, json
from dataclasses import dataclass, asdict
COMPONENT = "inspector_63a5f9"
@dataclass
class AppConfig:
    name: str = COMPONENT
    version: str = "1.0.0"
    log_level: str = "INFO"
    max_retries: int = 3
def load_config() -> AppConfig:
    cfg = AppConfig()
    cfg.log_level = os.getenv("LOG_LEVEL", cfg.log_level)
    cfg.max_retries = int(os.getenv("MAX_RETRIES", str(cfg.max_retries)))
    return cfg
def main():
    cfg = load_config()
    print(f"[{COMPONENT}] Config loaded:")
    print(json.dumps(asdict(cfg), indent=2))
if __name__ == "__main__":
    main()
