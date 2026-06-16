# Threat Profile Builder

An AI-assisted workflow for creating structured cyber threat profiles from recent open-source reporting.

## Overview

Threat Profile Builder is a prototype that demonstrates how generative AI can support cyber threat intelligence workflows. It helps transform public reporting into structured, executive-ready threat profiles while preserving the need for human review, source awareness, and analytic judgment.

The initial prototype was developed using Cl0p ransomware as a sample use case.

## Why I Built This

Cyber threat intelligence teams often need to synthesize fragmented reporting quickly and clearly for senior leaders, investigators, and operational stakeholders. This project explores how AI can support that process by helping analysts organize source material, draft structured profiles, and produce concise summaries that remain reviewable by a human analyst.

The goal is not to replace analytic judgment. The goal is to make repetitive synthesis work faster, more structured, and easier to review.

## What the Workflow Does

The workflow is designed to help an analyst:

* Collect and organize recent public reporting on a threat actor or campaign
* Structure key findings into a repeatable threat profile format
* Generate an executive-ready draft brief
* Maintain a source inventory for review
* Support human-in-the-loop validation and refinement

## Example Use Case

The prototype was tested using public reporting on Cl0p ransomware. The workflow generated draft outputs such as:

* Executive threat brief
* Source inventory
* Structured threat actor profile
* Report-ready narrative content

## Skills Demonstrated

This project demonstrates experience with:

* Cyber threat intelligence synthesis
* Generative AI workflow design
* Prompt engineering
* Python-based automation
* Executive communication
* Source-aware analysis
* Responsible AI implementation
* Human-in-the-loop review processes

## Responsible Use

This project is intended as a portfolio and learning demonstration. It should not be used with classified, proprietary, sensitive, or personally identifiable information.

AI-generated outputs should always be reviewed, edited, and validated by a human analyst before use.

## Repository Structure

* `src/` — Core project scripts
* `.gitignore` — Files and folders excluded from Git tracking
* `README.md` — Project overview and documentation

## Future Improvements

Potential future enhancements include:

* MITRE ATT&CK mapping
* Citation-aware output formatting
* Confidence or reliability scoring
* Batch processing for multiple threat actors
* Word or PDF export
* Analyst review checklist
* Sanitized sample output files

## Disclaimer

This repository uses only public or sanitized sample material. Any generated analysis should be independently reviewed and validated before operational or professional use.
