# OSINT Verification Techniques

Guide to verifying user-generated content (UGC), images, videos, and geolocation using open-source intelligence (OSINT) methods.

## Core Principles

1. **Default to skepticism**: Assume UGC/breaking information is inaccurate until verified
2. **Verify source first**: Who created it, when, where, why
3. **Triangulate**: Cross-check with multiple independent sources
4. **Document verification path**: Record what was checked, what was found, what remains uncertain

## Recommended Tool: Cursor IDE Browser

**cursor-ide-browser** (MCP server) is highly recommended for OSINT verification work. It enables browser automation directly within Cursor IDE, making verification more efficient and evidence capture more reliable.

**Key Advantages**:
- **Integrated workflow**: No need to switch between tools
- **Evidence capture**: Built-in screenshot and snapshot capabilities
- **Reproducible**: Can document exact verification path
- **Audit trail**: Timestamps and page states automatically captured

**Use browser automation for**:
- Reverse image/video search across multiple platforms
- Geolocation verification using map services
- Social media account verification
- Chronolocation using weather/timezone services
- Evidence capture (screenshots, snapshots) at each step

## UGC / Social Media Verification

### Verification Checklist

For each piece of UGC, verify:

1. **Originality**: Is this the original source or a repost?
   - Use reverse image/video search
   - Check posting history of account
   - Look for earlier versions

2. **Source**: Who posted it?
   - Account verification status
   - Account history and credibility
   - Potential bias or agenda

3. **Location**: Where was it created?
   - Geolocation techniques (see below)
   - Location metadata (if available)
   - Cross-reference with claimed location

4. **Time**: When was it created?
   - Post timestamp
   - Metadata timestamps
   - Cross-reference with claimed event time
   - Check for timezone issues

5. **Motivation**: Why was it created?
   - Context of post
   - Account purpose
   - Potential manipulation or misinformation

### Tools & Techniques

**Using Cursor IDE Browser (Recommended)**:
- **Reverse image search**: Navigate to Google Images, TinEye, Yandex; capture search results as screenshots
- **Reverse video search**: Navigate to YouTube, InVid; extract frames and search; capture evidence
- **Social media analysis**: Navigate to platforms; capture account snapshots with timestamps
- **Multi-platform verification**: Use browser to check same content across platforms

**Traditional Tools** (if browser not available):
- **Reverse image search**: Google Images, TinEye, Yandex
- **Reverse video search**: YouTube, InVid, Yandex Video
- **Social media analysis**: Account history, follower analysis, cross-platform verification
- **Metadata extraction**: EXIF data, video metadata (use with caution, can be manipulated)

**Best Practice**: Always capture screenshots/snapshots when using browser for verification. This creates an auditable evidence chain.

## Image Verification

### Step-by-Step Process

**Using Cursor IDE Browser** (Recommended):

1. **Reverse image search** (navigate to multiple engines):
   - Navigate to Google Images, upload/search image
   - Capture search results page as screenshot
   - Navigate to TinEye, repeat search
   - Navigate to Yandex (often best for non-English content)
   - Navigate to Baidu (for Chinese content)
   - Compare results across platforms, capture comparison screenshots

**Traditional Method** (if browser not available):

1. **Reverse image search** (multiple engines):
   - Google Images
   - TinEye
   - Yandex (often best for non-English content)
   - Baidu (for Chinese content)

2. **Check earliest appearance**:
   - When did this image first appear online?
   - Is it being reused from an earlier event?

3. **Metadata analysis** (if available):
   - EXIF data (camera, settings, timestamp)
   - Note: Can be manipulated, use as supporting evidence only

4. **Content analysis**:
   - Weather conditions (match claimed date/location?)
   - Shadows (time of day, direction)
   - Clothing/season (match claimed time?)
   - Visible landmarks or text (language, signs)

5. **Cross-reference**:
   - Does content match other verified sources?
   - Are there inconsistencies?

### Common Manipulation Techniques

- **Old images repurposed**: Reverse search to find original
- **Deepfakes/AI-generated**: Look for artifacts, inconsistencies
- **Compositing**: Check for lighting/shadow inconsistencies
- **Metadata manipulation**: Don't rely solely on metadata

## Video Verification

### Step-by-Step Process

1. **Extract frames/thumbnails**:
   - Key frames showing location, people, events
   - Thumbnails for reverse search

2. **Reverse image search on frames**:
   - Find earliest appearance of similar frames
   - Check if video is being reused

3. **Geolocation** (if location is claimed):
   - Extract landmarks, signs, terrain
   - Match to satellite/map imagery
   - See geolocation section below

4. **Chronolocation** (time verification):
   - Shadows (direction, length → time of day)
   - Weather (match weather records for date/location?)
   - Visible clocks, timestamps in video
   - Clothing/season indicators

5. **Content analysis**:
   - Language spoken (match claimed location?)
   - Vehicles, license plates (region)
   - Architecture, infrastructure (region-specific)

