"""
Project-Specific SOP Parser
Supports additional formatting, tagging, and standard structures used in GCP project SOPs.
"""

import re

def extract_sections(text):
    """
    Extract section headers and content blocks based on numbered headings like 1., 1.1, 2., etc.
    Returns a list of tuples (section_heading, content).
    """
    sections = []
    current_section = None
    buffer = []

    lines = text.split("\n")
    for line in lines:
        if re.match(r'^(\d+(\.\d+)*\.?)(\s+)([A-Z].*)', line.strip()):
            if current_section:
                sections.append((current_section, "\n".join(buffer).strip()))
                buffer = []
            current_section = line.strip()
        else:
            buffer.append(line.strip())
    if current_section and buffer:
        sections.append((current_section, "\n".join(buffer).strip()))
    return sections

def extract_glossary(text):
    """
    Extract glossary terms from a section labeled 'Glossary' or similar.
    """
    glossary = {}
    lines = text.split("\n")
    inside_glossary = False
    for line in lines:
        if 'glossary' in line.lower():
            inside_glossary = True
            continue
        if inside_glossary:
            if line.strip() == "":
                continue
            parts = line.split(':', 1)
            if len(parts) == 2:
                term, definition = parts
                glossary[term.strip()] = definition.strip()
    return glossary
