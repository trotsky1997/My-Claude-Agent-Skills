# Terminology Building and Maintenance Guide

A systematic approach to building and maintaining a comprehensive terminology glossary during codebase reading.

## Why Terminology Matters

**Problem:** Without a clear terminology glossary, you'll encounter:
- Ambiguous acronyms (CTC? CLS? DB? NMS?)
- Domain-specific terms that aren't self-explanatory
- Confusion between similar concepts (Detection vs Recognition, Orientation vs CLS)
- Difficulty understanding architecture discussions and code reviews
- Wasted time repeatedly looking up the same terms

**Solution:** Build a living terminology glossary early and maintain it continuously.

## Core Principles

### 1. Start Early, Build Incrementally

**Don't wait until you understand everything.** Start building the glossary as soon as you encounter unfamiliar terms. It's easier to refine than to build from scratch later.

**Best practice:** Create a dedicated terminology section in your `code-reading.md` file from day 1, even if it's mostly empty. Add entries as you encounter them.

### 2. Classify by Domain and Abstraction Level

Organize terminology by:
- **Domain categories** (e.g., OCR-specific, ML-specific, project-specific)
- **Abstraction levels** (concepts, algorithms, data structures, implementation details)
- **Relationships** (parent-child, synonyms, related concepts)

**Example structure:**
```
## Terminology

### Domain-Specific Terms (e.g., OCR)
- Detection (检测)
- Recognition (识别)
- ...

### Project-Specific Terms
- ProjectName
- KeyLibrary
- ...

### Data Structures
- MainStruct
- ConfigStruct
- ...

### Algorithms
- AlgorithmName
- ...
```

### 3. Include Context and Relationships

Each term entry should include:
- **Definition**: What it is
- **Context**: Where it's used
- **Relationships**: Related concepts, parent/child terms
- **Code references**: Where it's implemented or used
- **Acronym expansion**: If applicable

**Good example:**
```markdown
- **CTC (Connectionist Temporal Classification)**: 
  - **Definition**: Sequence-to-sequence decoding algorithm for text recognition
  - **Context**: Used in `rec.rs` for converting model output to text strings
  - **Implementation**: `rec.rs::decode_ctc()`
  - **Related**: Greedy Decoding, Beam Search
```

**Bad example:**
```markdown
- **CTC**: Used for text recognition
```

### 4. Cross-Reference with Code

Link terminology entries to:
- Implementation locations (file:line references)
- Architecture diagrams (C4 levels)
- API flow documentation
- Module analysis documents

**Example:**
```markdown
- **Detection (检测)**: Locating text regions in images, outputting bounding boxes
  - **Implementation**: `src/det.rs`
  - **Flow**: See `api-flow.md` section 4.1
  - **Architecture**: Component in Level 3 (C4 model)
```

## Methodology: 5-Step Process

### Step 1: Initial Collection (First Reading Pass)

**When:** During Steps 1-4 of codebase reading (Goal Definition, Bootstrap, Architecture, Entry Point Tracing)

**What to collect:**
- Acronyms and abbreviations (scan README, docs, comments)
- Domain-specific terms (from README, project description)
- Key data structures (from type definitions, public APIs)
- Configuration terms (from config files, structs)
- Algorithm names (from function names, comments)

**Tools:**
```bash
# Find acronyms (all caps, 2-5 letters)
rg "\b[A-Z]{2,5}\b" . | grep -v "TODO\|FIXME"

# Find key structs/types
rg "^(pub )?(struct|enum|type|trait)" src/

# Find configuration fields
rg "config\|Config\|CONFIG" -i .

# Find domain terms in README/docs
rg "^\s*\*\*.*\*\*" README.md docs/
```

**Output:** Initial terminology list (even if incomplete)

### Step 2: Deep Dive Collection (Code Reading)

**When:** During detailed module analysis (Step 10: Modules for Deeper Study)

**What to collect:**
- Implementation details and technical terms
- Internal data structures and enums
- Process flow terms (preprocessing, inference, postprocessing)
- Coordinate system terms
- Error handling terms

**Method:**
- Read each key module systematically
- Extract terms from:
  - Function names and signatures
  - Variable names (especially struct fields)
  - Comments explaining algorithms
  - Error messages and types
  - Test names and descriptions

**Tools:**
```bash
# Find enum variants
rg "^\s+[A-Z][A-Za-z0-9_]*" src/types.rs

# Find struct fields
rg "^\s+pub?\s+\w+:" src/types.rs

# Find algorithm mentions in comments
rg "//.*(algorithm|method|technique)" -i .
```

