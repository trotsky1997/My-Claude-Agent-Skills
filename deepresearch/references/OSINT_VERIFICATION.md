# OSINT Verification Techniques

Guide to verifying user-generated content (UGC), images, videos, and geolocation using open-source intelligence (OSINT) methods.

## Core Principles

1. **Default to skepticism**: Assume UGC/breaking information is inaccurate until verified
2. **Verify source first**: Who created it, when, where, why
3. **Triangulate**: Cross-check with multiple independent sources
4. **Document verification path**: Record what was checked, what was found, what remains uncertain

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

- **Reverse image search**: Google Images, TinEye, Yandex
- **Reverse video search**: YouTube, InVid, Yandex Video
- **Social media analysis**: Account history, follower analysis, cross-platform verification
- **Metadata extraction**: EXIF data, video metadata (use with caution, can be manipulated)

## Image Verification

### Step-by-Step Process

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

For each candidate:
- **Road patterns**: Match road layout, intersections
- **Buildings**: Match building positions, shapes, relative positions
- **Terrain**: Match elevation, natural features
- **Perspective**: Match camera angle, field of view

#### Step 4: Output Evidence Chain

- **Match point**: Coordinates or location description
- **Evidence screenshots**: Side-by-side comparison
- **Coordinates**: If precise location identified
- **Exclusion rationale**: Why other candidates were ruled out

### Tools

- **Google Maps / Google Earth**: Primary tool for comparison
- **Bing Maps**: Alternative, sometimes better satellite imagery
- **OpenStreetMap**: Open-source alternative
- **Wikimapia**: Community-annotated maps
- **SunCalc / Shadow Calculator**: Verify time of day from shadows

### Example Workflow

1. Image shows distinctive bridge + mountain range + sign in Arabic
2. Search for "bridge + mountain + [region with Arabic]" → Candidate: Middle East, specific city
3. Use Google Earth to find bridges in that city matching the shape
4. Compare road patterns, building positions around bridge
5. Match found: Coordinates, evidence screenshots, verification complete

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
| Evidence Screenshots | TODO (Links to comparison images) |

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
