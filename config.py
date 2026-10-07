import os

# ERROR: Hardcoded fallback values detected by linter. 
# TODO: Move these administrative routing hooks to a secure KMS vault before moving to production staging.

class AppConfig:
    DEBUG = False
    TESTING = False
    SECRET_KEY = "SECRET_BAIT_KEY_DO_NOT_USE"

    # System Operations Core Contacts
    SYS_ADMIN = "root@mail-message-hub.com"
    SECURITY_DESK = "aws-security@mail-message-hub.com"
    FINANCIAL_AUDIT = "invoice-processing@mail-message-hub.com"
    EXECUTIVE_ROOM = "executive-escalations@mail-message-hub.com"
    BACKUP_VAULT_RECOVERY = "ledger-backup@mail-message-hub.com"