**Output:** Expanded terminology with technical details

### Step 3: Classification and Organization

**When:** After initial collection, refine during ongoing reading

**How to classify:**

1. **By Domain:**
   - Domain-specific (OCR, ML, Computer Vision)
   - General programming (struct, enum, trait)
   - Project-specific (project name, internal abstractions)

2. **By Abstraction Level:**
   - **Concepts**: High-level ideas (Detection, Recognition)
   - **Algorithms**: Specific methods (CTC, NMS, DB)
   - **Data Structures**: Types and structs (Mat, Point2f, BBox)
   - **Implementation Details**: Code-level terms (Session, Interpreter, Tensor)

3. **By Scope:**
   - **Public API**: Terms users need to know
   - **Internal**: Terms only relevant to implementation
   - **Configuration**: Terms used in config files
   - **Output**: Terms in result structures

**Organization template:**
```markdown
## Terminology Glossary

### Domain Concepts
(High-level domain terms)

### Algorithms
(Specific algorithms and methods)

### Data Structures
(Types, structs, enums)

### Configuration Terms
(Config-related terminology)

### Process Flow Terms
(Preprocessing, inference, postprocessing stages)

### Coordinate Systems
(Coordinate transformation terminology)

### Model/Engine Terms
(Inference engine, model-related terms)

### Implementation Details
(Code-level technical terms)
```

### Step 4: Enrichment with Context

