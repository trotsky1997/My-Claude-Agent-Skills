# Session Management Reference

## Creating Sessions

### Explicit Creation

```bash
# Create empty session
CHAT_ID=$(agent create-chat)
echo "Chat ID: $CHAT_ID"
```

### Automatic Creation

```bash
# Direct start (auto-creates session)
agent

# Or with initial prompt
agent "帮我设计一个用户认证系统"
```

## Resuming Sessions

### Resume Latest

```bash
# Resume most recent session
agent resume
```

### Resume Specific Session

```bash
# Resume by ID
agent --resume <chatId>

# Example
agent --resume 29c59afb-35c5-4b09-83dd-c78cbf698234
```

### List All Sessions

```bash
# List all sessions
agent ls
```

## Session Storage

**Location**: `~/.cursor/chats/<workspace-hash>/<chat-id>/store.db`

**Format**: SQLite database

**Content**:
- Complete message history
- Tool call records
- Context information
- Metadata (timestamps, models, etc.)

## Project-Level Management

### Single Project Session

```bash
# Create project session
PROJECT_CHAT=$(agent create-chat)
echo $PROJECT_CHAT > .chat_id

# Use in scripts
agent --resume $(cat .chat_id) --print "continue task"
```

### Multiple Task Sessions

```bash
# Different tasks, different sessions
DB_CHAT=$(agent create-chat)
echo $DB_CHAT > .db_chat_id

API_CHAT=$(agent create-chat)
echo $API_CHAT > .api_chat_id

FRONTEND_CHAT=$(agent create-chat)
echo $FRONTEND_CHAT > .frontend_chat_id

# Switch between sessions
agent --resume $(cat .db_chat_id)      # Database design
agent --resume $(cat .api_chat_id)     # API development
agent --resume $(cat .frontend_chat_id) # Frontend development
```

## Long-Term Projects

```bash
# Day 1: Create session
PROJECT_CHAT=$(agent create-chat)
echo $PROJECT_CHAT > .chat_id

agent --resume $PROJECT_CHAT
> 设计项目架构
> exit

# Day 2 (or weeks later): Resume
agent --resume $(cat .chat_id)
> 继续开发（AI 记得之前的对话）
```

## Session Backup and Recovery

```bash
# Backup sessions
BACKUP_DIR="$HOME/.cursor/chats_backup_$(date +%Y%m%d)"
mkdir -p "$BACKUP_DIR"
cp -r ~/.cursor/chats/* "$BACKUP_DIR/"

# Restore sessions
cp -r "$BACKUP_DIR"/* ~/.cursor/chats/
```

## Session Cleanup

```bash
# Delete old sessions (30+ days)
find ~/.cursor/chats -name "store.db" -mtime +30 -delete

# Delete empty session directories
find ~/.cursor/chats -type d -empty -delete

# View session sizes
du -sh ~/.cursor/chats/*/
```

## Session Statistics

```bash
#!/bin/bash
# session_stats.sh

echo "=== 会话统计 ==="
echo "总会话数: $(find ~/.cursor/chats -name "store.db" | wc -l)"
echo "总存储: $(du -sh ~/.cursor/chats/ | awk '{print $1}')"
echo ""
echo "按工作区分组:"
find ~/.cursor/chats -type d -mindepth 1 -maxdepth 1 | while read dir; do
    count=$(find "$dir" -name "store.db" | wc -l)
    size=$(du -sh "$dir" | awk '{print $1}')
    echo "  $(basename $dir): $count 个会话, $size"
done
```
