# Threat Profile Builder

An AI-assisted workflow for creating structured cyber threat profiles from recent open-source reporting.

This project demonstrates how generative AI can support cyber threat intelligence workflows by helping analysts synthesize public reporting, organize source material, and produce executive-ready threat actor profiles. The initial prototype focused on Cl0p ransomware as a sample use case.

## Purpose

Cyber threat intelligence teams often need to transform fragmented reporting into concise, decision-ready products. This project explores how AI can support that process while preserving human review, source awareness, and analytic judgment.

The workflow is designed to help with:

* Source organization
* Threat actor profiling
* Executive brief generation
* Source inventory creation
* Repeatable analytic structure
* Human-in-the-loop review

## Example Use Case

The prototype was tested using recent public reporting on Cl0p ransomware. The workflow generated outputs such as:

* Executive threat brief
* Source inventory
* Structured actor profile
* Draft report content suitable for analyst review

## Project Workflow

1. Collect recent public source material on a threat actor or campaign.
2. Organize the material into a structured source inventory.
3. Use an AI-assisted prompt workflow to generate a draft threat profile.
4. Review, edit, validate, and refine the output.
5. Produce an executive-ready summary or report.

## Repository Contents

```text
src/        Core workflow scripts
prompts/    Prompt templates used for structured generation
examples/   Sanitized sample outputs
docs/       Workflow notes and design rationale
```

## Responsible Use

This project is intended as a portfolio and learning demonstration. It does not replace analyst judgment, source validation, or structured intelligence tradecraft.

The workflow should not be used to process classified, proprietary, sensitive, or personally identifiable information. Outputs should be reviewed by a human analyst before use.

## Skills Demonstrated

* Cyber threat intelligence synthesis
* Generative AI workflow design
* Prompt engineering
* Source-aware analysis
* Executive communication
* Python-based automation
* Responsible AI implementation

## Future Improvements

Potential future enhancements include:

* Structured MITRE ATT&CK mapping
* Automated source metadata extraction
* Confidence scoring
* Citation-aware output formatting
* Batch processing for multiple threat actors
* Export to Word or PDF
* Analyst review checklist

## Disclaimer

This repository uses only public or sanitized sample material. Any generated analysis should be independently reviewed and validated before operational use.
