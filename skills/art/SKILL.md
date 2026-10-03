---
name: nutshell-art
description: Generates topic-agnostic, mathematically strict 2D flat vector keyframe prompts adhering to the Kurzgesagt color theory, geometric primitive design, and anti-photorealism constraints.
---

# Kurzgesagt Visual Style Bible & Concept Art Directive

## 1. Visual Philosophy & Mathematical Rules
The visual aesthetic of Kurzgesagt is rooted in flat German Bauhaus vector design, mid-century modern infographic clarity, and bold geometry. It is not cartoonish in a messy sense; it is an engineered visual language.

### Absolute Prohibitions (Negative Constraints)
- NO 3D Elements: Zero volumetric shading, zero ray-tracing, zero CGI reflections, zero bevels, zero specular highlights.
- NO Photorealism: No real-world textures, no lens flares, no photographic depth-of-field blur, no bokeh.
- NO Smooth Gradients: Colors meet at razor-sharp vector boundary lines. If a shading effect is needed, use stepped tone bands (cel-shaded blocks of color), never smooth diffuse gradients.
- NO Over-Detailing: Never draw individual hairs, skin pores, complex cloth weaves, or naturalistic debris. Everything must be reduced to geometric primitives (circles, rounded rectangles, pill shapes, clean arcs).

## 2. Color Theory & Palette Formula
Every image must adhere to a strict 3-tier color balance:
- Tier 1: Dominant Background (60%) -> Deep Cosmic Navy / Void (#0B0F2A, #08071A, #120D31)
- Tier 2: Structural Geometry (30%) -> Desaturated Teal, Slate Blue, Warm Charcoal (#1E3A5F, #2A4365, #4A5568)
- Tier 3: Focal Pop / Energy (10%) -> High-Saturation Neon Yellow (#FFDF00), Cyan (#00F0FF), Hot Magenta (#FF007F)

- Outlines: Bold, clean, consistent-weight vector strokes (#0A0E27 or dark indigo), slightly darker than the fill color. Never pure harsh black #000000.
- Character Design: Stylized spherical or pill-shaped animals (such as the signature yellow scientist duck, round penguins, or circular red blood cells). Huge expressive circular eyes with solid black pupil dots and small white geometric catchlights. Clean lab coats, minimal goggles, or simple spacesuits.

## 3. Compositional Archetypes
Every generated concept art piece must choose one of four distinct compositional layouts:
1. The Cosmic Hero Shot: Tiny silhouette or small circular character on a flat cliff/platform in the bottom third, looking upward at a massive, geometric celestial body or abstract system spanning the upper two-thirds.
2. The Cutaway / Cross-Section Infographic: Clean isometric or front-elevation cutaway revealing the interior machinery of a cell, a planet, an engine, or a living room with clean label callouts.
3. The Scale Comparison Lineup: Horizontal progression from left to right showing elements ordered by size, wavelength, or complexity, anchored to a solid horizon baseline.
4. The Molecular / Microscopic Arena: Flat dark void populated by floating stylized geometric molecules, viruses, or particles interacting like puzzle pieces or lock-and-key gears.

## 4. Prompt Engineering Blueprint
When generating prompts for text-to-image engines (Google Imagen 3, Midjourney v6, or DALL-E 3), format the output following this exact phrasing:

Minimalist flat 2D vector graphic of [Subject / Action] in Kurzgesagt aesthetic. [Compositional layout]. Stylized geometric shapes, bold clean vector outlines, flat solid saturated colors ([Accent 1], [Accent 2]) set against a deep cosmic dark navy background (#0B0F2A). Clean educational infographic style, 16:9 widescreen composition. Strictly flat 2D vector art, zero 3D elements, no gradients, no photorealism, no volumetric lighting.

## 5. Execution Routine
When invoked via /nutshell-art [Subject / Scene Description]:
1. Provide a Visual Breakdown: Identify the primary focal primitive, the chosen color palette trio (Hex codes), and the compositional archetype.
2. Deliver the final, copy-pasteable image generation prompt formatted for Google Imagen and Midjourney.