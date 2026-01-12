# Workflows and Patterns Reference

## Common Patterns

### Pattern 1: Project Initialization

```bash
mkdir project && cd project
CHAT_ID=$(agent create-chat)
echo $CHAT_ID > .chat_id

agent --resume $CHAT_ID --print "create project structure" > main.py
```

### Pattern 2: Feature Addition

```bash
agent --resume $(cat .chat_id) --print "add feature: [description]" > feature.py
```

### Pattern 3: Code Review

```bash
REVIEW_CHAT=$(agent create-chat)
agent --resume $REVIEW_CHAT --print "review code quality" < code.py > review.md
```

### Pattern 4: Automated Testing

```bash
agent --resume $(cat .chat_id) --print "generate unit tests" > test_code.py
pytest test_code.py
```

## Advanced Workflows

### 1. Automated Code Review

```bash
#!/bin/bash
# Batch review code files
for file in *.py; do
    echo "Reviewing $file"
    agent --print --output-format json "Review code quality and potential issues" < "$file" > "review_${file}.json"
done
```

### 2. CI/CD Integration

```bash
# Use in CI/CD pipelines
agent --print --approve-mcps --force "generate test report" > test_report.md
```

### 3. Multi-Model Comparison

```bash
#!/bin/bash
# Generate code with different models and compare
for model in gpt-5.2 sonnet-4.5 opus-4.5; do
    echo "=== $model ==="
    agent --model $model --print "implement quicksort" > "quicksort_${model}.py"
done
```

### 4. Streaming Document Generation

```bash
# Real-time generate long documents
agent --print --output-format stream-json --stream-partial-output \
  "Generate complete project documentation" | \
  tee project_docs.json | \
  jq -r '.content' > project_docs.md
```

### 5. Rule-Driven Development

```bash
# 1. Generate project rules
agent rule

# 2. Use rules to guide development
agent "根据项目规则实现新功能"
```

### 6. MCP Tool Chain

```bash
# Combine multiple MCP servers
agent --print --approve-mcps \
  "Use context7 to query docs, use filesystem to read files, complete task"
```

### 7. Model Selection Strategy

```bash
#!/bin/bash
# Select model based on task type
TASK="$1"

case $TASK in
    "code")
        MODEL="gpt-5.2"
        ;;
    "analysis")
        MODEL="opus-4.5-thinking"
        ;;
    "quick")
        MODEL="gemini-3-flash"
        ;;
    *)
        MODEL="auto"
        ;;
esac

agent --model $MODEL --print "$2"
```

## Best Practices

### 1. Clear Prompts

**Bad**: `agent --print "write code"`

**Good**: `agent --print "Create a TUI game with:
- Rich library interface
- Keyboard controls (W/S, arrows)
- Complete game logic
- Unit tests"`

### 2. Iterative Development

Don't ask for everything at once:

```bash
# Step 1: Basic framework
agent --resume $CHAT_ID --print "create basic structure"

# Step 2: Add features
agent --resume $CHAT_ID --print "add specific feature"

# Step 3: Optimize
agent --resume $CHAT_ID --print "optimize performance"
```

### 3. Session Persistence

- Save session IDs to files (`.chat_id`, `.dev_chat_id`, `.qa_chat_id`)
- Use sessions for long-term projects
- Resume sessions across terminals and days

### 4. Development-Verification Separation

- Use separate sessions for development and verification
- Clear separation of concerns
- Independent quality checks

## Troubleshooting Patterns

### Session Not Found

```bash
# Check session exists
ls ~/.cursor/chats/*/<chatId>/

# Recreate if needed
agent create-chat > .chat_id
```

### Permission Issues

```bash
# Use sandbox mode
agent --sandbox enabled "task"

# Or force allow (careful)
agent --force "task"
```

### MCP Connection Issues

```bash
# Check MCP status
agent mcp list

# Re-enable server
agent mcp enable server-name
```
