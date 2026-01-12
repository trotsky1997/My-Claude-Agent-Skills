# Development-Verification Loop Reference

## Setup Phase

### 1. Create Two Sessions

```bash
DEV_CHAT=$(agent create-chat)
echo $DEV_CHAT > .dev_chat_id

QA_CHAT=$(agent create-chat)
echo $QA_CHAT > .qa_chat_id
```

### 2. Define Requirements

Create `开发任务和验收标准.md`:

```markdown
# 开发任务

## 核心功能
1. 功能1
2. 功能2

## 验收标准

### 功能验收
- [ ] 功能1正常工作
- [ ] 功能2正常工作

### 代码验收
- [ ] 代码结构清晰
- [ ] 包含单元测试
- [ ] 测试通过率 100%

### 界面验收
- [ ] 界面美观
- [ ] 实时更新流畅
```

## Development Loop

### Step 1: Development Phase

```bash
DEV_CHAT=$(cat .dev_chat_id)
agent --resume $DEV_CHAT --print "开发任务：[详细描述]" > output.py
```

### Step 2: Verification Phase

```bash
QA_CHAT=$(cat .qa_chat_id)
agent --resume $QA_CHAT --print "验收检查：根据验收标准检查代码，给出详细报告" > 验收报告.md
```

### Step 3: Decision

- **If verification passes** → End loop
- **If issues found** → Continue loop (back to Step 1 with fixes)

## Complete Example

```bash
# Round 1: Initial development
agent --resume $DEV_CHAT --print "创建完整项目" > game.py

# Round 2: Verification
agent --resume $QA_CHAT --print "检查代码质量" > 验收报告.md

# Round 3: Fix issues (if any)
agent --resume $DEV_CHAT --print "修复问题：[列出问题]" > game_fixed.py

# Round 4: Final verification
agent --resume $QA_CHAT --print "最终验收检查" > 最终验收报告.md
```

## Best Practices

1. **Clear requirements**: Define specific acceptance criteria
2. **Separate sessions**: Use different sessions for dev and QA
3. **Iterative approach**: Fix issues incrementally
4. **Document decisions**: Keep records of verification results