6. **Metadata** (if available):
   - Video file metadata
   - Upload timestamps
   - Platform-specific metadata

### Tools

- **InVid**: Video verification plugin
- **YouTube DataViewer**: Extract thumbnails, check upload time
- **FFmpeg**: Extract frames for analysis
- **Reverse search**: Same as image verification

## Geolocation

### Process: Clues → Candidates → Comparison → Evidence Chain

#### Step 1: Extract Clues from Image/Video

Look for:
- **Landmarks**: Distinctive buildings, monuments, natural features
- **Signs**: Street signs, store signs, language, script
- **Infrastructure**: Road patterns, bridges, power lines, cell towers
- **Terrain**: Mountains, bodies of water, vegetation
- **Architecture**: Building styles, roof types, materials
- **Vehicles**: License plates, vehicle types common to region

#### Step 2: Generate Candidate Regions

- Use landmarks to narrow geographic area
- Consider language/script on signs
- Use terrain features to identify region
- Consider infrastructure patterns

#### Step 3: Compare with Maps/Satellite Imagery

**Using Cursor IDE Browser** (Recommended):

For each candidate:
- Navigate to Google Maps / Google Earth in browser
- Use satellite view to compare with image/video
- **Road patterns**: Match road layout, intersections (capture comparison screenshot)
- **Buildings**: Match building positions, shapes, relative positions (side-by-side screenshot)
- **Terrain**: Match elevation, natural features
- **Perspective**: Match camera angle, field of view
- Capture all comparison screenshots for evidence chain

**Traditional Method** (if browser not available):

For each candidate:
- **Road patterns**: Match road layout, intersections
- **Buildings**: Match building positions, shapes, relative positions
- **Terrain**: Match elevation, natural features
- **Perspective**: Match camera angle, field of view

#### Step 4: Output Evidence Chain

- **Match point**: Coordinates or location description
- **Evidence screenshots**: Side-by-side comparison (browser-captured)
- **Coordinates**: If precise location identified
- **Exclusion rationale**: Why other candidates were ruled out

### Tools

**Using Cursor IDE Browser**:
- **Google Maps / Google Earth**: Navigate in browser, capture comparison screenshots
- **Bing Maps**: Alternative, sometimes better satellite imagery
- **OpenStreetMap**: Open-source alternative
- **Wikimapia**: Community-annotated maps
- **SunCalc / Shadow Calculator**: Navigate to verify time of day from shadows

**Traditional Tools** (if browser not available):
- **Google Maps / Google Earth**: Primary tool for comparison
- **Bing Maps**: Alternative, sometimes better satellite imagery
- **OpenStreetMap**: Open-source alternative
- **Wikimapia**: Community-annotated maps
- **SunCalc / Shadow Calculator**: Verify time of day from shadows

### Example Workflow (Using Browser)

1. Image shows distinctive bridge + mountain range + sign in Arabic
2. Use browser to search for "bridge + mountain + [region with Arabic]" → Candidate: Middle East, specific city
3. Navigate to Google Earth in browser, find bridges in that city matching the shape
4. Compare road patterns, building positions around bridge (capture side-by-side screenshots)
5. Match found: Coordinates, browser-captured evidence screenshots, verification complete

## Verification Log Template

For each piece of content verified, maintain:

| Field | Content |
|------|---------|
| Content URL/ID | TODO |
| Platform | TODO |
| Upload Time (claimed) | TODO |
| Verification Date | TODO |
| Originality Check | TODO (Original/Repost, earliest appearance) |
| Source Verification | TODO (Account credibility, bias assessment) |
| Location Verification | TODO (Geolocation result, confidence) |
| Time Verification | TODO (Chronolocation result, confidence) |
| Content Analysis | TODO (Language, landmarks, consistency checks) |
| Cross-Reference | TODO (Other sources confirming/contradicting) |
| Overall Assessment | TODO (Verified/Likely/Uncertain/False) |
| Remaining Uncertainties | TODO |
| Evidence Screenshots | TODO (Links to browser-captured comparison images) |
| Browser Evidence | TODO (Screenshots, snapshots, verification path) |

**Note**: When using Cursor IDE Browser, include browser-captured evidence (screenshots, snapshots) in the verification log. This creates a complete, auditable evidence chain.

## Common Failure Modes

1. **Accepting metadata at face value**: Metadata can be manipulated
2. **Single source verification**: Always triangulate
3. **Ignoring inconsistencies**: If something doesn't match, investigate
4. **Not checking originality**: Old content repurposed for new events
5. **Timezone errors**: Confusing local time with UTC, or different timezones

## Red Flags

- Account created recently, only posts about one topic
- Content appears too perfect or staged
- Metadata doesn't match claimed location/time
- Reverse search finds earlier appearance with different context
- Inconsistencies between claimed and visible evidence (weather, shadows, etc.)
- No independent verification possible

## References

- Bellingcat's Online Investigation Toolkit
- Verification Handbook (EJC)
- Exposing the Invisible: Geolocation Methods
- First Draft News Verification Field Guide