**Add to each entry:**
- **Definition** (what it is)
- **Purpose** (why it exists)
- **Usage context** (where/how it's used)
- **Code reference** (file:line or file reference)
- **Relationships** (related terms, parent/child concepts)
- **Examples** (code snippets or usage examples)
- **Acronym** (if applicable, with expansion)

**Enriched entry example:**
```markdown
### OCR 相关术语

- **Detection (检测)**
  - **定义**: 定位图像中的文本区域，输出文本行的边界框（通常是四边形）
  - **用途**: OCR 流程的第一步，找到文本位置
  - **实现位置**: `src/det.rs`
  - **执行流程**: 见 `api-flow.md` 4.1 节
  - **输出格式**: `Vec<[Point2f; 4]>` (四边形顶点列表)
  - **相关术语**: Recognition（识别）, NMS（后处理）, DB（检测算法）
  - **配置**: `DetConfig` (模型路径、预处理参数、后处理阈值)

- **Recognition (识别)**
  - **定义**: 识别检测到的文本区域中的文字内容，输出文本字符串
  - **用途**: OCR 流程的第二步，将图像转换为文本
  - **实现位置**: `src/rec.rs`
  - **执行流程**: 见 `api-flow.md` 4.2 节
  - **输入**: 裁剪后的文本区域图像
  - **输出格式**: `Vec<String>` (文本列表)
  - **相关术语**: Detection（检测）, CTC（解码算法）, CLS（方向分类）
  - **配置**: `RecConfig` (模型路径、字典路径、批量大小)
```

### Step 5: Maintenance and Evolution

**Continuous updates:**
- Add new terms as you encounter them
- Refine definitions as understanding deepens
- Add cross-references when connections are discovered
- Mark deprecated or unused terms
- Update relationships as architecture understanding improves

**Maintenance triggers:**
- Reading new modules → Check for new terms
- Understanding new relationships → Update cross-references
- Encountering confusion → Refine definitions
- Architecture changes → Update scope classifications

**Review checklist:**
- [ ] All acronyms have expansions
- [ ] All domain terms have clear definitions
- [ ] All key data structures are documented
- [ ] Cross-references to code are accurate
- [ ] Related terms are linked
- [ ] Examples are provided for complex terms

## Classification Examples

### Example 1: OCR Domain Terms

**Classification:**
- **Domain**: OCR
- **Level**: Concept
- **Scope**: Public API

**Entry:**
```markdown
### OCR 相关术语

- **Detection (检测)**: [Definition, context, code reference]
- **Recognition (识别)**: [Definition, context, code reference]
- **CLS (Classification)**: [Definition, context, code reference]
- **Orientation (方向分类)**: [Definition, context, code reference]
```

### Example 2: Data Structures

**Classification:**
- **Domain**: Programming (Rust types)
- **Level**: Data Structure
- **Scope**: Implementation (may be public API)

**Entry:**
```markdown
#### 几何结构

- **`Mat`**: 图像矩阵抽象（类似 OpenCV 的 Mat），封装了 `DynamicImage` 或 `opencv::core::Mat`
  - **实现位置**: `src/image_impl.rs`
  - **用途**: 统一的图像表示，支持 Pure Rust 和 OpenCV 后端
  - **相关**: `DynamicImage`, `opencv::core::Mat`
```

### Example 3: Algorithms

**Classification:**
- **Domain**: Computer Vision / ML
- **Level**: Algorithm
- **Scope**: Implementation detail

**Entry:**
```markdown
### 算法相关术语

- **NMS (Non-Maximum Suppression)**: 非极大值抑制算法，用于去除重叠的检测框
  - **实现位置**: `src/geometry.rs::nms()`
  - **用途**: 检测后处理，过滤重复检测框
  - **参数**: IOU 阈值
  - **相关**: IOU (Intersection over Union), Detection
```

### Example 4: Process Flow Terms

**Classification:**
- **Domain**: General ML Pipeline
- **Level**: Process Stage
- **Scope**: Internal (but important for understanding)

**Entry:**
```markdown
#### 处理流程术语

- **Preprocessing (预处理)**: 图像变换（resize、归一化、格式转换）为模型输入格式
  - **阶段**: OCR 流程中的准备阶段
  - **实现**: 各模块的预处理函数（`det.rs`, `rec.rs`, `orient.rs`）
  - **输出**: 模型输入张量
  - **相关**: Inference (推理), Postprocessing (后处理)
```

## Integration with Other Documentation

### Link to Architecture (C4 Model)

```markdown
- **Term**: See `architecture.md` Level 3 - Components section
- **Component usage**: Referenced in system context diagram
```

### Link to API Flow

```markdown
- **Term**: See execution flow in `api-flow.md` section X.Y
- **Step**: Part of preprocessing stage in detection pipeline
```

### Link to Module Analysis

```markdown
- **Term**: Detailed implementation in `key-modules.md` - ModuleName section
- **Key functions**: `module.rs::function_name()`
```

### Link to Tests

```markdown
- **Term**: Usage example in `tests/test_module.rs`
- **Test case**: `test_term_behavior()` demonstrates expected behavior
```

## Common Patterns and Anti-Patterns

### ✅ Good Patterns

1. **Start simple, enrich later**: Begin with basic definitions, add context as understanding grows
2. **Cross-reference everything**: Link terms to code, architecture, flows
3. **Group related terms**: Organize by domain and relationship
4. **Include examples**: Code snippets or usage examples for complex terms
5. **Mark evolution**: Note when understanding changes or deepens

### ❌ Anti-Patterns

1. **Too generic**: "Algorithm used for processing" → Be specific: "CTC decoding algorithm for sequence-to-sequence text recognition"
2. **No context**: Just the term name → Include where it's used, why it exists
3. **No cross-references**: Isolated entries → Link to related terms, code, docs
4. **Abandoned after initial creation**: Created once, never updated → Continuously maintain
5. **Mixed abstraction levels**: Concepts mixed with implementation details → Separate by abstraction level

## Tooling Support

### Automated Term Extraction (Optional)

```bash
# Extract struct/enum/trait names (Rust)
rg "^(pub )?(struct|enum|trait|type) \w+" src/ -o | sort -u

# Extract acronyms (all caps, 2-5 chars)
rg "\b[A-Z]{2,5}\b" README.md docs/ | sort -u

# Extract config keys
rg "Config.*\{|struct \w+Config" src/ -A 20 | grep "^\s+\w+:"
```

### Validation Checklist

```bash
# Verify all acronyms are expanded (manual review)
grep -E "\*\*[A-Z]{2,}.*\*\*" code-reading.md | grep -v "//"

# Check for orphaned cross-references (links that don't exist)
rg "`\w+\.rs`|`\w+\.md`" code-reading.md
```

## Success Indicators

You have a good terminology glossary when:

✅ You can explain any domain-specific term in one sentence
✅ All acronyms have expansions and definitions
✅ Key data structures are documented with purpose and usage
✅ Terms are cross-referenced to code locations
✅ Related terms are linked together
✅ The glossary helps newcomers understand the codebase quickly
✅ You rarely need to re-lookup the same term

## References

- **Terminology section**: Should be part of your main `code-reading.md` (e.g., section 9)
- **Cross-references**: Use consistent linking format throughout documentation
- **Updates**: Review and update terminology section during each major reading milestone
