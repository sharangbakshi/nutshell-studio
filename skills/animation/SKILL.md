---
name: nutshell-animation
description: Generates topic-agnostic Image-to-Video prompts for Veo, Runway, and Sora enforcing 12 fps stepped vector motion graphics, 2D camera mechanics, and cyclic looping.
---

# Kurzgesagt Motion Graphics & Animation Directive

## 1. The Physics of Kurzgesagt Motion
Kurzgesagt animation mimics traditional hand-crafted 2D vector motion graphics animated on "twos" (12 frames per second inside a 24 fps timeline). It rejects fluid, organic, or AI-morphed movement in favor of snappy, mechanical, and geometric transitions.

### Core Motion Principles
- Stepped 12 fps Cadence: Animation must feel rhythmic, snappy, and illustrative, not floaty, gelatinous, or hyper-interpolated.
- Secondary Overshoot & Settle: When an object moves (like a character turning its head, a dial turning, or a beam striking), it snaps quickly to the destination, overshoots by 5-10%, and bounces back into place.
- Rigid 2D Camera Constraints:
  - Permitted Camera Moves: Static locked-off camera; linear horizontal tracking truck (left-to-right); vertical pedestal tilt (up-and-down); instantaneous flat zoom cuts (wide shot to close-up).
  - Prohibited Camera Moves: NO 3D orbit, NO drone-style fly-throughs, NO perspective tilts that reveal 3D volume, NO handheld camera wobble, NO AI morphing.
- Cyclic Looping Architecture: Whenever possible, background and mechanical elements (e.g., sine waves, rotating gears, pulsing energy rings, floating dust dots) must be directed to cycle cleanly so the resulting 5-8 second AI clip can loop indefinitely beneath extended voiceover.

## 2. Animation Categories & Directives

### Type A: Kinetic Infographics & Field Physics
- Subject: Wave propagation, field ripples, atomic collisions, planetary orbits, data counters.
- Directive: "Rhythmic stepped motion graphics. Waves translate horizontally along the axis at constant velocity. Concentric geometric rings pulse outward sequentially. Digits on HUD panels tick upward crisply. Camera remains locked."

### Type B: Character & Creature Acting
- Subject: Scientist duck, immune system killer cells, historical figures, astronauts.
- Directive: "Minimalist flat 2D character animation. Snappy eye-blinks with distinct circular lids. Subtle vertical body bobbing during idle states. Mechanical, crisp arm movements holding props. Snappy head-turns with zero 3D head rotation."

### Type C: Cataclysmic Impact & Structural Rupture
- Subject: Supernovae, DNA bond breakage, nuclear fission, bacterial membrane rupture.
- Directive: "Dynamic 2D vector action shot. Fast diagonal acceleration into frame. Instantaneous clean impact with sharp vector fracture into clean geometric polygonal fragments floating outward in slow motion. Single-frame screen flash. Minimalist 2D camera shake."

## 3. Motion Prompt Template (Image-to-Video)
When directing video generation engines (such as Google Veo 3.1, Runway Gen-3, or Sora), pair the static source frame with this exact phrasing:

Stepped 2D vector motion graphics, 12 fps aesthetic. [Subject description] performs [specific snappy mechanical movement]. [Secondary elements] pulse/translate in rhythmic loop. Camera [locked / 2D horizontal truck / pedestal tilt]. Flat 2D vector animation style, strictly no 3D distortion, no perspective morphing, no photorealistic textures.

## 4. Execution Routine
When invoked via /nutshell-animation [Image description or scene action]:
1. Classify the animation into Type A (Infographic), Type B (Character), or Type C (Impact).
2. Detail the Pacing & Looping Strategy (how the 8-second clip sustains visual interest or loops).
3. Output the exact copy-paste prompt ready for Veo or video generation tools.