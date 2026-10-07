# RuView

| | |
|---|---|
| Formerly | WiFi-DensePose (the old repo redirects) |
| Category | Sensing: camera-free presence, activity and pose from WiFi signals |
| Status | **Research and prototype**, in its own words, and "not medical devices". npm `@ruvnet/ruview` 0.9.1 (2026-10-02). The on-device pose model is a "first cut". MIT. |
| Snapshot | 2026-10-07 |
| Sources | [src:ruview-repo] [src:ruview-npm] [src:ruvnet-profile] |

## In plain words

Software that uses the way WiFi signals bounce around a room to tell whether someone is there, roughly what
they're doing, and even breathing and heart rate, without cameras. Real sensing needs inexpensive
WiFi boards (ESP32-S3) or a research WiFi card; a normal laptop's WiFi only gives rough presence.
[src:ruview-repo]

## What it's for

Exploring privacy-preserving sensing: detecting presence or activity in a space without recording video.
rUv's index files it under "camera-free WiFi spatial intelligence and sensing research". [src:ruvnet-profile]

## Use when

- The project is about **sensing people or spaces without cameras**: occupancy, presence, research
  prototypes, smart-space experiments.
- The user is comfortable with hardware (flashing small boards) and with research-grade accuracy.
- It's a lab, hobby or proof-of-concept build, not a safety- or health-critical product.

## Avoid when

- Anything medical, safety-critical or legally sensitive. The project says it isn't a medical device, and it
  has publicly retracted an earlier accuracy claim. [src:ruview-repo]
- The need is ordinary software: apps, agents, search, memory. RuView is unrelated to those.
- Reliable occupancy is the goal and a standard sensor would do: motion (PIR), door contacts, mmWave
  presence sensors, or camera analytics where cameras are acceptable.

## What people use instead

- Off-the-shelf presence sensors (PIR motion, mmWave radar modules).
- Camera-based analytics, where cameras are acceptable.
- Wearables, for heart rate and breathing.

## Advantages it can buy

privacy, local execution, specialized performance

## Lightest path

**LOW: the Docker mode with simulated data**, which needs no hardware. Follow the README's Docker quickstart
in a scratch folder and look at what it shows before buying any boards. [src:ruview-repo]

**MEDIUM: one ESP32-S3 board** for real signals, then a small mesh of three to six for coverage. That's a
hardware project: flashing firmware, placement, calibration.

## What a full install changes

A local service and, for real sensing, dedicated boards on the network. Nothing in a coding assistant's
configuration. Health readings and pose estimates should be treated as experimental output.

## Maturity

Very active (frequent automated releases), but explicitly research-grade. The accuracy figures it reports
are **claims** from specific benchmarks; a synthetic-data model is described as such in the README.
[src:ruview-repo]

## Verify live before relying on

- The README's "what's real, what's not" notes on the models: [src:ruview-repo]
- Supported hardware and the Docker quickstart command: [src:ruview-repo]
- The current package version: [src:ruview-npm]

## Related

- rUv's index pairs it with rvCSI and RuField (perception) and WiFi Veil and RuCelium (sensing
  governance). See `../ecosystem-map.md`.
